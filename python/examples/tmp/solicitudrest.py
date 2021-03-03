import urllib.request
import json

def main():
    url = 'https://developer.spotify.com'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print(json.dumps(data, sort_keys=True))

if __name__ == "__main__":
    main()