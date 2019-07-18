import unittest
from Show import Show
from datetime import datetime

# pytest

class ShowTest(unittest.TestCase):

    def setUp(self):
        self.show1 = Show("Mainstage", "07-01-2019 20:00:00", "07-01-2019 21:30:00", "improv")
        self.show2 = Show("Comedy Lab", "07-01-2019 19:30:00", "07-01-2019 21:00:00")
        self.show3 = Show("Peoples Show", "07-01-2019 21:30:00", "07-01-2019 23:00:00", "standup")
        self.show4 = Show("Sketch Planet", "07-01-2019 18:00:00", "07-01-2019 19:30:00", "sketch")

    def test_Show_displays_correct_name(self):
        self.assertEqual(self.show1.get_name(), "Mainstage")
        self.assertEqual(self.show2.get_name(), "Comedy Lab")
        self.assertEqual(self.show3.get_name(), "Peoples Show")
        self.assertEqual(self.show4.get_name(), "Sketch Planet")

    def test_Show_displays_correct_start_time(self):
        self.assertEqual(self.show1.get_start_time(), "07-01-2019 20:00:00")
        self.assertEqual(self.show2.get_start_time(), "07-01-2019 19:30:00")
        self.assertEqual(self.show3.get_start_time(), "07-01-2019 21:30:00")
        self.assertEqual(self.show4.get_start_time(), "07-01-2019 18:00:00")

    def test_Show_displays_correct_end_time(self):
        self.assertEqual(self.show1.get_end_time(), "07-01-2019 21:30:00")
        self.assertEqual(self.show2.get_end_time(), "07-01-2019 21:00:00")
        self.assertEqual(self.show3.get_end_time(), "07-01-2019 23:00:00")
        self.assertEqual(self.show4.get_end_time(), "07-01-2019 19:30:00")

    def test_Show_displays_correct_category(self):
        self.assertEqual(self.show1.get_category(), "improv")
        self.assertEqual(self.show2.get_category(), "improv")
        self.assertEqual(self.show3.get_category(), "standup")
        self.assertEqual(self.show4.get_category(), "sketch")

