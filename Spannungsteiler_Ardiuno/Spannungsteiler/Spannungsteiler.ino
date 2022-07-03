//Tieftöner
const int port_0 = 4;   //200
const int port_1 = 5;   //100 Tief mit 6700 ohm
const int port_2 = 6;   //50 Tief mit 100
const int port_3 = 7;   //20 Tief mit 150 ohm
char val;


//Hochtöner
const int port_4 = 8;   //3000 tief mit 24 ohm
const int port_5 = 9;   //1500-2000 hoch mit 6700 ohm
const int port_6 = 10;  //1000 hoch mit 100 ohm
const int port_7 = 11;  //500  hoch mit 150 ohm
const int port_8 = 12;  //300-400 hoch mit 24 ohm

void setup() {
  Serial.begin(115200);
  pinMode(port_0, OUTPUT);
  pinMode(port_1, OUTPUT);
  pinMode(port_2, OUTPUT);
  pinMode(port_3, OUTPUT);
  pinMode(port_4, OUTPUT);
  pinMode(port_5, OUTPUT);
  pinMode(port_6, OUTPUT);
  pinMode(port_7, OUTPUT);
  pinMode(port_8, OUTPUT);
  pinMode(13, OUTPUT);
  
   
  
}

void loop() {


  
  if (Serial.available()>0) {
    
    //int val=(Serial.write(Serial.read()));
    
     //Serial.println(val);
     val=Serial.read();
    
     if (val == '0') {
        Serial.println("i am in 0");
        digitalWrite(port_3, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
     } else if (val == '1') {
        Serial.println("i am in 1");
        digitalWrite(port_2, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
  
     } else if (val == '2') {
        Serial.println("i am in 2");
        digitalWrite(port_1, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == '3'){
        Serial.println("i am in 3");
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == '4') {
        Serial.println("i am in 4");
        digitalWrite(port_8, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == '5') {
        Serial.println("i am in 5");
        digitalWrite(port_7, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == '6') {
        //while(val=='6'){
        Serial.println("i am in 6");
        digitalWrite(port_6, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        //}
      } else if (val == '7') {
        Serial.println("i am in 7");
        digitalWrite(port_5, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        
        delay(5000);
        
      } else if (val == '8') {
        digitalWrite(port_0, LOW);                                          /////////////////////////////////////////////////////////////////////////////
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == '9') {
        digitalWrite(port_4, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      }else if (val == 'A') {      //// tiefton
     
        digitalWrite(port_1, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
     } else if (val == 'B') {
        
        digitalWrite(port_3, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
  
     } else if (val == 'C') {
        
        digitalWrite(port_6, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == 'D'){
        
        digitalWrite(port_4, HIGH);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_0, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);

      }else if (val == 'a') { ///// hochton
     
        digitalWrite(port_5, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
     } else if (val == 'b') {
        
        digitalWrite(port_7, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
  
     } else if (val == 'c') {
        
        digitalWrite(port_6, HIGH);
        digitalWrite(port_0, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_8, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
        
      } else if (val == 'd'){
        
        digitalWrite(port_8, HIGH);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_0, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(13,HIGH);
        delay(5000);
      }else if (val == 'e'){

         digitalWrite(port_8,LOW);
        digitalWrite(port_1, LOW);
        digitalWrite(port_2, LOW);
        digitalWrite(port_3, LOW);
        digitalWrite(port_0, LOW);
        digitalWrite(port_5, LOW);
        digitalWrite(port_6, LOW);
        digitalWrite(port_7, LOW);
        digitalWrite(port_4, LOW);
        digitalWrite(13,HIGH);
        delay(5000);

        
      }
      
        ////////////////////////////////////
     
  }else {
  digitalWrite(13,LOW);
  pinMode(port_0, LOW);
  pinMode(port_1, LOW);
  pinMode(port_2, LOW);
  pinMode(port_3, LOW);
  pinMode(port_4, LOW);
  pinMode(port_5, LOW);
  pinMode(port_6, LOW);
  pinMode(port_7, LOW);
  pinMode(port_8, LOW);
  delay(3000);
      }
 
  
  } 

