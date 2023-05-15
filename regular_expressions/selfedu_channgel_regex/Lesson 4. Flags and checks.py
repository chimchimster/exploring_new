import re

# Block 1
# _______

# text = "подоходный налог, доход"
# match = re.findall(r'\b(?:прибыль|обретение|доход)\b', text)
# print(match)

# text = """<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Уроки по Python</title>
# </head>
# <body>
# <script type="text/javascript">
# let o = document.getElementById('id_div');
# console.log(obj);
# </script>
#     <p align=center>Hello World!</p>
# </body>
# </html>"""

# match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
# print(match)

# match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE)
# print(match)

# match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.MULTILINE|re.VERBOSE)
# print(match)

# text = "Python, python, PYTHON"
# match = re.findall(r"(?im)python", text)
# print(match)