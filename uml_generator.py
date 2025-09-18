import subprocess
import os

def generate_diagram(puml_file_path):
    """
    Generiše PNG dijagram iz PlantUML fajla koristeći plantuml.jar.
    Vraća True za uspeh, False za neuspeh.
    """
    if not os.path.exists(puml_file_path):
        print(f"Greska: Fajl {puml_file_path} ne postoji.")
        return False

    command = ['java', '-jar', 'plantuml.jar', puml_file_path]

    try:
        print(f"Pokrecem PlantUML za: {puml_file_path}...")
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=30)
        print("PlantUML izvrsen uspjesno.")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"PlantUML se zavrsio sa greskom (status kod {e.returncode}):")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("Greska: Nije moguce pronaci 'java' komandu. Provjerite da li je Java instalirana.")
        return False
    except subprocess.TimeoutExpired:
        print("Greska: PlantUML je premasio vremensko ogranicenje.")
        return False