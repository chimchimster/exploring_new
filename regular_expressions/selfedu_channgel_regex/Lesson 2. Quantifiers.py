import re

# Block 1
# _______

# text = "Google, Gooogle, Goooooogle"
# match = re.findall(r'o{2,5}?', text)
# print(match)

# Block 2
# _______

# text = "Google, Gooogle, Goooooogle"
# match = re.findall(r"Go{,4}gle", text)
# print(match)

# Block 3
# _______

# text = "89123456789"
# match = re.findall(r"8\d{10}", text)
# print(match)

# Block 4
# _______

# text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
# match = re.findall(r"(\w+)\s*=\s*([^;]+)", text)
# print(match)

# Block 5
# _______

# text = "<p>Картинка <img alt='картинка' src='bg.jpg'> а тексте</p>"
# match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)
# print(match)