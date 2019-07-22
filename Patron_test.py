import unittest
from Patron import Patron
from Show import Show

# pytest

class ShowTest(unittest.TestCase):

    def setUp(self):
        self.patron1 = Patron("Janes", "Lashe", "jlashe@gmail.com", ["improv"])
        self.patron2 = Patron("Callahan", "Burgess", "cburg@gmail.com", ["standup", "drama"])
        self.patron3 = Patron("Gaugino", "Julio", "cjules@gmail.com")
        self.patron4 = Patron("Wilhelmina", "Smith", "wilhelmsmith@gmail.com", ["improv", "sketch", "standup"])

        self.show1 = Show("Mainstage", "07-01-2019 20:00", "07-01-2019 21:30", 20, "improv")
        self.show3 = Show("Peoples Show", "07-01-2019 21:30", "07-01-2019 23:00", 5, "standup")

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

    def test_Patron_matches_preferences_in_show_category(self):
        self.assertEqual(self.patron1.match_preference(self.show1), True)
        self.assertEqual(self.patron1.match_preference(self.show3), False)
        self.assertEqual(self.patron2.match_preference(self.show1), False)
        self.assertEqual(self.patron3.match_preference(self.show1), True)
        self.assertEqual(self.patron3.match_preference(self.show3), True)
        self.assertEqual(self.patron4.match_preference(self.show3), True)

