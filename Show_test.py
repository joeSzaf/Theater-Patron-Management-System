import unittest
from Show import Show
from Patron import Patron
from datetime import datetime

# pytest

class ShowTest(unittest.TestCase):

    def setUp(self):
        self.show1 = Show("Mainstage", "07-01-2019 20:00", "07-01-2019 21:30", 20, 90, "improv")
        self.show2 = Show("Comedy Lab", "07-01-2019 19:30", "07-01-2019 21:00", 15, 40)
        self.show3 = Show("Peoples Show", "07-01-2019 21:30", "07-01-2019 23:00", 5, 40, "standup")
        self.show4 = Show("Sketch Planet", "07-01-2019 18:00", "07-01-2019 19:30", 15, 40, "sketch")
        self.show5 = Show("Small Show", "07-01-2019 18:00", "07-01-2019 19:30", 15, 3, "sketch")

        self.patron1 = Patron("Janes", "Lashe", "jlashe@gmail.com", ["improv"])
        self.patron2 = Patron("Callahan", "Burgess", "cburg@gmail.com", ["standup", "drama"])
        self.patron3 = Patron("Gaugino", "Julio", "cjules@gmail.com")
        self.patron4 = Patron("Wilhelmina", "Smith", "wilhelmsmith@gmail.com", ["improv", "sketch", "standup"])

    def test_Show_displays_correct_name(self):
        self.assertEqual(self.show1.get_name(), "Mainstage")
        self.assertEqual(self.show2.get_name(), "Comedy Lab")
        self.assertEqual(self.show3.get_name(), "Peoples Show")
        self.assertEqual(self.show4.get_name(), "Sketch Planet")

    # def test_Show_displays_correct_start_time(self):
    #     self.assertEqual(self.show1.get_start_time(), "07-01-2019 20:00")
    #     self.assertEqual(self.show2.get_start_time(), "07-01-2019 19:30")
    #     self.assertEqual(self.show3.get_start_time(), "07-01-2019 21:30")
    #     self.assertEqual(self.show4.get_start_time(), "07-01-2019 18:00")
    #
    # def test_Show_displays_correct_end_time(self):
    #     self.assertEqual(self.show1.get_end_time(), "07-01-2019 21:30")
    #     self.assertEqual(self.show2.get_end_time(), "07-01-2019 21:00")
    #     self.assertEqual(self.show3.get_end_time(), "07-01-2019 23:00")
    #     self.assertEqual(self.show4.get_end_time(), "07-01-2019 19:30")

    def test_Show_displays_correct_category(self):
        self.assertEqual(self.show1.get_category(), "improv")
        self.assertEqual(self.show2.get_category(), "improv")
        self.assertEqual(self.show3.get_category(), "standup")
        self.assertEqual(self.show4.get_category(), "sketch")

    def test_Show_returns_correct_ticket_price(self):
        self.assertEqual(self.show1.get_ticket_price(), 20)
        self.assertEqual(self.show2.get_ticket_price(), 15)
        self.assertEqual(self.show3.get_ticket_price(), 5)
        self.assertEqual(self.show4.get_ticket_price(), 15)

    def test_Show_returns_correct_capacity(self):
        self.assertEqual(self.show1.get_capacity(), 90)
        self.assertEqual(self.show2.get_capacity(), 40)
        self.assertEqual(self.show3.get_capacity(), 40)
        self.assertEqual(self.show4.get_capacity(), 40)

    def test_Show_successfully_adds_patrons_to_show(self):
        self.assertEqual(self.show5.get_patrons(), [])
        self.assertEqual(self.show5.add_patron(self.patron1), True)
        self.assertEqual(self.show5.get_number_of_patrons(), 1)
        self.assertEqual(self.show5.get_patrons()[0].get_email(), "jlashe@gmail.com")
        self.assertEqual(self.show5.add_patron(self.patron2), True)
        self.assertEqual(self.show5.add_patron(self.patron3), True)
        self.assertEqual(self.show5.get_number_of_patrons(), 3)
        self.assertEqual(self.show5.get_patrons()[-1].get_email(), "cjules@gmail.com")

        # should not be able to add patrons to the show since it is now at capacity
        self.assertEqual(self.show5.add_patron(self.patron4), False)
        self.assertEqual(self.show5.get_number_of_patrons(), 3)
        self.assertEqual(self.show5.get_patrons()[-1].get_email(), "cjules@gmail.com")

