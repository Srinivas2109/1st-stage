
from setuptools import setup, find_packages

setup(
    name="gemma-chatbot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "torch",
        "transformers",
        "bitsandbytes",
        "python-dotenv",
    ],
)
