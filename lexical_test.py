import unittest


from  lexer import LexicalAnalyzer
class MyTestCase(unittest.TestCase):
    def test_lexer(self):
        analyzer = LexicalAnalyzer()
        s = "abcde"
        analyzer.run(s)
        ans = ["abcde"]
        tokens = analyzer.tokens

        self.assertEqual(all( [ans[i] == tokens[i].value for i in range(len(ans))]), True)

        analyzer = LexicalAnalyzer()

        s = "ab | bb"
        analyzer
        analyzer.run(s)

        ans = ["ab", "|", "bb"]

        tokens = analyzer.tokens
        print(tokens)
        self.assertEqual(all([ans[i] == tokens[i].value for i in range(len(ans))]), True)

        analyzer = LexicalAnalyzer()

        s = "(a | bb)* abb"
        analyzer.run(s)

        ans = ["(", "a", "|", "bb", ")", "*", "abb"]

        tokens = analyzer.tokens
        print(tokens)
        self.assertEqual(all([ans[i] == tokens[i].value for i in range(len(ans))]), True)


if __name__ == '__main__':
    unittest.main()
