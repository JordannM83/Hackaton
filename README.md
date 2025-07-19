# 🧠 Holbies Learning Hub

Un système de quiz interactif avec un thème Matrix pour l'apprentissage technique, développé avec FastAPI, PostgreSQL et un design geek sombre inspiré de Matrix.

![Matrix Theme](https://img.shields.io/badge/Theme-Matrix-00ff41)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)

## ✨ Fonctionnalités

### 🎯 Système de Quiz
- **50+ questions** style PLD Holberton School
- **Correcteur automatique** avec explications détaillées
- **Catégories variées** : Algorithmes, Python, C, JavaScript, Web, SQL, Linux, Git
- **Suivi des performances** et statistiques personnelles
- **Sessions sauvegardées** avec historique complet

### 🎨 Interface Matrix
- **Thème sombre** avec couleurs néon vertes (#00ff41)
- **Animations Matrix** : code rain, effets de glitch, particules flottantes
- **Design responsive** optimisé mobile et desktop
- **Polices monospace** (Orbitron, Source Code Pro)
- **Effets visuels** immersifs et interactifs

### 🔐 Authentification Sécurisée
- **JWT tokens** pour l'authentification
- **Hachage bcrypt** des mots de passe
- **Validation avancée** côté client et serveur
- **Sessions persistantes** et sécurisées
- **🎬 Vidéo de bienvenue** automatique après connexion avec fermeture auto

### 🎥 Système de Vidéo de Bienvenue
- **Lecture automatique** après connexion réussie
- **Modal plein écran** avec design Matrix intégré
- **Support multi-formats** (MP4, WebM, OGV)
- **Fermeture automatique** à la fin de la vidéo
- **Contrôles manuels** (Escape, clic extérieur, bouton X)
- **Animation de fallback** si aucune vidéo n'est présente
- **Effets visuels Matrix** avec bordures animées

### 📊 Dashboard Interactif
- **Statistiques détaillées** : score moyen, meilleur score, séries
- **Graphiques de performance** avec Chart.js
- **Historique complet** des sessions de quiz
- **Indicateurs de progression** visuels

## 🚀 Installation Rapide

### Méthode 1 : Script Automatique
```bash
git clone https://github.com/votre-repo/holbies-learning-hub.git
cd holbies-learning-hub
./start.sh
```

### Méthode 2 : Manuel
```bash
# 1. Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer la base de données
cp .env.example .env
# Modifier .env avec vos paramètres PostgreSQL

# 4. Créer les tables et données
python3 -c "from app.database import engine; from app.models import Base; Base.metadata.create_all(bind=engine)"
python3 populate_db.py

# 5. Créer un admin (optionnel)
python3 create_admin.py

# 6. Démarrer le serveur
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Méthode 3 : Docker
```bash
docker-compose up --build
```

## 🌐 Accès à l'Application

Une fois démarré, l'application est accessible à :

- **🏠 Accueil** : http://localhost:8000
- **🔐 Connexion** : http://localhost:8000/login
- **📝 Inscription** : http://localhost:8000/register
- **🧠 Quiz** : http://localhost:8000/quiz
- **📊 Dashboard** : http://localhost:8000/dashboard
- **📚 API Docs** : http://localhost:8000/docs

## 🛠️ Technologies Utilisées

### Backend
- **FastAPI** - Framework web moderne et rapide
- **SQLAlchemy** - ORM Python avancé
- **PostgreSQL** - Base de données relationnelle
- **Alembic** - Migrations de base de données
- **python-jose** - JWT pour l'authentification
- **passlib** - Hachage sécurisé des mots de passe

### Frontend
- **HTML5/CSS3** - Structure et styles modernes
- **JavaScript ES6+** - Logique interactive
- **CSS Variables** - Thématisation avancée
- **Chart.js** - Graphiques de performance
- **Animations CSS** - Effets Matrix immersifs

### Sécurité
- **JWT Authentication** - Tokens sécurisés
- **bcrypt** - Hachage des mots de passe
- **CORS** - Protection cross-origin
- **Variables d'environnement** - Configuration sécurisée

## 📁 Structure du Projet

```
holbies-learning-hub/
├── 🐍 Backend Python
│   ├── app/
│   │   ├── auth.py          # Authentification JWT
│   │   ├── database.py      # Configuration DB
│   │   ├── models.py        # Modèles SQLAlchemy
│   │   ├── schemas.py       # Schémas Pydantic
│   │   └── routers/         # Routes API
│   ├── main.py              # Point d'entrée FastAPI
│   └── requirements.txt     # Dépendances
├── 🌐 Frontend
│   ├── static/
│   │   ├── css/style.css    # Styles Matrix
│   │   ├── js/              # JavaScript modules
│   │   │   ├── video-modal.js          # Système vidéo de bienvenue
│   │   │   ├── welcome-video-generator.js # Animation de fallback
│   │   │   └── auth.js      # Authentification avec vidéo
│   │   └── video/           # Vidéos de bienvenue
│   └── templates/           # Templates Jinja2
├── 🗄️ Base de données
│   ├── alembic/             # Migrations
│   ├── populate_db.py       # Questions de quiz
│   └── alembic.ini          # Configuration
├── 🛠️ Scripts utilitaires
│   ├── start.sh             # Démarrage automatique
│   ├── create_admin.py      # Création admin
│   └── test_installation.py # Tests d'installation
└── 🐳 Déploiement
    ├── Dockerfile
    └── docker-compose.yml
```

## 🧪 Test de l'Installation

Vérifiez que tout fonctionne correctement :

```bash
python3 test_installation.py
```

Ce script teste :
- ✅ Imports Python
- ✅ Connexion base de données
- ✅ Modèles de données
- ✅ Fichiers statiques
- ✅ Templates HTML
- ✅ Serveur web

## 🎮 Guide d'Utilisation

### Pour les Étudiants

1. **📝 Inscription**
   - Créer un compte avec username, email, mot de passe
   - Validation en temps réel des champs
   - Indicateur de force du mot de passe

2. **🔐 Connexion**
   - Authentification sécurisée avec JWT
   - **🎬 Vidéo de bienvenue automatique** après connexion
   - Session persistante
   - Redirection automatique vers le dashboard

3. **🧠 Quiz**
   - Questions à choix multiples
   - Feedback instantané avec explications
   - Progression visuelle
   - Scores en temps réel

4. **📊 Dashboard**
   - Statistiques personnelles
   - Graphique de performance
   - Historique des sessions
   - Actions rapides

### Pour les Développeurs

1. **🔧 API REST**
   - Documentation interactive avec Swagger
   - Endpoints sécurisés avec JWT
   - Validation automatique des données
   - Gestion d'erreurs complète

2. **🗄️ Base de Données**
   - Modèles SQLAlchemy bien structurés
   - Migrations avec Alembic
   - Relations optimisées
   - Index pour les performances

## 🎨 Personnalisation du Thème

Le thème Matrix est entièrement personnalisable via les variables CSS :

```css
:root {
    --primary-green: #00ff41;      /* Vert Matrix principal */
    --secondary-green: #008f11;    /* Vert secondaire */
    --matrix-black: #0d1117;       /* Noir de fond */
    --matrix-dark: #161b22;        /* Gris foncé */
    --text-light: #c9d1d9;         /* Texte clair */
    /* ... autres variables */
}
```

## 📚 Questions du Quiz

### Catégories Disponibles

- **🔢 Algorithms** : Complexité, structures de données, tri
- **🐍 Python** : Syntaxe, types, méthodes, concepts avancés
- **⚙️ C Programming** : Pointeurs, mémoire, syntaxe
- **🌐 JavaScript** : ES6+, DOM, JSON, types
- **🌍 Web** : HTML, CSS, HTTP/HTTPS, APIs REST
- **🗄️ SQL** : Requêtes, jointures, optimisation
- **🐧 Linux** : Commandes, permissions, système
- **📚 Git** : Contrôle de version, branches, workflow
- **🔐 Security** : Vulnérabilités, authentification
- **🏗️ OOP** : Héritage, polymorphisme, encapsulation

### Niveaux de Difficulté

- **🟢 Easy** : Concepts de base, syntaxe simple
- **🟡 Medium** : Applications pratiques, concepts intermédiaires
- **🔴 Hard** : Optimisation, concepts avancés, algorithmes complexes

## 🔧 Configuration Avancée

### Variables d'Environnement

```env
# Base de données
DATABASE_URL=postgresql://user:pass@localhost/holbies_db

# JWT Configuration
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### Ajout de Questions

Pour ajouter vos propres questions :

1. Modifier `populate_db.py`
2. Ajouter dans `QUIZ_QUESTIONS` :

```python
{
    "question_text": "Votre question ?",
    "option_a": "Option A",
    "option_b": "Option B", 
    "option_c": "Option C",
    "option_d": "Option D",
    "correct_answer": "a",  # a, b, c, ou d
    "explanation": "Explication de la réponse",
    "difficulty": "medium",  # easy, medium, hard
    "category": "votre-categorie"
}
```

3. Relancer : `python3 populate_db.py`

## 🎬 Configuration de la Vidéo de Bienvenue

### Ajouter une Vidéo Personnalisée

1. **Placer votre vidéo** dans le dossier `/static/video/`
2. **Nommer le fichier** `welcome.mp4` (ou `.webm`, `.ogv`)
3. **Redémarrer le serveur** pour appliquer les changements

```bash
# Exemple d'ajout de vidéo
cp votre-video.mp4 static/video/welcome.mp4
python main.py
```

### Format Vidéo Recommandé

- **Format** : MP4 (H.264) pour une compatibilité maximale
- **Résolution** : 1280x720 ou 1920x1080
- **Durée** : 3-8 secondes pour une expérience optimale
- **Taille** : Maximum 10-15MB
- **Audio** : AAC, volume modéré

### Optimisation avec FFmpeg

```bash
# Optimiser une vidéo pour le web
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k -movflags +faststart static/video/welcome.mp4
```

### Fonctionnement

- ✅ **Détection automatique** de la présence de vidéo
- ✅ **Lecture avec son** après connexion réussie
- ✅ **Fermeture automatique** à la fin
- ✅ **Animation de fallback** si pas de vidéo
- ✅ **Contrôles utilisateur** (Escape, clic, bouton X)

## 🚀 Déploiement en Production

### Avec Gunicorn

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Avec Docker

```bash
docker build -t holbies-hub .
docker run -p 8000:8000 holbies-hub
```

### Variables de Production

```env
DEBUG=False
SECRET_KEY=your-production-secret-key-very-long-and-complex
DATABASE_URL=postgresql://prod_user:prod_pass@prod_host/prod_db
```

## 🤝 Contribution

1. 🍴 Fork le projet
2. 🌿 Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. 💾 Commit (`git commit -am 'Ajouter nouvelle fonctionnalité'`)
4. 📤 Push (`git push origin feature/nouvelle-fonctionnalite`)
5. 🔄 Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir `LICENSE` pour plus de détails.

## 🎯 Roadmap

### Version 2.0
- [ ] 🏆 Système de badges et récompenses
- [ ] ⏱️ Quiz chronométrés avec mode challenge
- [ ] 💻 Questions de code avec syntax highlighting
- [ ] 🥇 Classements et compétitions
- [ ] 👥 Mode multijoueur en temps réel
- [ ] 📱 Application mobile Progressive Web App

### Version 2.1
- [ ] 📁 Import/Export de questions (JSON, CSV)
- [ ] 🎨 Thèmes personnalisables (Cyberpunk, Retro, etc.)
- [ ] 🔊 Effets sonores et musique d'ambiance
- [ ] 🎬 Vidéos de bienvenue personnalisées par utilisateur
- [ ] 📈 Analytics avancées et rapports
- [ ] 🌍 Support multilingue (EN, FR, ES)
- [ ] ☁️ Sauvegarde cloud et synchronisation

---

**Créé avec ❤️ pour la communauté des développeurs**

🌟 **Star ce projet** si il vous a plu !  
🐛 **Reportez les bugs** dans les Issues  
💡 **Proposez des améliorations** via Pull Request
