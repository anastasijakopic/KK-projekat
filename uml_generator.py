import os
import subprocess
import shutil

OUTPUT_FOLDER = "output"
PLANTUML_JAR = "plantuml.jar"

def generate_uml_image(plantuml_code: str, base_name: str):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    if not shutil.which("java"):
        print("[GREŠKA] Java nije instalirana ili nije dostupna u PATH-u.")
        return

    if not os.path.exists(PLANTUML_JAR):
        print(f"[GREŠKA] Ne postoji fajl: {PLANTUML_JAR}")
        return

    puml_path = os.path.join(OUTPUT_FOLDER, base_name + ".puml")
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write("@startuml\n")
        f.write(plantuml_code)
        f.write("\n@enduml\n")

    subprocess.run(["java", "-jar", PLANTUML_JAR, puml_path], check=True)
    print(f"Dijagram generisan: {os.path.join(OUTPUT_FOLDER, base_name + '.png')}")
