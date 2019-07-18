class Patron:

    def __init__(self, first_name, last_name, email, preference = ["improv", "sketch", "standup", "drama"]):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__preference = preference

    def get_full_name(self):
        return self.__first_name + " " + self.__last_name

    def get_email(self):
        return self.__email

    def get_preferences(self):
        return self.__preference

