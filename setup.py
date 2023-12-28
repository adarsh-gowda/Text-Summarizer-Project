import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

repo_name = "Text-Summarizer-Project"
author_name = "adarsh"
author_email = "adarshgowda2711@gmail.com"
src_repo = "textSummarizer"


setuptools.setup(
    name=repo_name,
    version=__version__,
    author=author_name,
    author_email="adarshgowda2711@gmail.com",
    description="A small python package for NLP applications",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/adarshgowda2711/textSummarizer",
    project_urls={
        "Bug Tracker": "https://github.com/adarshgowda2711/textSummarizer/issues"
        
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
