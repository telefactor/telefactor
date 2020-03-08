from setuptools import setup

setup(
    name='tfr',
    version='0.1',
    py_modules=['tfr'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tfr=tfr.cli:cli
    ''',
)