# ros2-workshop
ROS 2 workshop for Ascend Team 2022

## What is ROS?

![ROS foxy](https://docs.ros.org/en/foxy/_static/foxy-small.png)


## Installation

This workshop is built on Ubuntu 20.04. Make sure that you are running the same distribution before continuing. 
Check your current version by typing the following into your terminal.
```
lsb_release -a
```
This should reveal your Ubuntu distro. 

### Step 1: Cloning the repository
> Prerequesites: You should already have set up github with ssh-keys.
Clone the reposetory in your home directory.

```
git clone git@github.com:AscendNTNU/ros2-workshop.git 
```
If you have set up your ssh-keys correctly, this should download the ros2-workshop directory.

### Step 2: Setting up our workspace

#### Installing docker
> Note: If you already have docker installed, you can skip this sub-step.
 
To install all the necessary packages for the workshop, you first need to give your user permission
to excecute the installation scripts.

```
cd  ~/ros2-workshop
```
```
pwd
```
This will basicly print out where you are on your computer, you should now be in the ros2-workshop directory. The next lines will give our installation scripts access to install and excecute packages.
```
sudo chmod +x scripts/dockerInstall.sh
```
```
sudo chmod +x scripts/vscodeInstall.sh
```
We now excecute the installation scripts.
```
./scripts/dockerInstall.sh
```
We now test if everything was installed successfully, but first we need to source our new enviroment variables. 
```
source ../.bashrc
```
```
docker run -rm docker/whalesay cowsay Docker install completed
```
You should now see a very cute whale printed in your terminal.

#### Installing VSCode
> Note: If you have VSCode installed on your machine, you can skip the next step.

```
./scripts/vscodeInstall.sh
```

### Step 3: Launching the workspace
Open ros2-workshop in VSCode and make sure to install the extensions in the pop-up that should appear in you bottom-right corner. 
After installing the extensions for VSCode, you should reload your window. Ctrl + Shift + P should open your VSCode command palette.
Excecute "Reload Window". You should now see a prompt in your bottom left that should say "Reopen in Containter". The same can be achieved by 
excecuting "Remote-Containers: Reopen in Container" in the VSCode command palette. Your window should now reload, and launch your ros-workspace in
an isolated container. We can now begin programming with ROS2.



<details>
  <summary>For the curious: Containers</summary>
  Our current workspace is now running in a container, but what is a container? A container is a filesystem isolated from your root filesystem. We achieve this by restricting all the processes inside to this filesystem. From programs inside a container can only access the resources and files allocated to it. It is in some sense a virtual machine, but is sharing the resources with the host machine. If you want to learn more, we reccomend this video https://www.youtube.com/watch?v=8fi7uSYlOdc. 
 
</details>


## Assignment 1: "Hello World!"
> Note: Make sure you are in the container you ran in the previous section. 

 ROS 2 relies on the notion of combining workspaces using the shell environment. Every ROS project has a workspace. “Workspace” is a ROS term for the location on your system where you’re developing with ROS 2. You can have several workspaces on your machine, but we'll only use one. This feature enables easy switching between different versions of ROS. This is accomplished by sourcing setup files, which include ROS environment variables. **Without sourcing ROS setup files you wont be able to access any ROS2 commands.** 

 ```
 source /opt/ros/foxy/setup.bash
 ```
 Not sourcing setup files is one of the most common mistakes when working with ROS in a shell. The ros2-workshop repo is a ROS2 workspace, and is the root for all the packages we will build in this workshop. The `src` directory contains all our source files including package information about what we want to build. When we build our workspace, the ROS build tool `colcon` will generate the necessary files and directories to run our packages. We will now build our workspace to see what `colcon` generates. In VSCode you can do this with Ctrl + Shift + B, or in the terminal with


```
colcon build --merge-install
```
> Note: The --merge-install is just a convenience argument, and is not that important for us to understand

<details>
  <summary>For the curious: Colcon</summary>
  https://colcon.readthedocs.io/en/released/reference/verb/build.html
</details>


You can now see several new directories in the root directory of our workspace. The `install` directory contains the `setup.bash` files that include the workspace environment variables we need to run our packages. Source this file with the same syntax as we used when sourcing ROS setup files. We should now be able to run our example code.
```
ros2 run assignment1 hello_world
```
You should now have a node printing out "Hello World" in your terminal. 
> Note: Ctrl + C to terminate the program




## Assignment 2: Nodes and Topics



The `hello_world` program in assignment 1 is a ROS `node`. Every ROS program is a node, communicating in a graph of other nodes. A node can both receive and send messages. When `hello_world` prints out a message, every other node can chose to listen to `hello_world`s message. A message is sent to communication channels which in ROS are called `topic`s. Other nodes can listen and/or post messages to a `topic`. One analogy is a Slack channel. One node/user can post, listen or ignore a `topic`/channel. When a node/user posts a message to a `topic`/channel the ones subscribing to that `topic` are notified, and can read that message. A node can have a ROS `subscriber` that listens to a `topic`. The opposite is a ROS `publisher` that posts to a `topic`. 

![Graph Viz](https://docs.ros.org/en/foxy/_images/Topic-MultiplePublisherandMultipleSubscriber.gif)

Now we'll run our `hello_world` program. Open a new bash shell in VSCode ("+" icon in the top left in your current shell). 

> Note: Make sure that ROS is sourced

### Useful commands

```
ros2 node list

ros2 node info /some-node

ros2 topic list

ros2 topic echo some-topic

ros2 topic pub some-topic some-msg-type some-msg
```

### Tasks
> Note: Press `tab` for autocomplete
* List all running nodes
* Echo two topics
* Post a message to the topic `hello_world` posts to




## Assignment 3: Nodes and topics




  <summary>Hint</summary>
  
  ```python
  ```
</details>

## Assignment 4: Services and Turtlesim


![Graph Viz](https://docs.ros.org/en/foxy/_images/Nodes-TopicandService.gif)
  <summary>Hint</summary>
  
  ```python
  ```
</details>

## Assignment 5 Talking to another computer
TODO
  <summary>Hint</summary>
  
  ```python
  ```
</details>

## Extra

## Sources
https://industrial-training-dev.readthedocs.io/en/latest/
https://docs.ros.org/en/foxy/index.html
