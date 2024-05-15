from setuptools import setup, find_packages

setup(
    name='historical_analysis_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'plotly'
    ],
    entry_points={
        'console_scripts': [
            'historical_analysis=historical_analysis.main:main',
        ],
    },
)
