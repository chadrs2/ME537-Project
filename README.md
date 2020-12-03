# ME537-Project

## Contents
* [Set up a base station or personal laptop](#set-up-a-base-station-or-personal-computer)
* [Set up a Jetson (rover computer)](#set-up-a-jetson)
* [FAQ](#faq)
* [Known bugs](#known-bugs)

## Requirements
* [Ubuntu 18.04](https://ubuntu.com/download/desktop) (preferred) or Ubuntu 16.04
* [Git](https://git-scm.com/download/linux)

----------

## Installation

Clone the repository to your Home directory:
```
cd ~
git clone https://github.com/chadrs2/ME537-Project.git
```

### Set up personal computer
Run the following command:

```
bash -i ~/ME537-Project/devel/setup.sh; source ~/.bashrc;
```

------------

## Simulation
### Clone baxter simulation
1. Clone simulator in ME537-Project/src/ run:
```
git clone https://github.com/RethinkRobotics/baxter_simulator.git
```
2. Change directory into baxter_simulator:
```
cd ~/ME537-Project/src/baxter_simulator/
```
3. Get pull request to be able to use the simulator in ros-melodic and create your own branch with that corrected pull request in it
```
git fetch origin pull/130/head:<name_of_your_branch_here>
git checkout <name_of_your_branch_here>
```
4. You can try catkin_make now in your "root" repository:
```
cd ~/ME537-Project/
catkin_make
```
5. It will likely tell you you're missing some stuff. Install the two things you're missing:
```
sudo apt install ros-melodic-effort-controllers
sudo apt install qt4-default
```

### Install simulator now
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

## Example Physical Baxter Setup
1. Source setup script
```
source ~/robotics_ws/devel/setup.sh
```
2. Change into simulation baxter environment within main ~/robotics_ws directory:
```
./baxter.sh
```
3. Resets robot: ``` rosrun baxter_tools enable_robot.py -r ```
4. Enables robot: ``` rosrun baxter_tools enable_robot.py -e ```
5. Untucks robot arms: ``` rosrun baxter_tools tuck_arms.py -u ```
6. Now run python command files in ipython, using the "run" command before the file name.

## Example Simulation Setup
1. Source setup script
```
source ~/robotics_ws/devel/setup.sh
```
2. Change into simulation baxter environment within main ~/robotics_ws directory:
```
./baxter.sh sim
```
3. Start up baxter in gazebo:
```
roslaunch baxter_gazebo baxter_world.launch
```

In a new terminal (repeat steps 1 & 2 in new terminal):
3. Resets reobot: ``` rosrun baxter_tools enable_robot.py -r ```
4. Enables robot: ``` rosrun baxter_tools enable_robot.py -e ```
5. Untucks robot arms: ``` rosrun baxter_tools tuck_arms.py -u ```
6. Now run our own files!

------------
