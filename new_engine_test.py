import unittest


from  engine import  drawNewNFA

class MyTestCase(unittest.TestCase):
    def test_sequence(self):
        seq = "010"

        drawNewNFA(seq, "test_sequence")

    def test_or(self):
        seq = "01|10|11"

        drawNewNFA(seq, "test_or")


    def test_star(self):
        re= "a*"

        drawNewNFA(re, "test_star")

    def test_combination(self):
        re = "(0|1)010"

        drawNewNFA(re, "test_combination")

    def test_combination1(self):
        re = "(0|1)*010"

        drawNewNFA(re, "test_combination1")
if __name__ == '__main__':
    unittest.main()
