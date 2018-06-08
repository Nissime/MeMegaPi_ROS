#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32


def UlstraSonicCallback(msg):
    if msg.data < 400.0 :
        print msg.data

rospy.init_node('mBot_Subscriber')

rospy.Subscriber("makeblock_ros_ultrasensor", Float32, UlstraSonicCallback)

rospy.spin()
