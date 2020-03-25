"""
classical BNF for expression
expr->product ((+ ) expr)
product->value ((* ) product)
value->num | '('expr')'

re-> star re | or re | value re
star-> value '*'
or->  value '|' or
value -> sequence | '('re')'


the key lines in how you understand the grammar, then converts grammar to the parsing program.

re-> value '*' re | value '|' OR  re| value re
value-> sequence | '('re')'
OR-> value | value '|' OR

## get stuck here, oh, fuck!
"""
from lexer import RE_SYMBOL, SEQUENCE, PARENTHESIS, LexicalAnalyzer


INTERVAL_LEN = 5
class SequenceAST():
    def __init__(self, token):
        self.token = token

    def run(self):
        ## todo
        return self.token

    def get_print_len(self):
        return len(self.token) + INTERVAL_LEN

    def get_childs(self):
        childs = [self.token]

        return childs
    def __repr__(self):
        return self.token

class ReAST():
    def __init__(self):
        self.children = []

    def get_childs(self):
        return self.children
    def add (self, ast):
        self.children.append(ast)
        return self

    def pop(self):
        child = self.children.pop()
        return child
    def run(self):
        pass

    def get_print_len(self):
        l = 0
        for child in self.children:
            l += child.get_print_len()
        return l

    def __repr__(self):
        ans = [child.__repr__() for child in self.children]
        return "".join(ans)

class StarAST():
    def __init__(self, ast):
        self.child = ast
    def get_print_len(self):
        l = 0
        return  self.child.get_print_len() + 1

    def get_childs(self):
        return [self.child, "*"]

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

    def get_childs(self):
        childs = []
        for i in range(len(self.childs)):
            childs.append(self.childs[i])

            if i != len(self.childs) - 1:
                childs.append("|")

        return childs
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

    def get_print_len(self):
        l = 0
        for child in self.childs:
            l += child.get_print_len()

        l += (len(self.childs) - 1)

        return l

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
            ## todo my grammar is not understandable right now
            while lex.hasNext() and lex.peak().value != ")":
                tree = self.re_parser.parse(lex)
            if not lex.hasNext():
                raise ValueError("syntax, error")
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

