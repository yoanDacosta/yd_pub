
Bienvenue dans mon dépôt public ! Ce projet contient des **scripts Python et Shell**, organisés en deux branches principales :
- `dev` → **Branche de développement** (expérimentations et brouillons)
- `main` → **Branche stable** (scripts validés et prêts à l'emploi)

## 📁 Structure du Projet`` 
```bash
yd_pub/ 
│── dev/ # Scripts en cours de développement 
│ ├── python/ 
│ ├── shell/ 
│ ├── TODO.md # Liste des tâches à faire 
│ ├── notes.md # Notes techniques et idées 
│ │── stable/ # Scripts validés et stables 
│ ├── python/ 
│ ├── shell/ 
│ ├── VERSION.md # Suivi des versions stables 
│ │── tests/ # Scripts de tests avant passage en stable 
│── docs/ # Documentation 
│── scripts/ # Scripts internes (ex: move_to_stable.py) 
│── .github/workflows/ # Automatisations GitHub Actions 
│── README.md # Documentation principale 
│── LICENSE # Licence du projet
```
## 🤖 Automatisation avec GitHub Actions

-   📌 **Fusion `dev` → `main`** déclenche automatiquement un **tag de version** via `tag-release.yml`.
-   📌 **Tests automatiques** exécutés via `.github/workflows/tests.yml`.

----------

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser et de le modifier.