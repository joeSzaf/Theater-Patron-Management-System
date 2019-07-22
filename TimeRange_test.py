import unittest
from TimeRange import TimeRange

# pytest

class TimeRangeTest(unittest.TestCase):

    def setUp(self):
        self.time_range_1 = TimeRange("07-01-2019 10:00", "07-01-2019 20:00")
        self.time_range_2 = TimeRange("07-01-2019 12:00", "07-01-2019 15:30")
        self.time_range_3 = TimeRange("07-02-2019 10:00", "07-02-2019 15:30")
        self.time_range_4 = TimeRange("07-01-2019 18:00", "07-01-2019 20:01")

    def test_TimeRange_displays_start_time_string(self):
        self.assertEqual(self.time_range_1.get_start_time_string(), "07-01-2019 10:00")
        self.assertEqual(self.time_range_2.get_start_time_string(), "07-01-2019 12:00")

    def test_TimeRange_displays_end_time_string(self):
        self.assertEqual(self.time_range_3.get_end_time_string(), "07-02-2019 15:30")
        self.assertEqual(self.time_range_4.get_end_time_string(), "07-01-2019 20:01")

    def test_TimeRange_in_range_determines_if_daterange_in_range(self):
        self.assertEqual(self.time_range_1.in_range(self.time_range_2), True)
        self.assertEqual(self.time_range_1.in_range(self.time_range_3), False)
        self.assertEqual(self.time_range_2.in_range(self.time_range_1), False)
        self.assertEqual(self.time_range_1.in_range(self.time_range_4), False)



