!wget -q -nc https://github.com/hungpq7/data-chilly/raw/main/data/chinook.db
!pip install -q ipython-sql
%reload_ext sql
%sql sqlite:///chinook.db
%config SqlMagic.style = '_DEPRECATED_DEFAULT'
%config SqlMagic.displaycon=False
%config SqlMagic.feedback=False