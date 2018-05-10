import requests

def main():
    response = requests.get(
        'https://maps.googleapis.com/maps/api/place/textsearch/json?query=渋谷+丸亀製麺&key=AIzaSyDHL-wDp355XM2xzalZLOc3FyP3whnj3f8'
    )
    print(response.json())

if __name__ == '__main__':
    main()