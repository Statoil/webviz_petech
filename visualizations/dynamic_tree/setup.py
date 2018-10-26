from setuptools import setup, find_packages

setup(
    name='webviz_dynamic_tree',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        'webviz_dynamic_tree': [
            'templates/*',
            'resources/js/*',
            'resources/css/*'
        ]},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'six'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'DynamicTree = webviz_dynamic_tree:DynamicTree',
        ]
    },
    zip_safe=False
)

