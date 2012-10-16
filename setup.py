from setuptools import setup, find_packages


VERSION = __import__("pybrightcove").__version__


setup(
    name="pybrightcove",
    version=VERSION,
    author="Patrick Altman",
    author_email="paltman@eldarion.com",
    url="http://github.com/studionow/pybrightcove/",
    description="""A Python interface for the Brightcove APIs""",
    packages=find_packages(),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    license="MIT",
    install_requires=["requests==0.14.1"]
)
