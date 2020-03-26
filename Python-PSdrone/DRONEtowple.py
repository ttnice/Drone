from ps_drone import *
from threading import Thread


class DroneTowple(Thread):

    def __init__(self):
        self.drone = Drone()  # Start using drone
        self.drone.startup()  # Connects to drone and starts subprocesses
        self.drone.reset()  # Always good, at start

        while self.drone.getBattery()[0] == -1:    time.sleep(0.1)  # Waits until the drone has done its reset

        ''' ICI LE NOM DES PACKAGES '''
        self.packages = ['altitude', 'demo', 'pressure_raw', 'wind_speed', 'pwm']

        self.drone.setConfig("control vz max", "0.04")
        self.drone.useDemoMode(False)
        self.drone.getNDpackage(self.packages)

        Thread.__init__(self)
        self.Quit = False
        self.start()

    def run(self):
        input('Entre Enter pour quitter')
        self.Quit = True
        self.drone.land()

    def NavData(self):
        navData = self.drone.NavData
        return navData


