from setuptools import setup, find_packages

setup(
    name='aadhaar-detection',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'tensorflow>=2.7'
    ],
    author='Girinath',
    author_email='girinathr@simplfin.tech',
    description='Aadhaar card detection library',
    long_description='A library for detecting Aadhaar cards in images.',
    url='https://github.com/GirinathRG/aadhaarlib/tree/main',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)


