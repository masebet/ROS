#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0

def poseCallback(posisi_message):
    global x, y, z, yaw
    x = posisi_message.x
    y = posisi_message.y
    yaw = posisi_message.theta

def move(speed, distance, is_forward):
    # deklarasi pesan Twist untuk mengirim perintah kecepatan
    velocity_message = Twist()

    # get current lokasi
    global x, y
    x0 = x
    y0 = y
    
    if is_forward:
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(10)      # 10Hz (10 kali perdetik)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    while True:
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)

        loop_rate.sleep()

        distance_moved = abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
        print distance_moved
        if not distance_moved < distance:
            rospy.loginfo("telah sampai")
            break
    
    # berhentikan robot kalau sudah sampai
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


if __name__ == "__main__":
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        position_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(1)

        while True:
            # ini buat test si turtle maju
            move(2.0, 2.0, True)
            # ini buat test si turtle mundur
            move(2.0, 2.0, False)
            # ini buat test si turtle maju
            move(5.0, 1.0, True)
            # ini buat test si turtle mundur
            move(1.0, 3.0, False)
            # ini buat test si turtle maju
            move(5.0, 2.0, True)
        
        # rotate(90, 90, True)
    
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")