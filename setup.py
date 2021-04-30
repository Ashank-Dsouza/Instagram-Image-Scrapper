from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'Console'

executables = [
    Executable('main.py', base=base, target_name = 'Scrapper')
]

setup(name='Scrapper',
      version = '1.0',
      description = 'Scrapper',
      options = {'build_exe': build_options},
      executables = executables)
