String input = "";
long time_now = 0;

void setup() 
{
  // put your setup code here, to run once:
  Serial.begin(9600); //Set Baudrate
}

void loop() 
{
  // put your main code here, to run repeatedly:
  //delay(5000);
  // Send sensor reading every 5 seconds
  if(millis()-time_now > 5000)  // Check if 5 seconds have been completed since last update
  {
    time_now = millis();        // Update current time
    String message = "Hello from Arduino!"; //Create Message String
    Serial.println(message);    // prints message to USB port Raspberry Pi
  }

  // Check for any incoming data through Serial USB port Raspberry Pi
  if(Serial.available())        // If incoming data is available
  {
    input = Serial.readString();  // Read the incoming data and store
    Serial.println("Received: "+input);             // Reply to Raspberry Pi
  }
}
