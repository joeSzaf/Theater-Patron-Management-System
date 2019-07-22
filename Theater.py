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

    def get_earnings(self):
        return self.__earnings

    def sell_ticket(self, patron):
        for show in self.__shows:
            if patron.match_preference(show) and patron.match_time_availability(show):
                if show.add_patron(patron):
                    self.__earnings += show.get_ticket_price()
                    break
        self.__patrons_not_seeing_shows.append(patron)

    def handle_patrons(self, patrons):
        for patron in patrons:
            self.sell_ticket(patron)

