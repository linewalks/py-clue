from setuptools import setup, find_packages

from pyclue import __version__ as version


setup(
    name="pyclue",
    version=version,
    description="Python interface to the MDwalks CLUE",
    author="Linewalks",
    author_email="jungwoo@linewalks.com",
    url="https://github.com/linewalks/py-clue",
    license="Linewalks",
    python_requires=">=3.6",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "grpcio",
        "protobuf"
    ],
    test_suite="tests",
    tests_require=["pytest"],
    packages=find_packages(include=["pyclue", "pyclue.*"])
)