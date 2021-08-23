FROM ros:foxy

RUN apt update  && apt install -y ros-foxy-turtlesim vim git
COPY scripts/ros_entrypoint.sh ros_entrypoint.sh
WORKDIR /images
COPY images ./
WORKDIR /
ENTRYPOINT [ "/ros_entrypoint.sh"]

