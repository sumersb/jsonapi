from setuptools import setup, find_packages

setup(
    name="jsonapi",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # Include test packages as well
    test_suite="tests",
    # Include additional package metadata here
    author="Sumer Bal",
    description="A Python package",
    install_requires=[
        # List your dependencies here
    ],
)