# networked_warehouse_automation

Repository for ARTPARK Networked Warehouse Automation project

## Getting Started

The project is based on Ubuntu 20.04, ROS2 Foxy, gazebo 11.0. Links to the instructions for installing ROS2, Gazebo, etc. are provided below
- [Install ROS2](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
- [Install gazebo 11.0](http://gazebosim.org/tutorials?cat=install&tut=install_ubuntu&ver=11.0)

## Installation
- Clone the repo inside ~/<warehouse_ws>/src/

## Common Instructions to Run
- Source the ROS environment script
	
	```
	source /opt/ros/foxy/setup.bash
	```
- Install Dependencies
 
	```
    cd ~/warehouse_ws
	rosdep install --from-paths src --ignore-src -y -r
	```
- Build

	```
	colcon build
	```
- Source the setup file
	```
	. install/setup.bash
	```
- Open warehouse world in gazebo, opens world file set in wareohuse_gazebo/config/world_params.yaml
	```
	ros2 launch warehouse_gazebo warehouse.launch.py
## To open warehouse world in gazebo 
- opens world file set in wareohuse_gazebo/config/world_params.yaml
	```
	ros2 launch warehouse_gazebo small_warehouse.launch.py
	```
## To run Task Allocation
In separate terminals, run the following commands
-	Task generator node
	```
	ros2 launch warehouse_task_allocator task_launch.py
	```
-	Task allocator node
	```
	ros2 launch warehouse_task_allocator task_allocator_launch.py
	```
-	Dummy robot nodes
	```
	ros2 launch warehouse_task_allocator robots_launch.py
	```
-	Robot_nodes (different from dummy robot nodes as these also handle the task being allocated to the robot)
	```
	ros2 launch warehouse_task_allocator robot_node_launch.py
	```
- Dummy order publisher	
	```
	ros2 topic pub --once orders std_msgs/msg/String {}
	```
	OR
	```
	ros2 topic pub --rate 1 orders std_msgs/msg/String {}
	```
	
## Instructions to bringup the docker environment(ROS 2 foxy with gazebo-11)
- Place the Dockerfile and the docker-compose.yml file inside ~/your_workspace/. **NOTE:** The dockerfile will copy your entire src folder to the image.
- **To build the image:**

	```
	docker-compose build
	```
	**NOTE:**  This step might be time consuming.

- **To run the container:**
	```
	cd  ~/your_workspace/
	```

	```
	 ./bringup_foxy_devel.sh
	 ```
	 
	 Wait for the bash script to execute. In another terminal 
	 
	 ```
	 docker-compose exec warehouse_sim /bin/bash
	 ```
	 
## Acknowledgements
- [AWS Robotics](https://github.com/aws-robotics/aws-robomaker-small-warehouse-world)

## DOCUMENTATION
- [Sensor_fusion](https://drive.google.com/file/d/16wvkc_muDiQ8p2saD6U0r3i4AtBjJzsU/view?usp=sharing)
