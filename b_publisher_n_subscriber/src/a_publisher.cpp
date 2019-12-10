#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "si_publisher");      // ROS Node dengan nama "si_publisher"
    ros::NodeHandle n;      // membuat nodehandle, referensi ke node baru
    ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("nge_gosip", 1000);
    ros::Rate loop_rate(10.0);       // satuan Hz, jadi kalau misalnya di isi 1.0 maka 1Hz

    int count = 0;
    while (ros::ok())
    {
        std_msgs::String msg;       // membuat pesan baru dengan tipe data String
        std::stringstream ss;       // membuat string
        ss << "wooooyyy ..... " << count;
        msg.data = ss.str();         // menetapkan data string ke dalam message ROS data field
        ROS_INFO("si dia %s\n", msg.data.c_str());

        chatter_publisher.publish(msg);     // publish pesan
        ros::spinOnce();        // need to call this function often to allow ROS process incoming message
        loop_rate.sleep();      // Sleep for the rest of cycle, to enforce the loop rate
        count++;
    }

    return 0;
    
}

/*
Tahap-tahap compile program
1. Selesaikan membuat program a_publisher.cpp
2. Buka dan edit file CMakeList.txt (hasilnya seperti itu)
3. cd ~/catkin_ws && catkin_make
4. source devel/setup.bash      (opsional)
5. roscore
6. buka terminal baru
7. rosrun b_publisher_n_subscriber si_publisher
8. enjoy the result
*/