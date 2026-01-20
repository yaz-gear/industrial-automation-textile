# programmed_automation.py
def run_programmed_routine():
    """
    Simplified programmed automation routine.
    Real system schedules sequences for motors and valves.
    """
    print("Starting programmed automation routine")
    steps = [
        "Activate motor_1 at speed 100",
        "Open valve_A",
        "Activate motor_2 at speed 80",
        "Close valve_A"
    ]
    for step in steps:
        print(step)

if __name__ == "__main__":
    run_programmed_routine()
