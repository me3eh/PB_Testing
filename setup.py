from setuptools import find_packages, setup

setup(
    name='pb_testing',
    packages=find_packages(include=['pb_testing']),
    version='0.1.2.52',
    scripts=['bin/prepare', 'bin/scan_for_urls', 'bin/create-scenario', 'bin/extra_modules_for_pb_testing.py',
                'bin/pb_configuration', 'bin/create-scenario-gui', 'bin/step_creator'],
    description='Library for bdd testing',
    author='Me',
    license='MIT',
    install_requires=[
        'bs4 >= 0.0.1',
        'behave >= 1.2.5'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    include_package_data=True
)