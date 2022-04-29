import time

def countdown(x):
    while(x):
        min, sec = divmod(x, 60)
        clock = '{:02d}:{:02d}'.format(min,sec)
        print(clock, end='\n')
        time.sleep(1)
        x -= 1


print('Time\'s up!')

x = input("Enter the time in seconds.")

countdown(int(x))