# ME537-Project

## Contents
* [Installation](#installation)
* [Physical Baxter Example Run](#physical-baxter-example-run)
* [Simulation Example Run](#simulation-example-run)
* [Known Bugs](#known-bugs)

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

## Known Bugs
### Not Found `rospkg`. Occurs normally when trying to do a `rosrun` command
You probably don't have ros setup for python3. Run the following commands
```
sudo apt-get install python3-pip python3-yaml
sudo pip3 install rospkg catkin_pkg
```
