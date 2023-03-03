# general description

This is an app for monitoring new python packages releases.

Whole solution contains two parts:

1. Monitoring/Downloading script

Once per day list of packages is read from the page:
https://pypi.org/rss/packages.xml
and stored in database, by script:

main.py

2. Listing and filtering web app

packages_filtering_app

For security reasons all db related informations are read from environment variables from local system

- this should be provided by user before launching the app.

# packages_read_filter_display_app

App for reading python packages , save it in db and display, filter through web app

# environment variables

ITEMS_PER_PAGE - resposible for number of items displayed per page

db related variables:
USER - user name
PASSWORD - user password
HOST - host on which db is run
PORT - port on which db is run
DB - db name
