#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String

def set_goal_from_string(goal_string):
    # Parse the goal string to get position and orientation
    position_str, orientation_str = goal_string.split("/")
    x, y, z = [float(i.split("=")[1]) for i in position_str.split()[1:]]
    qx, qy, qz = [float(i.split("=")[1]) for i in orientation_str.split()[1:]]
    qw = 1.0

    # Create a PoseStamped message
    goal = PoseStamped()
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = z
    goal.pose.orientation.x = qx
    goal.pose.orientation.y = qy
    goal.pose.orientation.z = qz
    goal.pose.orientation.w = qw
    return goal

def goal_callback(data):
    # Parse the goal string and set the goal
    goal_string = data.data
    goal = set_goal_from_string(goal_string)
    # Publish the goal
    pub.publish(goal)

if __name__ == '__main__':
    rospy.init_node('goal_subscriber', anonymous=True)
    rospy.Subscriber("/unreal_msgs", String, goal_callback)
    pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)
    rospy.spin()
