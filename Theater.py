class Theater:

    def __init__(self, name, shows):
        self.__name = name
        self.__shows = shows

    def get_name(self):
        return self.__name

    def get_shows(self):
        return self.__shows