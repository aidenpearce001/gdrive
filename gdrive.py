import requests
import sys
import re

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: 
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2 :
            print("Usage: python gdrive.py shareable-link filename")
        # elif len(sys.argv) == 2 :
        #     destination = '.'
        elif len(sys.argv) == 3 :
            destination = sys.argv[2]
        link = sys.argv[1]
        result = re.search(r"""d/([^-]*)/""", link)
        print(result.group(1))
        download_file_from_google_drive(result.group(1), destination)
    except:
        print('Invalid link')
        sys.exit(0)
   
    