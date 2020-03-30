import unittest
from PIL import Image, ImageDraw, ImageFont


from  parser_second import  SequenceAST, OrAST
from  nfa import  NFA
from  drawer import  NFADrawer
from drawer import  NFALayout
from  nfa import mergeOR, mergeStar ,mergeConcatenation
class MyTestCase(unittest.TestCase):
    def test_draw(self):
        seq = SequenceAST("abcde")
        nfa_obj = seq.get_nfa()

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNFA(nfa_obj)

    def test_draw_text(self):
        # get a font
        im = Image.new('RGB', (500, 300), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        draw.text((20, 70), "welcom", fill="black")

        im.save("./test.jpg")


    def test_new_draw(self):
        seq = SequenceAST("abc")
        nfa_obj = seq.get_nfa()

        nfa_layout = NFALayout(nfa_obj)

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_layout)

    def test_concatenation_draw(self):
        seq = SequenceAST("abc")
        nfa1 = seq.get_nfa()


        nfa2 = SequenceAST("ef").get_nfa()

        nfa = mergeConcatenation([nfa1, nfa2])
        nfa_layout = NFALayout(nfa)

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_layout)

    def test_or_draw(self):
        nfa1 = SequenceAST("ab").get_nfa()
        nfa2 = SequenceAST("cd").get_nfa()
        nfa3 = SequenceAST("efg").get_nfa()
        nfa = mergeOR([nfa1, nfa2, nfa3])
        nfa_layout = NFALayout(nfa)

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_layout)

    def test_star_draw(self):
        nfa1 = SequenceAST("ab").get_nfa()

        nfa = mergeStar(nfa1)

        nfa_layout = NFALayout(nfa)

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_layout)

    def test_or_concatenation_draw(self):
        nfa1 = SequenceAST("ab").get_nfa()
        nfa2 = SequenceAST("cd").get_nfa()
        nfa3 = SequenceAST("efg").get_nfa()
        nfa = mergeOR([nfa2, nfa3])
        new_nfa = mergeConcatenation([nfa1, nfa])

        nfa_layout = NFALayout(new_nfa)

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_layout)

if __name__ == '__main__':
    unittest.main()
