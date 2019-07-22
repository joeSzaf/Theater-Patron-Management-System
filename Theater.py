class Theater:

    def __init__(self, name, shows):
        self.__name = name
        self.__shows = shows
        self.__earnings = 0
        self.__patrons_not_seeing_shows = []

    def get_name(self):
        return self.__name

    def get_shows(self):
        return self.__shows

    # def sell_ticket(self, patron):
    #     for show in self.__shows:
    #         if

