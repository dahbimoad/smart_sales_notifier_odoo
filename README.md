
<h1 align="center">🚀 Smart Sales Notifier</h1>

<p align="center">
  <strong>Module Odoo 17 avec Intelligence Artificielle</strong><br>
  Automatisation intelligente des notifications de ventes via n8n, Groq LLaMA & Telegram
</p>

<p align="center">
  <a href="#-fonctionnalités">Fonctionnalités</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-documentation">Documentation</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Odoo-17.0-purple?style=for-the-badge&logo=odoo" alt="Odoo 17"/>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/n8n-Workflow-orange?style=for-the-badge" alt="n8n"/>
  <img src="https://img.shields.io/badge/AI-Groq_LLaMA-green?style=for-the-badge" alt="Groq"/>
  <img src="https://img.shields.io/badge/License-LGPL--3-yellow?style=for-the-badge" alt="License"/>
</p>

---

## 📋 Description

**Smart Sales Notifier** est un module Odoo 17 innovant qui intègre l'Intelligence Artificielle pour automatiser l'analyse et les notifications des commandes de vente. Le système utilise n8n pour l'orchestration, Groq LLaMA 3.1 pour l'analyse IA, et Telegram pour les notifications en temps réel.

### 🎯 Problématique

Les équipes commerciales font face à plusieurs défis :
- 📊 Volume élevé de commandes à traiter
- ⏱️ Priorisation manuelle chronophage
- 🔔 Notifications tardives ou inexistantes
- 📈 Manque d'analyse intelligente des ventes

### ✅ Solution

Notre module apporte une solution complète :
- 🤖 **Analyse IA automatique** de chaque commande
- 🎯 **Priorisation intelligente** (low, medium, high, urgent)
- 📱 **Notifications Telegram** en temps réel
- 📊 **Insights actionnables** pour les équipes commerciales

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| 🔔 **Notification Automatique** | Envoi automatique des données de commande à n8n |
| 🧠 **Analyse IA** | Traitement intelligent via Groq LLaMA 3.1 |
| 🎯 **Scoring Prioritaire** | Classification automatique des commandes |
| 📱 **Telegram Bot** | Notifications instantanées sur mobile |
| ⚙️ **Configuration Flexible** | Paramètres personnalisables |
| 🔄 **Cron Job** | Vérification automatique des commandes |

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Odoo ERP      │────▶│   Webhook   │────▶│    n8n      │────▶│  Groq AI    │
│  (Sale Order)   │     │   (POST)    │     │  Workflow   │     │ LLaMA 3.1   │
└─────────────────┘     └─────────────┘     └──────┬──────┘     └──────┬──────┘
                                                   │                   │
                                                   ▼                   │
                                            ┌─────────────┐            │
                                            │  Telegram   │◀───────────┘
                                            │    Bot      │
                                            └─────────────┘
