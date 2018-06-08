#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32


def encoder2_callback(msg):
    print msg.data

rospy.init_node('mBot_encoder_subscribe')

rospy.Subscriber("rosbot_encoder_2", Float32, encoder2_callback)

rospy.spin()
