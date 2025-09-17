from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = [line.strip() for line in f.readlines() if line.strip()]

packages = find_packages(include=["kinopapi", "kinopapi.*"])

setup(
    name="kinopapi",
    version="1.1.0",
    author="cls.",
    description="Library for working with Kinopoisk API.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cloudsucker/kinopapi",
    packages=packages,
    install_requires=install_requires,
    python_requires=">=3.12",
    include_package_data=True,
)
