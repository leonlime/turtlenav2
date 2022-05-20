#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')
    navigation2 = get_package_share_directory('turtlebot3_navigation2')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(turtlebot3_gazebo, 'launch', 'turtlebot3_world.launch.py')
            ),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(navigation2, 'launch', 'navigation2.launch.py')
            ),
        ),
    ])
