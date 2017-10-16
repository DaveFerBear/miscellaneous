void setup() {
  Serial.begin(9600);
}

int amp1;

void loop() {
  amp1 = analogRead(A0);
  Serial.println(amp1);
}
