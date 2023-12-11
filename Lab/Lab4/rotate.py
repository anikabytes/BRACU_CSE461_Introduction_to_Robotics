#!/usr/bin/python3
import rospy # Communication
from geometry_msgs.msg import Twist # Message: position, angle etc

def rotate():
  # Starts a new node
  rospy.init_node('robot_cleaner', anonymous=True)
  velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  vel_msg = Twist()

  #Receiveing the user's input
  print("Let's move your robot")
  speed = input("Input your speed:") # Say 1
  radius = input("Input your radius:") # Say 1

  speed = float(speed)
  radius = float(0.2)

  angular_speed = speed/radius 

  #Since we are moving just in x-axis
  vel_msg.linear.x = speed
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  #vel_msg.angular.z = angular_speed
  count = 0

  goal = input("Input your goal:")

  goal = float(goal)

  while not rospy.is_shutdown():

      #Setting the current time for distance calculus
      t0 = rospy.Time.now().to_sec()
      current_distance = 0

      #Loop to move the turtle in an specified distance
      while(current_distance < goal):
          #Publish the velocity
          vel_msg.angular.z = angular_speed
          velocity_publisher.publish(vel_msg)
          angular_speed = speed/radius 
          #Takes actual time to velocity calculus
          t1=rospy.Time.now().to_sec()
          #Calculates distancePoseStamped
          current_distance= speed*(t1-t0)
        
          if count == 0 :
             radius += 0.0002
          count = (count+1)%7


if __name__ == '__main__':
  try:
      #Testing our function
      rotate()
  except rospy.ROSInterruptException: pass
