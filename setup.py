from distutils.core import setup, find_packages

setup(name='pipeable',
      version='0.0.0',
      description='A utility for making Python scripts compatible with the | operator on the command line.',
      author='Brian Budge',
      author_email='budgebrian21@gmail.com',
      url='https://github.com/budgebi/pipeable',
      license='MIT',
      packages=find_packages(exclude=('tests')),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='pipeline, pipe, pipeable',
      install_require=[],
      extra_require=[]
     )
