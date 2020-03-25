import unittest

from  parser_second import  SequenceAST
from  nfa import  NFA
from  drawer import  NFADrawer
class MyTestCase(unittest.TestCase):
    def test_draw(self):
        seq = SequenceAST("ab")
        nfa_obj = seq.get_nfa()

        nfaDrawer = NFADrawer()

        nfaDrawer.drawImage(nfa_obj)


if __name__ == '__main__':
    unittest.main()
