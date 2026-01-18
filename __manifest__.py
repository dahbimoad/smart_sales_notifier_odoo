# -*- coding: utf-8 -*-
{
    'name': 'Smart Sales Notifier',
    'version': '1.0.0',
    'category': 'Sales',
    'summary': 'AI-Powered Sales Notifications via n8n Integration',
    'description': """
        Smart Sales Notifier - Module ERP avec Intelligence Artificielle
        ================================================================
        
        Ce module permet de:
        - Détecter automatiquement les nouvelles commandes
        - Envoyer les données à n8n pour traitement IA (Groq/LLaMA)
        - Générer des notifications intelligentes via Telegram
        - Analyser les ventes en temps réel avec l'IA
        - Prioriser les commandes automatiquement
        
        Fonctionnalités:
        ----------------
        ✅ Intégration n8n pour l'automatisation
        ✅ Analyse IA avec Groq (LLaMA 3.1)
        ✅ Notifications Telegram en temps réel
        ✅ Scoring de priorité automatique
        ✅ Dashboard des commandes analysées
        
        Développé par: Dahbi Moad
        Date: Janvier 2026
        Projet: ERP - Master MSID
    """,
    'author': 'Dahbi Moad',
    'website': 'https://n8n.dahbimoad.com',
    'license': 'LGPL-3',
    'depends': ['sale', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/demo_data.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
        'data/ir_cron.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
