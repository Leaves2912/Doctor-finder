import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import re

sub=input("What would you like to study today ?")

print('1.) POWERPOINT PRESENTATIONS - \n')

def get_source_with_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()  # Formatted HTML output
sub_url=f"https://www.google.com/search?q=+{sub}+filetype:pptx"
# Example usage (use responsibly and ethically)
if __name__ == '__main__':
    target_url = sub_url # Replace with the actual URL
    sc = get_source_with_scraping(target_url)
pattern = r'https\S*pptx'
matches = re.findall(pattern,sc)
for x in range(len(matches)):
    if x>0 and x<6 :
        print(f"[{x}]: {unquote(unquote(matches[x]))}")
        print("\n")

print('2.) WORD FILES - \n')

def get_source_with_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()  # Formatted HTML output
sub_url=f"https://www.google.com/search?q=+{sub}+filetype:docx"
# Example usage (use responsibly and ethically)
if __name__ == '__main__':
    target_url = sub_url # Replace with the actual URL
    sc = get_source_with_scraping(target_url)
pattern = r'https\S*docx'
matches = re.findall(pattern,sc)
for x in range(len(matches)):
    if x>0 and x<6 :
        print(f"[{x}]: {unquote(unquote(matches[x]))}")
print("\n")

print('3.) PDF FILES - \n')

def get_source_with_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()  # Formatted HTML output
sub_url=(f"https://www.google.com/search?q=+{sub}+filetype:pdf")
# Example usage (use responsibly and ethically)
if __name__ == '__main__':
    target_url = sub_url # Replace with the actual URL
    sc = get_source_with_scraping(target_url)
pattern = r'https\S*pdf'
matches = re.findall(pattern,sc)
for x in range(len(matches)):
    if x>0 and x<6 :
        print(f"[{x}]: {unquote(unquote(matches[x]))}")
print("\n")

print('4.) MIT OCW COURSES - \n')

def get_source_with_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()  # Formatted HTML output
sub_url=f"https://www.google.com/search?q=+{sub}+site%3Aocw.mit.edu"
# Example usage (use responsibly and ethically)
if __name__ == '__main__':
    target_url = sub_url # Replace with the actual URL
    sc = get_source_with_scraping(target_url)
pattern = r'https\S*courses\S*/'
matches = re.findall(pattern,sc)
for x in range(len(matches)):
    if x>0 and x<30 :
        if len(matches[x])<90 and "resources" not in matches[x] and "pages" not in matches[x]:
            print(f"[{len(matches[x])}]: {unquote(unquote(matches[x]))}")
print("\n")

print('5.) YOUTUBE PLAYLISTS - \n')

def get_source_with_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()  # Formatted HTML output
sub_url=f"https://www.google.com/search?q={sub}+site%3Awww.youtube.com"
    # Example usage (use responsibly and ethically)
if __name__ == '__main__':
    target_url = sub_url # Replace with the actual URL
    sc = get_source_with_scraping(target_url)
pattern = r'https\S*watch%3Fv\S*'
matches = re.findall(pattern,sc)
matches1 = []
for x in matches:
    for j in range(len(x)):
        if x[j] == '&':
            matches1.append(x[:j])
            break
matches1=list(set(matches1))
for x in range(len(matches1)):
    if x>0 and x<10 :
        print(f"[{x}]: {unquote(unquote(matches1[x]))}")
print("\n")

print('6.) GITHUB - \n')

def get_source_with_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()  # Formatted HTML output
sub_url=f"https://www.google.com/search?q={sub}+site%3Agithub.io"
# Example usage (use responsibly and ethically)
if __name__ == '__main__':
    target_url = sub_url # Replace with the actual URL
    sc = get_source_with_scraping(target_url)
pattern = r'https\S*github.io\S*'
matches = re.findall(pattern,sc)
matches1 = []
for x in matches:
    for j in range(len(x)):
        if x[j] == '&':
            matches1.append(x[:j])
            break
        
for x in range(len(matches1)):
    if x>0 and x<10 :
        if "pdf" not in matches1[x]:
            print(f"[{x}]: {unquote(unquote(matches1[x]))}")
