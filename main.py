import os
import sys
from antlr4 import *
from antlr_gen.Dart2Lexer import Dart2Lexer
from antlr_gen.Dart2Parser import Dart2Parser
from diagram_generator import DartActivityListenerImpl
from semantic_analyzer import SemanticAnalyzer
from uml_generator import generate_uml_image

INPUT_FOLDER = "examples"
OUTPUT_FOLDER = "output"

def parse_dart_file(filename):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = Dart2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Dart2Parser(stream)
    print(f"Parsiram fajl: {filename}...")
    tree = parser.program()

    
    analyzer = SemanticAnalyzer()
    errors = analyzer.analyze(tree)
    if errors:
        print("\n".join(errors))
        return None

    listener = DartActivityListenerImpl()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.get_plantuml()

def main():
    if len(sys.argv) < 2:
        print("Upotreba: python main.py file1.dart file2.dart ...")
        sys.exit(1)

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for fname in sys.argv[1:]:
        input_path = os.path.join(INPUT_FOLDER, fname)
        if not os.path.isfile(input_path):
            print(f"File not found: {input_path}")
            continue

        base_name = os.path.splitext(fname)[0]
        puml_path = os.path.join(OUTPUT_FOLDER, base_name + ".puml")
        png_path = os.path.join(OUTPUT_FOLDER, base_name + ".png")

        print(f"\nGenerisanje dijagrama za {fname}...")

        uml_code = parse_dart_file(input_path)
        if uml_code is None:
            print(f"Preskakanje generisanja za {fname} zbog semantičkih grešaka.\n")
            continue

        generate_uml_image(uml_code, base_name)

if __name__ == "__main__":
    main()
