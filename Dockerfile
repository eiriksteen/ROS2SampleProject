FROM ros:foxy

RUN apt update  && apt install -y ros-foxy-turtlesim vim
COPY ros2_ws /
COPY scripts/ros_entrypoint.sh /ros2_ws/ros_entrypoint.sh
ENTRYPOINT [ "/ros2_ws/ros_entrypoint.sh"]

