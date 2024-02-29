from setuptools import setup

with open('README.md', 'r') as mdfile:
    des = mdfile.read()

setup(
    name='hxml',
    version='0.0.4',
    scripts=['hxml.py'],
    author="Hollo",
    author_email="hollo1234567890e@gmail.com",
    long_description=des,
    long_description_content_type="text/markdown",
    install_requires=[
        "hollos-get-data-recursive==0.0.1",
        "requests==2.31.0"
    ],
    url="https://github.com/DevHollo/hxml"
)
