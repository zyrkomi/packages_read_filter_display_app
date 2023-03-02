import requests
from lxml import etree
import psycopg2
import datetime
import time
import os



# Define a function to download the XML data from the URL
def download_xml(url):
    response = requests.get(url)
    return response.content

# Define a function to parse the XML data and return a list of dictionaries
def parse_xml(xml_content):
    root = etree.fromstring(xml_content)
    packages = []
    for item in root.xpath("//item"):
        package = {}
        package["title"] = item.xpath("./title/text()")[0]
        package["link"] = item.xpath("./link/text()")[0]
        package["description"] = item.xpath("./description/text()")[0]
        package["pub_date"] = item.xpath("./pubDate/text()")[0]
        packages.append(package)
    return packages

# Define a function to insert the data into the PostgreSQL database
def insert_data(data):
    cur = conn.cursor()
    for package in data:
        cur.execute("INSERT INTO packages (title, link, description, pub_date) VALUES (%s, %s, %s, %s)",
                    (package["title"], package["link"], package["description"], package["pub_date"]))
    conn.commit()
    cur.close()

# Define a function to run the app
def run():
    url = "https://pypi.org/rss/packages.xml"
    xml_content = download_xml(url)
    data = parse_xml(xml_content)
    insert_data(data)



if __name__ == "__main__":

    try:

        # Get environment variables
        USER = os.getenv('API_USER')
        PASSWORD = os.environ.get('API_PASSWORD')
        DATABASE = os.environ.get('API_PASSWORD')
        HOST = os.environ.get('API_PASSWORD')
        PORT = os.environ.get('API_PASSWORD')

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

        # Schedule the app to run once per day
        while True:
            now = datetime.datetime.now()
            if now.hour == 15 and now.minute == 0:
                run()
            time.sleep(60)

    finally:
        # Close the PostgreSQL connection
        conn.close()




