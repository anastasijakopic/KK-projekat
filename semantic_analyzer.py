# semantic_analyzer.py
from antlr_gen.Dart2ParserListener import Dart2ParserListener

class SemanticAnalyzer(Dart2ParserListener):
    def __init__(self):
        super().__init__()
        self.symbol_table = {} # Rečnik za čuvanje promenljivih: {ime: tip}
        self.errors = []       # Lista za sve greške koje naidjemo

    # TODO: DODATI METODE ZA ANALIZU
    
