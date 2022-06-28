from setuptools import find_packages, setup

setup(
    name='pb_testing',
    packages=find_packages(include=['pb_testing']),
    version='0.1.2',
    scripts=['bin/create-dirs', 'bin/new-scenario'],
    description='Library for bdd testing',
    author='Me',
    license='MIT',
    install_requires=["setuptools", "behave", "selenium"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    include_package_data=True
)