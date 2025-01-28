from setuptools import setup, find_packages
with open(r"C:\pythonCode\congressUtility\ViscaSmithCore\readMe.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="viscaSmithCore",
    version="0.4.0",
    author="Alessio Michelassi",
    author_email="alessio.michelassi@gmail.com",
    description="Una libreria per controllare telecamere VISCA tramite UDP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlessioMichelassi/ViscaSmithCore",
    packages=find_packages(include=["visca_control", "visca_control.*"]),
    include_package_data=True,  # Includi file non Python (es. JSON)
    install_requires=["PyQt6", "PyQt6-sip", "PyQt6-Qt6", "PyQt6-Qt6-sip", "PyQt6-Designer"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)