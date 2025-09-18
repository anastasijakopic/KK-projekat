# uml_generator.py
import subprocess
import os

def generate_diagram(puml_file_path):
    """
    Generiše PNG dijagram iz PlantUML fajla koristeći plantuml.jar.
    Vraća True za uspeh, False za neuspeh.
    """
    # Proveri da li postoji ulazni fajl
    if not os.path.exists(puml_file_path):
        print(f"Greška: Fajl {puml_file_path} ne postoji.")
        return False

    # Komanda za Javu
    command = ['java', '-jar', 'plantuml.jar', puml_file_path]

    try:
        print(f"Pokrećem PlantUML za: {puml_file_path}...")
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=30)
        print("PlantUML izvršen uspešno.")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"PlantUML se završio sa greškom (status kod {e.returncode}):")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("Greška: Nije moguće pronaći 'java' komandu. Proverite da li je Java instalirana.")
        return False
    except subprocess.TimeoutExpired:
        print("Greška: PlantUML je premašio vremensko ograničenje.")
        return False