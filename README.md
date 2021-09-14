# ros2-workshop
ROS 2 workshop for Ascend Team 2022

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
We first navigate to our home directory
```
cd
```
```
cd ros2-workshop
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
We now test if everything was installed successfully. 
```
source ../.bashrc
```
```
docker run docker/whalesay cowsay Docker install completed
```
You should now see a very cute whale printed in your terminal.

#### Installing VSCode
> Note: If you have VSCode installed on your machine, you can skip the next step.

```
./scripts/vscodeInstall.sh
```


### Step 3: Launching the workspace

<details>
  <summary>Hint</summary>
  
  ```python
  ```
</details>


<details>
  <summary>For the curious</summary>
  
  ```
  
  ```
</details>

## Introduction

## Building a Container

## Turtlesim
### Connecting to another computer
### Controlling Turtle with an external host

# Sources
https://husarnet.com/blog/ros2-docker/


