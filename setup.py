from setuptools import setup

lcns = 'License :: OSI Approved :: GNU General Public License v3 or later'\
          '(GPLv3+)'
setup(name='n_queens',
      author='Maksim Grinman',
      author_email='maxchgr@gmail.com',
      description='Solves the n-Queens puzzle',
      keywords=['queens', 'chess', 'puzzle'],
      version='1.0',
      py_modules=['n_queens'],
      license='GPLv3+',
      classifiers = [lcns])
