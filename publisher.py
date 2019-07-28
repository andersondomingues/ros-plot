#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from std_msgs.msg import Float32

def pid(): 

    engineA = rospy.Publisher('engineA', Float32, queue_size = 10)
    engineB = rospy.Publisher('engineB', Float32, queue_size = 10)
    engineC = rospy.Publisher('engineC', Float32, queue_size = 10)
    engineD = rospy.Publisher('engineD', Float32, queue_size = 10)   
    
    rospy.init_node('pid', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        rospy.loginfo(random.random())
        engineA.publish(random.random())
        engineB.publish(random.random())
        engineC.publish(random.random())
        engineD.publish(random.random())
        rate.sleep()

if __name__ == '__main__':
    try:
        pid()
    except rospy.ROSInterruptException:
        pass
