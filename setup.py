from pathlib import Path
from setuptools import find_packages, setup


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_requirements(req_path: Path):
    # Parse a pip-compile style requirements file, ignoring comments and blanks
    requires = []
    for line in read_text(req_path).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        # keep requirement spec as-is (supports extras and markers)
        requires.append(stripped)
    return requires


README = read_text(Path(__file__).parent / "README.md")
REQUIRES = read_requirements(Path(__file__).parent / "requirements.txt")


def get_version():
    global_vars = {}
    exec(Path("src/py_eveng/cli/version.py").read_text(), global_vars)
    return global_vars["__version__"]


setup(
    name="eve-ng",
    keywords=["eve-ng", "eveng", "unetlab", "py-eveng"],
    license="MIT license",
    version=get_version(),
    author="Abhimanyu Saharan",
    author_email="asaharan@onemindservices.com",
    maintainer="Onemind Services LLC",
    maintainer_email="developers@onemindservices.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    description=(
        "Python SDK and command line utilities to work with the EVE-NG REST API"
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Onemind-Services-LLC/py-eveng.git",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=REQUIRES,
    entry_points={
        "console_scripts": [
            "eve-ng=py_eveng.cli.cli:main",
            "eveng=py_eveng.cli.cli:main",
        ],
    },
    include_package_data=True,
)
