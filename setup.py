import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbmanager",
    version="2",
    authors="Saeed Ghadiri, MohammadJafar Karimi",
    author_email="mjkb90@gmail.com",
    description="access to mongoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MJKB92/dbmanager",
    project_urls={
        "Bug Tracker": "https://github.com/MJKB92/dbmanager/issues",
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['dbmanager'],
    python_requires=">=3.6",
    
    install_requires=[
        'pymongo',
        'datetime',
        'pytz',
        'pandas',
        'numpy'
    ]
)