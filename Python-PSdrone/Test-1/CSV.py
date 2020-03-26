import time, csv
from ps_drone import *
import matplotlib.pyplot as plt

tableau = [["Temps", "Altitude", "Altitude cm", "Pitch",  "Vitesse", "Battery"]]





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
    drone.addNDpackage(["demo"])


    #drone.takeoff()

    for i in range(100):
        #drone.moveUp()
        # print(f'{i} sec')
        navdata = drone.NavData
        try:
            alt = navdata["altitude"][3]
            altcm = navdata["demo"][3]
            pitch = navdata["demo"][2][0]
            speed = navdata["demo"][4][0]


            print(f'{i} valeures')
            #tableau.append([i, alt])
            tableau.append([i, alt ,altcm, pitch, speed, int(drone.getBattery()[0])])
        except:
            print('Pass Altitude')
            print(f'NavData = {navdata}')
            tableau.append([i, "P"])
        time.sleep(0.1)
    drone.land()

    with open("tableau.csv", "w") as f_write:
        writer = csv.writer(f_write)
        for row in tableau:
            writer.writerow(row)