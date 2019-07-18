import unittest
from Patron import Patron

# pytest

class ShowTest(unittest.TestCase):

    def setUp(self):
        self.patron1 = Patron("Janes", "Lashe", "jlashe@gmail.com", ["improv"])
        self.patron2 = Patron("Callahan", "Burgess", "cburg@gmail.com", ["standup", "drama"])
        self.patron3 = Patron("Gaugino", "Julio", "cjules@gmail.com")
        self.patron4 = Patron("Wilhelmina", "Smith", "wilhelmsmith@gmail.com", ["improv", "sketch", "standup"])

    def test_Patron_displays_correct_name(self):
        self.assertEqual(self.patron1.get_full_name(), "Janes Lashe")
        self.assertEqual(self.patron2.get_full_name(), "Callahan Burgess")
        self.assertEqual(self.patron3.get_full_name(), "Gaugino Julio")
        self.assertEqual(self.patron4.get_full_name(), "Wilhelmina Smith")

    def test_Patron_displays_correct_email(self):
        self.assertEqual(self.patron1.get_email(), "jlashe@gmail.com")
        self.assertEqual(self.patron3.get_email(), "cjules@gmail.com")

    def test_Patron_displays_correct_show_preferences(self):
        self.assertEqual(self.patron1.get_preferences(), ["improv"])
        self.assertEqual(self.patron4.get_preferences(), ["improv", "sketch", "standup"])
        self.assertEqual(len(self.patron3.get_preferences()), 4)

