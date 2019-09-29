char inChar;
int d, t9a;
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
int a = 1;
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
  digitalWrite(6, 1); 
  delayMicroseconds(2);
  digitalWrite(6, 1);
  delayMicroseconds(10);
  digitalWrite(6, 0); 
  d = pulseIn(5, 1);
}
  port = 9;
  t9a =500;
  q = 0;
  if (Serial.available()>0)
  {
    inChar = Serial.read();
    if(inChar=='c'){
 while (q != 1){
    if (a == 1/*он видит стаканчик*/){
    //берет стаканчик
     q = 1;
    Serial.print(1111);
    }
    if (/* не видит стаканчик*/|| q != 1){
    digitalWrite(port,1);
    delay(t9a);
    digitalWrite(port,0);
    delay(t);
    a++;
    }
    port--;
    t9a +=450;
    }
  }
if ( inChar=='b'){
 while (q != 1){
    if (/*он видит видит банан*/){
    //берет стаканчик
    q = 1;
    
    }
    if (/* не видит банан*/|| q != 1){
    digitalWrite(port,1);
    delay(t9a);
    digitalWrite(port,0);
    delay(t);
    }
    port--;
    t9a *=2;
    }


}

  
  }
  }
  Serial.print(9999);
  delay(10000);
  
/*if(work==1){
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
 }*/
}
