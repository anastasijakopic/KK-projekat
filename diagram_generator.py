from antlr_gen.DartParserListener import DartParserListener

class DiagramGenerator(DartParserListener):
    def __init__(self):
        super().__init__()
        self.uml_lines = []
        self.in_for = False
        self.in_if = False
        self.for_condition = ""

    def clean_text(self, text):
        if text:
            text = text.replace(';', '').replace('"', '\\"').strip()
            text = text.replace('var ', '')
            return text
        return ""

    # FUNKCIJE - POČETAK
    def enterFunctionSignature(self, ctx):
        if ctx.identifier():
            func_name = ctx.identifier().getText()
            self.uml_lines.append("start")
            self.uml_lines.append(f":{func_name}()")

    # VARIJABLE
    def enterInitializedVariableDeclaration(self, ctx):
        try:
            if hasattr(ctx, 'declaredIdentifier') and ctx.declaredIdentifier():
                declared_ctx = ctx.declaredIdentifier()
                if hasattr(declared_ctx, 'identifier') and declared_ctx.identifier():
                    var_name = declared_ctx.identifier().getText()
                    
                    if ctx.getChildCount() > 1 and ctx.getChild(1).getText() == '=':
                        value = self.clean_text(ctx.expr().getText())
                        if value:
                            self.uml_lines.append(f":{var_name} = {value};")
        except:
            pass

    # FOR PETLJE
    def enterForStatement(self, ctx):
        self.in_for = True
        self.for_condition = ""
        
        # Pokušaj da izvučeš for uslov iz forLoopParts
        if ctx.forLoopParts():
            for_parts = ctx.forLoopParts()
            # Uslov (drugi dio for petlje)
            if hasattr(for_parts, 'expr') and for_parts.expr():
                self.for_condition = self.clean_text(for_parts.expr().getText())
            
            # Inicijalizacija (prvi dio for petlje)
            if hasattr(for_parts, 'forInitializerStatement') and for_parts.forInitializerStatement():
                init_stmt = for_parts.forInitializerStatement()
                if hasattr(init_stmt, 'expr') and init_stmt.expr():
                    init_text = self.clean_text(init_stmt.expr().getText())
                    if init_text:
                        self.uml_lines.append(f":{init_text};")

        if self.for_condition:
            self.uml_lines.append(f"group for ({self.for_condition})")
        else:
            self.uml_lines.append("group for")

    def exitForStatement(self, ctx):
        self.in_for = False
        self.uml_lines.append("end group")

    # IF STATEMENTS
    def enterIfStatement(self, ctx):
        self.in_if = True
        if ctx.expr():
            condition = self.clean_text(ctx.expr().getText())
            self.uml_lines.append(f"if ({condition}) then (yes)")

    def exitIfStatement(self, ctx):
        self.in_if = False
        self.uml_lines.append("endif")

    # EXPRESSION STATEMENTS (izuzev u for/if blokovima)
    def enterExpressionStatement(self, ctx):
        if ctx.expr() and not self.in_for and not self.in_if:
            expr_text = self.clean_text(ctx.expr().getText())
            if expr_text and expr_text not in ['', '{}', '()']:
                expr_text = expr_text.replace('var ', '')
                self.uml_lines.append(f":{expr_text};")

    # ASSIGNMENT U FOR/IF BLOKOVIMA
    def enterExpr(self, ctx):
        if (self.in_for or self.in_if) and ctx.getChildCount() > 2:
            # Pokušaj da prepoznaš assignment (npr. sum = sum + numbers[i])
            try:
                left = self.clean_text(ctx.getChild(0).getText())
                op = self.clean_text(ctx.getChild(1).getText())
                right = self.clean_text(ctx.getChild(2).getText())
                
                if op == '=' and left and right:
                    self.uml_lines.append(f":{left} = {right};")
            except:
                pass

    # FUNCTION CALLS
    def enterPostfixExpression(self, ctx):
        try:
            if ctx.selector() and ctx.primary():
                primary_ctx = ctx.primary()
                if hasattr(primary_ctx, 'identifier') and primary_ctx.identifier():
                    func_name = primary_ctx.identifier().getText()
                    
                    selector_ctx = ctx.selector()
                    if hasattr(selector_ctx, 'argumentPart') and selector_ctx.argumentPart():
                        args_ctx = selector_ctx.argumentPart()
                        if hasattr(args_ctx, 'arguments') and args_ctx.arguments():
                            args_text = self.clean_text(args_ctx.arguments().getText())
                            args_text = args_text.replace('(', '').replace(')', '')
                            if args_text:
                                self.uml_lines.append(f":{func_name}({args_text});")
        except:
            pass

    # COMPILATION UNIT - KRAJ
    def exitCompilationUnit(self, ctx):
        self.uml_lines.append("stop")

    def get_plantuml_code(self):
        # Filtriraj duplikate i prazne linije
        filtered_lines = []
        seen = set()
        for line in self.uml_lines:
            if line and line not in seen and not line.endswith('();'):
                filtered_lines.append(line)
                seen.add(line)
        return "\n".join(filtered_lines)