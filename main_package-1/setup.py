from setuptools import setup, find_packages

setup(
    name='rl-agents',
    version='1.0.dev0',
    description='A collection of Reinforcement Learning agents',
    url='https://github.com/eleurent/rl-agents',
    author='Edouard Leurent',
    author_email='eleurent@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Researchers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='reinforcement learning agents',
    packages=find_packages(exclude=['gym', 'highway','gym-0.25.0.dist-info','highway_env-1.4.dist-info']),
    install_requires=['numpy', 'pandas', 'numba', 'pygame', 'matplotlib', 'seaborn', 'six', 'docopt','osqp','scipy','importlib-metadata==4.13.0','cloudpickle>=1.2.0','gym-notices>=0.0.4','tensorboardX','torch','tensorboard'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

