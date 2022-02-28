import rick_and_morty


def test_character_cleanup():
    input = {
        "created": "2017-11-04T18:48:46.250Z",
        "episode": [
            "https://rickandmortyapi.com/api/episode/1",
            "https://rickandmortyapi.com/api/episode/2",
        ],
        "gender": "Male",
        "id": 1,
        "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
        "location": {
            "name": "Earth (Replacement Dimension)",
            "url": "https://rickandmortyapi.com/api/location/20",
        },
        "name": "Rick Sanchez",
        "origin": {
            "name": "Earth (C-137)",
            "url": "https://rickandmortyapi.com/api/location/1",
        },
        "species": "Human",
        "status": "Alive",
        "type": "",
        "url": "https://rickandmortyapi.com/api/character/1",
    }

    expected_output = {
        "created": "2017-11-04T18:48:46.250Z",
        "episode_ids": [1, 2],
        "gender": "Male",
        "id": 1,
        "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
        "location_id": 20,
        "name": "Rick Sanchez",
        "origin_id": 1,
        "species": "Human",
        "status": "Alive",
        "type": "",
        "url": "https://rickandmortyapi.com/api/character/1",
    }

    assert rick_and_morty.character_cleanup(input) == expected_output

def test_episode_cleanup():
    input = {'id': 1,
        'name': 'Pilot',
        'air_date': 'December 2, 2013',
        'episode': 'S01E01',
        'characters': ['https://rickandmortyapi.com/api/character/1',
            'https://rickandmortyapi.com/api/character/2',
            'https://rickandmortyapi.com/api/character/35'],
        'created': '2017-11-10T12:56:33.798Z'
            }

    expected_output = {'id': 1,
        'name': 'Pilot',
        'air_date': 'December 2, 2013',
        'episode': 'S01E01',
        'character_ids': [1, 2, 35],
        'created': '2017-11-10T12:56:33.798Z'
        }

    assert rick_and_morty.episode_cleanup(input) == expected_output

def test_location_cleanup():

    input = {'id': 1,
        'name': 'Earth (C-137)',
        'type': 'Planet',
        'dimension': 'Dimension C-137',
        'residents': ['https://rickandmortyapi.com/api/character/38', 'https://rickandmortyapi.com/api/character/45', 'https://rickandmortyapi.com/api/character/71'],
        'url': 'https://rickandmortyapi.com/api/location/1',
        'created': '2017-11-10T12:42:04.162Z'
        }

    expected_output = {'id': 1,
        'name': 'Earth (C-137)',
        'type': 'Planet',
        'dimension': 'Dimension C-137',
        'resident_ids': [38, 45, 71],
        'url': 'https://rickandmortyapi.com/api/location/1',
        'created': '2017-11-10T12:42:04.162Z'
        }

    assert rick_and_morty.location_cleanup(input) == expected_output



def test_extract_id_from_url():
    input = "https://rickandmortyapi.com/api/location/1"

    expected_output = 1

    rick_and_morty.extract_id_from_url(input) == expected_output

    input = ''
    expected_output = None

    rick_and_morty.extract_id_from_url(input) == expected_output
