from antlr_gen.DartParserListener import DartParserListener

class SemanticAnalyzer(DartParserListener):
    def __init__(self):
        super().__init__()
        self.symbol_table = {}
        self.errors = []

    def enterVariableDeclaration(self, ctx):
        try:
            if hasattr(ctx, 'initializedIdentifier') and ctx.initializedIdentifier():
                var_text = ctx.initializedIdentifier().getText()
                if '=' in var_text:
                    var_name = var_text.split('=')[0].strip()
                else:
                    var_name = var_text.strip()
                
                if var_name in self.symbol_table:
                    self.errors.append(f"[SEMANTIČKA GREŠKA] Varijabla '{var_name}' je već deklarisana.")
                else:
                    self.symbol_table[var_name] = 'var'
        except:
            pass

    def enterEveryRule(self, ctx):
        pass

    def exitEveryRule(self, ctx):
        pass