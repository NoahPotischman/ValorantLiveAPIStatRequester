import requests

# Define the Riot API endpoint.
endpoint = "https://na.api.riotgames.com/val/account/v1/accounts/by-riot-id/"

# Define the Valorant API endpoint for retrieving player stats.
stats_endpoint = "https://na.api.riotgames.com/val/stats/v1/player-stats/"

# Define the API headers, including your Riot API key.
headers = {
    "X-Riot-Token": "Your Riot API-KEY should go here"
}

# Request the player's Riot ID.
riot_id = input("Enter player Riot ID (e.g. player1#1234): ")
region = input("Enter player region (e.g. na): ")
url = endpoint + riot_id + "?game=val&region=" + region
response = requests.get(url, headers=headers)

# Retrieve the player's performance metrics if the Riot ID was found.
if response.status_code == 200:
    player_id = response.json()["puuid"]
    stats_url = stats_endpoint + player_id + "/competitive"
    stats_response = requests.get(stats_url, headers=headers)

    # Parse the performance metrics from the response and display them.
    if stats_response.status_code == 200:
        stats_json = stats_response.json()
        print(f"\nPerformance metrics for {riot_id}:")
        print(f"Kills per round: {stats_json['killStats']['killsPerRound']:.2f}")
        print(f"Deaths per round: {stats_json['killStats']['deathsPerRound']:.2f}")
        print(f"Assists per round: {stats_json['assistsPerRound']:.2f}")
        print(f"Headshot percentage: {stats_json['headshotPercentage']:.2f}%")
        print(f"Win percentage: {stats_json['winRate']:.2f}%")
    else:
        print("Unable to retrieve player stats.")
        print(f"Response code: {stats_response.status_code}")
        print(f"Response message: {stats_response.json()['message']}")
else:
    print("Player not found.")
    print(f"Response code: {response.status_code}")
    print(f"Response message: {response.json()['message']}")
