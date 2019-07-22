#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
import numpy as np

from std_msgs.msg import String

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)  
    rand_val = np.random.randn(1)

    global y_vec
    y_vec[-1] = rand_val
    
    global line1
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],1.0)
     
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
#global vars
    global size
    size = 100
    global x_vec
    x_vec = np.linspace(0,1,size+1)[0:-1]
    global y_vec
    y_vec = np.random.randn(len(x_vec))
    global line1
    line1 = []
    listener()
   