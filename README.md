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
  <summary>Hint</summary>
  
  ```python
  ```
</details>


<details>
  <summary>For the curious</summary>
  
  ```
  
  ```
</details>


## Assignment 1: Navigating your workspace
TODO: 

## Assignment 2: "Hello world!"
TODO:
## Assignment 3: Ndes and topics
TODO:
## Assignment 4: Services and Turtlesim

## Assignment 5 Talking to another computer
TODO

## Extra
