# ME537-Project

## Contents
* [Installation](#installation)
* [Simulation Installation](#simulation-installation)
* [Physical Baxter Example Run](#physical-baxter-example-run)
* [Simulation Example Run](#simulation-example-run)

## Requirements
* [Ubuntu 18.04](https://ubuntu.com/download/desktop) (preferred) or Ubuntu 16.04
* [Git](https://git-scm.com/download/linux)

----------
## Installation
### Clone the repository and update the submodules
```
cd ~
git clone https://github.com/chadrs2/ME537-Project.git
cd ~/ME537-Project
git submodule update --init --recursive
```
### Build repository 
1. Remove current `build` and `devel` folders
```
sudo rm -rf build devel
```
2. Install necessary ROS dependency packages
```
sudo apt install ros-<ros_version>-effort-controllers
sudo apt install qt4-default
```
3) Run `catkin_make`

### Set up personal computer
Run the following command:

```
bash -i ~/ME537-Project/devel/setup.sh; source ~/.bashrc;
```

------------

## Simulation Installation
### Install simulator
1. Change into main directory src folder and run the following commands:
```
cd ~/ME537-Project/src/
wstool . init
wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter_simulator/master/baxter_simulator.rosinstall
wstool update
```
2. Build source now by running the following commands:
```
source ~/.bashrc
source ~/ME537-Project/devel/setup.bash
```
3. Now do catkin_make
```
cd ~/ME537-Project/
catkin_make
```

------------

## Physical Baxter Example Run
1. Source setup script
```
source ~/ME537-Project/devel/setup.sh
```
2. Change into simulation baxter environment within main ~/ME537-Project directory:
```
./baxter.sh
```
3. Resets robot: ``` rosrun baxter_tools enable_robot.py -r ```
4. Enables robot: ``` rosrun baxter_tools enable_robot.py -e ```
5. Untucks robot arms: ``` rosrun baxter_tools tuck_arms.py -u ```
6. Now run python command files in ipython, using the "run" command before the file name.

## Simulation Example Run
1. Source setup script
```
source ~/ME537-Project/devel/setup.sh
```
2. Check that `~/ME537-Project/baxter.sh` file has your own computer's IP address 
3. Change into simulation baxter environment within main ~/ME537-Project directory:
```
./baxter.sh sim
```
4. Start up baxter in gazebo:
```
roslaunch baxter_gazebo baxter_world.launch
```
5. In a new terminal (repeat steps 1 & 3 in new terminal):
6. Resets robot: ``` rosrun baxter_tools enable_robot.py -r ```
7. Enables robot: ``` rosrun baxter_tools enable_robot.py -e ```
8. Untucks robot arms: ``` rosrun baxter_tools tuck_arms.py -u ```
9. Now run your own files!

------------

## Bugs
### `rospkg` Not Found
You probably don't have ros setup for python3. Run the following commands
```
sudo apt-get install python3-pip python3-yaml
sudo pip3 install rospkg catkin_pkg
```
