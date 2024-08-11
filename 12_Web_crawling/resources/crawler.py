import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

RED = "\033[31m"
DEF = "\033[0m"

target = "http://192.168.56.106/.hidden/"
readme = "README"
flag = "flag"

def fetch_page(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
		return response.text
	except requests.RequestException as e:
		print(f"Error fetching {url}: {e}")
		return None

def parse_links(page_content, base_url):
	soup = BeautifulSoup(page_content, 'html.parser')
	links = set()
	for anchor in soup.find_all('a', href=True):
		href = anchor['href']
		full_url = urljoin(base_url, href)
		if urlparse(full_url).path != '/':
			links.add(full_url)
	return links

def crawl(url, visited=None):
	if visited is None:
		visited = set()
	if url in visited:
		return
	page_content = fetch_page(url)
	if page_content is None:
		return

	visited.add(url)

	if readme in url:
		sys.stdout.write(f"\rChecking {url}")
		sys.stdout.flush()
		if page_content and flag in page_content:
			print(f"\n\n     {RED}MATCH FOUND!{DEF}\n")
			print(f"Contents of {readme} at {url}: ")
			print(page_content)
			sys.exit(0)

	links = parse_links(page_content, url)
	for link in links:
		crawl(link, visited)

def print_spider():
	print(f"\n     {RED}  / _ \\")
	print(f"     \\_\\(_)/_/     Starting crawler at {target}")
	print(f"      _//o\\\\_      looking for {readme} containing '{flag}'")
	print(f"       /   \\{DEF}\n")

if __name__ == "__main__":
	try:
		print_spider()
		crawl(target)
	except KeyboardInterrupt:
		print(f"\n{RED}Exitting...{DEF}")
		sys.exit(0)
