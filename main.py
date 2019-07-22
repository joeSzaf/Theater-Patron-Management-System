from Patron import Patron
from Theater import Theater
from Show import Show
from TimeRange import TimeRange

def main():
    patron1 = Patron("Janes", "Lashe", "jlashe@gmail.com", preferences=["improv"])
    patron2 = Patron("Callahan", "Burgess", "cburg@gmail.com", preferences=["standup", "drama"])
    patron3 = Patron("Gaugino", "Julio", "cjules@gmail.com")
    patron4 = Patron("Wilhelmina", "Smith", "wilhelmsmith@gmail.com",
                          [("07-01-2019 10:00", "07-01-2019 17:00"), ("07-01-2019 18:30", "07-01-2019 22:00")],
                          ["improv", "sketch", "standup"])

    show1 = Show("Mainstage", "07-01-2019 20:00", "07-01-2019 21:30", 20, 90, "improv")
    show2 = Show("Comedy Lab", "07-01-2019 19:30", "07-01-2019 21:00", 15, 40)
    show3 = Show("Peoples Show", "07-01-2019 21:30", "07-01-2019 23:00", 5, 40, "standup")
    show4 = Show("Sketch Planet", "07-01-2019 18:00", "07-01-2019 19:30", 15, 40, "sketch")

    shows = [show1, show2, show3, show4]
    patrons =[patron1, patron2, patron3, patron4]

    theater = Theater("ImprovBoston", shows)
    theater.handle_patrons(patrons)
    print(theater.get_earnings())




main()