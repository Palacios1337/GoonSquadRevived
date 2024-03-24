#include <LiquidCrystal.h>
#include "StatusLight.h"

// Define the GPIO pins on the ESP32 connected to the LCD
const int rs = 4, en = 16, d4 = 17, d5 = 5, d6 = 18, d7 = 19;
const int status_pin_A = 32, status_pin_B = 33, status_pin_C = 25; // Status light pins

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
StatusLight myStatusLight(status_pin_A, status_pin_B, status_pin_C);

void setup() {
  // Initialize LCD
  lcd.begin(16, 2); // Adjust according to your LCD's dimensions
  lcd.print("Upload an Image:");
  Serial.begin(115200); // Initialize serial communication with baud rate 115200

  // Initialize Status Light
  myStatusLight.setupStatusLight();
}

void loop() {
  if (Serial.available()) { // Check if data is available to read
    String inputString = Serial.readStringUntil('\n'); // Read input as string until newline
    int inputNumber = inputString.toInt(); // Convert string to integer

    if (inputString.length() > 0 && inputNumber >= 0 && inputNumber <= 3) { // Check if input is valid
      lcd.clear(); // Clear the LCD screen
      lcd.setCursor(0, 1); // Set cursor to the second line
      
      // Display different messages based on input number
      switch (inputNumber) {
        case 0:
          myStatusLight.turnOff();
          lcd.print("All Clear!");
          break;
        case 1:
          myStatusLight.setSolid(status_pin_C);
          lcd.setCursor(0, 0); // Set cursor to first row, first column
          lcd.print("Palm Tree Found");
          lcd.setCursor(0, 1); // Set cursor to second row, first column
          lcd.print("Beware Coconuts");
          break;
        case 2:
          myStatusLight.setSolid(status_pin_A);
          lcd.setCursor(0, 0); // Set cursor to first row, first column
          lcd.print("Beach Found");
          lcd.setCursor(0, 1); // Set cursor to second row, first column
          lcd.print("Beware Sharks!");
          break;
        case 3:
          myStatusLight.setSolid(status_pin_B);
          lcd.setCursor(0, 0); // Set cursor to first row, first column
          lcd.print("Volcano Found");
          lcd.setCursor(0, 1); // Set cursor to second row, first column
          lcd.print("Run away!");
          break;
      }
    } else { // Invalid input
      myStatusLight.turnOff();
      lcd.clear(); // Clear the LCD screen
      lcd.print("Invalid Input");
    }
  }
}
