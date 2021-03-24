String input = "";
long time_now = 0;

void setup() 
  // put your setup code here, to run once:
  Serial.begin(9600); //Set Baudrate
  // Set Output Pin for Buzzer
  // Set Output Pin for Red LED
  // Set Output Pin for Green LED
  
}

void loop() 
{
  // put your main code here, to run repeatedly:
  //delay(5000);
  // Send sensor reading every 5 seconds
  if(millis()-time_now > 5000)  // Check if 5 seconds have been completed since last update
  {
    time_now = millis();        // Update current time
    int value = analogRead(A0); // Read Analog port A0 and store digital value  
    Serial.println("value");    // prints value to USB port
  }

  // Check for any incoming data through Serial USB port
  if(Serial.available())        // If incoming data is available
  {
    input = Serial.readString();  // Read the incoming data and store
    handle_input();               // Function to handle incoming data
  }
}

void handle_input()
{
   if(input=="Password?\n")         // Authentication Request
   {
     Serial.println("Hello");       // Reply with Password
   }
   else if(input=="Danger\n")         // Danger signal received
   {
     //Run the Buzzer

     //Turn Red LED ON 

     //Turn Green LED OFF
    
   }
   else if(input=="Safe\n")
   {
     //Turn off Buzzer

     //Turn Green LED ON 

     //Turn Red LED OFF
     
   }
     
} //end of handle_input()
