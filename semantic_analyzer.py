from antlr_gen.Dart2ParserListener import Dart2ParserListener

class SemanticAnalyzer(Dart2ParserListener):
    def __init__(self):
        super().__init__()
        self.symbol_table = {}  # {ime_varijable: tip}
        self.errors = []
        self.current_scope = "global"

    def enterVariableDeclaration(self, ctx):
        # Dobij tip varijable (var, int, String...)
        type_ctx = ctx.type_() 
        var_type = type_ctx.getText() if type_ctx else 'var'
        
        # Dobij ime varijable
        var_name = ctx.ID().getText()
        
        # Provjeri da li varijabla već postoji
        if var_name in self.symbol_table:
            self.errors.append(f"[SEMANTICKA GRESKA] Varijabla '{var_name}' je vec deklarisana.")
        else:
            self.symbol_table[var_name] = var_type
        print(f"Deklarisana varijabla: {var_name} = {var_type}")  # DEBUG

    def enterAssignment(self, ctx):
        var_name = ctx.ID().getText()
        # Provjeri da li varijabla postoji prije korištenja
        if var_name not in self.symbol_table:
            self.errors.append(f"[SEMANTICKA GRESKA] Varijabla '{var_name}' nije deklarisana.")
        print(f"Dodjela varijable: {var_name}")  # DEBUG

    def enterExpression(self, ctx):
        # Osnovna provjera tipova za operacije - SAMO ZA BINARNE OPERACIJE
        if ctx.getChildCount() == 3:  # Binarna operacija (npr. a + b)
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            op = ctx.getChild(1).getText()
            
            # Dobij tipove operanada
            left_type = self.get_expression_type(left)
            right_type = self.get_expression_type(right)
            
            # Provjeri kompatibilnost tipova
            if left_type and right_type and left_type != right_type:
                self.errors.append(f"[SEMANTICKA GRESKA] Operator '{op}' ne moze se koristiti za tipove '{left_type}' i '{right_type}'")
            print(f"Operacija: {left_type} {op} {right_type}")  # DEBUG

    def get_expression_type(self, ctx):
        # Poboljšana metoda za određivanje tipa izraza
        text = ctx.getText()
        
        # Provjeri literale
        if text.isdigit():
            return 'int'
        elif self.is_float(text):
            return 'double'
        elif text in ['true', 'false']:
            return 'bool'
        elif text.startswith('"') and text.endswith('"'):
            return 'String'
        
        # Provjeri da li je varijabla
        if hasattr(ctx, 'ID'):
            var_name = ctx.ID().getText() if ctx.ID() else text
            return self.symbol_table.get(var_name)
        
        # Rekurzivno provjeri dubije ako je složen izraz
        if hasattr(ctx, 'getChildCount') and ctx.getChildCount() > 0:
            return self.get_expression_type(ctx.getChild(0))
        
        return None

    def is_float(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False

    # Dodajemo prazne metode za sve kontekste koje koristimo
    def enterEveryRule(self, ctx):
        pass  # Prazna implementacija za sva pravila

    def exitEveryRule(self, ctx):
        pass  # Prazna implementacija za sva pravila

    # DODAJ OVO U semantic_analyzer.py

    def enterFunctionCall(self, ctx):
        # Provjeri da li se poziva postojeca funkcija
        func_name = ctx.ID().getText()
        if func_name not in ['print', 'main']:  # Dodaj ostale built-in funkcije
            self.errors.append(f"[SEMANTIČKA GREŠKA] Funkcija '{func_name}' nije deklarisana.")

    def enterReturnStatement(self, ctx):
        # Provjeri da li return odgovara tipu funkcije
        if ctx.expression():
            return_type = self.get_expression_type(ctx.expression())
            # Ovo zahteva da pratiš trenutnu funkciju koja se analizira
            print(f"Return tip: {return_type}")  # DEBUG