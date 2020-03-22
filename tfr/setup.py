from setuptools import setup, find_packages

setup(
    name='tfr',
    version='0.1',
    py_modules=['tfr'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tfr=tfr.cli:cli
    ''',
)
