import json

def process_nba_data(json_content: str)->list | dict:

    # Convert the JSON string to a Python object
    players_data = json.loads(json_content)

    # List to store player dictionaries
    players_list = []

    # Dictionary to store cumulative data for each position
    position_stats = {}

    # Processing data from JSON content
    for player in players_data:
        # Creating a player dictionary and adding it to the list
        player_dict = {
            "playerName": player["playerName"],
            "position": player["position"],
            "team": player["team"],
            "twoPercent": player["twoPercent"],
            "threePercent": player["threePercent"],
            "games": player["games"],
            "assists": player["assists"],
            "turnovers": player["turnovers"],
            "points": player["points"],
            "season": player["season"],
            "playerId": player["playerId"],
        }
        players_list.append(player_dict)

        # Updating cumulative data for the position
        position = player["position"]
        points = player["points"]

        if position not in position_stats:
            position_stats[position] = {"count": 0, "total_points": 0}

        position_stats[position]["count"] += 1
        position_stats[position]["total_points"] += points

    return players_list, position_stats

