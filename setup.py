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
    python_requires=">=3.9,<3.13",
    install_requires=[
        "numpy<2",
        "tensorflow>=2.15,<2.16",
        "scipy",
        "scikit-learn",
        "kneed",
        "anndata",
        "tensorflow_probability>=0.23,<0.24",
        "scanpy>1.3.3",
        "tf-keras",
        "leidenalg",
    ],
)
