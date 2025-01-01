from setuptools import setup, find_packages

setup(
    name="g4fp",
    version="1.1.6",
    description="A library for unlimited use of LLM through g4f, using a proxy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Leonid",
    author_email="leo.gladkikh2@gmail.com",
    url="https://github.com/Leolox228/g4fp",
    license="GPL-3.0",
    packages=find_packages(),
    install_requires=[
        "free-proxy",
        "g4f"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
