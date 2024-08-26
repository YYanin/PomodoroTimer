###Code for the timer
import time

##For the timer
import sys

##This way we can clear the old print statements
import os



def main():

    dogWorking="""
    
             .--~~,__
:-....,-------`~~'._.'
 `-,,,  ,_      ;'~U'
  _,-' ,'`-__; '--.
 (_/'~~      ''''(;
    
    """
    
    clearScreen()
    
    dogResting="""
    
  __    __
o-''))_____\\
"--__/ * * * )
c_c__/-c____/
    
    """
    
    clearScreen()    


    x=getInput(("Enter the time for pure concentration in minutes: "))
    
    y=getInput(("Enter the time for rest and relaxation: "))
    
    z=getInput(("Enter how many sets of work you want to do: "))
    
    
    #Create the main loop
    while z>=0:
        ##Run the work countdown
        countDown(x,dogWorking)
        ##Now we can run the rest period
        countDown(y,dogResting)
        
        z=z-1    
    

    
    ## Now we can add the end screen
    
    
    
    
    
    return 0



def clearScreen():
    # clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def getInput(prompt):

    ##Grab the values and convert them to int
    x=int(input(prompt))
    
    clearScreen()
    
    return x



def countDown(count,art):
    
    ##Convert Min to Sec
    seconds=count*60
    
    ##Print the art
    print(art, end="\r")
    
    while(seconds>=0):
        
        #Check how many min are left
        minutes=seconds/60
        
        #Check how many seconds are left
        secondsLeft=seconds
        while secondsLeft>=60:
            secondsLeft=secondsLeft-60
        
        ##Show double zeros if there are no seconds left for visual appeal
        if secondsLeft==0:
            sys.stdout.write('\r        {min}:00 '.format(min=int(minutes)))
            time.sleep(1)
            seconds=seconds-1  
        else:
            ##Write an updating countdown 
            ##The space after the seconds value allows us to overwrite the second zero in the seconds tab as stdout doesn't overwrite the 
            sys.stdout.write('\r        {min}:{sec} '.format(min=int(minutes),sec=int(secondsLeft)))
            time.sleep(1)
            seconds=seconds-1
        
    clearScreen()
    return 0

def end():
    clearScreen()
    
    x="""
    
    
    
    
    """
    #print()


if __name__== '__main__':
    main()