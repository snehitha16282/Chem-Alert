# 🚨 Chem-Alert  
**IoT-Based Hazardous Gas Detection System using ESP32, MQ2 Sensor & Adafruit IO**

---

## 📌 Overview  
Chem-Alert is an **IoT-based real-time gas detection system** designed to improve **public and industrial safety**.  
It detects hazardous gases like **LPG, methane, and alcohol** using an MQ2 sensor and sends **instant alerts both locally and to the cloud**.

The system integrates **hardware + cloud + real-time monitoring**, making it suitable for **labs, industries, and smart homes**.

---

## 🎥 Demo  
👉 

---

## 🌐 Live Dashboard  
👉 https://io.adafruit.com/snehitha16282/dashboards/chem-alert

---

## 🎯 Objectives  
- Real-time hazardous gas detection  
- Immediate **local alerts** using buzzer + LED  
- Remote **cloud alerts** via Adafruit IO  
- Display gas status on **LCD screen**  
- Improve safety in **workplaces and homes**

---

## ⚙️ Components Used  
- ESP32 DevKit  
- MQ2 Gas Sensor  
- 16x2 I2C LCD Display  
- Buzzer  
- LED  
- Adafruit IO (Cloud Platform)

---

## 🏗 System Architecture  
📂 <img width="822" height="333" alt="image" src="https://github.com/user-attachments/assets/62c16404-1136-4b9b-b957-e8bd39b08cfa" />
---

## 📜 Features  
- 🚨 Real-time gas detection  
- 🔊 Buzzer alert for immediate warning  
- 💡 LED indication for visual alert  
- 📟 LCD display showing gas status  
- 🌐 Cloud notifications via Adafruit IO  
- 📡 Remote monitoring from anywhere  

---

## 🧠 Working Principle  
1. MQ2 sensor continuously monitors gas concentration in the environment  
2. ESP32 reads analog values from the sensor  
3. If gas level exceeds a predefined threshold:  
   - Buzzer is activated  
   - LED turns ON  
   - Alert is sent to Adafruit IO  
4. LCD displays real-time gas level and alert status  
5. Cloud dashboard updates data every few seconds  

---

## 📊 Results  
- Gas detection response time: ~2–3 seconds  
- Real-time LCD updates with gas levels  
- Successful alert triggering for LPG exposure  
- Cloud data updates every 3–5 seconds  
- Reliable performance during continuous testing  

---

## 🚀 Setup Instructions  

### 1. Hardware Setup  
- Connect MQ2 sensor to ESP32 (Analog pin)  
- Connect LCD using I2C interface  
- Attach buzzer and LED to digital pins  

### 2. Software Setup  
- Install Arduino IDE  
- Install ESP32 board package  
- Install required libraries:  
  - Adafruit MQTT  
  - WiFi  
  - LiquidCrystal_I2C  

### 3. Configuration  
- Add your WiFi credentials in code  
- Add Adafruit IO username and key  

### 4. Upload Code  
- Connect ESP32 via USB  
- Upload code using Arduino IDE  
- Open Serial Monitor for debugging  

---

## 🚀 Future Improvements  
- Mobile app integration for push notifications  
- AI-based gas level prediction  
- Multi-gas detection system (CO, CO₂, smoke)  
- Battery-powered portable device  
- Integration with industrial safety systems  

---

## 🧩 Applications  
- Industrial safety monitoring  
- Gas leakage detection in homes  
- Chemical laboratories  
- Smart city safety systems  

---

## 📌 Conclusion  
Chem-Alert demonstrates how **IoT + embedded systems + cloud integration** can be used to build **real-time safety solutions**.  
It provides a scalable and efficient approach to prevent hazardous gas accidents.
