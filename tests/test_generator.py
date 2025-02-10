import unittest
from usf.generator import USFGenerator

class TestUSFGenerator(unittest.TestCase):
    def test_generate(self):
        generator = USFGenerator()
        generator.add_subject("Math", "Dr. Smith", "Room 101")
        generator.add_schedule(0, "Monday", "08:00-10:00", "all")
        self.assertEqual(len(generator.data["subjects"]), 1)
        self.assertEqual(len(generator.data["schedule"]), 1)

if __name__ == "__main__":
    unittest.main()
