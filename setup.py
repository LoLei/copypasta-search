"""copypasta-search - setup.py"""
import setuptools

LONG_DESC = open('README.md').read()

setuptools.setup(
    name="copypasta-search",
    version="1.2",
    author="Lorenz Leitner",
    author_email="lrnz.ltnr@gmail.com",
    description="Python Copypasta Search using Reddit",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    url="https://github.com/lolei/copypasta-search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": [
        "copypasta-search=copypasta_search:main"]},
    python_requires=">=3.5",
    install_requires=[
        'praw',
        'pyperclip'
    ],
)
