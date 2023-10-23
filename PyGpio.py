import matplotlib.pyplot as plt
import tkinter

import pigpio
import time




pi1 = pigpio.pi()

z = 0

pi1.write(18, 1)

anfang = 0
counter = 0
last_tick = 0
start_tick = 0
last_tick2 = 0

schw_dauern=[]

tickdiff = 0

anzahl = 18

count = 10

root= tkinter.Tk()

def cbf(gpio, level, tick):

    global counter
    global anfang
    global start_tick
    global last_tick
    global schw_dauern

    global count

   

    #if counter >= 2:
    if tick-last_tick > 10000:
        counter += 1
        last_tick = tick
        

    if counter >= 2:
        counter = 0
        print((tick-start_tick)/1e6)
        schw_dauern.append((tick-start_tick)/1e6)
        start_tick = tick

        
            
    #print(counter)

    
    #print(gpio, level, tick)

   




    
cb1 = pi1.callback(12, pigpio.FALLING_EDGE, cbf)


while len(schw_dauern) < count:
    time.sleep(1)

    


##while counter < anzahl:
##    time.sleep(.1)

del schw_dauern[0]
cb1.cancel()




print(schw_dauern)

plt.plot(schw_dauern)
plt.show()







#while(1):
    
   

        

        #while(pi1.read(12) == 1):
            
            #time.sleep(1)
            #z += 1
            
            #print(z)

            #print(time.clock())

              


