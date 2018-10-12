# Task List
1. Get data from the postgreSQL DB. Display 1yr YTD yield, and volatility on a daily basis
2. Make scripts to get daily price quote and post to DB
3. Make volatility calculation more accurate based on high/low
4. Make volatility calculation more accurate based on open/mid/close
5. Make volatility calculation more accurate based on hourly pricing
6. Make volatility calculation more accurate based on minute pricing 
7. Make volatility calculation more accurate based on seconds pricing 
8. Allow users to make profiles to save and track stocks
9. Make reddit feature for feature voting

# Purpose
Easily compare public stocks by the risk-adjusted-yield. 

# About
Built with Django, and PostgreSQL

# Django Notes:
- Projects contain multiple apps
- To create new apps, go to the `migrate.py` directory and type `python3 manage.py startapp appName`
- There are 4 pieces to the `path()` argument: route URL, view function, kwargs (optional), and name (optional)
- When using a non SQLite db, update the default `databases` array in `app/settings.py`
- Each app has a `model.py` file to set up the data structure.
- Once an app is made, the configuration path is added to the `installed apps` on the project's `project/settings.py`   file
- When making changes, there is a 3 step process: 1) changes, 2) `python3 manage.py makemigrations` 3) `python3 manage.py migrate`
- Django has a free API included - access it through the python shell with `python manage.py shell`
- Each view will either return the `HTTPResponse` object or a 404 not found.
- When making templates for views, use the naming scheme: `/appName/templates/appName/index.html`


# Django Admin
- Admin functionality is built into Django to allow site managers to publish content without needing a separate         abstraction.
- First, make a superuser with the command: `python3 manage.py createsuperuser`
- Username: `anthony`
- email: `ajc-sorin@protonmail.com`
- password: `passwordt0nyj0n4!`
- Migrate to `http://127.0.0.1:8000/admin`



# Build Log:
- `python3 manage.py migrate` to update server
- `python3 manage.py runserver` to run server
- `pip3 install psycopg2` to get postgresql package



