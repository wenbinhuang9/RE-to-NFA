

from  engine import drawNFA

import unittest


## add assert, make it auto

class MyTestCase(unittest.TestCase):
    ##todo add unite test
    ## todo this part has a layout bug
    def test_or_engine(self):
        input = "cd|(eff)*|(ab)*"

        drawNFA(input)

    def test_or_stat_concatenation_engine(self):
        input = "(0|1)*111"

        drawNFA(input)


    def test_starr(self):
        input = "1*"

        drawNFA(input)
if __name__ == '__main__':
    unittest.main()
