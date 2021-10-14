import datetime

hour = int(input('What is the hour number? - form 1 to 24'))
mint = int(input('What is the min number? - from 0 to 59'))
day = int(input('What is the day? - from 1 to 31'))
month = int(input('What is the mounth? - from 1 to 12'))
year = int(input('What is the year?'))

now = datetime.datetime.now()

past_time = datetime.datetime(year, month, day, hour, mint, 0)
now_list = str(now)
now_list = list(now_list)
now_list = now_list[:-7]
now_list2 = ''
for char in now_list:
    now_list2 += char
now_list = now_list2

while True:
    now = datetime.datetime.now()
    now_list = str(now)
    now_list = list(now_list)
    now_list = now_list[:-7]
    now_list2 = ''
    for char in now_list:
        now_list2 += char
    now_list = now_list2
    
    if now == past_time:
        print('DING-DONG')
        print('Time up!')
        break
    #print('Now ' + str(now))
    #print('Then ' + str(past_time))