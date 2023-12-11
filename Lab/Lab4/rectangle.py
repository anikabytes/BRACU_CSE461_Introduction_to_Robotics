#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist

def rectangle():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("jinhiwerjenr")
    
    speed = float(speed)
    height = float(height)
    width = int(width)
    

   # move forward 
    vel_msg.linear.x = -abs(speed)
    velocity_publisher.publish(vel_msg)
    rospy.sleep(width / speed)
    
    # stop after completing forward movement 
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
        
    # continue to move downward 
    vel_msg.linear.y = -abs(speed)
    velocity_publisher.publish(vel_msg)
    rospy.sleep(height / speed)
    
    # stop after completing downward movement 
    vel_msg.linear.y = 0
    velocity_publisher.publish(vel_msg)    
    
    # continue to move forward 
    vel_msg.linear.x = abs(speed)
    velocity_publisher.publish(vel_msg)
    rospy.sleep(width / speed)
    
    # stop after completing forward movement 
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    
    # continue to move upward 
    vel_msg.linear.y = abs(speed)
    velocity_publisher.publish(vel_msg)
    rospy.sleep(height / speed)
    
    # stop after completing upward movement 
    vel_msg.linear.y = 0
    velocity_publisher.publish(vel_msg)    
    
if __name__ == '__main__':
  try:
      #Testing our function
      rectangle()
  except rospy.ROSInterruptException: pass