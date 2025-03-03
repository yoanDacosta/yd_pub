## 🔄 Workflow Git : `dev` → `main`
### 🛠 1. Travailler sur `dev`
Tous les développements se font dans la branche `dev` :
```sh
git checkout dev  # Aller sur dev
git pull origin dev  # Mettre à jour la branche
git add .  # Ajouter les modifications
git commit -m "Message du commit"  # Commit les changements
git push origin dev  # Pousser sur GitHub`` 
```
----------

### 🔀 2. Déplacer un script en `stable/`

Quand un script est prêt, il est déplacé vers `stable/` :

`python scripts/move_to_stable.py dev/python/mon_script.py` 

Cela déplace le fichier, l’ajoute à Git et le commit automatiquement.

----------

### ✅ 3. Fusionner `dev` → `main`

Quand tout est testé et validé :


`git checkout main  # Aller sur la branche main
git pull origin main  # Mettre à jour la branche main
git merge dev  # Fusionner les changements de dev
git push origin main  # Pousser sur GitHub` 

Cela **valide la version stable** et déclenche un **tag automatique** via GitHub Actions.


## ⚡ Alias Git pour simplifier le workflow
| Commande |Action |
|--|--|
|`git dev`| Aller sur `dev` et le mettre à jour|
|`git dcommit "msg"`| Commit les fichiers sur `dev`|
|`git dpush` |Pousser `dev` sur GitHub|
|`git move-to-stable chemin/fichier.py`|Déplacer un fichier en `stable/`|
|`git merge-main`|Fusionner `dev` → `main` et pousser|
| | |
----------