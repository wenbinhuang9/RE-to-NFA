"""
classical BNF for expression
expr->product ((+ ) expr)
product->value ((* ) product)
value->num | '('expr')'

re-> star re | or re | value re
star-> value '*'
or->  value '|' or
value -> sequence | '('re')'

print tree representation
"""
from lexer import RE_SYMBOL, SEQUENCE, PARENTHESIS, LexicalAnalyzer

class SequenceAST():
    def __init__(self, token):
        self.token = token

    def run(self):
        ## todo
        return self.token

    def __repr__(self):
        return self.token
class ReAST():
    def __init__(self):
        self.children = []

    def add (self, ast):
        self.children.append(ast)
        return self

    def pop(self):
        self.children.pop()

    def run(self):
        pass

    def __repr__(self):
        pass

class StarAST():
    def __init__(self, ast):
        self.child = ast

    def run(self):
        pass

class OrAST():
    def __init__(self):
        self.childs = []

    def add(self, ast):
        self.childs.append(ast)

    def run(self):
        pass

STAR = "*"
OR_SYMBOL = "|"
class ReParser():
    def __init__(self ):
        self.valueParser = None
        self.reTree = None

    def setReTree(self, reTree ):
        self.reTree = reTree


    def parse(self,lex):
        token = lex.peak()

        if token == None:
            return self.valueParser.parse(lex)
        elif token.value == STAR:
            lex.nextToken()
            lastRe= self.reTree.pop()
            starAST = StarAST(lastRe)
            return starAST

        elif token.value == OR_SYMBOL:
            lex.nextToken()
            firstInOr = self.reTree.pop()
            secondInOr = self.parse(lex)
            orRe = OrAST()
            orRe.add(firstInOr)
            orRe.add(secondInOr)

            return  orRe
        else:
            seqRe = self.valueParser.parse(lex)
            return  seqRe

class ValueParser():
    def __init__(self, reParser):
        self.re_parser=  reParser

    def parse(self, lex):
        token = lex.peak()
        if token.type == SEQUENCE:
            token = lex.nextToken()
            return SequenceAST(token.value)

        elif token.type == PARENTHESIS:
            left = lex.nextToken()
            assert left.value == "("
            tree = self.re_parser.parse(lex)
            right = lex.nextToken()
            assert right.value == ")"
            return tree

        else:
            raise ValueError("invalid input")


"""
my BNF still has a problem 

re->  '*' re | '|' re | value re
value -> sequence | '('re')'

"""

class ParserEngine():
    def __init__(self):
        pass

    def run(self, input):
        lexx = LexicalAnalyzer()
        lexx.run(input)

        reParser = ReParser()
        valueParser = ValueParser(reParser)
        reParser.valueParser = valueParser
        tree = ReAST()

        reParser.setReTree(tree)
        while lexx.hasNext():
            subTree = reParser.parse(lexx)
            tree.add(subTree)
        return tree

