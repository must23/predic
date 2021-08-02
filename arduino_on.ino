#include <ros.h>
#include <Arduino.h>
#include <std_msgs/String.h>
#define LED 13

ros::NodeHandle  nh;
std_msgs::String str_msg;
ros::Publisher pub_tester("topic1", &str_msg);
ros::Subscriber<std_msgs::String> subs_tester("flag_arduino", &callback);

char atest[10] = "it works!";


void callback(const std_msgs::String &flag_on)
{
     if(flag_on == turn_on){
      digitalWrite(LED, HIGH); 
     }
}
     

void setup() { 
  pinMode(LED, OUTPUT);
  nh.initNode();  
  nh.advertise(pub_tester);
  nh.subscribe(subs_tester);
}

void loop() {  
  
  str_msg.data = atest;
  if(flag_on=="turn_on"){
  pub_tester.publish(&str_msg );
  nh.spinOnce();

  delay(10);
}
