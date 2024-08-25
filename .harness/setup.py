from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click==8.1.3',
        'Flask==2.2.2',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.1',
        'Werkzeug==2.2.2',
    ],
)

