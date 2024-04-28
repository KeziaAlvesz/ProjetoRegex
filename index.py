import re

data = "2022-11-30"
padrao = r'(\d{4})-(\d{2})-(\d{2})'
resultado = re.sub(padrao, r'\3/\2/\1', data)
print(resultado)