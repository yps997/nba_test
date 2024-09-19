from services.read_from_api import get_data_from_api
from services.process_nba_json_data import process_nba_data
from services.create_objects import Create_objects

DICT_CALCULATE_POSATION = {}

def Run_process(base_url_api: str, lst:list):
    SEASON = ""
    URL_API = f"{base_url_api}/{SEASON}"
    SEASON_LST = lst

    for i in SEASON_LST:
        SEASON = i
    #get data from api
        context_json = get_data_from_api(URL_API)
    #process json to list of dict and dict of position stats
        result = process_nba_data(context_json)
    #dict of position stats
        dict_posation_stats = next(item for item in result if isinstance(item, dict))
    #list of dict players
        list_of_dict_players = next(item for item in result if isinstance(item, list))

        #new dict with calculation results of scoring each position
        DICT_CALCULATE_POSATION = dict(map(
    lambda item: (item[0], item[1]["total_points"] / item[1]["count"] if item[1]['count'] > 0 else 0),
    dict_posation_stats.items()))


        for player in list_of_dict_players:
            create_object = Create_objects(player)





