from setuptools import setup, find_packages

setup(
    name='chottobondhu_gaza',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'transformers',
        'spacy',
        'twilio',  
        'numpy',
        'pandas',
    ],
    author='Nazrana Nahreen',
    author_email='nahreennazrana@gmail.com',
    description='AI-powered tool to detect trauma in children’s writings and messages during war or displacement.',
    long_description="An AI-powered tool for detecting trauma in children's text data.",
    long_description_content_type='text/markdown',
    url='https://github.com/dont-wantto/chottobondhu_gaza',  
    license='MIT',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
