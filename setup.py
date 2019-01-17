from setuptools import setup

setup(name='plaza-service',
      version='0.1',
      description='Helper to build plaza services.',
      author='kenkeiras',
      author_email='kenkeiras@codigoparallevar.com',
      license='MIT',
      packages=['plaza_service'],
      scripts=[],
      include_package_data=True,
      install_requires = [
          'websockets'
      ],
      zip_safe=False)
