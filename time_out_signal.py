import os
import sys

""" 
this program adapts the "signal.alarm" mechanism to count the execution time and adopts the "signal.signal" to handle the time out situation. 
First, set up the signal and signal alarm
Second, use the "try" to execute the program and to capture the TimeOutError exception
Third, the signal will raise up a TimeOutError exception if the execution time is too long. Then the "try" part will capture the exception and terminal the program. 
Forth, if the program finished before the timeout, the "try" will reset the signal.alarm. Then the TimeOutError will not be triggerd. 
"""


def bug_reproduce():
    import time
    time.sleep(5)
    return result

def time_out(func, args = (), kwargs={},timeout = 10):
    import signal  
    class TimeOutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeOutError()
    
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(4)
    try:
        result = func(*args,**kwargs)
    except TimeOutError as exc:
        result = 1                # 1 is the default return result. 
    finally:
        signal.alarm(0)

    return result

def run():
    cen_time = 100
    for i in range(cen_time):
        print (">>>>"+str(i) +">>>>>>")
        result = time_out(bug_reproduce,timeout = 1)
        if not result == 0:
            sys.exit(1)

if __name__ == "__main__":
    run()
	
