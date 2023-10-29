from setuptools import find_packages, setup

package_name = 'python_moveit2'

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
    maintainer='teba_knowaczyk',
    maintainer_email='k.nowaczyk@teb-akademia.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "python_moveit2 = python_moveit2.python_moveit2:main"
        ],
    },
)