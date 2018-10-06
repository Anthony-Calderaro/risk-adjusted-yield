# Task List
1. Get data from the postgreSQL DB. Display 1yr YTD yield, and volatility on a daily basis
2. Make scripts to get daily price quote and post to DB
3. Make volatility calculation more accurate based on high/low
4. Make volatility calculation more accurate based on open/mid/close
5. Make volatility calculation more accurate based on hourly pricing
6. Make volatility calculation more accurate based on minute pricing 
7. Make volatility calculation more accurate based on seconds pricing 

# Purpose
Easily compare public stocks by the risk-adjusted-yield. 

# About
Built with Flask, Django, and PostgreSQL

# Build Log:
`youtube.com/watch?v=zRwy8gtgJ1A`
- `Pip install flask`
- Create `app.py`
- `python app.py` to test on localhost
- Make `templates` folder
- Make `home.html` page
- Make `layout.html` template
Note: Everything in the `layout.html` page will appear on every page. This is a good spot for thinks like logos/nav bars
- Copy in Bootstrap from `bootstrapcdn.com`to the layout.html page
