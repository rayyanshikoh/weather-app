# Weather App
 A weather app

## What is it about?
 This uses requests to return weather data for user city and outputs them on html page.
 
## How to deploy?
 First create a .env file in home directory and specify api key in APIKEY="(your key here)". Then afterwards use pipenv to install dependenies automatically from the .lock file to your virtual environment. Then run python manage.py migrate, and then python manage.py runserver
