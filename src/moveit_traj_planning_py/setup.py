from setuptools import find_packages, setup

package_name = 'moveit_traj_planning_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tebainknowaczyk',
    maintainer_email='k.nowaczyk@teb-akademia.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "traj_node = moveit_traj_planning_py.traj_planning_node:main"
        ],
    },
)
