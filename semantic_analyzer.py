from antlr4 import *
from antlr_gen.Dart2ParserListener import Dart2ParserListener
from antlr_gen.Dart2Parser import Dart2Parser
import re

class SemanticAnalyzer(Dart2ParserListener):
    def __init__(self):
        self.global_symbols = {}
        self.local_symbols = {}
        self.errors = []
        self.reserved_literals = {"true", "false", "null"}
        self.builtin_identifiers = {"print"}
        self.builtin_properties = {"hashCode", "runtimeType"}

    # -------------------------------
    # POMOĆNE METODE
    # -------------------------------
    def _current_symbols(self):
        return {**self.global_symbols, **self.local_symbols}

    def _is_ignored(self, ident):
        symbols = self._current_symbols()
        return (
            ident in symbols or
            ident in self.reserved_literals or
            ident in self.builtin_identifiers or
            ident in self.builtin_properties or
            ident.isdigit() or
            (ident.startswith('"') and ident.endswith('"')) or
            (ident.startswith("'") and ident.endswith("'"))
        )

    def _extract_identifiers(self, expr_text):
        expr_text = re.sub(r'"[^"]*"', '', expr_text)
        expr_text = re.sub(r"'[^']*'", '', expr_text)
        return re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr_text)

    def _check_binary_expr_types(self, expr_text):
        if '+' in expr_text:
            parts = expr_text.split('+')
            if len(parts) == 2:
                left = parts[0].strip()
                right = parts[1].strip()
                left_type = self._current_symbols().get(left)
                right_type = self._current_symbols().get(right)
                if left_type and right_type and left_type != right_type:
                    self.errors.append(
                        f"[SEMANTIČKA GREŠKA] Operator '+' nije dozvoljen za tipove {left_type} i {right_type}"
                    )

    def check_expression_variables(self, expr_text, kontekst="izrazu"):
        for ident in self._extract_identifiers(expr_text):
            if not self._is_ignored(ident):
                self.errors.append(
                    f"[SEMANTIČKA GREŠKA] Nedefinisana promenljiva u {kontekst}: '{ident}'"
                )
        self._check_binary_expr_types(expr_text)

    # -------------------------------
    # VAR / FINAL / CONST
    # -------------------------------
    def enterVarDecl(self, ctx: Dart2Parser.VarDeclContext):
        name = ctx.ID().getText()
        if name in self._current_symbols():
            self.errors.append(f"[SEMANTIČKA GREŠKA] Promenljiva '{name}' je već definisana")
        self.global_symbols[name] = "dynamic"
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText())

    def enterFinalDecl(self, ctx: Dart2Parser.FinalDeclContext):
        name = ctx.ID().getText()
        if name in self._current_symbols():
            self.errors.append(f"[SEMANTIČKA GREŠKA] Promenljiva '{name}' je već definisana")
        self.global_symbols[name] = "dynamic"
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText())

    def enterConstDecl(self, ctx: Dart2Parser.ConstDeclContext):
        name = ctx.ID().getText()
        if name in self._current_symbols():
            self.errors.append(f"[SEMANTIČKA GREŠKA] Promenljiva '{name}' je već definisana")
        self.global_symbols[name] = "dynamic"
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText())

    def enterTypedVarDecl(self, ctx: Dart2Parser.TypedVarDeclContext):
        name = ctx.ID().getText()
        var_type = ctx.type_().getText()   # npr. int, double, String

        if name in self._current_symbols():
            self.errors.append(
                f"[SEMANTIČKA GREŠKA] Promenljiva '{name}' je već definisana"
            )

        # Dodaj u globalne simbole (ili local_symbols ako želiš blok scope)
        self.global_symbols[name] = var_type

        # Ako postoji inicijalizacija, proveri izraze
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText())

    
    # -------------------------------
    # EXPRESSIONS
    # -------------------------------
    def enterExpression(self, ctx: Dart2Parser.ExpressionContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            if op == "+":
                left_name = ctx.expression(0).getText()
                right_name = ctx.expression(1).getText()
                left_type = self._current_symbols().get(left_name)
                right_type = self._current_symbols().get(right_name)
                if left_type and right_type and left_type != right_type:
                    self.errors.append(
                        f"[SEMANTIČKA GREŠKA] Operator '+' nije dozvoljen za tipove {left_type} i {right_type}"
                    )

    def enterExprStatement(self, ctx: Dart2Parser.ExprStatementContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText())

    # -------------------------------
    # FUNCTIONS
    # -------------------------------
    def enterFunctionDecl(self, ctx: Dart2Parser.FunctionDeclContext):
        self.local_symbols = {}
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                name = param.ID().getText()
                type_ = param.type_().getText() if param.type_() else "dynamic"
                self.local_symbols[name] = type_

    def enterReturnStatement(self, ctx: Dart2Parser.ReturnStatementContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText(), "return")

    # -------------------------------
    # CONTROL STRUCTURES
    # -------------------------------
    def enterIfStatement(self, ctx: Dart2Parser.IfStatementContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText(), "if uslovu")

    def enterWhileStatement(self, ctx: Dart2Parser.WhileStatementContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText(), "while uslovu")

    def enterDoWhileStatement(self, ctx: Dart2Parser.DoWhileStatementContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText(), "do-while uslovu")

    def enterForStatement(self, ctx: Dart2Parser.ForStatementContext):
        if ctx.forLoopParts():
            for_parts = ctx.forLoopParts()
            
            # Inicijalizacija
            if for_parts.forInitializerStatement():
                init_stmt = for_parts.forInitializerStatement()
                if init_stmt.localVariableDeclaration():
                    var_name = init_stmt.localVariableDeclaration().ID().getText()
                    self.local_symbols[var_name] = "dynamic"
            
            # Uslov
            if for_parts.expression():
                self.check_expression_variables(for_parts.expression().getText(), "for uslovu")
            
            # Korak
            if for_parts.expressionList():
                for expr in for_parts.expressionList().expression():
                    self.check_expression_variables(expr.getText(), "for koraku")
            
            # Foreach stil
            if for_parts.declaredIdentifier() and for_parts.expression():
                var_name = for_parts.declaredIdentifier().ID().getText()
                self.local_symbols[var_name] = "dynamic"
                self.check_expression_variables(for_parts.expression().getText(), "foreach izrazu")
            elif for_parts.ID() and for_parts.expression():
                var_name = for_parts.ID().getText()
                if var_name not in self.local_symbols:
                    self.errors.append(f"[SEMANTIČKA GREŠKA] Promenljiva '{var_name}' u foreach nije deklarisana")
                self.check_expression_variables(for_parts.expression().getText(), "foreach izrazu")


    def enterListLiteral(self, ctx: Dart2Parser.ListLiteralContext):
        if ctx.expressionList():
            for expr in ctx.expressionList().expression():
                self.check_expression_variables(expr.getText(), "listi")

    def enterCatchClause(self, ctx: Dart2Parser.CatchClauseContext):
        if ctx.ID():
            self.local_symbols[ctx.ID().getText()] = "Exception"

    # -------------------------------
    # MAIN ANALYZE
    # -------------------------------
    def analyze(self, tree):
        walker = ParseTreeWalker()
        walker.walk(self, tree)
        return self.errors

    # -------------------------------
    # SWITCH STATEMENT
    # -------------------------------
    def enterSwitchStatement(self, ctx: Dart2Parser.SwitchStatementContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText(), "switch izrazu")

    def enterSwitchCase(self, ctx: Dart2Parser.SwitchCaseContext):
        if ctx.expression():
            self.check_expression_variables(ctx.expression().getText(), "case izrazu")

    def enterDefaultCase(self, ctx: Dart2Parser.DefaultCaseContext):
        # default nema uslov → ništa se ne proverava
        pass

    def enterTryStatement(self, ctx: Dart2Parser.TryStatementContext):
        has_catch = ctx.catchClause() and len(ctx.catchClause()) > 0
        has_finally = ctx.finallyClause() is not None
        if not has_catch and not has_finally:
            self.errors.append(
                "[SEMANTIČKA GREŠKA] 'try' blok mora imati bar jedan 'catch' ili 'finally' blok"
            )

    def enterForLoopParts(self, ctx):
        if hasattr(ctx, 'forInitializerStatement') and ctx.forInitializerStatement():
            init_stmt = ctx.forInitializerStatement()
            if hasattr(init_stmt, 'localVariableDeclaration') and init_stmt.localVariableDeclaration():
                var_name = init_stmt.localVariableDeclaration().ID().getText()
                self.local_symbols[var_name] = "int"  # Pretpostavka
        
        if hasattr(ctx, 'expr') and ctx.expr():
            self.check_expression_variables(ctx.expr().getText(), "for uslovu")