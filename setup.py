from setuptools import find_packages, setup

setup(
    name='drawportlab',
    packages=find_packages(include = ["drawportlab"]),
    version='0.4.0',
    description='Addon to reportlab with focus on mechanical drawings',
    author='Morey_W.',
    install_requires = ["reportlab >= 4.0.0"],
)