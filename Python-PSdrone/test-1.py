import time, csv
from ps_drone import *

tableau = [["Temps"], ["Altitude"]]





if __name__ == "__main__":
    drone = Drone()								# Start using drone
    drone.printBlue("Battery: ")

    drone.startup()											# Connects to drone and starts subprocesses
    drone.reset()											# Always good, at start


    while drone.getBattery()[0] == -1:	time.sleep(0.1)		# Waits until the drone has done its reset

    drone.printBlue("Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]))	# Gives a battery-status
    drone.setConfig("control vz max", "0.04")
    drone.useDemoMode(False)
    drone.getNDpackage(["altitude"])


    drone.takeoff()
    for i in range(100):
        drone.moveUp()
        # print(f'{i} sec')
        try:
            val = drone.NavData["altitude"][3]
            print(f'{i} - Altitude : {val}')
            tableau[0].append(i)
            tableau[1].append(val)
        except:
            print('Pass Altitude')
        time.sleep(0.1)
    drone.land()

    with open("tableau.csv", "w") as f_write:
        writer = csv.writer(f_write)
        for row in tableau:
            writer.writerow(row)

"""
stop = False
while not stop:
    key = drone.getKey()
    if key == " ":
        if drone.NavData["demo"][0][2] and not drone.NavData["demo"][0][3]:	drone.takeoff()
        else:																drone.land()
    elif key == "0":	drone.hover()
    elif key == "w":	drone.moveForward()
    elif key == "s":	drone.moveBackward()
    elif key == "a":	drone.moveLeft()
    elif key == "d":	drone.moveRight()
    elif key == "q":	drone.turnLeft()
    elif key == "e":	drone.turnRight()
    elif key == "7":	drone.turnAngle(-10,1)
    elif key == "9":	drone.turnAngle( 10,1)
    elif key == "4":	drone.turnAngle(-45,1)
    elif key == "6":	drone.turnAngle( 45,1)
    elif key == "1":	drone.turnAngle(-90,1)
    elif key == "3":	drone.turnAngle( 90,1)
    elif key == "8":	drone.moveUp()
    elif key == "2":	drone.moveDown()
    elif key == "*":	drone.doggyHop()
    elif key == "+":	drone.doggyNod()
    elif key == "-":	drone.doggyWag()
    elif key != "":		stop = True
"""