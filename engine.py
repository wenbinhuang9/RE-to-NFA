
from  parser import  ParserEngine

from graphviz_draw import  drawGraphNFA
def drawNFA(input, file = None):
    parserEngine = ParserEngine()

    tree = parserEngine.run(input)

    nfa = tree.get_nfa()

    drawGraphNFA(nfa, file)