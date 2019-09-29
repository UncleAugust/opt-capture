char inChar;
int t9a = 650;
int port = 9;
int q = 0;
int work = 0;
int t13 = 400;
int t12 = 600;
int t11 = 700;
int t10 = 500;
int t9 = 700;
int t8 = 680; //t9*0.97
int t7 = 750;
int t = 1000;
int a = -1;                    //
void setup() {
pinMode(13,OUTPUT); //13-открыть, 12-закрыть  
pinMode(12,OUTPUT);  
pinMode(11,OUTPUT); //11-поднять, 10-опустить
pinMode(10,OUTPUT);
pinMode(9,OUTPUT); //9-влевo, 8-вправо
pinMode(8,OUTPUT);  
pinMode(5, INPUT); // ec
pinMode(6, OUTPUT);// tr
Serial.begin(9600);
}

void loop() {
while (q != 1){
  if (Serial.available()>0)
  {
    inChar = Serial.read();
    if(inChar=='c' && q != 1){
digitalWrite(13,1);
delay(t13);
digitalWrite(13,0);
delay(t);
digitalWrite(10,1);
delay(t10);
digitalWrite(10,0);
delay(t);
digitalWrite(12,1);
delay(t12);
digitalWrite(12,0);
delay(t);
digitalWrite(11,1);
delay(t11);
digitalWrite(11,0);
delay(t);
digitalWrite(11,1);
delay(350);
digitalWrite(11,0);
delay(t);
digitalWrite(9,1);
delay(t9);
digitalWrite(9,0);
delay(t);
digitalWrite(10,1);
delay(t10);
digitalWrite(10,0);
delay(t);
digitalWrite(13,1);
delay(t13);
digitalWrite(13,0);
delay(t);
digitalWrite(11,1);
delay(t11);
digitalWrite(11,0);
delay(t);
digitalWrite(12,1);
delay(t12);
digitalWrite(12,0);
delay(t);
digitalWrite(8,1);
delay(t8);
digitalWrite(8,0);
delay(t);
q = 1;
    }
    }
    if (Serial.available()>0){
    inChar = Serial.read();
    if(inChar=='h' && q !=1 ){
      delay(4000);
    digitalWrite(port,1);
    delay(t9a);
    digitalWrite(port,0);
    delay(t);
   for (int i = 0; i<31;i++){
 Serial.println("d");
 delay(10);
    }
    }
    port--;
    t9a +=470;
  }
  }
}
 
