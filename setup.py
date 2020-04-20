from setuptools import setup

setup(
    name='linkyndle',
    version='1.0',
    description=' Fetch dataset from Enedis portal (need Linky) and push it to grafana ',
    license="GNU",
    author='Baptiste Candellier',
    author_email='git@beufa.net',
    url="https://beufa.net",
    packages=['linkyndle'],
    install_requires=[
        'python-dateutil',
        'influxdb',
        'fake_useragent'
    ],
    scripts=['scripts/linkyndle'],
)
