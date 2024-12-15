import requests

b = "\033[92mdeveloper: t.me/wexquix\nkanal: t.me/wexquixPython"
print(b)
a = "https://api.ipify.org"
response = requests.get(a)
s = response.text
print('\n')
print(f'\033[96mip adres: {s}')
