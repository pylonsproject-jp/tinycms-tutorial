from setuptools import setup, find_packages

requires = [
    "pyramid",
    "pyramid_layout",
    "pyramid_zodbconn",
    "pyramid_tm",
    "pyramid_deform",
    "ZODB",
    "deform_bootstrap",
    "webhelpers2",
    "paginate",
    "pillow",
    "repoze.folder",
    "python-magic",
    "unidecode",
    "dogpile.cache",
]

tests_require = [
    "pytest",
    "webtest",
    "testfixtures",
]

setup(name="tinycms",
      packages=find_packages("src"),
      package_dir={"": "src"},
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          "testing": tests_require,
      },
)
