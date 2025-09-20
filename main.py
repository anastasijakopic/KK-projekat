import sys
from antlr4 import *
from antlr_gen.DartLexer import DartLexer
from antlr_gen.DartParser import DartParser
from diagram_generator import DiagramGenerator
from uml_generator import generate_diagram
import os

def main():
    if len(sys.argv) != 2:
        print("Upotreba: python main.py <putanja_do_dart_fajla>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_puml = f"output/{base_name}.puml"

    try:
        input_stream = FileStream(input_file)
    except FileNotFoundError:
        print(f"Greška: Fajl '{input_file}' ne postoji.")
        sys.exit(1)

    lexer = DartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DartParser(token_stream)

    print(f"Parsiram fajl: {input_file}...")
    
    # Koristimo compilationUnit kao početno pravilo
    tree = parser.compilationUnit()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Parsiranje prekinuto zbog sintaksnih grešaka.")
        sys.exit(1)
    print("Sintaksna analiza uspešna.")

    # GENERISANJE DIJAGRAMA
    print("Generišem PlantUML kod...")
    walker = ParseTreeWalker()
    diagram_generator = DiagramGenerator()
    walker.walk(diagram_generator, tree)

    os.makedirs("output", exist_ok=True)
    with open(output_puml, "w") as f:
        uml_code = diagram_generator.get_plantuml_code()
        full_uml_code = f"@startuml\n{uml_code}\n@enduml"
        f.write(full_uml_code)
    
    print(f"PlantUML kod sačuvan u: {output_puml}")

    print("Generišem PNG dijagram...")
    success = generate_diagram(output_puml)
    if success:
        print(f"UML dijagram uspešno generisan! Proveri output folder.")
    else:
        print("Greška pri generisanju PNG dijagrama.")

if __name__ == '__main__':
    main()