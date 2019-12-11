#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('i_pub_node')
    pub = rospy.Publisher("i_pub_topic", String, queue_size=10)
    rate  = rospy.Rate(2)
    
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "hey, ini publisher python"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node berhenti")


'''
Tahap-tahap compile program
1. Buat program i_pub.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x i_pub.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber i_pub.py
9. enjoy the result
'''