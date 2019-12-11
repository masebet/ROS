#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(pesan):
    rospy.loginfo(rospy.get_caller_id() + "apa ya...%s", pesan.data)

def listener():
    # in ROS,nodes are uniquely name. If two nodes with the same node are launched
    # the previous one is kicked off.

    # the anonymous=True flag means that rospy will choose a unique name for out 'listener' node
    # so that multiple listener cans can run simultaneously
    rospy.init_node('py_subscriber', anonymous=True)
    rospy.Subscriber("py_bersabda", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    listener()



'''
Tahap-tahap compile program
1. Selesaikan membuat program d_subscriber.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x d_subscriber.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber c_publisher.py
9. buka terminal baru
9. rosrun b_publisher_n_subscriber d_subscriber.py
10. enjoy the result
'''