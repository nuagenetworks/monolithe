from setuptools import setup, find_packages

setup(
    name="monolithe",
    packages=find_packages(exclude=[""*tests*""]),
    include_package_data=True,
    version="0.0.2",
    description="Monolithe is the basis of the universe",
    author="Christophe Serafin, Antoine Mercadal",
    author_email="christophe.serafin@nuagenetworks.net, antoine@nuagenetworks.net",
    url="https://github.com/nuagenetworks/monolithe",
    classifiers=[],
    install_requires=[line for line in open("requirements.txt")],
    entry_points={
        "console_scripts": [
            "monogen-sdk = monolithe.generators.sdk.cli:main",
            "monogen-apidoc = monolithe.generators.apidoc.cli:main",
            "monogen-sdkdoc = monolithe.generators.sdkdoc.cli:main"]
    }
)
