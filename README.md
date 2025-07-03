# Hackaton
To do list

✅ 1. Définir le scope (ce qu’on fait vraiment)
 Cibler un seul thème du langage C (ex: les boucles, ou les pointeurs)

 Créer 1 ou 2 cours illustrés

 Préparer 3‑5 QCM simples

 Préparer 1 exercice où l’utilisateur écrit du code

⚡ 2. Choisir la stack rapide et simple
Frontend : React ou Vue (vite.js ou create-react-app pour démarrer vite)

Backend : Node.js avec Express (ou pas de backend si tout statique + API mock)

Sandbox de code : utiliser un service externe si possible (ex: JDoodle API, Sphere Engine, Judge0)

Base de données : JSON local ou Firebase pour gagner du temps

🛠 3. Développement MVP
 Page d’accueil avec présentation

 Page « Cours » avec texte et exemples de code C

 Page « QCM » :

 Question + 3‑4 réponses

 Affichage score en direct

 Page « Exercice » :

 Éditeur de code (Monaco Editor)

 Bouton « Exécuter » qui envoie le code à l’API et affiche le résultat

 Système minimal de navigation entre les pages

🎨 4. Design et UX simple
 Utiliser un kit UI (Bootstrap, Tailwind, Material UI) pour gagner du temps

 Responsive de base (mobile/tablette)

 Ajouter logo, couleurs cohérentes, titres clairs

🧪 5. Démo et test
 Vérifier que tout s’affiche et réagit comme prévu

 Corriger les bugs bloquants

 Préparer un petit script pour la présentation (pitch)

🚀 6. Présentation au jury
 Pitch clair (problème, solution, démo)

 Démontrer :

La page de cours

Le QCM qui donne le score

L’exercice avec exécution du code et affichage du résultat

 Parler des pistes d’amélioration futures (plus de cours, plus d’exercices, suivi des progrès…)

⚙️ Conseil bonus hackathon :

Démarrez direct par le plus impressionnant visuellement (éditeur + exécution)

[ Accueil ]
   |
   |-- Présentation du site
   |-- Lien vers Cours / QCM / Exercice

[ Cours ]
   |
   |-- Liste des chapitres
         |-- Variables en C
         |-- Boucles
         |-- Fonctions
   |-- Contenu texte + exemples de code

[ QCM ]
   |
   |-- Série de questions
         |-- Question 1 : variable entière ?
         |-- Question 2 : symbole de fin d’instruction ?
   |-- Boutons réponse
   |-- Score ou feedback immédiat

[ Exercice ]
   |
   |-- Énoncé (ex : afficher « Hello, World! »)
   |-- Éditeur de code intégré (textarea ou éditeur JS)
   |-- Bouton « Exécuter »
   |-- Zone d'affichage du résultat (output)

[ Navigation ]
   |
   |-- Barre de navigation globale (Accueil, Cours, QCM, Exercice)
   |-- Responsive : visible sur mobile / desktop

[ Scripts et interactivité ]
   |
   |-- JS pour vérifier les réponses QCM
   |-- JS pour simuler / exécuter le code (API ou mock)

[ Style & design ]
   |
   |-- Tailwind CSS ou CSS custom
   |-- Thème cohérent (couleurs, polices)
   |-- Boutons et cartes arrondis, ombres légères
