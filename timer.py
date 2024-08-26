###Code for the timer
import time

##For the timer
import sys

##This way we can clear the old print statements
import os



def main():
##https://www.asciiart.eu/animals/dogs
##No artist mentioned
    dogWorking="""
 __          __        _    
 \ \        / /       | |   
  \ \  /\  / /__  _ __| | __
   \ \/  \/ / _ \| '__| |/ /
    \  /\  / (_) | |  |   < 
     \/  \/ \___/|_|  |_|\_\\
                            
                                

    
                .--~~,__
    :-....,-------`~~'._.'
    `-,,,  ,_      ;'~U'
    _,-' ,'`-__; '--.
    (_/'~~      ''''(;
    
    """
    
    clearScreen()
    
    
##https://www.asciiart.eu/animals/dogs
##Art by Linda Ball    
    dogResting="""
  _____           _   
 |  __ \         | |  
 | |__) |___  ___| |_ 
 |  _  // _ \/ __| __|
 | | \ \  __/\__ \ |_ 
 |_|  \_\___||___/\__|
                      
                          
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
    while z>0:
        ##Run the work countdown
        countDown(x,dogWorking)
        
        z=z-1 
        if z>0:
            ##Now we can run the rest period
            countDown(y,dogResting)
           
    

    
    ## Now we can add the end screen
    end()
    
    
    
    
    return 0



def clearScreen():
    # clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def getInput(prompt):

    ##Grab the value
    y=input(prompt)
    if y.isdigit():
        #Clear the screen and convert the value to int
        clearScreen()
        x=int(y)
        return x
    else:
        ##Recurse back into the function to get a valid input if said input is anything other than a positive integer
        clearScreen()
        x=getInput("Invalid Input. Please enter a positive integer: ")
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
            sys.stdout.write('\r            {min}:00 '.format(min=int(minutes)))
            time.sleep(1)
            seconds=seconds-1
        elif secondsLeft>0 and secondsLeft<10:
            ##Adding this exception so that the timer shows a zero infront of a single digit second. This way the format is uniform
            sys.stdout.write('\r            {min}:0{sec} '.format(min=int(minutes),sec=int(secondsLeft)))
            time.sleep(1)
            seconds=seconds-1
        else:
            ##Write an updating countdown 
            ##The space after the seconds value allows us to overwrite the second zero in the seconds tab as stdout doesn't overwrite the 
            sys.stdout.write('\r            {min}:{sec} '.format(min=int(minutes),sec=int(secondsLeft)))
            time.sleep(1)
            seconds=seconds-1
        
    clearScreen()
    #Make a beeping sound
    print('\a')
    
    
    return 0

def end():
    clearScreen()
    
    x="""

   _____                 _        _       _     
  / ____|               | |      | |     | |    
 | |  __  ___   ___   __| |      | | ___ | |__  
 | | |_ |/ _ \ / _ \ / _` |  _   | |/ _ \| '_ \ 
 | |__| | (_) | (_) | (_| | | |__| | (_) | |_) |
  \_____|\___/ \___/ \__,_|  \____/ \___/|_.__/ 
                                                
                                                    
    
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'   
    
    """
    print(x)
    
    #Make a beeping sound 3 times
    print('\a')
    time.sleep(2)
    print('\a')
    time.sleep(2)
    print('\a')


if __name__== '__main__':
    main()
    
                