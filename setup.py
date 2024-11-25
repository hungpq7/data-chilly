import sys
from urllib.request import urlretrieve
from IPython.display import clear_output

DBFILE = 'chinook.db'

dbfile = sys.argv[1]
urlretrieve(f'https://github.com/hungpq7/data-chilly/raw/sql/data/{dbfile}', dbfile)
get_ipython().run_line_magic("pip", "install ipython-sql==0.5.0")
get_ipython().run_line_magic("reload_ext", "sql")
get_ipython().run_line_magic("sql", f"sqlite:///{dbfile}")
get_ipython().run_line_magic("config", "SqlMagic.style='_DEPRECATED_DEFAULT'")
get_ipython().run_line_magic("config", "SqlMagic.displaycon=False")
get_ipython().run_line_magic("config", "SqlMagic.feedback=False")

clear_output()
print(f'{dbfile} connected successfully!')
