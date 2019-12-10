## ================================ TAMBAH ini untuk a_publisher.cpp ================================
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
add_executable(si_publisher src/a_publisher.cpp)
target_link_libraries(si_publisher ${catkin_LIBRARIES})
## ================================ TAMBAH ini untuk a_publisher.cpp ================================