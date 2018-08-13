void setup() {
  Serial.begin(9600);
  pinMode(12, OUTPUT);
}

int amp1;
int duty_cycle = 0.5;
int i = 0;

void printAnalog() {
  amp1 = analogRead(A0);
  Serial.println(amp1);
}

void loop() {
  //amp1 = analogRead(A0);
  if (i==1000) {
    printAnalog();
    duty_cycle = amp1/1023.0;
  }
  i++;
  analogWrite(12, HIGH);
  delayMicroseconds(10.0*duty_cycle);
  analogWrite(12, LOW);
  delayMicroseconds(10.0*(1-duty_cycle));
  printAnalog();
}


