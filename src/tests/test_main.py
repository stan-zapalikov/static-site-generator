import unittest
from src.main import extract_title
from src.leafnode import LeafNode

class TestMain(unittest.TestCase):
    def testExtractTitleProper(self):
        result = LeafNode("h1", "This is a title")
        mdInput = "# This is a title\ntesting\ntesting"
        self.assertEqual(repr(extract_title(mdInput)), repr(result))

    def testExtractTitleMissing(self):
        mdInput = "There is no title\nHelp meee"
        self.assertRaises(Exception, extract_title, mdInput)

if __name__=='__main__':
    unittest.main()
