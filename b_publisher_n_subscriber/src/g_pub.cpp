#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "g_pub_node");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::String>("g_pub_topic", 10);     // nama topic, // 10 adalah buffer, klo di python itu queue_size=10
    
    ros::Rate rate(3);      // 3 Hz

    while (ros::ok()) {
        std_msgs::String msg;
        msg.data = "ini publisher...";
        pub.publish(msg);
        rate.sleep();
    }
}

/*
Tahap-tahap compile program
1. Buat program g_pub.cpp
2. Buka dan edit file CMakeList.txt (hasilnya seperti itu)
3. cd ~/catkin_ws && catkin_make
4. source devel/setup.bash      (opsional)
5. roscore
6. buka terminal baru
7. rosrun b_publisher_n_subscriber g_pub_node
8. enjoy the result
*/