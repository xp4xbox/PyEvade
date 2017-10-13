from distutils.core import setup
import py2exe

setup(script_args = ['py2exe'],
      windows=[{'script':'payload.py'}],
      options = {'py2exe': {'excludes': ['Tkconstants', 'Tkinter'],
							'bundle_files':1
                            },
                 },
		zipfile = None,
		)
