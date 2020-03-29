"""

BNF for this parser

re-> '(' re* ')' |value '*' re | value '|' re | value re | '*' re | '|' re
value-> sequence
"""

from lexer import RE_SYMBOL, SEQUENCE, PARENTHESIS, LexicalAnalyzer
from  nfa import NFA

INTERVAL_LEN = 5
class SequenceAST():
    def __init__(self, token):
        self.token = token


    def get_nfa(self):
        token_len = len(self.token)

        nfa_object = NFA().startState(0).acceptState(token_len - 1)

        for i in range(token_len):
            if i != token_len - 1:
                nfa_object.addTransitions(i, self.token[i], i + 1)

        return nfa_object

    def __repr__(self):
        return self.token

class ReAST():
    def __init__(self):
        self.children = []


    def add (self, ast):
        self.children.append(ast)
        return self

    def pop(self):
        child = self.children.pop()
        return child
    def run(self):
        pass


    def __repr__(self):
        ans = [child.__repr__() for child in self.children]
        return "".join(ans)

class StarAST():
    def __init__(self, ast):
        self.child = ast

    def run(self):
        pass

    def __repr__(self):
        if isinstance(self.child, SequenceAST):
            return "".join([ self.child.__repr__(), "*"])

        return "".join(["(", self.child.__repr__(), ")", "*"])

class OrAST():
    def __init__(self):
        self.childs = []

    def add(self, ast):
        self.childs.append(ast)


    def __repr__(self):
        ans = ["("]
        for i in range(len(self.childs)):
            ans.append(self.childs[i].__repr__())

            if i != len(self.childs) - 1:
                ans.append("|")
        ans.append(")")
        return "".join(ans)

    def run(self):
        pass



STAR = "*"
OR_SYMBOL = "|"



class ReParser():
    def __init__(self , valueParser = None):
        self.valueParser = valueParser
        self.reAST = ReAST()

    def parse(self,lex):
        token = lex.peak()
        ##s = "((faf)*)*"
        if token.type == PARENTHESIS:
            left = lex.nextToken()
            assert left.value == "("

            childReParser = ReParser(self.valueParser)

            childReParser.parse(lex)
            right = lex.peak()

            while right != None and right.value != ")":
                childReParser.parse(lex)
                right = lex.peak()

            right  = lex.nextToken()
            if right == None:
                raise ValueError("invalid syntax")
            assert right.value == ")"

            tree = childReParser.reAST
            self.reAST.add(tree)
            return tree
        elif token.value == "|":
            left = self.reAST.pop()

            symnbol = lex.nextToken()
            assert  symnbol.value == "|"
            right = ReParser(self.valueParser).parse(lex)
            orAst = OrAST()
            orAst.add(left)
            orAst.add(right)
            self.reAST.add(orAst)

            return orAst
        elif token.value == "*":
            star = self.reAST.pop()

            symbol = lex.nextToken()
            assert symbol.value == "*"

            starAst = StarAST(star)
            self.reAST.add(starAst)

            return starAst


        token1 = lex.peak(1)
        if token1 == None:
            tree = self.valueParser.parse(lex)

            self.reAST.add(tree)
            return tree

        elif token1.value == "*":
            tree = self.valueParser.parse(lex)
            star = lex.nextToken()
            assert  star.value == "*"
            starAST = StarAST(tree)

            self.reAST.add(starAST)

            return starAST
        elif token1.value == "|":
            left = self.valueParser.parse(lex)
            orSymbol = lex.nextToken()
            assert  orSymbol.value == "|"
            right = ReParser(self.valueParser).parse(lex)

            orAst = OrAST()
            orAst.add(left)
            orAst.add(right)

            self.reAST.add(orAst)
            return orAst

        else:
            seqRe = self.valueParser.parse(lex)

            self.reAST.add(seqRe)
            return seqRe

class OrParser():

    def __init__(self, valueParser):
        self.valueParser =valueParser

    def parse(self, lex):
        left = self.valueParser.parse(lex)
        token = lex.peak()
        if token.value == "*":
            lex.nextToken()
            starAST = StarAST(left)
            return starAST
        if token.value != "|":
            return left

        orSymbol = self.lex.nextToken()
        assert  orSymbol.value == "|"
        right = self.parse(lex)

        orAST = OrAST()
        orAST.add(left), orAST.add(right)

        return orAST


class ValueParser():
    def __init__(self ):
        pass
    def parse(self, lex):
        token = lex.peak()
        if token.type == SEQUENCE:
            token = lex.nextToken()
            return SequenceAST(token.value)
        else:
            raise ValueError("invalid input|it is not a sequence token|token={0}", token)




class ParserEngine():
    def __init__(self):
        pass

    def run(self, input):
        lexx = LexicalAnalyzer()
        lexx.run(input)

        reParser = ReParser()
        valueParser = ValueParser()

        reParser.valueParser = valueParser


        while lexx.hasNext():
             reParser.parse(lexx)
        return reParser.reAST
