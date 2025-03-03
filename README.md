
``# 🚀 Dépôt de Scripts : Workflow `dev` → `main`

Bienvenue dans mon dépôt public ! Ce projet contient des **scripts Python et Shell**, organisés en deux branches principales :
- `dev` → **Branche de développement** (expérimentations et brouillons)
- `main` → **Branche stable** (scripts validés et prêts à l'emploi)

## 📁 Structure du Projet`` 

yd_pub/ │── dev/ # Scripts en cours de développement │ ├── python/ │ ├── shell/ │ ├── TODO.md # Liste des tâches à faire │ ├── notes.md # Notes techniques et idées │ │── stable/ # Scripts validés et stables │ ├── python/ │ ├── shell/ │ ├── VERSION.md # Suivi des versions stables │ │── tests/ # Scripts de tests avant passage en stable │── docs/ # Documentation │── scripts/ # Scripts internes (ex: move_to_stable.py) │── .github/workflows/ # Automatisations GitHub Actions │── README.md # Documentation principale │── .gitignore # Fichiers à ignorer par Git │── LICENSE # Licence du projet

yaml

CopierModifier

 ``--- 
## 🔄 Workflow Git : `dev` → `main`
### 🛠 1. Travailler sur `dev`
Tous les développements se font dans la branche `dev` :
```sh
git checkout dev  # Aller sur dev
git pull origin dev  # Mettre à jour la branche
git add .  # Ajouter les modifications
git commit -m "Message du commit"  # Commit les changements
git push origin dev  # Pousser sur GitHub`` 

----------

### 🔀 2. Déplacer un script en `stable/`

Quand un script est prêt, il est déplacé vers `stable/` :

sh

CopierModifier

`python scripts/move_to_stable.py dev/python/mon_script.py` 

Cela déplace le fichier, l’ajoute à Git et le commit automatiquement.

----------

### ✅ 3. Fusionner `dev` → `main`

Quand tout est testé et validé :

sh

CopierModifier

`git checkout main  # Aller sur la branche main
git pull origin main  # Mettre à jour la branche main
git merge dev  # Fusionner les changements de dev
git push origin main  # Pousser sur GitHub` 

Cela **valide la version stable** et déclenche un **tag automatique** via GitHub Actions.

----------

### 🔖 4. Gérer les versions avec des tags

Voir tous les tags :

sh

CopierModifier

`git tag` 

Créer et pousser un tag manuellement :

sh

CopierModifier

`git tag -a v1.0 -m "Version stable 1.0"
git push origin v1.0` 

----------

## ⚡ Alias Git pour simplifier le workflow
| Commande |Action |
|--|--|
|git dev|`Aller sur `dev` et le mettre à jour|

`git dcommit "msg"`

Commit les fichiers sur `dev`

`git dpush`

Pousser `dev` sur GitHub

`git move-to-stable chemin/fichier.py`

Déplacer un fichier en `stable/`

`git merge-main`

Fusionner `dev` → `main` et pousser

`git tags`

Voir les tags

`git tag-create vX.Y "message"`

Créer et pousser un tag

----------

## 🤖 Automatisation avec GitHub Actions

-   📌 **Fusion `dev` → `main`** déclenche automatiquement un **tag de version** via `tag-release.yml`.
-   📌 **Tests automatiques** exécutés via `.github/workflows/tests.yml`.

----------

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser et de le modifier.