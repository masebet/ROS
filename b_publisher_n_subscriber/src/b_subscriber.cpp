#include "ros/ros.h"
#include "std_msgs/String.h"

// Topic message callback
void nge_gosipCallback(const std_msgs::String::ConstPtr& msg) {
    ROS_INFO("dia ngomong: %s\n", msg->data.c_str());
}

int main(int argc, char **argv) { 
    ros::init(argc, argv, "si_subscriber");     // inisialisasi Node ROS baru dengan nama "si_subscriber"
    ros::NodeHandle node;       // create a node handle: it reference assign to a new node
    ros::Subscriber sub = node.subscribe("nge_gosip", 1000, nge_gosipCallback);

    ros::spin();

    return 0;
}


/*
Tahap-tahap compile program
1. Selesaikan membuat program b_subscriber.cpp
2. Buka dan edit file CMakeList.txt (hasilnya seperti itu)
3. cd ~/catkin_ws && catkin_make
4. source devel/setup.bash      (opsional)
5. roscore
6. buka terminal baru
7. rosrun b_publisher_n_subscriber si_subscriber
8. enjoy the result
*/