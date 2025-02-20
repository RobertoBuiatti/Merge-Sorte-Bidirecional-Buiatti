"""
Configuração para distribuição do pacote merge_sort_bidirecional_buiatti
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="merge_sort_bidirecional_buiatti",
    version="1.0.0",
    author="Roberto Buiatti",
    description="Implementação do algoritmo Merge Sort Bidirecional em Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robertobuiatti/merge_sort_bidirecional_buiatti",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    test_suite="tests",
)
