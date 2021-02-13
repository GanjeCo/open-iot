import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "paho-mqtt==1.5.1"
]


setuptools.setup(
    name="open-iot-GanjeCo",
    version="0.0.1",
    author="Mostafa Ghofrani",
    author_email="mostafa_gho@yahoo.com",
    description="A light iot package to define Device and Things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GanjeCo/open-iot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)