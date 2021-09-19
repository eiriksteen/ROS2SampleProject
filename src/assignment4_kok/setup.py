from setuptools import setup

package_name = 'assignment4_kok'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='tordna@protonmail.com',
    description='Kok for assignment 4',
    license='Do wtf you want',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_draw_circle=assignment4_kok.CircleService:main'
        ],
    },
)
