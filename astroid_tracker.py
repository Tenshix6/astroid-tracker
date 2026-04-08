print('=================================')
print(" Angel's Asteroid Tracker"        )
print('=================================')



import requests

def send_alert(messages):

    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "avzj13t977tskeuu5fmv4hwpyb4tuf",
            "user": "u8asqgbzywtnrcsnbkwd58rx7qbfd6",
            "message": messages
        }
    )
API_KEY = "N9ZSF52fd0UHEwqs9VyJbrvPTRKBSg8twpMOFPjA"
url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={API_KEY}"

response = requests.get(url)
data = response.json()

asterioids = data["near_earth_objects"]

for date in asterioids:
    print("Date:", date)

    for asteroid in asterioids[date]:
        name = asteroid ["name"]
        hazardous = asteroid["is_potentially_hazardous_asteroid"]
        
        apporoach = asteroid["close_approach_data"][0]
                               
        distance = apporoach["miss_distance"]["kilometers"]
        speed = apporoach["relative_velocity"]["kilometers_per_hour"]


        print('asteroid:', name)
        print('hazardous:', hazardous)
        print('distance:', distance)
        print('speed:', speed)
        print("-------------------------------")

        
        if hazardous:
            alert = f"Hazardous Asteroid detected; {name}"
            print(alert)
            send_alert(alert)