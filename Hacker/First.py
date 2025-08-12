import requests
def req():
    try:
        r = requests.get("http://0.0.0.0:5002")
        file = r.text
        with open("scrap.html","w") as f:
            f.write(file)
    except Exception as e:
        pass
        print("Something Error: ",e)
def main():
    req()
if __name__ == "__main__":
    main()