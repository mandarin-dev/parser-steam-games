import xml.etree.ElementTree as ET
import requests


STEAM_ID = ''  # Steam ID64


def parse_games_from_profile():
    game_names = []

    response = requests.get(f'https://steamcommunity.com/profiles/{STEAM_ID}/games/?tab=all&xml=1')
    
    if response.status_code == 200:
        try:
            tree = ET.ElementTree(ET.fromstring(response.text))
            root = tree.getroot()
        except:
            print('Произошла ошибка во время парсинга!')


        for game in root.findall('.//games/game'):
            game_name = game.find('name').text
            game_names.append(game_name)
    
    return game_names

def export_game_list_to_txt(game_list, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for game in game_list:
            file.write(f"{game}\n")


if __name__ == '__main__':
    game_list = parse_games_from_profile()
    if game_list:
        export_game_list_to_txt(game_list, 'steam_game_list.txt')
        print('Список игр успешно экспортирован в файл steam_game_list.txt')
    else:
        print('Не удалось получить список игр.')
