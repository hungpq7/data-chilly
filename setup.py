import sys
from urllib.request import urlretrieve
from IPython.display import clear_output

DBFILE = 'chinook.db'

def setup():
    dbfile = sys.argv[1]
    urlretrieve(f'https://github.com/hungpq7/data-chilly/blob/sql/data/{dbfile}', dbfile)
    ipython = get_ipython()
    ipython.run_line_magic("pip", "install ipython-sql==0.5.0")
    ipython.run_line_magic("reload_ext", "sql")
    ipython.run_line_magic("sql", f"sqlite:///{dbfile}")
    ipython.run_line_magic("config", "SqlMagic.style='_DEPRECATED_DEFAULT'")
    ipython.run_line_magic("config", "SqlMagic.displaycon=False")
    ipython.run_line_magic("config", "SqlMagic.feedback=False")

    clear_output()
    print(f'{dbfile} connected successfully!')

setup()