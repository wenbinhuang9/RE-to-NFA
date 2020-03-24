import unittest


from parser import  ParserEngine
## todo how
class MyTestCase(unittest.TestCase):
    def test_parser(self):
        engine = ParserEngine()

        s = "(abc)*afaf|fa"
        tree = engine.run(s)

    def print_tree(self, tree):
        ## todo how to recursively print the tree
        ## todo it looks chanllengable
        pass
if __name__ == '__main__':
    unittest.main()
