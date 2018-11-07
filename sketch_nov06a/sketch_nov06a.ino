int pot_degeri = 0;
char userinput;
int pot = A7;
void setup() {
  pinMode(pot,INPUT);
  Serial.begin(9600);
}
void loop() {
  if(Serial.available()>0){
      userinput = Serial.read();
      if(userinput == 'y'){
        pot_degeri = analogRead(pot);
        Serial.println(pot_degeri);
        Serial.println(pot_degeri/2);
        Serial.println(pot_degeri+100);
    }
  }
}
