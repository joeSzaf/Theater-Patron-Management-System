from datetime import datetime

date_format = "%m-%d-%Y %H:%M:%S"

def main():
    start = datetime.strptime("07-01-2019 08:30:00", date_format)
    end = datetime.strptime("07-01-2019 10:0:00", date_format)
    diff = end - start

    print( end > start)



main()