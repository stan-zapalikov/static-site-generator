import unittest
from src.main import extract_title
from src.leafnode import LeafNode

class TestMain(unittest.TestCase):
    def testExtractTitleProper(self):
        result = "This is a title"
        mdInput = "# This is a title\ntesting\ntesting"
        self.assertEqual(extract_title(mdInput), result)

    def testExtractTitleMissing(self):
        mdInput = "There is no title\nHelp meee"
        self.assertRaises(Exception, extract_title, mdInput)

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__=='__main__':
    unittest.main()
