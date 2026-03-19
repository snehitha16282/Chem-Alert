# Chem-Alert
IoT based Hazardous Gas Detection System with ESP32,MQ2 Sensor,and AdaFruit IO Cloud Alerts


📌 Overview
ChemAlert is an **IoT-based real-time gas detection system** designed to enhance **public and worker safety**.  
It uses an **ESP32 microcontroller**, **MQ2 gas sensor**, **buzzer**, **LED**, and **16x2 I2C LCD display** to detect harmful gases like LPG, methane, and alcohol.  
The system sends **instant alerts to the cloud via Adafruit IO**, ensuring timely notifications.

🎥 Demo




🎯 Objectives
- Real-time hazardous gas detection.
- Immediate **local alerts** using buzzer + LED.
- Remote **cloud alerts** via Adafruit IO.
- Display gas status on **LCD screen**.
- Enhance **safety in chemical labs, industries, and households**.

---

⚙️ Components Used
- **ESP32 DevKit**  
- **MQ2 Gas Sensor**  
- **16x2 I2C LCD**  
- **Buzzer + LED**  
- **Adafruit IO (Cloud Platform)**  

---

🏗 System Architecture
📂 <img width="822" height="333" alt="image" src="https://github.com/user-attachments/assets/62c16404-1136-4b9b-b957-e8bd39b08cfa" />

---

📜 Features
 🔊 Buzzer alert for immediate warning
 💡 LED indication for visual alert
 📟 LCD display showing gas status
 🌐 Cloud notifications via Adafruit IO
 📡 Remote monitoring from anywhere
 
🧠 Working Principle
 MQ2 sensor continuously monitors gas concentration in the environment
 ESP32 reads analog values from the sensor
 If gas level exceeds a predefined threshold:
 Buzzer is activated
 LED turns ON
 Alert is sent to Adafruit IO
 LCD displays real-time gas level and alert status
 Cloud dashboard updates data every few seconds

📊 Results
 Gas detection response time: ~2–3 seconds
 Real-time LCD updates with gas levels
 Successful alert triggering for LPG exposure
 Cloud data updates every 3–5 seconds
 Reliable performance during continuous testing 
 
🚀 Setup Instructions
 1. Hardware Setup
  Connect MQ2 sensor to ESP32 (Analog pin)
  Connect LCD using I2C interface
  Attach buzzer and LED to digital pins
 2. Software Setup
  Install Arduino IDE
  Install ESP32 board package
  Install required libraries:
  Adafruit MQTT
  WiFi
  LiquidCrystal_I2C
 3. Configuration
  Add your WiFi credentials in code
  Add Adafruit IO username and key
 4. Upload Code
  Connect ESP32 via USB
  Upload code using Arduino IDE
  Open Serial Monitor for debugging
