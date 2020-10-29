#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float64

pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
rospy.init_node('rrbot_control')
r = rospy.Rate(10)
time.sleep(3)
x = 0
while not rospy.is_shutdown():
    x += 0.01
    pub.publish(x)
    r.sleep()
