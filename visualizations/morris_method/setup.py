from setuptools import setup, find_packages

setup(
    name='webviz_morris_method',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={'webviz_morris_method': ['templates/*']},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'MorrisMethod = webviz_morris_method:MorrisMethod',
        ]
    },
    zip_safe=False
)

