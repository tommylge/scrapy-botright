import setuptools

from scrapy_botright import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="scrapy-botright",
    version=__version__,
    license="BSD",
    description="Botright integration for Scrapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tom LARGE",
    author_email="tle@sahar.fr",
    url="https://github.com/scrapy-plugins/scrapy-playwright",
    packages=["scrapy_botright"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Scrapy",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scrapy>=2.0,!=2.4.0",
        # "git+https://github.com/tommylge/Botright@light-weight",
    ],
)
