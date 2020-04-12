

from  engine import drawNFA

import unittest

import  filecmp
## add assert, make it auto

class MyTestCase(unittest.TestCase):
    def test_or_engine0(self):
        input = "a|b"
        file = "a_b_or.jpg"
        drawNFA(input, file)



    def test_or_engine(self):
        input = "cd|eff|(ab)*"
        file = "cd_eff_ab_or"
        svgfile = file + ".svg"
        correctfile = "cd_eff_ab_or_correct.svg"
        drawNFA(input, "cd_eff_ab_or")

        self.assertEqual(filecmp.cmp(svgfile, correctfile), True)

    ## todo parsing bug here
    def test_or_engine2(self):
        input = "cd|eff|ab*"

        drawNFA(input)

    def test_or_stat_concatenation_engine(self):
        ## todo this graph is too complex
        input = "(0|1)*111"
        file = "end_with_111"
        drawNFA(input, file)


    def test_starr(self):
        input = "1*"

        drawNFA(input)

  ## todo parsing bug here
    def test_or_engine10(self):
        input = "cd|ef|ab"

        drawNFA(input, "test_or_engine10")

    def test_special_char(self):
        print(chr(945))
if __name__ == '__main__':
    unittest.main()
