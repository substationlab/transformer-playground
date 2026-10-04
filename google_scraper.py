import requests
from bs4 import BeautifulSoup

def get_google_first_and_fifth_word():
    url = 'https://www.google.com'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        words = text.split()
        
        if len(words) >= 5:
            first_word = words[0]
            fifth_word = words[4]
            print(f"First word: {first_word}")
            print(f"Fifth word: {fifth_word}")
        else:
            print("Not enough words on the page.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == '__main__':
    get_google_first_and_fifth_word()
