import re


def findCalibrationValues(lines):
  p = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
  sum = 0

  word2digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }

  for line in lines:
    digits = p.findall(line)
    first = digits[0]
    last = digits[-1]

    digit_first = word2digit.get(first, first)
    digit_last = word2digit.get(last, last)

    value = digit_first + digit_last
    sum = sum + int(value)

  return sum


def test():
  test_lines = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
  ]

  assert findCalibrationValues(test_lines) == 281, 'Test failed!'


if __name__ == '__main__':
  test()

  with open('./input.txt') as f:
    sum = findCalibrationValues(f.readlines())
    print(sum)