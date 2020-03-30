import unittest
from PIL import Image, ImageDraw, ImageFont


from  parser import  SequenceAST, OrAST
from  nfa import  NFA
from  drawer import  NFADrawer
from drawer import  NFALayout
from  nfa import mergeOR, mergeStar ,mergeConcatenation
class MyTestCase(unittest.TestCase):


    def test_line(self):
        im = Image.new('RGB', (500, 300), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        draw.line((30, 80, 100, 50), fill='black', width=1, joint="curved")

        im.save("./line.jpg")

    def test_arc(self):
        im = Image.new('RGB', (500, 300), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        ##draw.arc((100, 50, 30, 50), start=300, end=300, fill='black', width=3)
        ##draw.chord((0, 0, 200, 200), 180, 0, fill="black", outline="#FF0000")
        draw.line((30, 50, 100, 80), fill='black', width=5, joint="curved")
        ##draw.arc((20, 40, 200, 100), 180, 0, 0)
        ##s = ImageDraw.Outline()
        ##s.curve(30, 50, )
        draw.arc((20, 40, 200, 100), 180, 0, 0)

        im.save("./arc.jpg")
    def test_draw(self):
        seq = SequenceAST("abcde")
        nfa_obj = seq.get_nfa()

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_obj)

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
        nfa = mergeOR([nfa1, nfa2])
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


    ## todo bug here
    def test_or_concatenation_star_draw(self):
        ##nfa1 = SequenceAST("ab").get_nfa()
        nfa2 = SequenceAST("cd").get_nfa()
        nfa3 = SequenceAST("efg").get_nfa()
        starNfa = mergeStar(nfa3)
        nfa = mergeOR([nfa2, starNfa])
        ##new_nfa = mergeConcatenation([nfa1, nfa])
        new_nfa = nfa
        nfa_layout = NFALayout(new_nfa)

        nfaDrawer = NFADrawer()

        nfaDrawer.drawNewNFA(nfa_layout)


if __name__ == '__main__':
    unittest.main()
