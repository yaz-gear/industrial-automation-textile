# main_controller.py
from sensors import read_temperature
from actuators import activate_motor, activate_valve
import time

def main_loop():
    """
    Simplified backend control loop for industrial automation.
    Real system controls 16 relays for motors and valves.
    """
    while True:
        temp = read_temperature()

        # Temperature-based automation
        if temp > 50:
            activate_valve("valve_A", True)
        else:
            activate_valve("valve_A", False)

        # Motor control simulation
        activate_motor("motor_1", speed=100)
        activate_motor("motor_2", speed=80)

        # Sleep to simulate loop delay
        time.sleep(2)

if __name__ == "__main__":
    main_loop()
