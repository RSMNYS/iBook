from setuptools import setup, find_namespace_packages

setup(name='iBook',
      version='5',
      description='iBook',
      url='https://github.com/RSMNYS/iBook',
      author='MagicDevs',
      author_email='magic.devs@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=[
            'annotated-types==0.6.0',
            'anyio==4.3.0',
            'certifi==2024.2.2',
            'colorama==0.4.6',
            'distro==1.9.0',
            'h11==0.14.0',
            'httpcore==1.0.4',
            'httpx==0.27.0',
            'idna==3.6',
            'openai==1.13.3',
            'prompt-toolkit==3.0.43',
            'pydantic==2.6.4',
            'pydantic_core==2.16.3',
            'python-dotenv==1.0.1',
            'sniffio==1.3.1',
            'tqdm==4.66.2',
            'typing_extensions==4.10.0',
            'wcwidth==0.2.13'
            ],
      extras_require={
            'dev': [
                  'pytest==8.1.1',
                  'pytest-mock==3.12.0'
                  ]
            },
      entry_points={"console_scripts": ["run_book = iBook.main:main"]},
      )