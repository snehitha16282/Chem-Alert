#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"

LiquidCrystal_I2C lcd(0x27, 16, 2);

// -------------------- WIFI --------------------
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// -------------------- ADAFRUIT -----------------
#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883
#define AIO_USERNAME    ""
#define AIO_KEY         ""

WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
Adafruit_MQTT_Publish alertFeed = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/gas-alert");

// ---------------- SENSOR + ALERT PINS ------------
#define GAS_SENSOR_PIN 34
#define BUZZER_PIN 25
#define LED_PIN 27

// -------------- TREND VARIABLES -------------------
int previous_value = 0;
int buffer[10];
int idx = 0;
bool full = false;

void connectMQTT() {
  if (!mqtt.connected()) {
    mqtt.connect();
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.print("Connecting WiFi");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(300);
  }

  lcd.clear();
  lcd.print("MQTT Connecting");
  connectMQTT();

  lcd.clear();
  lcd.print("ChemAlert 2.0");
  delay(1500);
  lcd.clear();
}

void loop() {

  connectMQTT();  // Ensure stable MQTT connection

  int current = analogRead(GAS_SENSOR_PIN);
  int slope = current - previous_value;

  buffer[idx] = current;
  idx++;
  if (idx >= 10) { idx = 0; full = true; }

  float avg = 0;
  int n = full ? 10 : idx;
  for (int i = 0; i < n; i++) avg += buffer[i];
  avg = avg / n;

  lcd.setCursor(0,0);
  lcd.print("Val:");
  lcd.print(current);
  lcd.print("   ");

  lcd.setCursor(0,1);

  // ------------------ ALERT LOGIC -------------------
  if (slope > 50 && slope < 200) {
    lcd.print("Early Warning   ");
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 700);
    alertFeed.publish("EARLY WARNING: Gas Increase Detected");
  }
  else if (slope >= 200 && slope < 400) {
    lcd.print("High Alert      ");
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 900);
    alertFeed.publish("HIGH ALERT: Rapid Gas Rise!");
  }
  else if (slope >= 400 || avg > 3200) {
    lcd.print("CRITICAL LEAK!  ");
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 1200);
    alertFeed.publish("CRITICAL LEAK: Check Area Immediately!");
  }
  else {
    lcd.print("Normal          ");
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);
    alertFeed.publish("SAFE: No Hazard");
  }

  previous_value = current;
  delay(700);
}
