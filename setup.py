from setuptools import setup

requirements = [
    'soap>=0.4'
]

setup(
    name='PEA_connect',
    version='1.0',
    description="Facilitates retrieval/manipulation of Exeter Connect Data",
    url="https://github.com/Exeter/PEA_connect",
    download_url="https://github.com/Exeter/PEA_connect",
    author="Sean Lee",
    author_email="freshdried@gmail.com",
    packages=['PEA_connect'],
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ]
)
