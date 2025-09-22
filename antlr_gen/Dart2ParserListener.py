# Generated from grammar/Dart2Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Dart2Parser import Dart2Parser
else:
    from Dart2Parser import Dart2Parser

# This class defines a complete listener for a parse tree produced by Dart2Parser.
class Dart2ParserListener(ParseTreeListener):

    # Enter a parse tree produced by Dart2Parser#program.
    def enterProgram(self, ctx:Dart2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Dart2Parser#program.
    def exitProgram(self, ctx:Dart2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Dart2Parser#statement.
    def enterStatement(self, ctx:Dart2Parser.StatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#statement.
    def exitStatement(self, ctx:Dart2Parser.StatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#printStatement.
    def enterPrintStatement(self, ctx:Dart2Parser.PrintStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#printStatement.
    def exitPrintStatement(self, ctx:Dart2Parser.PrintStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#functionDecl.
    def enterFunctionDecl(self, ctx:Dart2Parser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by Dart2Parser#functionDecl.
    def exitFunctionDecl(self, ctx:Dart2Parser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by Dart2Parser#parameterList.
    def enterParameterList(self, ctx:Dart2Parser.ParameterListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#parameterList.
    def exitParameterList(self, ctx:Dart2Parser.ParameterListContext):
        pass


    # Enter a parse tree produced by Dart2Parser#parameter.
    def enterParameter(self, ctx:Dart2Parser.ParameterContext):
        pass

    # Exit a parse tree produced by Dart2Parser#parameter.
    def exitParameter(self, ctx:Dart2Parser.ParameterContext):
        pass


    # Enter a parse tree produced by Dart2Parser#type.
    def enterType(self, ctx:Dart2Parser.TypeContext):
        pass

    # Exit a parse tree produced by Dart2Parser#type.
    def exitType(self, ctx:Dart2Parser.TypeContext):
        pass


    # Enter a parse tree produced by Dart2Parser#ifStatement.
    def enterIfStatement(self, ctx:Dart2Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#ifStatement.
    def exitIfStatement(self, ctx:Dart2Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#whileStatement.
    def enterWhileStatement(self, ctx:Dart2Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#whileStatement.
    def exitWhileStatement(self, ctx:Dart2Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:Dart2Parser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:Dart2Parser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#forStatement.
    def enterForStatement(self, ctx:Dart2Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#forStatement.
    def exitForStatement(self, ctx:Dart2Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#forLoopParts.
    def enterForLoopParts(self, ctx:Dart2Parser.ForLoopPartsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#forLoopParts.
    def exitForLoopParts(self, ctx:Dart2Parser.ForLoopPartsContext):
        pass


    # Enter a parse tree produced by Dart2Parser#forInitializerStatement.
    def enterForInitializerStatement(self, ctx:Dart2Parser.ForInitializerStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#forInitializerStatement.
    def exitForInitializerStatement(self, ctx:Dart2Parser.ForInitializerStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#switchStatement.
    def enterSwitchStatement(self, ctx:Dart2Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#switchStatement.
    def exitSwitchStatement(self, ctx:Dart2Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#switchCase.
    def enterSwitchCase(self, ctx:Dart2Parser.SwitchCaseContext):
        pass

    # Exit a parse tree produced by Dart2Parser#switchCase.
    def exitSwitchCase(self, ctx:Dart2Parser.SwitchCaseContext):
        pass


    # Enter a parse tree produced by Dart2Parser#defaultCase.
    def enterDefaultCase(self, ctx:Dart2Parser.DefaultCaseContext):
        pass

    # Exit a parse tree produced by Dart2Parser#defaultCase.
    def exitDefaultCase(self, ctx:Dart2Parser.DefaultCaseContext):
        pass


    # Enter a parse tree produced by Dart2Parser#tryStatement.
    def enterTryStatement(self, ctx:Dart2Parser.TryStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#tryStatement.
    def exitTryStatement(self, ctx:Dart2Parser.TryStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#onClause.
    def enterOnClause(self, ctx:Dart2Parser.OnClauseContext):
        pass

    # Exit a parse tree produced by Dart2Parser#onClause.
    def exitOnClause(self, ctx:Dart2Parser.OnClauseContext):
        pass


    # Enter a parse tree produced by Dart2Parser#catchClause.
    def enterCatchClause(self, ctx:Dart2Parser.CatchClauseContext):
        pass

    # Exit a parse tree produced by Dart2Parser#catchClause.
    def exitCatchClause(self, ctx:Dart2Parser.CatchClauseContext):
        pass


    # Enter a parse tree produced by Dart2Parser#finallyClause.
    def enterFinallyClause(self, ctx:Dart2Parser.FinallyClauseContext):
        pass

    # Exit a parse tree produced by Dart2Parser#finallyClause.
    def exitFinallyClause(self, ctx:Dart2Parser.FinallyClauseContext):
        pass


    # Enter a parse tree produced by Dart2Parser#returnStatement.
    def enterReturnStatement(self, ctx:Dart2Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#returnStatement.
    def exitReturnStatement(self, ctx:Dart2Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#varDecl.
    def enterVarDecl(self, ctx:Dart2Parser.VarDeclContext):
        pass

    # Exit a parse tree produced by Dart2Parser#varDecl.
    def exitVarDecl(self, ctx:Dart2Parser.VarDeclContext):
        pass


    # Enter a parse tree produced by Dart2Parser#finalDecl.
    def enterFinalDecl(self, ctx:Dart2Parser.FinalDeclContext):
        pass

    # Exit a parse tree produced by Dart2Parser#finalDecl.
    def exitFinalDecl(self, ctx:Dart2Parser.FinalDeclContext):
        pass


    # Enter a parse tree produced by Dart2Parser#constDecl.
    def enterConstDecl(self, ctx:Dart2Parser.ConstDeclContext):
        pass

    # Exit a parse tree produced by Dart2Parser#constDecl.
    def exitConstDecl(self, ctx:Dart2Parser.ConstDeclContext):
        pass


    # Enter a parse tree produced by Dart2Parser#typedVarDecl.
    def enterTypedVarDecl(self, ctx:Dart2Parser.TypedVarDeclContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typedVarDecl.
    def exitTypedVarDecl(self, ctx:Dart2Parser.TypedVarDeclContext):
        pass


    # Enter a parse tree produced by Dart2Parser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:Dart2Parser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:Dart2Parser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by Dart2Parser#declaredIdentifier.
    def enterDeclaredIdentifier(self, ctx:Dart2Parser.DeclaredIdentifierContext):
        pass

    # Exit a parse tree produced by Dart2Parser#declaredIdentifier.
    def exitDeclaredIdentifier(self, ctx:Dart2Parser.DeclaredIdentifierContext):
        pass


    # Enter a parse tree produced by Dart2Parser#exprStatement.
    def enterExprStatement(self, ctx:Dart2Parser.ExprStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#exprStatement.
    def exitExprStatement(self, ctx:Dart2Parser.ExprStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#block.
    def enterBlock(self, ctx:Dart2Parser.BlockContext):
        pass

    # Exit a parse tree produced by Dart2Parser#block.
    def exitBlock(self, ctx:Dart2Parser.BlockContext):
        pass


    # Enter a parse tree produced by Dart2Parser#breakStatement.
    def enterBreakStatement(self, ctx:Dart2Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#breakStatement.
    def exitBreakStatement(self, ctx:Dart2Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#continueStatement.
    def enterContinueStatement(self, ctx:Dart2Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#continueStatement.
    def exitContinueStatement(self, ctx:Dart2Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#throwStatement.
    def enterThrowStatement(self, ctx:Dart2Parser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by Dart2Parser#throwStatement.
    def exitThrowStatement(self, ctx:Dart2Parser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by Dart2Parser#expression.
    def enterExpression(self, ctx:Dart2Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Dart2Parser#expression.
    def exitExpression(self, ctx:Dart2Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Dart2Parser#listLiteral.
    def enterListLiteral(self, ctx:Dart2Parser.ListLiteralContext):
        pass

    # Exit a parse tree produced by Dart2Parser#listLiteral.
    def exitListLiteral(self, ctx:Dart2Parser.ListLiteralContext):
        pass


    # Enter a parse tree produced by Dart2Parser#expressionList.
    def enterExpressionList(self, ctx:Dart2Parser.ExpressionListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#expressionList.
    def exitExpressionList(self, ctx:Dart2Parser.ExpressionListContext):
        pass


    # Enter a parse tree produced by Dart2Parser#metadata.
    def enterMetadata(self, ctx:Dart2Parser.MetadataContext):
        pass

    # Exit a parse tree produced by Dart2Parser#metadata.
    def exitMetadata(self, ctx:Dart2Parser.MetadataContext):
        pass


    # Enter a parse tree produced by Dart2Parser#metadatum.
    def enterMetadatum(self, ctx:Dart2Parser.MetadatumContext):
        pass

    # Exit a parse tree produced by Dart2Parser#metadatum.
    def exitMetadatum(self, ctx:Dart2Parser.MetadatumContext):
        pass


    # Enter a parse tree produced by Dart2Parser#constructorDesignation.
    def enterConstructorDesignation(self, ctx:Dart2Parser.ConstructorDesignationContext):
        pass

    # Exit a parse tree produced by Dart2Parser#constructorDesignation.
    def exitConstructorDesignation(self, ctx:Dart2Parser.ConstructorDesignationContext):
        pass


    # Enter a parse tree produced by Dart2Parser#typeName.
    def enterTypeName(self, ctx:Dart2Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeName.
    def exitTypeName(self, ctx:Dart2Parser.TypeNameContext):
        pass


    # Enter a parse tree produced by Dart2Parser#typeArguments.
    def enterTypeArguments(self, ctx:Dart2Parser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeArguments.
    def exitTypeArguments(self, ctx:Dart2Parser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by Dart2Parser#typeList.
    def enterTypeList(self, ctx:Dart2Parser.TypeListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#typeList.
    def exitTypeList(self, ctx:Dart2Parser.TypeListContext):
        pass


    # Enter a parse tree produced by Dart2Parser#arguments.
    def enterArguments(self, ctx:Dart2Parser.ArgumentsContext):
        pass

    # Exit a parse tree produced by Dart2Parser#arguments.
    def exitArguments(self, ctx:Dart2Parser.ArgumentsContext):
        pass


    # Enter a parse tree produced by Dart2Parser#argumentList.
    def enterArgumentList(self, ctx:Dart2Parser.ArgumentListContext):
        pass

    # Exit a parse tree produced by Dart2Parser#argumentList.
    def exitArgumentList(self, ctx:Dart2Parser.ArgumentListContext):
        pass


    # Enter a parse tree produced by Dart2Parser#literal.
    def enterLiteral(self, ctx:Dart2Parser.LiteralContext):
        pass

    # Exit a parse tree produced by Dart2Parser#literal.
    def exitLiteral(self, ctx:Dart2Parser.LiteralContext):
        pass


    # Enter a parse tree produced by Dart2Parser#binaryOp.
    def enterBinaryOp(self, ctx:Dart2Parser.BinaryOpContext):
        pass

    # Exit a parse tree produced by Dart2Parser#binaryOp.
    def exitBinaryOp(self, ctx:Dart2Parser.BinaryOpContext):
        pass


    # Enter a parse tree produced by Dart2Parser#unaryOp.
    def enterUnaryOp(self, ctx:Dart2Parser.UnaryOpContext):
        pass

    # Exit a parse tree produced by Dart2Parser#unaryOp.
    def exitUnaryOp(self, ctx:Dart2Parser.UnaryOpContext):
        pass


    # Enter a parse tree produced by Dart2Parser#unaryPostfixOp.
    def enterUnaryPostfixOp(self, ctx:Dart2Parser.UnaryPostfixOpContext):
        pass

    # Exit a parse tree produced by Dart2Parser#unaryPostfixOp.
    def exitUnaryPostfixOp(self, ctx:Dart2Parser.UnaryPostfixOpContext):
        pass



del Dart2Parser