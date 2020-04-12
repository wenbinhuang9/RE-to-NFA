
from  parser import  ParserEngine

from graphviz_draw import  drawGraphNFA
def drawNFA(input, file = None):
    parserEngine = ParserEngine()

    tree = parserEngine.run(input)

    nfa = tree.get_nfa()

   # nfa_layout = NFALayout(nfa)

   # drawNewNFA(nfa_layout, file )

    drawGraphNFA(nfa, file)