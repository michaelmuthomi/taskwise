from setuptools import find_packages, setup

with open("app/readme.md", "r") as f:
    long_description = f.read()

setup(
    name="taskwise",
    version="1.0.3",
    description="Taskwise is a CLI application for managing tasks through command line",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    entry_points="""
    [console_scripts]
    taskwise= taskwise.main:main
    """,
    keywords="taskwise, cli, task management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjanCodes/2023-package",
    author="Aman Deep",
    author_email="deep.aman6174@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["click>=8.1.6",
"markdown-it-py>=3.0.0",
"mdurl>=0.1.2",
"prompt-toolkit>=3.0.39",
"Pygments>=2.15.1",
"questionary>=1.10.0",
"rich>=13.5.2",
"shellingham>=1.5.0.post1",
"typer>=0.9.0",
"typing_extensions>=4.7.1",
"wcwidth>=0.2.6",
],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)