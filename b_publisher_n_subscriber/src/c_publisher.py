#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('py_bersabda', String, queue_size=10)     # membuat publisher baru dengan nama 'py_bersabda' dan queue_size = 10
    rospy.init_node('py_publisher', anonymous=True)     # inisilisasi node dengan nama 'py_publisher'
    
    rate = rospy.Rate(10)        # 10Hz

    i = 0
    while not rospy.is_shutdown():
        hello_str = "hey hamba %s" %i   # hello_str = "hey world kamu %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i += 1

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


'''
Tahap-tahap compile program
1. Selesaikan membuat program c_publisher.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x c_publisher.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber c_publisher.py
9. enjoy the result
'''