import os
import sys
import subprocess

def move_file(file_path):
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
        return

    stable_path = file_path.replace("dev/", "stable/", 1)
    os.makedirs(os.path.dirname(stable_path), exist_ok=True)

    os.rename(file_path, stable_path)
    print(f"✅ Fichier déplacé : {file_path} → {stable_path}")

    # Ajouter et commit le fichier
    subprocess.run(["git", "add", stable_path], check=True)
    subprocess.run(["git", "commit", "-m", f"Déplacement de {file_path} vers stable"], check=True)
    subprocess.run(["git", "push", "origin", "dev"], check=True)
    print("✅ Modifications poussées sur dev.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python scripts/move_to_stable.py <fichier>")
        sys.exit(1)

    move_file(sys.argv[1])
