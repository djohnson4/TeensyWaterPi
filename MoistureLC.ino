int sensor0 = A0;
int sensor1 = A1;
int out0, out1, avg;

void setup() {
  Serial.begin(9600);
  // Serial.println("Reading moisture");
  //delay(2000);

}

void loop() {
   out0 = analogRead(sensor0);
   out1 = analogRead(sensor1);
   avg = map(((out0 + out1) / 2), 550, 10, 0, 100);
   // Serial.print("Moisture: ");
   // Serial.print(avg);
   // Serial.println("%");
   delay(1000);

}
