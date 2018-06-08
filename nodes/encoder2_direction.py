#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
current_count=0
prev_count=0

def encoder2_callback(msg):
    current_count=msg.data
    global prev_count

    if current_count > prev_count:
        print ("fwd")

    if current_count < prev_count:
        print ("bkw")

    prev_count=current_count

rospy.init_node('mBot_encoder_subscribe')

rospy.Subscriber("rosbot_encoder_2", Float32, encoder2_callback)

rospy.spin()
