from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lumen-ai",  # Replace with your own package name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered platform for detecting fraudulent activities on the Solana blockchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/lumen-ai",  # Replace with your own repository URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas==1.3.3",
        "pyyaml==5.4.1",
        "torch==1.9.0",
        "solana==0.18.0",  # Ensure this matches the version you're using
        "requests==2.26.0",
        "scikit-learn==0.24.2",
    ],
    entry_points={
        "console_scripts": [
            "lumen-ai=src.main:main",
        ],
    },
)
