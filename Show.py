class Show:

    def __init__(self, name, start_time, end_time, ticket_price, category = "improv"):
        self.__name = name
        self.__start_time = start_time
        self.__end_time = end_time
        self.__ticket_price = ticket_price
        self.__category = category

    def get_name(self):
        return self.__name

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_category(self):
        return self.__category

    def get_ticket_price(self):
        return self.__ticket_price



