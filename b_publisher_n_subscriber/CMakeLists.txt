### ================================ TAMBAH ini untuk a_publisher.cpp dan b_subscriber.cpp ================================
#cmake_minimum_required(VERSION 2.8.3)
#project(b_publisher_n_subscriber)
#
#find_package(catkin REQUIRED COMPONENTS
#  roscpp
#  rospy
#  std_msgs
#)
#
#catkin_package(
#)
#
#include_directories(
#  ${catkin_INCLUDE_DIRS}
#)
#
## Declare a cpp executable
#add_executable(si_publisher src/a_publisher.cpp)
#target_link_libraries(si_publisher ${catkin_LIBRARIES})
#
#add_executable(si_subscriber src/b_subscriber.cpp)
#target_link_libraries(si_subscriber ${catkin_LIBRARIES})
### ================================ TAMBAH ini untuk a_publisher.cpp dan b_subscriber.cpp ================================

### ================================ TAMBAH ini untuk e_node_cpp.cpp ================================
#cmake_minimum_required(VERSION 2.8.3)
#project(b_publisher_n_subscriber)
#
#find_package(catkin REQUIRED COMPONENTS
#  roscpp
#  rospy
#  std_msgs
#)
#
#catkin_package()
#
#include_directories(
#  ${catkin_INCLUDE_DIRS}
#)
#add_executable(ini_node_cpp src/e_node_cpp.cpp)
#target_link_libraries(ini_node_cpp ${catkin_LIBRARIES})
### ================================ TAMBAH ini untuk e_node_cpp.cpp ================================

## ================================ TAMBAH ini untuk g_pub.cpp dan h_sub.cpp ================================
cmake_minimum_required(VERSION 2.8.3)
project(b_publisher_n_subscriber)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Declare a cpp executable
add_executable(g_pub_node src/g_pub.cpp)
target_link_libraries(g_pub_node ${catkin_LIBRARIES})

add_executable(g_sub_node src/h_sub.cpp)
target_link_libraries(g_sub_node ${catkin_LIBRARIES})
## ================================ TAMBAH ini untuk g_pub.cpp dan h_sub.cpp ================================