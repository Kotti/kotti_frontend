import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'Kotti>=1.0.0',
    'Paste',
    'kotti_backend',
    'pyramid_html_renderer',
    ]

setup(name='kotti_frontend',
      version='0.0.1.dev0',
      description='kotti_frontend',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Framework :: Pylons",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "License :: Repoze Public License",
          ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='kotti_frontend',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = kotti_frontend:main
      """,
      )
