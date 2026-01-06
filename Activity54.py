import random 
import time 
def generate_random_date(start_date, end_date):
    x = random.random()
    y = "%d/%m/%y"
    print(f"Printing random date between {start_date} and {end_date}")
    start_time = time.mktime(time.strptime(start_date,y))
    end_time = time.mktime(time.strptime(end_date,y))
    randontime = start_time+x*(end_time-start_time)
    random_date = time.strftime(y,time.localtime(random.time))
    return random_date
print(generate_random_date("1/1/2026", "31/12/2026"))
