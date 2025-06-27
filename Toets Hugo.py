from time import sleep

def teller ():
    teller = 0
    while True:
        print(teller)
        teller += 1
        sleep(.5)
        
teller()
