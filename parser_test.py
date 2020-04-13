import unittest


from  lexer import  LexicalAnalyzer

from  parser import  RegExParser
class MyTestCase(unittest.TestCase):
    def test_primitive_parser(self):
        re = "a"
        l = LexicalAnalyzer()
        l.run(re)

        parser = RegExParser(l)
        tree = parser.regex()

        print(tree)

        self.assertEqual(tree.__repr__() == re, True)

    def test_concatenation_parser(self):
        re = "abc"
        l = LexicalAnalyzer()
        l.run(re)

        parser = RegExParser(l)
        tree = parser.regex()

        print(tree)

        self.assertEqual(tree.__repr__() == re, True)


    def test_or_parser(self):
        re = "a|b|c"
        l = LexicalAnalyzer()
        l.run(re)

        parser = RegExParser(l)
        tree = parser.regex()

        print(tree)

        self.assertEqual(tree.__repr__() == re, True)


    def test_star_parser(self):
        re = "a**"
        l = LexicalAnalyzer()
        l.run(re)

        parser = RegExParser(l)
        tree = parser.regex()

        print(tree)
        self.assertEqual(tree.__repr__() == re, True)


    def test_combination_parser(self):
        re = "a|b*|(cd)*e"
        l = LexicalAnalyzer()
        l.run(re)

        parser = RegExParser(l)
        tree = parser.regex()

        print(tree)
        self.assertEqual(tree.__repr__() == re, True)

    def test_combination1_parser(self):
        re = "(0|1)*010"
        l = LexicalAnalyzer()
        l.run(re)

        parser = RegExParser(l)
        tree = parser.regex()

        print(tree)
        self.assertEqual(tree.__repr__() == re, True)


if __name__ == '__main__':
    unittest.main()
