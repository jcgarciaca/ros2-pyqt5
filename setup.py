from setuptools import setup, find_packages

package_name = 'py_qt5_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),#[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juliocesar',
    maintainer_email='julio.jcgc@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_qt5_ros.publisher_fn:main',
            'gui = py_qt5_ros.ui_qt_ros:main'
        ],
    },
)
