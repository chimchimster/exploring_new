import re

# Block 1
# _______

# text = 'Карта map и объект bitmap - это разные вещи'
# match = re.findall(r'\bmap\b', text)
# print(match)

# Block 2
# _______

# text = '(еда), беда, победа'
# match = re.findall(r'\(еда\)', text)
# print(match)

# Block 3
# _______
#
# text = 'Еда, беду, -5 55 победа'
# match = re.findall(r"\w", text, re.ASCII)
#
# print(match)

# Block 4
# _______
#
# text = "0xf, 0xa, 0x5"
# match = re.findall(r"0x[\da-fA-F]", text)
#
# print(match)