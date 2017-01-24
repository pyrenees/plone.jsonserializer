from setuptools import setup, find_packages

version = '0.9.3.dev0'

long_description = (
    open('README.md').read() + '\n' +
    open('CHANGES.md').read() + '\n'
)

setup(name='plone.jsonserializer',
      version=version,
      description="JSON serialization/deserialization adapters for Plone.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Plone Foundation',
      author_email='foundation@plone.org',
      url='https://github.com/pyrenees/plone.jsonserializer/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require={
          'test': [
              'plone.app.testing >= 4.2.2',
          ]},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
