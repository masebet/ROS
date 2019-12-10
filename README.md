# ROS-Basic
How to learn about ROS from basic

Latihan Dasar ROS dengan distro Kinetic


A. cara membuat packaga

1. masuk ke directory dulu lewat terminal
    misal
	cd $HOME/catkin_ws/src/ROS_Basic/


2. buat package, misalnya seperti ini
	catkin_create_pkg a_contoh_package std_msgs roscpp rospy


3. akan muncul directory nya menjadi	
	$HOME/catkin_ws/src/ROS_Basics/a_contoh_package

4. nah di dalem nya sudah terbuat package ROS

5. kemudian compile project tersebut dengan cara,  
    cd ~/catkin_ws
    kemudian jalankan
    catkin_make

