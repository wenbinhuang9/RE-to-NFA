import unittest

import filecmp

from  engine import  drawNFA

class MyTestCase(unittest.TestCase):
    def test_sequence(self):
        seq = "010"

        drawNFA(seq, "test_sequence")

    def test_or(self):
        seq = "01|10|11"

        drawNFA(seq, "test_or")


    def test_star(self):
        re= "a*"

        drawNFA(re, "test_star")

    def test_combination(self):
        re = "(11|01|00)010"

        drawNFA(re, "test_combination")

    def test_combination1(self):
        re = "(0|1)*010"
        file = "test_combination1"
        drawNFA(re, file)

        self.assertEqual(filecmp.cmp(file + ".svg", file+"_correct.svg"), True)

    def test_combination2(self):
        re= "(|)*101(0|1)*"

        drawNFA(re, "test_combination2")
if __name__ == '__main__':
    unittest.main()
