

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
        file = "cd_eff_ab_or.jpg"
        correctfile = "cd_eff_ab_or_correct.jpg"
        drawNFA(input, "cd_eff_ab_or.jpg")

        self.assertEqual(filecmp.cmp(file, correctfile), True)

    ## todo parsing bug here
    def test_or_engine2(self):
        input = "cd|eff|ab*"

        drawNFA(input)

    def test_or_stat_concatenation_engine(self):
        input = "(0|1)*111"

        drawNFA(input)


    def test_starr(self):
        input = "1*"

        drawNFA(input)
if __name__ == '__main__':
    unittest.main()