```

### Stack Technologique

| Composant | Technologie | Version |
|-----------|-------------|---------|
| ERP | Odoo | 17.0 |
| Base de données | PostgreSQL | 15 |
| Orchestration | n8n | 1.113.3+ |
| Intelligence Artificielle | Groq (LLaMA 3.1 8B) | API |
| Notifications | Telegram Bot | API |
| Conteneurisation | Docker | Latest |
| Langage | Python | 3.10+ |

---

## 📁 Structure du Projet

```
smart_sales_notifier/
├── 📄 __manifest__.py              # Configuration du module Odoo
├── 📄 __init__.py                  # Imports Python
├── 📄 docker-compose.yml           # Configuration Docker
├── 📄 README.md                    # Documentation (ce fichier)
├── 📄 .gitignore                   # Fichiers ignorés par Git
│
├── 📁 models/
│   ├── __init__.py
│   ├── sale_order.py               # Extension du modèle de vente
│   └── res_config_settings.py      # Paramètres de configuration
│
├── 📁 views/
│   ├── res_config_settings_views.xml   # Vue des paramètres
│   └── sale_order_views.xml            # Vue des commandes
│
├── 📁 data/
│   ├── ir_cron.xml                 # Tâches planifiées
│   └── demo_data.xml               # Données de démonstration
│
├── 📁 security/
│   └── ir.model.access.csv         # Droits d'accès
│
├── 📁 static/
│   └── description/
│       └── icon.svg                # Icône du module
│
├── 📁 docs/
│   ├── rapport.pdf                 # Rapport de projet complet
│   ├── presentation.pptx            # Présentation PowerPoint
│
│
└── 📄 n8n_Smart Sales Notifier.json    # Workflow n8n exporté
```

---

## 🚀 Installation

### Prérequis

- Docker Desktop installé
- Git
- Compte Groq (API Key gratuite)
- Bot Telegram créé via @BotFather

### 1. Cloner le repository

```bash
git clone https://github.com/dahbimoad/smart_sales_notifier_odoo.git
cd smart_sales_notifier_odoo
```

### 2. Lancer avec Docker Compose

```bash
docker-compose up -d
```

### 3. Accéder à Odoo

Ouvrir dans le navigateur : **http://localhost:8069**

### 4. Créer la base de données

- Master Password: `admin`
- Database Name: `odoo_db`
- Email: votre email
- Password: votre mot de passe

### 5. Activer le mode développeur

`Paramètres` → `Outils développeur` → `Activer le mode développeur`

### 6. Installer le module

`Apps` → `Mettre à jour la liste` → Rechercher **"Smart Sales Notifier"** → `Installer`

---

## ⚙️ Configuration

### Configuration Odoo

1. Aller dans **Paramètres** → **Smart Sales Notifier**
2. Configurer :
   - **n8n Webhook URL** : `https://votre-instance-n8n.com/webhook/sales-notifier`
   - **High Value Threshold** : Montant pour alertes prioritaires (ex: 1000)

### Configuration n8n

1. Importer le workflow depuis `n8n_Smart Sales Notifier.json`
2. Configurer les credentials :
   - **Groq API Key** : Obtenir sur [console.groq.com](https://console.groq.com)
   - **Telegram Bot Token** : Obtenir via @BotFather
   - **Chat ID** : Obtenir via @userinfobot

### Configuration Telegram

1. Créer un bot : Contacter @BotFather sur Telegram
2. Envoyer `/newbot` et suivre les instructions
3. Copier le token dans n8n

---

## 📊 Utilisation

1. **Créer une commande** dans Odoo (module Ventes)
2. **Confirmer la commande** (bouton "Confirmer")
3. **Cliquer sur "AI Analysis"** pour déclencher l'analyse
4. **Recevoir la notification** sur Telegram avec :
   - Résumé de la commande
   - Analyse IA
   - Niveau de priorité
   - Action recommandée
5. **Consulter l'analyse** dans l'onglet "AI Analysis" de la commande

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| 📄 [Rapport PDF](docs/rapport.pdf) | Rapport complet du projet (problématique, cahier des charges, solution, tests) |
| 📊 [Présentation PDF](docs/presentation.pdf) | Slides de présentation du projet |
| 📁 [Screenshots](docs/screenshots/) | Captures d'écran de l'application |
| 🔧 [Workflow n8n](n8n_Smart%20Sales%20Notifier.json) | Workflow n8n prêt à importer |

---

## 🎥 Démonstration

📺 **Vidéo de démonstration** : [Voir sur Google Drive](https://drive.google.com/drive/folders/1VhpLWys0xJnrltJVffv65LXgDvlXMtEo?usp=sharing)

---

## 👥 Auteurs

| Nom | Rôle |
|-----|------|
| **Dahbi Moad** | Développeur Principal |
| **Bouker Mohamed** | Développeur |
| **Allam Elarbi** | Développeur |

**Encadré par** : Pr. Hassan BADIR

**Institution** : École Nationale des Sciences Appliquées de Tanger (ENSA Tanger)

**Date** : Janvier 2026


---

<p align="center">
  <sub>Développé avec ❤️ à ENSA Tanger</sub>
</p>
