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





if __name__ == '__main__':
    unittest.main()
