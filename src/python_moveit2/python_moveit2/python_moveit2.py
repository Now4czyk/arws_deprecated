import rclpy
from rclpy.node import Node
from moveit_msgs.msg import RobotState
from moveit_msgs.srv import GetPositionIK
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import PositionIKRequest
from moveit_msgs.srv import GetPositionFK
from moveit_msgs.srv import GetPositionIK
from std_msgs.msg import Header

class MoveItPlanningExample(Node):

    def __init__(self):
        super().__init__('python_moveit')
        self.robot_state = RobotState()
        self.robot_state.joint_state.name = ["joint2_to_joint1", "joint3_to_joint2", "joint4_to_joint3", "joint5_to_joint4", "joint6_to_joint5", "joint6output_to_joint6"]
        self.robot_state.joint_state.position = [.0, .0, .0, .0, .0, .0]

        self.planning_scene_service = self.create_client(GetPositionIK, 'compute_ik')
        self.wait_for_service_available(self.planning_scene_service)
        
        self.execute_plan()

    def wait_for_service_available(self, client):
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def execute_plan(self):
        pose_target = PoseStamped()
        pose_target.header.frame_id = 'base'
        pose_target.pose.position.x = 0.28
        pose_target.pose.position.y = -0.2
        pose_target.pose.position.z = 0.5
        pose_target.pose.orientation.w = 1.0

        ik_request = PositionIKRequest()
        ik_request.group_name = "manipulator"
        ik_request.pose_stamped = pose_target

        request = GetPositionIK.Request()
        request.robot_state = self.robot_state
        request.ik_request = ik_request

        future = self.planning_scene_service.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None:
            response = future.result()
            if response.error_code.val == response.error_code.SUCCESS:
                self.get_logger().info('IK Solution found!')
                plan = response.solution.joint_state.position
                self.execute_trajectory(plan)
            else:
                self.get_logger().error('IK Solution failed with code: %d', response.error_code.val)
        else:
            self.get_logger().error('Service call failed')

    def execute_trajectory(self, joint_positions):
        # Add your code to execute the trajectory here
        self.get_logger().info('Executing trajectory: {}'.format(joint_positions))

def main(args=None):
    rclpy.init(args=args)
    node = MoveItPlanningExample()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
