#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton

def button_1_Click():
    # form.close()
    msg = String()
    msg.data = "1"
    pub.publish(msg)

def button_2_Click():
    msg = String()
    msg.data = "2"
    pub.publish(msg)

def button_3_Click():
    msg = String()
    msg.data = "3"
    pub.publish(msg)

def button_4_Click():
    msg = String()
    msg.data = "4"
    pub.publish(msg)

if __name__ == "__main__":
    rospy.init_node('k_pub_with_gui_node')
    pub = rospy.Publisher("k_pub_with_gui_topic", String, queue_size=10)

    a = QApplication(sys.argv)

    form = QWidget()
    form.resize(500, 300)
    form.move(200, 200)
    form.setWindowTitle('Publisher menggunakan User Interface')

    label = QLabel('Silahkan Pilih Angka')
    label.move(180, 30)
    label.setParent(form)

    button_1 = QPushButton('Ini No 1')
    button_1.move(280,80)
    button_1.setParent(form)

    button_2 = QPushButton('Ini No 2')
    button_2.move(120,80)
    button_2.setParent(form)

    button_3 = QPushButton('Ini No 3')
    button_3.move(120,170)
    button_3.setParent(form)

    button_4 = QPushButton('Ini No 4')
    button_4.move(280,170)
    button_4.setParent(form)

    button_1.clicked.connect(button_1_Click)
    button_2.clicked.connect(button_2_Click)
    button_3.clicked.connect(button_3_Click)
    button_4.clicked.connect(button_4_Click)

    form.show()

    a.exec_()

'''
Tahap-tahap compile program
1. Buat program k_pub_with_gui.py
2. cd ~/catkin_ws/src/ROS-Basic/b_publisher_n_subscriber/src
3. chmod +x k_pub_with_gui.py
4. cd ~/catkin_ws && catkin_make
5. source devel/setup.bash      (opsional)
6. roscore
7. buka terminal baru
8. rosrun b_publisher_n_subscriber k_pub_with_gui.py
9. enjoy the result
'''