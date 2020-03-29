import unittest
from PIL import Image, ImageDraw, ImageFont


from  parser_second import  SequenceAST
from  nfa import  NFA
from  drawer import  NFADrawer
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

if __name__ == '__main__':
    unittest.main()
