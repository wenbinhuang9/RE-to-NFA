

"""
<re> ::=  <term> '|' <re> | <term>
<term> ::= { <factor> }
<factor> ::= <base> {'*'}
<base> ::= <char> | '(' <re> ')'
"""

from  lexer import LexicalAnalyzer
from nfa import  mergeConcatenation, mergeOR, mergeStar, NFA



class RegExParser():
    def __init__(self, lexer):
        self.lexer = lexer
    def regex(self):
        term_v = self.term()

        if (self.lexer.more() and self.lexer.peak() == "|"):
            self.lexer.eat("|")
            re_v  = self.regex()

            return OrAST().add([term_v, re_v])
        else:
            if (self.lexer.more()):
                print("invalid re")
                return None

            return term_v

    """
    <re> ::=  <term> '|' <re> | <term>
    <term> ::= { <factor> }
    <factor> ::= <base> {'*'}
    <base> ::= <char> | '(' <re> ')'
    """
    def term(self):
        seq = SequenceAST()
        while self.lexer.more() and self.lexer.peak()!= ')' and self.lexer.peak() != '|':
            factor_v = self.factor()
            seq.add(factor_v)

        return seq

    def factor(self):
        base_v =self.base()

        while self.lexer.more() and self.lexer.peak() == '*':
            self.lexer.eat("*")
            v = StarAST(base_v)
            base_v = v

        return base_v
    def base(self):
        if self.lexer.peak() == "(":
            self.lexer.eat("(")
            re_v = self.regex()
            self.lexer.eat(")")
            return  re_v

        else:
            return Primitive(self.lexer.nextToken().text())

class Primitive():
    def __init__(self, c):
        self.c = c

    ##todo 
    def get_nfa(self):
        pass

    def __repr__(self):
        return self.c
class StarAST():
    def __init__(self, ast):
        self.child = ast

    def get_nfa(self):
        child_nfa = self.child.get_nfa()
        return mergeStar(child_nfa)

    def __repr__(self):
        if isinstance(self.child, SequenceAST):
            return "".join(["(", self.child.__repr__(), ")", "*"])
        else:

            return "".join([ self.child.__repr__(), "*"])


class SequenceAST():
    def __init__(self):
        self.childs = []

    def add(self, c):
        self.childs.append(c)

        return self
    def get_nfa(self):
        pass

    def __repr__(self):
        return "".join([c.__repr__() for c in self.childs])


class OrAST():
    def __init__(self):
        self.childs = []

    def add(self, ast):
        if isinstance(ast, list):
            self.childs.extend(ast)
        else:
            self.childs.append(ast)

    def get_nfa(self):
        child_nfa_list = []

        for child in self.childs:
            child_nfa = child.get_nfa()
            child_nfa_list.append(child_nfa)

        return mergeOR(child_nfa_list)

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
