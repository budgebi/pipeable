from setuptools import setup, find_packages

setup(name='pipeable',
      version='1.0.3',
      description='A utility for making Python scripts compatible with the | operator on the command line.',
      author='Brian Budge',
      author_email='budgebrian21@gmail.com',
      url='https://github.com/budgebi/pipeable',
      license='MIT',
      packages= find_packages(exclude=['test']),
      python_requires='>=3',
      keywords='pipeline, pipe, pipeable',
      install_require=[],
      extra_require=[]
     )
