import unittest
from usf.parser import USFParser

class TestUSFParser(unittest.TestCase):
    def test_load(self):
        parser = USFParser("sample.usf")
        parser.load()
        self.assertIsInstance(parser.data, dict)

if __name__ == "__main__":
    unittest.main()
