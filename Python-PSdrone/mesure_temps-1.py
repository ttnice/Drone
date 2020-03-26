import time
from ps_drone import *
if __name__ == "__main__":
    drone = Drone()								# Start using drone
    drone.printBlue("Battery: ")

    drone.startup()											# Connects to drone and starts subprocesses
    drone.reset()											# Always good, at start


    while drone.getBattery()[0] == -1:	time.sleep(0.1)		# Waits until the drone has done its reset

    drone.printBlue("Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]))	# Gives a battery-status

    startVal = int(drone.getBattery()[0])
    stopVal = startVal-10

    currentVal = int(drone.getBattery()[0])
    starTime = time.time()
    while currentVal >= stopVal:
        currentVal = int(drone.getBattery()[0])
        print(f'Battery : {currentVal} %')
        time.sleep(1)
        drone.takeoff()
    drone.land()

    stopTime = time.time()
    print(f'Total flying time is {stopTime-starTime}')

#32; 30 sec pour puissance max en 10%