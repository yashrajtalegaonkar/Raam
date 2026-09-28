# Project Title
ESP32 Local Device-to-Device Communication Without Internet

## Date
1 February 2026

## Team / Individual
Dr MS Swaminathan

## Track / Domain
Internet of Things (IoT)  
Embedded Systems  
Wireless Communication

---

## Problem Statement
Most IoT systems rely heavily on internet connectivity or centralized routers for communication between devices. In scenarios such as remote locations, disaster zones, highways, or secure industrial environments, internet access may be unavailable or unreliable. There is a need for a robust, low-latency, and direct communication mechanism between IoT devices without dependency on the internet.

---

## Objective
To establish a reliable wireless network between two ESP32 development boards and enable direct data transfer between them without using the internet or any external router.

---

## Proposed Solution
The project implements peer-to-peer communication between two ESP32 devices using the ESP-NOW protocol. ESP-NOW allows direct device-to-device data exchange over Wi-Fi radio without requiring an access point or internet connection. One ESP32 acts as a sender and the other as a receiver, exchanging structured data packets efficiently and securely.

---

## System Architecture
- Two ESP32 development boards  
- Peer-to-peer wireless communication  
- No router, no internet dependency  
- Communication based on device MAC addresses  

---

## Technology Stack
### Hardware
- ESP32 Development Boards (2 units)
- USB cables
- Laptop / PC

### Software
- Arduino IDE
- ESP32 Board Package (Espressif)
- ESP-NOW Protocol
- Embedded C/C++

---

## Methodology
1. Install and configure ESP32 board support in Arduino IDE.
2. Retrieve the MAC address of each ESP32 device.
3. Initialize Wi-Fi in station mode on both devices.
4. Initialize ESP-NOW protocol.
5. Register peer devices using MAC addresses.
6. Define a structured data format for communication.
7. Implement sender logic to transmit data periodically.
8. Implement receiver callback function to process incoming data.
9. Validate communication using Serial Monitor.

---

## Data Flow
1. Sender ESP32 generates or collects data.
2. Data is packaged into a structured format.
3. ESP-NOW transmits data wirelessly using MAC addressing.
4. Receiver ESP32 captures data using a receive callback.
5. Received data is displayed or processed further.

---

## Key Features
- Internet-independent communication
- Low latency data transfer
- Low power consumption
- Scalable to multiple ESP32 nodes
- Suitable for real-time IoT and IIoT applications

---

## Use Cases
- Vehicle-to-vehicle communication
- Sensor-to-controller systems
- Smart agriculture
- Industrial automation
- Emergency and disaster response systems

---

## Challenges
- Limited payload size per ESP-NOW packet
- MAC address management for multiple devices
- Debugging wireless communication issues

---

## Future Enhancements
- Add encryption for secure data transmission
- Implement multi-node ESP-NOW mesh
- Integrate sensors and actuators
- Add acknowledgment and retry mechanisms
- Combine with gateway node for cloud upload (optional)

---

## Conclusion
This project successfully demonstrates local, reliable, and efficient communication between two ESP32 devices without relying on internet connectivity. The ESP-NOW protocol proves to be an effective solution for decentralized IoT systems where speed, reliability, and independence from infrastructure are critical.

---

## References
- Espressif ESP-NOW Documentation
- ESP32 Technical Reference Manual
- Arduino ESP32 Core Documentation
