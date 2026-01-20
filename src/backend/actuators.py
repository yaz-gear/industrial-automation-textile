# actuators.py
def activate_motor(name, speed):
    """
    Simplified motor activation.
    Real system uses GPIO to control relay connected to motor.
    """
    print(f"Activating {name} at speed {speed}")

def activate_valve(name, state):
    """
    Simplified solenoid valve activation.
    """
    status = "OPEN" if state else "CLOSED"
    print(f"{name} is {status}")
