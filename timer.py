###Code for the timer
import time
import sys


def main():
    print("Pomodoro Timer \n")

    print("Enter the work time: \n")

    ##Grab the values and convert them to an int
    x=int(input("Enter the time for pure concentration in minutes: "))
    
    y=int(input("Enter the time for rest and relaxation: "))
    
    z=int(input("Enter how many sets of work you want to do: "))
    
    countDown(x,y,z)
    
    return 0

def countDown(work,rest,set):
    
    ##Convert Min to Sec
    seconds=work*60
    
    
    while(seconds>=0):
        
        #Check how many min are left
        minutes=seconds/60
        
        #Check how many seconds are left
        secondsLeft=seconds
        while secondsLeft>=60:
            secondsLeft=secondsLeft-60
        
        ##Show double zeros if there are no seconds left for visual appeal
        if secondsLeft==0:
            sys.stdout.write('\r{min}:00'.format(min=int(minutes)))
            time.sleep(1)
            seconds=seconds-1
        ##elif secondsLeft==0 and minutes==0:
            ##This elif will be triggered when the timer reaches zero
            
        else:
            ##Write an updating countdown 
            ##The space after the seconds value allows us to overwrite the second zero in the seconds tab as stdout doesn't overwrite the 
            sys.stdout.write('\r{min}:{sec} '.format(min=int(minutes),sec=int(secondsLeft)))
            time.sleep(1)
            seconds=seconds-1
        
    
    return 0
    


if __name__== '__main__':
    main()