import setuptools

long_description = open('README.md', 'r').read()

requirements = list(open('requirements.txt', 'r'))

setuptools.setup(
    author='Ammar Hazrin',
    author_email='ammarhazrinn@gmail.com',
    name='peribadi-search',
    version='0.1',
    include_package_data=True,
    install_requires=requirements,
    description='A discreet Google metasearch engine with privacy enabled and ad-free feature. ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://google.com',
    entry_points={
        'console_scripts': [
            'peribadi-search=app.routes:run_app',
        ]
    },
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
