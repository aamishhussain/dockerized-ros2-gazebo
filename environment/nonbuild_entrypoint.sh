#!/bin/bash
set -e

# Source the ROS 2 setup script
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.bash
#workspace building and sourcing
cd /ws_ros2_gazebo
source install/setup.bash

exec "$@"