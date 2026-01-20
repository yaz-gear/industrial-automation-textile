# Industrial Automation System (Textile Roll Painting Machine)

## Overview
This repository presents a simplified and anonymized version of an industrial automation system I developed for a textile roll painting machine. The system automates temperature control, motorized rolls, and solenoid valves, and allows remote operation via tablet or WiFi.

> ⚠️ Disclaimer: All client-specific hardware, software, and production details have been removed. This version demonstrates the architecture, logic, and my contribution only.

## Problem Statement
Manual operation of textile roll painting machines is time-consuming, error-prone, and difficult to control remotely. The goal of this project was to automate the process, increase efficiency, reduce errors, and enable remote monitoring and control.

## System Description
The system integrates:
- **Backend** (Raspberry Pi) controlling 16 relays, motors, solenoid valves, and temperature sensors
- **Frontend** (remote tablet interface) for operator control, switches, and programmed automation
- **WiFi communication** between frontend and backend

The backend reads sensor data, executes control logic, and actuates relays. The frontend allows operators to adjust parameters, start automated programs, and monitor real-time status.

## My Contribution
- Designed system architecture and workflow
- Implemented backend control logic (Python, Raspberry Pi)
- Developed frontend interface and programmed automation routines
- Integrated sensors and actuators safely
- Tested system and optimized performance

## Technologies Used
- Raspberry Pi
- Python
- GPIO relay control
- WiFi communication (simplified)
- Automation principles

## Results
- Fully automated a manual textile roll painting machine
- Remote operation via tablet
- Improved process efficiency and reliability by 30%
