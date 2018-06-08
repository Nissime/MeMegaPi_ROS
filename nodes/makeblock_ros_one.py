#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from megapi import *
from makeblock_ros.srv import *

bot = None

<<<<<<< HEAD
def onRead_ultrasonic(v):

    rospy.loginfo(v)
    pub_usonic.publish(v)

def onRead_enc_1(v):
    rospy.loginfo(v)
    pub_enc1.publish(v)

def onRead_enc_2(v):
    rospy.loginfo(v)
    pub_enc2.publish(v)

def handle_makeblock_motors(req):
    global bot
    #rospy.loginfo(req.s2)
=======

def onRead(v):
    #rospy.loginfo(v)
    pub.publish(v)


def handle_makeblock_motors(req):
    global bot
>>>>>>> be1c14b473719aba2bf9dd93f1ce4997d035e929
    #bot.motorRun(M1, req.s1)
    #bot.motorRun(M2, req.s2)
    bot.encoderMotorRun(1, req.s1)
    bot.encoderMotorRun(2, req.s2)
    return 1


<<<<<<< HEAD
pub_usonic = rospy.Publisher('makeblock_ros_ultrasensor', Float32, queue_size=1)
pub_enc1 = rospy.Publisher('rosbot_encoder_1', Float32, queue_size=1)
pub_enc2 = rospy.Publisher('rosbot_encoder_2', Float32, queue_size=1)


=======
pub = rospy.Publisher('makeblock_ros_ultrasensor', Float32, queue_size=1)
>>>>>>> be1c14b473719aba2bf9dd93f1ce4997d035e929
s = rospy.Service('makeblock_ros_move_motors', MakeBlockMover,
                  handle_makeblock_motors)


def main():
    global bot
    bot = MegaPi()
    bot.start("/dev/ttyUSB0")
<<<<<<< HEAD
    sleep(1)

=======
>>>>>>> be1c14b473719aba2bf9dd93f1ce4997d035e929
    rospy.init_node('makeblock_ros', anonymous=False)

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
<<<<<<< HEAD
        #import pdb; pdb.set_trace()
        bot.ultrasonicSensorRead(6, onRead_ultrasonic)
        #bot.encoderMotorPosition( 1, onRead_enc_1 )
        #bot.encoderMotorPosition( 2, onRead_enc_2 )
=======
        sleep(0.1)
        #bot.ultrasonicSensorRead(6, onRead)
        bot.encoderMotorPosition( 1, onRead )
>>>>>>> be1c14b473719aba2bf9dd93f1ce4997d035e929


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
