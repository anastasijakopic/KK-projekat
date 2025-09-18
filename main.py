# main.py
import sys
from antlr4 import *
from antlr_gen.Dart2Lexer import Dart2Lexer
from antlr_gen.Dart2Parser import Dart2Parser
from semantic_analyzer import SemanticAnalyzer
from diagram_generator import DiagramGenerator
from uml_generator import generate_diagram
import os

def main():
    # 1. Proveri argumente komandne linije
    if len(sys.argv) != 2:
        print("Upotreba: python main.py <putanja_do_dart_fajla>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(input_file))[0] # 'test' iz 'test.dart'
    output_puml = f"output/{base_name}.puml"

    # 2. Pročitaj ulazni Dart kod
    try:
        input_stream = FileStream(input_file)
    except FileNotFoundError:
        print(f"Greška: Fajl '{input_file}' ne postoji.")
        sys.exit(1)

    # 3. Inicijalizuj lexer i parser
    lexer = Dart2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Dart2Parser(token_stream)

    # 4. Zapocni parsiranje (počni od pravila 'libraryUnit')
    print(f"Parsiram fajl: {input_file}...")
    tree = parser.libraryUnit() # Ovo je "početno pravilo" za Dart gramatiku

    # 5. Proveri sintaksne greške
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Parsiranje prekinuto zbog sintaksnih grešaka.")
        sys.exit(1)
    print("Sintaksna analiza uspešna.")

    # 6. Izvrši SEMANTIČKU ANALIZU
    print("Pokrećem semantičku analizu...")
    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)

    # Proveri da li je bilo semantičkih grešaka
    if semantic_analyzer.errors:
        print("Pronađene su semantičke greške:")
        for error in semantic_analyzer.errors:
            print(f"  {error}")
        print("Generisanje dijagrama preskočeno.")
        sys.exit(1)
    print("Semantička analiza uspešna.")

    # 7. GENERIŠI PLANTUML KOD (ako nema grešaka)
    print("Generišem PlantUML kod...")
    diagram_generator = DiagramGenerator()
    walker.walk(diagram_generator, tree)

    # Sačuvaj generisani PlantUML kod
    os.makedirs("output", exist_ok=True)
    with open(output_puml, "w") as f:
        # Započni i završi PlantUML okvir
        full_uml_code = "@startuml\nstart\n" + "\n".join(diagram_generator.uml_lines) + "\nstop\n@enduml"
        f.write(full_uml_code)
    print(f"PlantUML kod sačuvan u: {output_puml}")

    # 8. GENERIŠI PNG DIJAGRAM iz .puml fajla
    print("Generišem PNG dijagram...")
    success = generate_diagram(output_puml)
    if success:
        print(f"UML dijagram uspešno generisan! Proveri output folder.")
    else:
        print("Greška pri generisanju PNG dijagrama.")

if __name__ == '__main__':
    main()