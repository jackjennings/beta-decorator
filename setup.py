from setuptools import setup

from beta import __version__


setup(
    name='beta-decorator',
    version=__version__,
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    packages=['beta'],
    url='http://github.com/jackjennings/beta-decorator',
    license='LICENSE',
    description='For beta stuff',
    long_description=open('README.rst').read()
)
