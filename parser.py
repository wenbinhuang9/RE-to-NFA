

"""
<re> ::=  <term> '|' <re> | <term>
<term> ::= { <factor> }
<factor> ::= <base> {'*'}
<base> ::= <char> | '(' <re> ')'
"""

from nfa import NFA, EPSILON

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

    def text(self):
        return self.c

    def __repr__(self):
        return self.c
class StarAST():
    def __init__(self, ast):
        self.child = ast

    def get_nfa(self, idgenerator):

        start = idgenerator.nextID()
        accept =start
        root_nfa = NFA().acceptState(accept).startState(start)

        if isinstance(self.child, Primitive):
            root_nfa.addTransitions(start, self.child.text(), start)
        else:
            sub_nfa = self.child.get_nfa(idgenerator)

            root_nfa.addSingle(sub_nfa)
            root_nfa.addTransitions(start, EPSILON, sub_nfa.start)
            root_nfa.addTransitions(sub_nfa.accept, EPSILON, accept)

        return root_nfa

    def __repr__(self):
        if isinstance(self.child, SequenceAST) or isinstance(self.child, OrAST):
            return "".join(["(", self.child.__repr__(), ")", "*"])
        else:

            return "".join([ self.child.__repr__(), "*"])


class SequenceAST():
    def __init__(self):
        self.childs = []

    def add(self, c):
        self.childs.append(c)

        return self
    def get_nfa(self, idgenerator):
        start = idgenerator.nextID()
        nfa_v = NFA().startState(start)

        cur_state = nfa_v.start
        for c in self.childs:
            if isinstance(c, Primitive):
                next_state = idgenerator.nextID()
                nfa_v.addTransitions(cur_state, c.text(), next_state)
                cur_state = next_state

            else:
                sub_nfa = c.get_nfa(idgenerator)
                nfa_v.addTransitions(cur_state, EPSILON, sub_nfa.start)
                cur_state = sub_nfa.accept
                nfa_v.addSingle(sub_nfa)

        nfa_v.acceptState(cur_state)
        return nfa_v

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

        return self

    def get_nfa(self, idgenerator):
        left = self.childs[0]
        right = self.childs[1]

        left_nfa = left.get_nfa(idgenerator)
        right_nfa = right.get_nfa(idgenerator)

        start, accept = idgenerator.nextID(), idgenerator.nextID()

        root_nfa = NFA().startState(start).acceptState(accept)

        root_nfa.append([left_nfa, right_nfa])

        for  sub_nfa in [left_nfa, right_nfa]:
            root_nfa.addTransitions(start, EPSILON, sub_nfa.start)
            root_nfa.addTransitions(sub_nfa.accept, EPSILON, accept)

        return root_nfa



    def __repr__(self):
        ans = []
        for i in range(len(self.childs)):
            ans.append(self.childs[i].__repr__())

            if i != len(self.childs) - 1:
                ans.append("|")

        return "".join(ans)

    def run(self):
        pass
