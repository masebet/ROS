#include <ros/ros.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "ini_node_cpp");
    ros::NodeHandle n;

    // ====== cara PERTAMA ======
    ROS_INFO("Node has been started");
    ros::Duration(1.0).sleep();
    ROS_INFO("Exit");

    // ====== cara KEDUA ======
    ros::Rate rate(10);
    while(ros::ok()) {
        ROS_INFO("heyyy....");
        rate.sleep();
    }

}

/*
Tahap-tahap compile program
1. Buat program e_node_cpp.cpp
2. Buka dan edit file CMakeList.txt (hasilnya seperti itu)
3. cd ~/catkin_ws && catkin_make
4. source devel/setup.bash      (opsional)
5. roscore
6. buka terminal baru
7. rosrun b_publisher_n_subscriber ini_node_cpp
8. enjoy the result
*/