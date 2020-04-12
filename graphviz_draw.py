from  nfa import NFA

import  graphviz as gv

from nfa import EPSILON
LAMBDA = "<&lambda;>"
class NFAGraph():
    def __init__(self, nfa):
        self.node = set([])
        self.graph = self.__createSvg()
        self.nfa = nfa
    def __createSvg(self):
        graph = gv.Digraph(format='svg')
        graph.attr('graph',rankdir="LR")
        return graph

    def doubleEdge(self, a, b):
        self.edge(a, b)
        self.edge(b, a)
    def edge(self, a, b, symbol = ""):

        self.drawNode(a)
        self.drawNode(b)

        if symbol == EPSILON:
            symbol = LAMBDA
        self.graph.edge(a, b, label=symbol)


    def drawNode(self, a):
        if a not in self.node:
            self.node.add(a)
            if a != self.nfa.accept:
                self.graph.node(a)
            else:
                self.graph.node(a, peripheries="2")

    def render(self, file):
        self.graph.render(file)



def drawGraphNFA(nfa, file):
    g = NFAGraph(nfa)


    for key, statelist in nfa.transitions.items():
        startState , symbo = key[0], key[1]
        for sourceState in statelist:
            g.edge(startState, sourceState, symbo)

    g.render(file)

