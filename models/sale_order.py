# -*- coding: utf-8 -*-
import json
import logging
import requests
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class SaleOrderSmartNotifier(models.Model):
    _inherit = 'sale.order'

    # New fields for smart notifications
    smart_notified = fields.Boolean(
        string='Smart Notification Sent',
        default=False,
        help='Indicates if AI notification was sent via n8n'
    )
    smart_notification_date = fields.Datetime(
        string='Notification Date',
        help='Date when the smart notification was sent'
    )
    ai_analysis = fields.Text(
        string='AI Analysis',
        help='AI-generated analysis from n8n'
    )
    priority_score = fields.Selection([
        ('low', 'Low Priority'),
        ('medium', 'Medium Priority'),
        ('high', 'High Priority'),
        ('urgent', 'Urgent'),
    ], string='AI Priority', help='Priority determined by AI analysis')

    def action_confirm(self):
        """Override to send notification when order is confirmed"""
        res = super(SaleOrderSmartNotifier, self).action_confirm()
        for order in self:
            order._send_smart_notification('order_confirmed')
        return res

    def _send_smart_notification(self, event_type):
        """Send order data to n8n webhook for AI processing"""
        self.ensure_one()
        
        # Get webhook URL from settings
        webhook_url = self.env['ir.config_parameter'].sudo().get_param(
            'smart_sales_notifier.n8n_webhook_url', ''
        )
        
        if not webhook_url:
            _logger.warning('Smart Sales Notifier: No n8n webhook URL configured')
            return False

        # Prepare order data for AI analysis
        order_data = {
            'event_type': event_type,
            'order_id': self.id,
            'order_name': self.name,
            'customer_name': self.partner_id.name,
            'customer_email': self.partner_id.email or '',
            'customer_phone': self.partner_id.phone or '',
            'total_amount': self.amount_total,
            'currency': self.currency_id.name,
            'order_date': self.date_order.isoformat() if self.date_order else '',
            'products': [],
            'company_name': self.company_id.name,
            'salesperson': self.user_id.name if self.user_id else '',
            'note': self.note or '',
        }

        # Add product details
        for line in self.order_line:
            order_data['products'].append({
                'product_name': line.product_id.name,
                'quantity': line.product_uom_qty,
                'unit_price': line.price_unit,
                'subtotal': line.price_subtotal,
            })

        try:
            # Send to n8n webhook
            response = requests.post(
                webhook_url,
                json=order_data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200:
                # Update order with notification status
                self.write({
                    'smart_notified': True,
                    'smart_notification_date': fields.Datetime.now(),
                })
                _logger.info(f'Smart notification sent for order {self.name}')
                
                # Try to get AI response
                try:
                    ai_response = response.json()
                    if ai_response.get('ai_analysis'):
                        self.write({
                            'ai_analysis': ai_response.get('ai_analysis'),
                            'priority_score': ai_response.get('priority', 'medium'),
                        })
                except:
                    pass
                    
                return True
            else:
                _logger.error(f'Smart notification failed: {response.status_code}')
                return False
                
        except requests.exceptions.RequestException as e:
            _logger.error(f'Smart notification error: {str(e)}')
            return False

    def action_send_smart_notification(self):
        """Manual action to send smart notification"""
        for order in self:
            order._send_smart_notification('manual_notification')
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Smart Notification',
                'message': 'Notification sent to n8n for AI processing!',
                'type': 'success',
                'sticky': False,
            }
        }

    @api.model
    def _cron_check_high_value_orders(self):
        """Cron job to notify about high-value orders"""
        threshold = float(self.env['ir.config_parameter'].sudo().get_param(
            'smart_sales_notifier.high_value_threshold', '1000'
        ))
        
        # Find confirmed orders above threshold not yet notified
        high_value_orders = self.search([
            ('state', 'in', ['sale', 'done']),
            ('amount_total', '>=', threshold),
            ('smart_notified', '=', False),
        ])
        
        for order in high_value_orders:
            order._send_smart_notification('high_value_order')
        
        _logger.info(f'Processed {len(high_value_orders)} high-value orders')
