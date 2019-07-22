import unittest
from Theater import Theater
from Show import Show
from Patron import Patron
from datetime import datetime

# pytest

class ShowTest(unittest.TestCase):

    def setUp(self):
        self.show1 = Show("Mainstage", "07-01-2019 20:00:00", "07-01-2019 21:30:00", "improv")
        self.show2 = Show("Comedy Lab", "07-01-2019 19:30:00", "07-01-2019 21:00:00")
        self.show3 = Show("Peoples Show", "07-01-2019 21:30:00", "07-01-2019 23:00:00", "standup")
        self.show4 = Show("Sketch Planet", "07-01-2019 18:00:00", "07-01-2019 19:30:00", "sketch")

        self.patron1 = Patron("Janes", "Lashe", "jlashe@gmail.com", ["improv"])
        self.patron2 = Patron("Callahan", "Burgess", "cburg@gmail.com", ["standup", "drama"])
        self.patron3 = Patron("Gaugino", "Julio", "cjules@gmail.com")
        self.patron4 = Patron("Wilhelmina", "Smith", "wilhelmsmith@gmail.com", ["improv", "sketch", "standup"])

        self.theater = Theater("ImprovBoston", [self.show1, self.show2, self.show3, self.show4])

    def test_Theater_displays_correct_name(self):
        self.assertEqual(self.theater.get_name(), "ImprovBoston")

    def test_Theater_displays_correct_shows(self):
        self.assertEqual(self.theater.get_shows()[0], self.show1)
        self.assertEqual(self.theater.get_shows()[1].get_name(), "Comedy Lab")
        self.assertEqual(len(self.theater.get_shows()), 4)

