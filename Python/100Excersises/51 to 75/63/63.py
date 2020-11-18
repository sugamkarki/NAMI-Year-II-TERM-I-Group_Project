import time
timerDelay=0
while(True):
    if(timerDelay==4):
        print("end of loop")
        break
    time.sleep(timerDelay)
    print("hello")
    timerDelay+=1