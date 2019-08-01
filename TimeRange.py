from datetime import datetime


class TimeRange:
    def __init__(self, start_time, end_time):
        self.__start_time = datetime.strptime(start_time, '%m-%d-%Y %H:%M')
        self.__end_time = datetime.strptime(end_time, '%m-%d-%Y %H:%M')

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_start_time_string(self):
        return self.__start_time.strftime('%m-%d-%Y %H:%M')

    def get_end_time_string(self):
        return self.__end_time.strftime('%m-%d-%Y %H:%M')

    def in_range(self, time_range):
        return time_range.get_start_time() >= self.__start_time and time_range.get_end_time() <= self.__end_time
