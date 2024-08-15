import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

RED = "\033[31m"
DEF = "\033[0m"

max_pages = 10000

def fetch_page(url):
	response = requests.get(url)
	response.raise_for_status()
	return response.text

def parse_links(page_content, base_url):
	soup = BeautifulSoup(page_content, 'html.parser')
	links = set()
	for anchor in soup.find_all('a', href=True):
		href = anchor['href']
		full_url = urljoin(base_url, href)
		if urlparse(full_url).path != '/':
			links.add(full_url)
	return links

def crawl(target_url, target_file, keyword, visited=None):
	if visited is None:
		visited = set()
	if target_url in visited:
		return
	if len(visited) > max_pages:
		print(f"\n\n{RED}No match found within the maximum page limit.{DEF}")
		print("Consider changing the search query or increasing the maximum page limit.\n")
		sys.exit(0)
	page_content = fetch_page(target_url)
	if page_content is None:
		return

	visited.add(target_url)

	sys.stdout.write(f"\r{RED}Checking{DEF} {target_url}")
	sys.stdout.flush()

	if target_file in target_url:
		if page_content and keyword in page_content:
			print(f"\n\n     {RED}MATCH FOUND!{DEF}\n")
			print(f"Contents of {target_file} at {target_url}: ")
			print(page_content)
			sys.exit(0)

	new_links = parse_links(page_content, target_url)
	for link in new_links:
		crawl(link, target_file, keyword, visited)

def print_spider(target_url, target_file, keyword):
	print(f"\n     {RED}  / _ \\")
	print(f"     \\_\\(_)/_/     {DEF}Starting crawler at {RED}{target_url}")
	print(f"      _//o\\\\_      {DEF}looking for file {RED}{target_file}{DEF} containing keyword {RED}{keyword}")
	print(f"       /   \\{DEF}\n")

if __name__ == "__main__":
	if len(sys.argv) not in [4, 5]:
		print(f"{RED}usage:{DEF} python3 crawler.py <target_URL> <target_file> <keyword> [optional: max_pages]")
		sys.exit(1)
	try:
		if len(sys.argv) == 5:
			max_pages = int(sys.argv[4])
		print_spider(sys.argv[1], sys.argv[2], sys.argv[3])
		crawl(sys.argv[1], sys.argv[2], sys.argv[3])
	except KeyboardInterrupt:
		print(f"\n{RED}Exitting...{DEF}")
		sys.exit(0)
	except Exception as e:
		print(f"{RED}Error:{DEF} {e}")
		sys.exit(0)
