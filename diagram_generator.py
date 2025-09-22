from antlr_gen.Dart2ParserListener import Dart2ParserListener
from antlr_gen.Dart2Parser import Dart2Parser

class DartActivityListenerImpl(Dart2ParserListener):
    def __init__(self):
        self.uml_lines = []
        self.label_count = 0
        self.inside_function = False

    def get_plantuml(self):
        return "\n".join(self.uml_lines)

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    # -------------------------------
    # FUNKCIJE
    # -------------------------------
    def enterFunctionDecl(self, ctx: Dart2Parser.FunctionDeclContext):
        self.uml_lines.append("start")
        self.inside_function = True

    def exitFunctionDecl(self, ctx: Dart2Parser.FunctionDeclContext):
        self.uml_lines.append("stop")
        self.inside_function = False

    # -------------------------------
    # RETURN
    # -------------------------------
    def enterReturnStatement(self, ctx: Dart2Parser.ReturnStatementContext):
        if ctx.expression():
            expr_text = ctx.expression().getText()
            self.uml_lines.append(f":return {expr_text};")
        else:
            self.uml_lines.append(":return;")

    # -------------------------------
    # IF / ELSE
    # -------------------------------
    def enterIfStatement(self, ctx: Dart2Parser.IfStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"if ({condition}) then (yes)")

    def exitIfStatement(self, ctx: Dart2Parser.IfStatementContext):
        if ctx.ELSE():
            self.uml_lines.insert(-1, "else (no)")
        self.uml_lines.append("endif")

    # -------------------------------
    # FOR
    # -------------------------------
    '''def enterForStatement(self, ctx: Dart2Parser.ForStatementContext):
        var_name = ctx.ID().getText() if ctx.ID() else "?"
        expr = ctx.expression().getText() if ctx.expression() else "?"
        self.uml_lines.append(f"group for {var_name} in {expr}")'''
    def enterForStatement(self, ctx: Dart2Parser.ForStatementContext):
        self.in_for = True
        self.for_condition = ""
        
        if ctx.forLoopParts():
            for_parts = ctx.forLoopParts()
            
            # Inicijalizacija
            if for_parts.forInitializerStatement():
                init_stmt = for_parts.forInitializerStatement()
                if init_stmt.localVariableDeclaration():
                    var_text = init_stmt.localVariableDeclaration().getText()
                    self.uml_lines.append(f":{var_text};")
            
            # Uslov
            if for_parts.expression():
                self.for_condition = self.clean_text(for_parts.expression().getText())
            
            # Korak
            if for_parts.expressionList():
                step_text = self.clean_text(for_parts.expressionList().getText())
                if step_text:
                    self.uml_lines.append(f":{step_text};")

            # Foreach stil
            if for_parts.declaredIdentifier() and for_parts.expression():
                var_name = for_parts.declaredIdentifier().getText()
                expr_text = for_parts.expression().getText()
                self.uml_lines.append(f"group foreach {var_name} in {expr_text}")

        if self.for_condition:
            self.uml_lines.append(f"group for ({self.for_condition})")
        else:
            self.uml_lines.append("group for")

    def enterListLiteral(self, ctx: Dart2Parser.ListLiteralContext):
        if ctx.expressionList():
            elements = [self.clean_text(expr.getText()) for expr in ctx.expressionList().expression()]
            list_text = f"[{', '.join(elements)}]"
            self.uml_lines.append(f":{list_text};")

    def exitForStatement(self, ctx):
        self.in_for = False
        self.uml_lines.append("end group")

    

    # -------------------------------
    # WHILE / DO-WHILE
    # -------------------------------
    def enterWhileStatement(self, ctx: Dart2Parser.WhileStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"while ({condition}) is (true)")

    def exitWhileStatement(self, ctx: Dart2Parser.WhileStatementContext):
        self.uml_lines.append("endwhile")

    def enterDoWhileStatement(self, ctx: Dart2Parser.DoWhileStatementContext):
        self.uml_lines.append("repeat")

    def exitDoWhileStatement(self, ctx: Dart2Parser.DoWhileStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"repeat while ({condition})")

    # -------------------------------
    # IZRAZI I PRINT
    # -------------------------------
    def enterExprStatement(self, ctx: Dart2Parser.ExprStatementContext):
        expr_text = ctx.expression().getText()
        if "+=" in expr_text:
            var, value = expr_text.split("+=")
            var = var.strip()
            value = value.strip()
            expr_text = f"{var} = {var} + {value}"
        self.uml_lines.append(f":{expr_text};")

    # -------------------------------
    # DEKLARACIJE PROMENLJIVIH
    # -------------------------------
    def enterVarDecl(self, ctx: Dart2Parser.VarDeclContext):
        var_name = ctx.ID().getText()
        if ctx.expression():
            value = ctx.expression().getText()
            self.uml_lines.append(f":{var_name} = {value};")

    def enterFinalDecl(self, ctx: Dart2Parser.FinalDeclContext):
        var_name = ctx.ID().getText()
        if ctx.expression():
            value = ctx.expression().getText()
            self.uml_lines.append(f":{var_name} = {value};")

    def enterConstDecl(self, ctx: Dart2Parser.ConstDeclContext):
        var_name = ctx.ID().getText()
        if ctx.expression():
            value = ctx.expression().getText()
            self.uml_lines.append(f":{var_name} = {value};")

    # -------------------------------
    # PRINT
    # -------------------------------
    def enterPrintStatement(self, ctx: Dart2Parser.PrintStatementContext):
        if ctx.expression():
            expr_text = ctx.expression().getText()
            self.uml_lines.append(f":print {expr_text};")
        else:
            self.uml_lines.append(":print;")

    # -------------------------------
    # SWITCH / CASE
    # -------------------------------
    def enterSwitchStatement(self, ctx: Dart2Parser.SwitchStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"switch ({condition})")

    def enterSwitchCase(self, ctx: Dart2Parser.SwitchCaseContext):
        expr = ctx.expression()
        label = expr.getText() if expr else "default"
        self.uml_lines.append(f"case ({label})")

    def enterDefaultCase(self, ctx: Dart2Parser.DefaultCaseContext):
        self.uml_lines.append("case (default)")

    def exitSwitchStatement(self, ctx: Dart2Parser.SwitchStatementContext):
        self.uml_lines.append("endswitch")

    # -------------------------------
    # TRY / CATCH / FINALLY
    # -------------------------------
    def enterTryStatement(self, ctx: Dart2Parser.TryStatementContext):
        self.uml_lines.append("group try")

    def enterCatchClause(self, ctx: Dart2Parser.CatchClauseContext):
        var_name = ctx.ID().getText() if ctx.ID() else "exception"
        self.uml_lines.append(f"group catch ({var_name})")

    def exitCatchClause(self, ctx: Dart2Parser.CatchClauseContext):
        self.uml_lines.append("end group")

    def enterFinallyClause(self, ctx: Dart2Parser.FinallyClauseContext):
        self.uml_lines.append("group finally")

    def exitFinallyClause(self, ctx: Dart2Parser.FinallyClauseContext):
        self.uml_lines.append("end group")

    def exitTryStatement(self, ctx: Dart2Parser.TryStatementContext):
        self.uml_lines.append("end group")

    # -------------------------------
    # BREAK / CONTINUE / THROW
    # -------------------------------
    def enterBreakStatement(self, ctx: Dart2Parser.BreakStatementContext):
        self.uml_lines.append(":break;")

    def enterContinueStatement(self, ctx: Dart2Parser.ContinueStatementContext):
        self.uml_lines.append(":continue;")

    def enterThrowStatement(self, ctx: Dart2Parser.ThrowStatementContext):
        expr = ctx.expression().getText()
        self.uml_lines.append(f":throw {expr};")

    def clean_text(self, text):
        if text:
            text = text.replace(';', '').replace('"', '\\"').strip()
            text = text.replace('var ', '')
            return text
        return ""
