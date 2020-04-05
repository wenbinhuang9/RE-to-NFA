import unittest


from parser import  ParserEngine
## todo the problem right now lies in I embed my print code into the parser, how to deperate it?

class MyTestCase(unittest.TestCase):
    def test_parser(self):
        engine = ParserEngine()

        #s = "abfda*|fadf|faf|(fadfas)"
        ## todo these two case will fail
        #s = "((FADSF|faf|fa)*fa*|fad*)*"
        #s = "(a|b)*abb|cd|ef|hi*"
        s = "((a|b)*|(a|b)*)*"
        tree = engine.run(s)
        print (tree)


    def test_parser1(self):
        engine = ParserEngine()

        s = "cd|eff|(ab)*"
        tree = engine.run(s)

        tree_repr = tree.__repr__()

        self.assertEqual(tree_repr[1:-1] == s, True)


    ## todo here has parsing problem
    ## todo
    def test_parser2(self):
        engine = ParserEngine()

        s = "cd|eff|ab*"

        tree = engine.run(s)
        print(tree)

if __name__ == '__main__':
    unittest.main()
