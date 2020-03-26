# -*- coding: UTF-8 -*-

import olympe
from olympe.messages.ardrone2.Piloting import TakeOff


# drone = olympe.Drone("192.168.1.2")
drone = olympe.Drone("fe80::fcd0:f84a:2915:e327")
drone.connection()
drone(TakeOff()).wait()
drone.disconnection()
