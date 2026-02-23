import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="vaeda",
    version="0.0.30",
    author="Hannah Schriever",
    author_email="hcs31@pitt.edu",
    packages=["vaeda"],
    description="A computational tool for annotating doublets in scRNAseq data.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/kostkalab/vaeda",
    license="MIT",
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24",
        "tensorflow>=2.15",
        "scipy>=1.10",
        "scikit-learn>=1.2",
        "kneed>=0.8",
        "anndata>=0.9",
        "tensorflow_probability>=0.23",
        "scanpy>1.3.3",
        "tf-keras>=2.15",
        "leidenalg>=0.9",
    ],
)
