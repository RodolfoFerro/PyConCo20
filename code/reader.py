import requests


def check_status(url : str) -> str:
    """Function to verify API status."""
    
    r = requests.get(url)
    return r.text
    

if __name__ == '__main__':
    r = check_status('http://localhost:5000/api/status')
    print(r)