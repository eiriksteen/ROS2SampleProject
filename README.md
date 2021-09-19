# ros2-workshop
ROS 2 workshop for Ascend Team 2022

## What is ROS?


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


## Assignment 1: Navigating the workspace
> Note: Make sure you are in the container you ran in the previous section. 

Every ROS project has a workspace. A ROS workspace is a directory that contains everything related to your project, packages etc.. The ros2-workshop repo is a ROS2 workspace, and is the root for all the packages we will build in this workshop. The `src` folder contains all our source files including package information about what we want to build. When we build our workspace, the ROS build tool `colcon` will generate the necessary files and directories to run our packages. We will now build our workspace to see what `colcon` generates. In VSCode you can do this with Ctrl + Shift + B, or in the terminal with


```
colcon build --merge-install
```
> Note: The --merge-install is just an convenience argument, and is not that important for us to understand

<details>
  <summary>For the curious: Colcon</summary>
  https://colcon.readthedocs.io/en/released/reference/verb/build.html
</details>





<details>


## Assignment 2: "Hello world!"
TODO:
 
   <summary>Hint</summary>
  
  ```python
  ```
</details>
## Assignment 3: Nodes and topics
TODO:
  <summary>Hint</summary>
  
  ```python
  ```
</details>
## Assignment 4: Services and Turtlesim
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
