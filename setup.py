from distutils.core import setup

setup(name='gemeindeverzeichnis',
      version='0.1',
      author='Igor Podolskiy',
      author_email='igor.podolskiy@vwi-stuttgart.de',
      maintainer="Theodor Diesner-Mayer",
      maintainer_email="theo.dm94@gmail.com",
      package_dir={'gemeindeverzeichnis': 'gemeindeverzeichnis'},
      packages=['gemeindeverzeichnis', 'gemeindeverzeichnis.objects', 'gemeindeverzeichnis.enums'],
      package_data={'gemeindeverzeichnis': ['data/GV100AD_301123.txt']},
      )
