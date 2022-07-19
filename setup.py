import setuptools

setuptools.setup(
    name='related-ontologies',
    version='0.0.1',
    description='A package to generate related clinical ontologies (LOINC, SNOMED-CT)',
    url='https://github.com/alistairewj/bert-deid',
    author='Justin Xu',
    author_email='justin13601@hotmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[

    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['related-ontologies = related-ontologies.__main__:main'],
        'related-ontologies.__main__':
            [
                'apply = related-ontologies.__main__:apply',
                'download = related-ontologies.__main__:download'
            ]
    },
)