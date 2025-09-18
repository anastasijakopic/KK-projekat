import sys
from antlr4 import *
from antlr_gen.Dart2Lexer import Dart2Lexer
from antlr_gen.Dart2Parser import Dart2Parser
from semantic_analyzer import SemanticAnalyzer
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
        print(f"Greska: Fajl '{input_file}' ne postoji.")
        sys.exit(1)

    lexer = Dart2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Dart2Parser(token_stream)

    print(f"Parsiram fajl: {input_file}...")
    tree = parser.program()  # PROMJENJENO: program() umjesto libraryUnit()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Parsiranje prekinuto zbog sintaksnih gresaka.")
        sys.exit(1)
    print("Sintaksna analiza uspjesna.")

    print("Pokrecem semantičku analizu...")
    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)

    if semantic_analyzer.errors:
        print("Pronadjene su semantičke greske:")
        for error in semantic_analyzer.errors:
            print(f"  {error}")
        print("Generisanje dijagrama preskoceno.")
        sys.exit(1)
    print("Semantička analiza uspjesna.")

    print("Generisem PlantUML kod...")
    diagram_generator = DiagramGenerator()
    walker.walk(diagram_generator, tree)

    os.makedirs("output", exist_ok=True)
    with open(output_puml, "w") as f:
        full_uml_code = "@startuml\nstart\n" + "\n".join(diagram_generator.uml_lines) + "\nstop\n@enduml"
        f.write(full_uml_code)
    print(f"PlantUML kod sacuvan u: {output_puml}")

    print("Generisem PNG dijagram...")
    success = generate_diagram(output_puml)
    if success:
        print(f"UML dijagram uspjesno generisan! Proveri output folder.")
    else:
        print("Greska pri generisanju PNG dijagrama.")

if __name__ == '__main__':
    main()