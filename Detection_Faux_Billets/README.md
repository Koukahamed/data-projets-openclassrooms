# 💰 Détection automatique de faux billets

## 📌 Contexte du projet
L'**Organisation nationale de lutte contre le faux-monnayage (ONCFM)** cherche à mettre en place un algorithme permettant d'identifier automatiquement les faux billets en euros. Cette détection repose sur l'analyse des **dimensions géométriques** des billets, qui présentent des différences subtiles entre les vrais et les faux.

## 🎯 Objectifs
L'objectif est de concevoir un algorithme capable de classer les billets comme **vrais** ou **faux** en fonction de leurs caractéristiques géométriques. Pour cela, nous allons :
- Effectuer une **analyse exploratoire des données**.
- Développer deux approches de classification :
  - **Régression logistique**
  - **K-Means avec utilisation des centroïdes pour la prédiction**
- Évaluer les performances des modèles avec une **matrice de confusion**.

## 📂 Modèle de données
Les billets sont caractérisés par six dimensions géométriques :
- `length` : Longueur du billet (mm)
- `height_left` : Hauteur côté gauche (mm)
- `height_right` : Hauteur côté droit (mm)
- `margin_up` : Marge supérieure (mm)
- `margin_low` : Marge inférieure (mm)
- `diagonal` : Diagonale du billet (mm)

Nous disposons d'un **jeu de données** de **1 500 billets** (1 000 vrais et 500 faux), fourni sous forme de fichier CSV (`billets_production.csv`).

## 🛠️ Technologies utilisées
- **Langages** : Python ou R
- **Bibliothèques Python** : Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Outils** : Jupyter Notebook / Google Colab / VS Code

## 🚀 Installation & Exécution
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/ton-user/detection-faux-billets.git
   cd detection-faux-billets
   ```
2. **Créer un environnement virtuel** (optionnel) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
4. **Exécuter le notebook** :
   Ouvrir `notebook_detection.ipynb` et exécuter les cellules une par une.

## 📊 Évaluation des modèles
L'algorithme sera évalué à l'aide de **matrices de confusion** afin de comparer le nombre de **faux positifs** et **faux négatifs** pour chaque méthode (régression logistique et K-Means).

## 📜 Livrables attendus
- Un **notebook** Python ou R contenant :
  - L'analyse exploratoire des données
  - L'implémentation des algorithmes
  - L'évaluation des modèles
- Un fichier **billets_production