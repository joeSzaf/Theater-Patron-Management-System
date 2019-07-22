import unittest
from Patron import Patron
from Show import Show

# pytest

class ShowTest(unittest.TestCase):

    def setUp(self):
        self.patron1 = Patron("Janes", "Lashe", "jlashe@gmail.com", preferences = ["improv"])
        self.patron2 = Patron("Callahan", "Burgess", "cburg@gmail.com", preferences = ["standup", "drama"])
        self.patron3 = Patron("Gaugino", "Julio", "cjules@gmail.com")
        self.patron4 = Patron("Wilhelmina", "Smith", "wilhelmsmith@gmail.com", [("07-01-2019 10:00", "07-01-2019 17:00"), ("07-01-2019 18:30", "07-01-2019 22:00")], ["improv", "sketch", "standup"])

        self.show1 = Show("Mainstage", "07-01-2019 20:00", "07-01-2019 21:30", 20, 90, "improv")
        self.show2 = Show("Comedy Lab", "07-01-2019 19:30", "07-01-2019 21:00", 15, 40)
        self.show3 = Show("Peoples Show", "07-01-2019 21:30", "07-01-2019 23:00", 5, 40, "standup")
        self.show4 = Show("Sketch Planet", "07-01-2019 18:00", "07-01-2019 19:30", 15, 40, "sketch")

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

    def test_Patron_returns_correct_time_availability(self):
        self.assertEqual(self.patron1.get_availability()[0].get_start_time_string(), "07-01-2019 00:00")
        self.assertEqual(self.patron4.get_availability()[0].get_start_time_string(), "07-01-2019 10:00")
        self.assertEqual(len(self.patron4.get_availability()), 2)

    def test_Patron_matches_preferences_in_show_category(self):
        self.assertEqual(self.patron1.match_preference(self.show1), True)
        self.assertEqual(self.patron1.match_preference(self.show3), False)
        self.assertEqual(self.patron2.match_preference(self.show1), False)
        self.assertEqual(self.patron3.match_preference(self.show1), True)
        self.assertEqual(self.patron3.match_preference(self.show3), True)
        self.assertEqual(self.patron4.match_preference(self.show3), True)

    def test_Patron_availability_matches_show_availaiblity(self):
        self.assertEqual(self.patron1.match_time_availability(self.show1), True)
        self.assertEqual(self.patron4.match_time_availability(self.show4), False)
