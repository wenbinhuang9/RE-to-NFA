import unittest


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
        re = "(0|1)010"

        drawNFA(re, "test_combination")

    def test_combination1(self):
        re = "(0|1)*010"

        drawNFA(re, "test_combination1")
if __name__ == '__main__':
    unittest.main()
