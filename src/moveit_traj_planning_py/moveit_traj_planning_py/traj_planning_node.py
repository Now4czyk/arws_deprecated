import rclpy
from rclpy.node import Node
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('hello_moveit')

    logger = node.get_logger()

    # Create the MoveIt MoveGroup Interface
    move_group_interface = MoveGroupCommander('manipulator')

    # Set a target Pose
    target_pose = Pose()
    target_pose.orientation.w = 1.0
    target_pose.position.x = 0.28
    target_pose.position.y = -0.2
    target_pose.position.z = 0.5
    move_group_interface.set_pose_target(target_pose)

    # Create a plan to the target pose
    success, plan, _ = move_group_interface.plan()
    
    # Execute the plan
    if success:
        move_group_interface.execute(plan)
    else:
        logger.error("Planning failed!")

    # Shutdown ROS
    rclpy.shutdown()

if __name__ == '__main__':
    main()
