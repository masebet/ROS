#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_terima_dari_i_pub(msg):
    # rospy.loginfo("Pesan diterima: ")
    # rospy.loginfo(msg)
    print(msg.data)
    # int_x = int(msg.data)
    # print(int_x)

if __name__ == "__main__":
    rospy.init_node('j_sub_node')
    sub = rospy.Subscriber("i_pub_topic", String, callback_terima_dari_i_pub)
    rospy.spin()

'''
Tahap-tahap compile program
1. Selesaikan membuat program j_sub.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x j_sub.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber i_pub.py
9. buka terminal baru
9. rosrun b_publisher_n_subscriber j_sub.py
10. enjoy the result
'''