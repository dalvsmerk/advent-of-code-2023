def detect_adjacent_symbols(x: int, y: int, schematics: list[str]):
  test = lambda s: s != '.' and not s.isdigit() and not s.isspace()
  left, right, up, down, \
    top_left, top_right, bottom_left, bottom_right = [False] * 8

  if x > 0:
    left = test(schematics[y][x - 1])
  if x < len(schematics[y]) - 1:
    right = test(schematics[y][x + 1])
  if y > 0:
    up = test(schematics[y - 1][x])
  if y < len(schematics) - 1:
    down = test(schematics[y + 1][x])

  if x > 0 and y > 0:
    top_left = test(schematics[y - 1][x - 1])
  if x < len(schematics[y]) - 1 and y > 0:
    top_right = test(schematics[y - 1][x + 1])
  if x > 0 and y < len(schematics) - 1:
    bottom_left = test(schematics[y + 1][x - 1])
  if x < len(schematics[y]) - 1 and y < len(schematics) - 1:
    bottom_right = test(schematics[y + 1][x + 1])

  return left or right or up or down or \
    top_left or top_right or bottom_left or bottom_right

def find_engine_part_numbers(schematics: list[str]):
  numbers = []

  for y, line in enumerate(schematics):
    digits = []
    has_adjacent_symbol = False

    for x, symbol in enumerate(line):
      has_adjacent_symbol = has_adjacent_symbol or detect_adjacent_symbols(x, y, schematics)
      is_digit = symbol.isdigit()

      if is_digit:
        digits.append(symbol)
      else:
        if len(digits) > 0 and has_adjacent_symbol:
          part_number = int(''.join(digits))
          numbers.append(part_number)

        digits = []
        has_adjacent_symbol = False

      if y > 73 and y < 75:
        print((x, y), schematics[y][x], is_digit, has_adjacent_symbol)

  print(numbers)

  return numbers


def sum_part_numbers(part_numbers):
  sum = 0
  for part_number in part_numbers:
    sum += part_number
  return sum


if __name__ == '__main__':
  with open('input.txt') as f:
    lines = f.readlines()
    part_numbers = find_engine_part_numbers(lines)
    answer_one = sum_part_numbers(part_numbers)
    print('First star answer is', answer_one)