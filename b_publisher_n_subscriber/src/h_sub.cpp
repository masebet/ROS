#include <ros/ros.h>
#include <std_msgs/String.h>

void callback_terima_dari_g_pub(const std_msgs::String& msg) {
    ROS_INFO("Pesan dari g_pub: %s", msg.data.c_str());
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "g_sub_node");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("g_pub_topic", 1000, callback_terima_dari_g_pub);

    ros::spin();
}

/*
Tahap-tahap compile program
1. Buat program h_sub.cpp
2. Buka dan edit file CMakeList.txt (hasilnya seperti itu)
3. cd ~/catkin_ws && catkin_make
4. source devel/setup.bash      (opsional)
5. roscore
6. buka terminal baru
7. rosrun b_publisher_n_subscriber g_pub_node
8. buka terminal baru
9. rosrun b_publisher_n_subscriber g_sub_node
10. enjoy the result
*/