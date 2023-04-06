import timer

seconds = input("Enter the Time(in secs): ")

def countdownTimer(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        sec = int(seconds%60)
        
        timer = f'{mins}:{sec}'
        print(timer)

        #seconds = seconds - 1
        seconds -= 1
    print("TIME UP!")

countdownTimer(int(seconds))        
