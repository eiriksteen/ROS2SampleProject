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

## Assignment 3: Writing a Node
### How to write a node in ROS2
 Now that you have had a quick introduction to what nodes are, we will learn how to write our own nodes in ROS2. There is a convention about how to write your nodes. You have to create a class which inherits from the Node object (for example: rclcpp::Node in Cpp, rclpy.node.Node in Python). In this class you’ll have all your ROS2 functionalities. You can then implement your case specific functionality in this class.  
   ```python
 class SimpleNode(Node):
    def __init__(self):
        super().__init__('my_node_name')
        # Create publishers and subscribers

    def some_callback():
      #Do something
  ```
  The constructor of the `Node` class only takes in one parameter &mdash; the name the node is to be registered with. 

  To instantiate a node, you first have to initialize ROS communications. `rclpy.init(args)` will do that for you, with some arguments that you can pass when you launch the node.

  ```python
  def main(args=None):
    rclpy.init(args=args)

    node = SimpleNode()

    rclpy.spin(node)

    rclpy.shutdown()
  ```

 `rclpy.spin(node)` will pause the program execution here, waiting for you to request to kill the node (for example CTRL+C in the terminal). During this time, any thread/timer you’ve created in the node will continue to be executed. Also, spin will be able to call any callback function that you’ve defined for the node, allowing your node to communicate with other nodes.

 When you request to kill the node, the spin function will exit, and any callback won’t be callable anymore. `rclpy.shutdown()` will basically shutdown what you started when you executed `rclpy.init()`.


 ### Writing a simple publisher 

  A timer object can be created if we want to have an action repeated periodically. We then create a timer object using the function `create_timer(period, callback)`. This will then call the callback function with the specified period. 

  A publisher is a class that can publish a message on a specific topic. In ROS2 we can create a publisher by calling the member-function `create_publisher()` function.
  
  ```python
    self.publisher = self.create_publisher(Message_type, 'topic_name')
  ```
  The constructor takes in at least two arguments &ndash; message type and topic name. Messages are divided into different message types, with individual data fields. In this way we know how the data in the message is to be interpreted. Some examples of message types are `String` and `Image`. The publisher object has a member function called `publish(message)`, which takes in a message object of the type specified in the constructor. The message object needs to be created and it's data fields populated before it is published. 

  ```python
    msg = String()
    msg.data = "Some message"
  ```
  ### Task
  You now want to create a node that publishes a message in the form of a `String`. In the `PublisherNode.py` file we have provided you with a code skeleton. Create a publisher and publish a message with a desired period. Then build and run your node and make sure everything works.
 
  <details>
  <summary>Hint: Checking if it works</summary>

  ```
  Use 'ros2 topic echo' to make sure the node is publishing the message
  ```
  </details>

   <details>
  <summary>Hint: Publishing the message</summary>

  ```
  self.publisher.publish(msg)
  ```
  </details>

  ### Writing a simple subscriber
  A subscriber is an object that listens for messages on a topic. We can create a subscriber object by calling the member function `create_subscription(Message_type, 'topic_name', callback_function)`. Unlike publishers, subscribers have a third parameter &mdash; the callback function. This function is called each time a message is received.

  ```python
 class SimpleNode(Node):
    def __init__(self):
        super().__init__('my_node_name')
        self.subscriber(msg_type, 'topic_name', self.some_callback)

    def some_callback(self, msg):
      #Do something
  ```

  ### Task
  Now finnish the subscriber in `SubscriberNode.py`. Subscribe to the same topic you published on earlier and make the subscriber print out the message.

  ### Task
  Now play around with the publishing frequency. A useful tool is `ros2 topic hz topic_name`. Can you figure out what it does? 


## Assignment 4: Services and Turtlesim


## Assignment 5 Talking to another computer


## Extra

## Sources
https://industrial-training-dev.readthedocs.io/en/latest/
