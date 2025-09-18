from antlr_gen.Dart2ParserListener import Dart2ParserListener

class DiagramGenerator(Dart2ParserListener):
    def __init__(self):
        super().__init__()
        self.uml_lines = []
        self.indent_level = 0
        self.in_expression_statement = False  # DODATO: Pratimo da li smo u expression statement

    def clean_text(self, text):
        """Očisti tekst za PlantUML - ukloni specijalne karaktere"""
        text = text.replace(';', '').replace('"', '\\"')
        return text.strip()

    def enterExpressionStatement(self, ctx):
        # Označimo da smo u expression statement
        self.in_expression_statement = True
        expression_text = self.clean_text(ctx.getText())
        if expression_text:
            self.uml_lines.append(f":{expression_text};")

    def exitExpressionStatement(self, ctx):
        # Izlazimo iz expression statement
        self.in_expression_statement = False

    def enterFunctionCall(self, ctx):
        # Preskoči function call ako smo već u expression statement
        if not self.in_expression_statement:
            func_name = ctx.ID().getText()
            args = ctx.argumentList()
            if args:
                args_text = self.clean_text(args.getText())
                self.uml_lines.append(f":{func_name}({args_text});")
            else:
                self.uml_lines.append(f":{func_name}();")

    # Ostale metode ostaju iste...
    def enterVariableDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        expression = ctx.expression()
        if expression:
            value = self.clean_text(expression.getText())
            self.uml_lines.append(f":{var_name} = {value};")
        else:
            self.uml_lines.append(f":{var_name} = ...;")

    def enterReturnStatement(self, ctx):
        expression = ctx.expression()
        if expression:
            return_value = self.clean_text(expression.getText())
            self.uml_lines.append(f":return {return_value};")
        else:
            self.uml_lines.append(":return;")

    def enterIfStatement(self, ctx):
        condition = self.clean_text(ctx.expression().getText())
        self.uml_lines.append(f"if ({condition}) then (yes)")

    def exitIfStatement(self, ctx):
        if ctx.elseStatement():
            self.uml_lines.append("else (no)")
        self.uml_lines.append("endif")

    def enterForStatement(self, ctx):
        init = self.clean_text(ctx.forInitializer().getText()) if ctx.forInitializer() else ""
        condition = self.clean_text(ctx.expression().getText()) if ctx.expression() else "true"
        increment = self.clean_text(ctx.forIterator().getText()) if ctx.forIterator() else ""
        loop_header = f"{init}; {condition}; {increment}"
        self.uml_lines.append(f"group for ({loop_header})")

    def exitForStatement(self, ctx):
        self.uml_lines.append("end group")

    def enterWhileStatement(self, ctx):
        condition = self.clean_text(ctx.expression().getText())
        self.uml_lines.append(f"while ({condition})")

    def exitWhileStatement(self, ctx):
        self.uml_lines.append("end while")

    def enterBlock(self, ctx):
        if self.indent_level > 0:
            self.uml_lines.append("group")
        self.indent_level += 1

    def exitBlock(self, ctx):
        self.indent_level -= 1
        if self.indent_level > 0:
            self.uml_lines.append("end group")

    def enterEveryRule(self, ctx):
        pass

    def exitEveryRule(self, ctx):
        pass