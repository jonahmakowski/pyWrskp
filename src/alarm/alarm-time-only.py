import datetime

hour = int(input('What is the hour number - form 1 to 24'))
mint = int(input('What is the min number'))

now = datetime.datetime.now()

past_time = datetime.datetime(now.year, now.month, now.day, hour, mint)
past_time = past_time.strftime("%X")

now = now.strftime("%X")

while True:
    now = datetime.datetime.now()
    now = now.strftime("%X")
    if now == past_time:
        print('DING-DONG')
        print('Time up!')
        break
    #print('now ' + str(now))
    #print('Then ' + str(past_time))
