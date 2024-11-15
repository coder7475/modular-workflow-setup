from setuptools import find_packages, setup

# READ README.md file 
with open('README.md', 'r', encoding='utf-8') as f:
    long_description=f.read()

# READ requirements file
with open("requirements.txt") as f:
    required=f.read().splitlines()

setup(
    name="mlops_modular_project",
    version="0.1.0",
    author="Robiul Hossian",
    author_email="robiulhossain7475@gmail.com",
    description="A modular MLOPS pipeline project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="my-github-repo-url",
    packages=find_packages(),
     classifiers=[
        "Development Status :: 3 - Beta",
        "Intended Audience :: ML Engineers",
        "Programming Language :: Python >= 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=required,
    extras_require={
        'dev': [
            'pytest>=7.1.1',
            'pytest-cov>=2.12.1',
            'flake8>=3.9.0',
            'black>=22.3.0',
            'isort>=5.10.1',
            'mypy>=0.942',
        ],
    },
)