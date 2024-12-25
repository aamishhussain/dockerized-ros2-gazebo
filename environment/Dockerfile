# Base image with ROS 2 Humble
FROM osrf/ros:humble-desktop
ARG ROS_DISTRO=humble
# Install Gazebo
RUN sudo apt-get update 
RUN sudo apt-get install -y ros-${ROS_DISTRO}-ros-gz ros-${ROS_DISTRO}-gazebo-ros-pkgs
RUN sudo apt install nano

# install turtlebot3
RUN sudo apt-get update 
RUN sudo apt install -y ros-${ROS_DISTRO}-turtlebot3*
RUN sudo apt-get clean

   
# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY nonbuild_entrypoint.sh /nonbuild_entrypoint.sh
RUN chmod +x /nonbuild_entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD tail -f /dev/null