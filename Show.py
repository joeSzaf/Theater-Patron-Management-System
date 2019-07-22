class Show:

    def __init__(self, name, start_time, end_time, category = "improv"):
        self.__name = name
        self.__start_time = start_time
        self.__end_time = end_time
        self.__category = category

    def get_name(self):
        return self.__name

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_category(self):
        return self.__category



