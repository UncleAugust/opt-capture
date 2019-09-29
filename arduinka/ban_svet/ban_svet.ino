char inChar;


void setup() {
  pinMode(8, OUTPUT); // Инициализация светодиода
  Serial.begin(9600); // Инициализация Serial - порта
}

void loop() {
  if (Serial.available() > 0)
  {
    inChar = Serial.read();
    if (inChar=='h') // e - Enable - включить
    {
      digitalWrite(8,HIGH);
    }
  }
  
    else if (inChar=='d') // d - Disable - выключить
    {
      digitalWrite(8,LOW);
    }
  
    else if (inChar=='b')  // b - Blink - выключить режим мигания
    {
      while (true){
      digitalWrite(8,HIGH);
      delay(1000);
      digitalWrite(8,LOW);
      delay(1000);
    }
    }
}
