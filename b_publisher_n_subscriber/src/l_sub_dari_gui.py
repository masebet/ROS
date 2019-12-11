#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_dari_k_pub_with_gui(msg):
    rospy.loginfo("Pesan diterima: ")
    rospy.loginfo(msg)
    x = int(msg.data)
    print(x)

if __name__ == "__main__":
    rospy.init_node('l_sub_dari_gui')
    sub = rospy.Subscriber('k_pub_with_gui_topic', String, callback_dari_k_pub_with_gui)
    rospy.spin()

'''
Tahap-tahap compile program
1. Selesaikan membuat program l_sub_dari_gui.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x l_sub_dari_gui.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber k_sub_with_gui.py
9. buka terminal baru
9. rosrun b_publisher_n_subscriber l_sub_dari_gui.py
10. enjoy the result
'''