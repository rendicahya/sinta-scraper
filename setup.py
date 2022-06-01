import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sinta3-scraper',
    version='0.1.0',
    author='Randy Cahya Wihandika',
    author_email='rendicahya@gmail.com',
    description='Retrieves information from Sinta 3 (https://sinta3.kemdikbud.go.id) via scraping.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rendicahya/sinta3-scraper',
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4', 'requests', 'dicttoxml', 'dict2xml', 'python-string-utils'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
