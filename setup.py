import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as rp:
    req = rp.read()

setuptools.setup(
    name="pygelf4ovh",
    version="0.4",
    author="Samuel MEYNARD",
    author_email="samuel@meyn.fr",
    description="pygelf adaptation that work for OVH Logs Data Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olopost/pygelf4ovh",
    install_requires=req,
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_dir={'pygelf4ovh': 'pygelf4ovh'},
    package_data={
        'pygelf4ovh': [
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)