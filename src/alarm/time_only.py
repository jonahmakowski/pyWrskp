import datetime


def work(hour, mint, print_info=True):
    hour = int(hour)
    mint = int(mint)
    now = datetime.datetime.now()

    past_time = datetime.datetime(now.year, now.month, now.day, hour, mint)
    past_time = past_time.strftime("%X")

    while True:
        now = datetime.datetime.now()
        now = now.strftime("%X")
        if now == past_time:
            if print_info:
                print("DING-DONG")
                print("Time up!")
            return "DING-Dong"
