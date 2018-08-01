import setuptools

setuptools.setup(
    name="topology-yaml",
    version="0.1.1",
    url="https://github.com/lumina-networks/topology-yaml",

    author="Lumina NetDev",
    author_email="oss-dev@luminanetworks.com",

    description="Opinionated topology file generator and parser",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['click', 'click-plugins', 'PyYAML'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points='''
        [console_scripts]
        topology-yaml=topology.cli:cli
    ''',
)
