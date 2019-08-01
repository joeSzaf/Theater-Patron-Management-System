from TimeRange import TimeRange

class Patron:

    def __init__(self, first_name, last_name, email, availability=[("07-01-2019 00:00", "07-02-2019 00:00")], preferences=["improv", "sketch", "standup", "drama"]):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__preferences = preferences
        self.__availability = []
        for time_range in availability:
            self.__availability.append(TimeRange(time_range[0], time_range[1]))

    def get_full_name(self):
        return self.__first_name + " " + self.__last_name

    def get_email(self):
        return self.__email

    def get_preferences(self):
        return self.__preferences

    def get_availability(self):
        return self.__availability

    def match_preference(self, show):
        return show.get_category() in self.__preferences

    def match_time_availability(self, show):
        for time_range in self.__availability:
            if time_range.in_range(show.get_show_time_range()):
                return True
        return False
