

from  engine import convertREtoNFA

import unittest


class MyTestCase(unittest.TestCase):
    def test_or_engine(self):
        input = "cd|eff|ab"

        convertREtoNFA(input)

    def test_or_stat_concatenation_engine(self):
        input = "(0|1)*111"

        convertREtoNFA(input)


if __name__ == '__main__':
    unittest.main()
