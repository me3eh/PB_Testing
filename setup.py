from setuptools import find_packages, setup

setup(
    name='pb_testing',
    packages=find_packages(include=['pb_testing']),
    version='0.2.1',
    scripts=['bin/prepare',
             'bin/extra_modules_for_pb_testing.py',
             'bin/pb_configuration',
             'bin/step_creator'],
    description='Library for bdd testing',
    author='Me',
    license='MIT',
    install_requires=[
        'bs4 >= 0.0.1',
        'behave >= 1.2.5',
        'PySimpleGUI >= 4.60.4',
        'pyperclip >= 1.8.2',
        'mechanize >= 0.4.8',
        'selenium >= 4.6.0',
        'lxml >= 4.9.1'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    include_package_data=True
)
