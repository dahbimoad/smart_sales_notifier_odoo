# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    n8n_webhook_url = fields.Char(
        string='n8n Webhook URL',
        help='The n8n webhook URL for receiving sales notifications',
        config_parameter='smart_sales_notifier.n8n_webhook_url'
    )
    
    high_value_threshold = fields.Float(
        string='High Value Order Threshold',
        help='Orders above this amount will trigger special notifications',
        config_parameter='smart_sales_notifier.high_value_threshold',
        default=1000.0
    )
    
    enable_auto_notify = fields.Boolean(
        string='Enable Auto Notifications',
        help='Automatically send notifications when orders are confirmed',
        config_parameter='smart_sales_notifier.enable_auto_notify',
        default=True
    )
