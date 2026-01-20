# Industrial Automation System (Textile Roll Painting Machine)

## Overview
This repository presents a simplified and anonymized version of an industrial automation system I developed for a textile roll painting machine. The system automates temperature control, motorized rolls, and solenoid valves, and allows remote operation via tablet or WiFi.  

> ⚠️ Disclaimer: All client-specific hardware, software, and production details have been removed. This version demonstrates the architecture, logic, and my contribution only.

## Problem Statement
Manual operation of textile roll painting machines is time-consuming, error-prone, and difficult to control remotely. The goal of this project was to automate the process, increase efficiency, reduce errors, and enable remote monitoring and control.

## System Description
The system integrates the following components:
- **Raspberry Pi** as central controller
- **Thermometer** with a translation board converting binary signals to analog input
- **16 relays** controlling motors and solenoid valves
- **Motors and electro-valves** for material handling and painting
- **Remote control interface** via WiFi and tablet

The Raspberry Pi reads sensor data, executes control logic, and actuates relays accordingly. The system allows operators to monitor and adjust the machine remotely while ensuring safe operation.

## My Contribution
- Designed the system architecture and workflow
- Implemented control algorithms for motors and valves
- Integrated sensors with the Raspberry Pi
- Developed remote interface logic for WiFi control
- Tested and optimized system performance

## Technologies Used
- Raspberry Pi
- Python
- Relays and GPIO control
- WiFi-based remote communication
- Process automation principles

## Results
- Automated a fully manual textile roll painting machine
- Enabled remote operation and monitoring
- Improved process efficiency and reliability
