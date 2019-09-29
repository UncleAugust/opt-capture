void setup() {
Serial.begin(9600); 
Serial.println("Ready");
}

void loop() {
  char input_data = ' ';

  if(Serial.available()){ 
      char input_data = {Serial.read()}; 
      Serial.println(input_data); 
  }
delay(100); 
}
