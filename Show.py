class Show:

    def __init__(self, name, start_time, end_time, ticket_price, capacity, category = "improv"):
        self.__name = name
        self.__start_time = start_time
        self.__end_time = end_time
        self.__ticket_price = ticket_price
        self.__category = category
        self.__capacity = capacity
        self.__patrons = []

    def get_name(self):
        return self.__name

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_category(self):
        return self.__category

    def get_capacity(self):
        return self.__capacity

    def get_patrons(self):
        return self.__patrons

    def get_number_of_patrons(self):
        return len(self.__patrons)

    def add_patron(self, patron):
        if len(self.__patrons) >= self.get_capacity():
            return False
        else:
            self.__patrons.append(patron)
            return True

    def get_ticket_price(self):
        return self.__ticket_price



