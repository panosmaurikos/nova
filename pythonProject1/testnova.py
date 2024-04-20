from bs4 import BeautifulSoup
import requests

# Function to extract specific tags from multiple URLs
def extract_specific_tags_from_urls(urls, specific_class):
    all_data = []

    for url in urls:
        data = {}
        # Fetch the page content
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Extract <h1> and <time> tags
        data['h1'] = soup.find('h1').get_text(strip=True) if soup.find('h1') else None
        data['time'] = soup.find('time').get_text(strip=True) if soup.find('time') else None

        # Extract the content from the specified class
        specific_class_content = soup.find(class_=specific_class)
        data[specific_class] = specific_class_content.get_text(strip=True) if specific_class_content else None

        # Append the data to the results list
        all_data.append(data)

    return all_data

# List of URLs to process
urls = [
    'https://www.protothema.gr/greece/article/1444792/provlimata-sto-diktuo-tis-nova/',
    'https://www.in.gr/2020/03/30/sports/football/nova-ektos-realismou-ayksisi-omadon-sti-super-league-1-pio-pithani-meiosi/',
    'https://example.com/news/article/12345',
    'https://example.com/sports/article/67890'
]

# Name of the specific class to extract
specific_class = 'content'  # Change this to the class you need

# Extract data from each URL
result = extract_specific_tags_from_urls(urls, specific_class)

# Print the extracted data
for i, data in enumerate(result, 1):
    print(f"Data from URL {i}: {data}")
