from antlr_gen.Dart2ParserListener import Dart2ParserListener

class DiagramGenerator(Dart2ParserListener):
    def __init__(self):
        super().__init__()
        self.uml_lines = [] # Ovdje ćemo skladištiti sve linije PlantUML koda

    # 1. OBRADA OSNOVNIH IZRAZA (npr. "x = 5;")
    def enterExpressionStatement(self, ctx):
        expression_text = ctx.getText() # Ovo je grubo, ali za početak
        if expression_text: # Da izbegnemo prazne linije
            self.uml_lines.append(f":{expression_text};")

    # 2. OBRADA IF IZJAVA
    def enterIfStatement(self, ctx):
        # Pristupimo uslovnom izrazu unutar ifa
        condition_ctx = ctx.expression()
        condition_text = condition_ctx.getText() if condition_ctx else "true"
        self.uml_lines.append(f"if ({condition_text}) then (yes)")

    def exitIfStatement(self, ctx):
        # Proverimo da li postoji ELSE grana
        else_stmt = ctx.elseStatement()
        if else_stmt is not None:
            self.uml_lines.append("else (no)")
        self.uml_lines.append("endif")

    # 3. OBRADA FOR PETLJI (Jednostavan 'for' poput onog u C-u)
    def enterForStatement(self, ctx):
        # Ovo je pojednostavljeno. Trebalo bi bolje parsirati inicijalizaciju, uslov i inkrement.
        for_loop_header = ctx.getChild(2).getText() # Ovo će uhvatiti deo unutar ()
        self.uml_lines.append(f"group for ({for_loop_header})")

    def exitForStatement(self, ctx):
        self.uml_lines.append("end group")

    # TODO: DODAJ METODE ZA:
    # - enterWhileStatement / exitWhileStatement
    # - enterDoWhileStatement / exitDoWhileStatement
    # - enterBlock / exitBlock (možda za označavanje početka/kraja bloka '{ }')
    # - enterReturnStatement

    # ctx.getText() često vraća "ružan" tekst bez formatiranja.
    # Kasnije možeš da poboljšaš ovo da lepše izgleda u dijagramu.