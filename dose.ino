String incomingByte ;    

void setup() {

  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);

}
void loop() {

  if (Serial.available() > 0) {

  incomingByte = Serial.readStringUntil('\n');

    if(incomingByte == "1" ) {

      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      


      Serial.write("Led on");

    }
    if (incomingByte == "2" ) {

      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      Serial.write("Led on");

    }

    else if (incomingByte == "3" ) {

       digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
       digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);

      Serial.write("Led on");}

    else if (incomingByte == "4" ) {

      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
       digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      Serial.write("Led on");}

    else if (incomingByte == "off") {

      digitalWrite(LED_BUILTIN, LOW);

      Serial.write("Led off");

    }

    else{

     Serial.write("invald input");}

    
  }
  }