from dataclasses import dataclass
from typing import List

@dataclass
class GameSet:
  red: int
  green: int
  blue: int

@dataclass
class Game:
  id: int
  sets: List[GameSet]


@dataclass
class Bag(GameSet):
  pass


def parse_games(lines):
  games = []

  for line in lines:
    game_name_raw, game_sets_raw = line.split(':')
    game_id = int(game_name_raw.strip().split(' ')[1])
    sets_raw = game_sets_raw.strip().split(';')
    sets = []

    for set_raw in sets_raw:
      drops = list(map(lambda x: x.strip(), set_raw.split(',')))
      colors = {
        "red": 0,
        "green": 0,
        "blue": 0
      }

      for drop in drops:
        amount_raw, color = drop.split(' ')
        colors[color] = int(amount_raw)

      game_set = GameSet(**colors)
      sets.append(game_set)

    games.append(Game(id=game_id, sets=sets))

  return games


def is_game_valid(game: Game, bag: Bag):
  for game_set in game.sets:
    out_of_range = game_set.red > bag.red \
      or game_set.green > bag.green \
      or game_set.blue > bag.blue

    if out_of_range:
      return False

  return True


def find_valid_games(games, bag):
  valid_games = []

  for game in games:
    if is_game_valid(game, bag):
      valid_games.append(game)

  return valid_games


def sum_game_ids(games: List[Game]):
  sum = 0
  for game in games:
    sum += game.id
  return sum


def find_min_playable_set(game: Game):
  colors = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for game_set in game.sets:
    colors['red'] = max(colors['red'], game_set.red)
    colors['green'] = max(colors['green'], game_set.green)
    colors['blue'] = max(colors['blue'], game_set.blue)

  return GameSet(**colors)


def game_set_power(game_set: GameSet):
  return game_set.red * game_set.green * game_set.blue


def sum_game_set_powers(valid_games: GameSet):
  sum = 0
  for game in valid_games:
    min_playable_set = find_min_playable_set(game)
    sum += game_set_power(min_playable_set)

  return sum


if __name__ == '__main__':
  bag = Bag(red=12, green=13, blue=14)

  with open('./input.txt') as f:
    games = parse_games(f.readlines())
    valid = find_valid_games(games, bag)
    answer_one = sum_game_ids(valid)
    print('First star answer is', answer_one)

    answer_two = sum_game_set_powers(games)
    print('Second star answer is', answer_two)