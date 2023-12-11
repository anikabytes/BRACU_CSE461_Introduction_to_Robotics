#!/usr/bin/python3
import rospy # Communication
from geometry_msgs.msg import Twist # Message: position, angle etc

def move():
  # Starts a new node
  rospy.init_node('robot_cleaner', anonymous=True)
  velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  vel_msg = Twist()

  #Receiveing the user's input
  print("Let's move your robot")
  speed = input("Input your speed:") # Say 1
  distance = input("Type your distance:") # Say 1
  isForward = input("Foward?: ")#True or False (0/1)
  speed = float(speed)
  distance = float(distance)

  isForward = int(isForward)

  #Checking if the movement is forward or backwards
  if(isForward):
      vel_msg.linear.x = abs(speed)
  else:
      vel_msg.linear.x = -abs(speed)
  #Since we are moving just in x-axis
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = 0

  while not rospy.is_shutdown():

      #Setting the current time for distance calculus
      t0 = rospy.Time.now().to_sec()
      current_distance = 0

      #Loop to move the turtle in an specified distance
      while(current_distance < distance):
          #Publish the velocity
          velocity_publisher.publish(vel_msg)
          #Takes actual time to velocity calculus
          t1=rospy.Time.now().to_sec()
          #Calculates distancePoseStamped
          current_distance= speed*(t1-t0)
      #After the loop, stops the robot
      vel_msg.linear.x = 0
      #Force the robot to stop
      velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
  try:
      #Testing our function
      move()
  except rospy.ROSInterruptException: pass
