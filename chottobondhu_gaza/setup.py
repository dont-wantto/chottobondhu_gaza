from setuptools import setup, find_packages

setup(
    name='chottobondhu_gaza',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'transformers',
        'spacy',
        'twilio',  # for alerts
        'numpy',
        'pandas',
    ],
    author='Nazrana Nahreen',
    author_email='nahreennazrana@gmail.com',
    description='AI-powered tool to detect trauma in children’s writings and messages during war or displacement.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dont-wantto/chottobondhu_gaza',
    license='MIT',
)
