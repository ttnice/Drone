import CSVtowple
import DRONEtowple
import time

''' ICI LES VALEURS D'ENTREE '''
tableau = [["Temps",
            "Battery",
            "Altitude mm",
            "Altitude cm",
            "height ",
            "Pitch",
            "Yaw",
            "Roll",
            "Vitesse X",
            "Vitesse Y",
            "Vitesse Z",
            "pwm_fr",
            "pwm_fl",
            "pwm_br",
            "pwm_bl",
            "mA_fr",
            "mA_fl",
            "mA_br",
            "mA_bl",
            "Wind Speed",
            "Wind Angle"
            ]]


if __name__ == "__main__":
    my_drone = DRONEtowple.DroneTowple()
    my_drone.drone.takeoff()

    for i in range(60):
        my_drone.drone.move(0, 0, 0.5, 0)
        time.sleep(0.1)

    for i in range(200):
        my_drone.drone.move(0, 0.2, 0.1, 0)
        navdata = my_drone.NavData()

        if my_drone.Quit:
            break

        try:
            ''' ICI EXTRACT DONNES DE NAVDATA '''

            altmm = navdata["altitude"][3]
            altcm = navdata["demo"][3]
            height = navdata["pressure_raw"][1]


            pitch = navdata["demo"][2][0]
            yaw = navdata["demo"][2][1]
            roll = navdata["demo"][2][2]

            battery = navdata["demo"][1]

            pwm_fr = navdata["pwm"][0][0]
            pwm_fl = navdata["pwm"][0][1]
            pwm_br = navdata["pwm"][0][2]
            pwm_bl = navdata["pwm"][0][3]

            mA_fr = navdata["pwm"][9][0]
            mA_fl = navdata["pwm"][9][1]
            mA_br = navdata["pwm"][9][2]
            mA_bl = navdata["pwm"][9][3]

            speed_X = navdata["demo"][4][0]
            speed_Y = navdata["demo"][4][1]
            speed_Z = navdata["demo"][4][2]

            wind_speed = navdata['wind_speed'][0]
            wind_angle = navdata['wind_speed'][1]




            ''' ICI LES VALEURES TROUVEES '''
            tableau.append([i, battery , altmm, altcm, height, pitch, yaw , roll, speed_X, speed_Y, speed_Z , pwm_fr , pwm_fl , pwm_br, pwm_bl , mA_fr, mA_fl , mA_br , mA_bl , wind_speed , wind_angle])
        except:
            print('Pass Altitude')
            print(f'NavData = {navdata}')

            tableau.append([i]+["P" for i in range(1, len(tableau[0]))])
        time.sleep(0.1)
    my_drone.drone.land()

    CSVtowple.write('decollage2.csv', tableau)



