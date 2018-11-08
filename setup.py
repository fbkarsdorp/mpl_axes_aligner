from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='mpl_axes_aligner',
    version='1.1',
    author='ryutok',
    author_email='ryutokm@gmail.com',
    url='https://github.com/ryutok/mpl_axes_aligner',
    description='Adjust the plotting range of matplotlib.axes.Axes objects to align the origins with the given position',
    long_description=readme,
    packages=['mpl_axes_aligner'],
    license="MIT",
    install_requires=[
        'matplotlib',
    ],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-flake8'],
        'doc': ['sphinx', 'sphinx-rtd-theme'],
        'release': ['twine'],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
