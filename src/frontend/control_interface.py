# control_interface.py
def manual_control():
    """
    Simplified manual control simulation.
    In real system, this would be tablet or web interface.
    """
    print("Manual control active")
    # Example switch operations
    motor_cmd = input("Activate motor_1? (y/n): ")
    if motor_cmd.lower() == "y":
        print("Motor_1 activated (simulated)")

    valve_cmd = input("Open valve_A? (y/n): ")
    if valve_cmd.lower() == "y":
        print("Valve_A opened (simulated)")

if __name__ == "__main__":
    manual_control()
