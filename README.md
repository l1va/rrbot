# rrbot
Simple example of working with Gazebo in ROS 

### Prerequisits (ideally)
- Ubuntu 18.04

- ROS Melodic (full packet) http://wiki.ros.org/melodic/Installation/Ubuntu

- install controllers (`sudo apt-get install ros-melodic-ros-control ros-melodic-ros-controllers`)

### Preparation
- copy sources to ~/rrbot_ws/src ( this file will be at ~/rrbot_ws/src/rrbot/README.md )

### Build
- `cd ~/rrbot_ws`
- `catkin build`
- `source devel/setup.bash`

### Run
There are bunch of launch files, to run use command `roslaunch pkg_name launch_file_name`. 
For example: `roslaunch rrbot_gazebo gazebo.launch` 

### Problems you can meet
- Some changes requires rebuild (but not all)
- Do not forget `source` command (if you opened new terminal for example)
- If nothing helps try to manually remove everything except src folder in the workspace (rrbot_ws) and rebuild. 
- Do not forget to click play button in the gazebo.
- Do not forget to set chmod +x for your python script

### Send command from console
You can use command `rostopic list` to check what topics are exists.
You can use command 
`rostopic pub /rrbot/joint1_position_controller/command std_msgs/Float64 "data: 1.0" `
to move joint1 to another position.