#!/usr/bin/env python

import rospy

if __name__ == "__main__":
    rospy.init_node('ini_node')
    rospy.loginfo("this node has been started")

    rate = rospy.Rate(10)       # 10 Hertz -> send message 10 times per seconds

    while not rospy.is_shutdown():
        rospy.loginfo("cus....")
        rate.sleep()


'''
Tahap-tahap compile program
1. Buat program f_node_python.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x f_node_python.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber f_node_python.py
9. enjoy the result
'''