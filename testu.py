import rospy
from geometry_msgs.msg import Pose

def move_object():
    # Initialize ROS node
    rospy.init_node('move_object_node')

    # Create a publisher to send commands to the robot
    pub = rospy.Publisher('/robot/move_to_pose', Pose, queue_size=10)

    # Define the target position of the object
    target_pose = Pose()
    target_pose.position.x = 0.5
    target_pose.position.y = 0.5
    target_pose.position.z = 0.0

    # Send the target position to the robot
    pub.publish(target_pose)

if __name__ == '__main__':
    try:
        move_object()
    except rospy.ROSInterruptException:
        pass
