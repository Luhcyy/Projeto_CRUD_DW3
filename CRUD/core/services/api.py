import requests
import time

class GoogleBooksAPI:
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    RATE_LIMIT_DELAY = 1 
    API_KEY = 'AIzaSyBDHsG9KMack98IYOMa1CftHMk_gOv2qG4'

    @staticmethod
    def search_books_by_title(title, start_index=0):
        params = GoogleBooksAPI.build_params(title, start_index)
        response = GoogleBooksAPI.make_request(params)
        return GoogleBooksAPI.process_response(response)
    
    @staticmethod
    def build_params(title, start_index):
        return {
            'q': f'intitle:{title}',  
            'maxResults': 40,        
            'startIndex': start_index,  
            'key': GoogleBooksAPI.API_KEY
        }
    
    @staticmethod
    def make_request(params):
        try:
            time.sleep(GoogleBooksAPI.RATE_LIMIT_DELAY)
            response = requests.get(GoogleBooksAPI.BASE_URL, params=params)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Erro durante a requisição à API: {e}")
            return None
    
    @staticmethod
    def process_response(response):
        if response:
            data = response.json()
            return data.get('items', [])
        return []
