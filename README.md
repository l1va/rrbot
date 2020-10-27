# rrbot
Simple example of working with Gazebo in ROS 

### Prerequisits (ideally)
Ubuntu 18.04

ROS Melodic (full packet)

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
