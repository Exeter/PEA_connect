from setuptools import setup


setup(
    name='PEA_connect',
    version='1.0',
    description="Facilitates retrieval/manipulation of Exeter Connect Data",
    url="https://github.com/Exeter/PEA_connect",
    download_url="https://github.com/Exeter/PEA_connect",
    install_requires=["suds>=0.4"],
    author="Sean Lee",
    author_email="freshdried@gmail.com",
    packages=['PEA_connect'],
)
