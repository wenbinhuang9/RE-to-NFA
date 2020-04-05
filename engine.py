
from drawer import NFALayout, NFADrawer
from  parser import  ParserEngine
def drawNFA(input, file = None):
    parserEngine = ParserEngine()

    tree = parserEngine.run(input)

    nfa = tree.get_nfa()

    nfa_layout = NFALayout(nfa)

    drawer = NFADrawer()

    drawer.drawNewNFA(nfa_layout, file )
