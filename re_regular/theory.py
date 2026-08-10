from re import *

data = "k t kait lev kat"
pattern = r"k.t"
matches = finditer(pattern, data)
print(*matches)

#metasimvoly
# . -rovno odin luboi simvol
# \d - lubaia cifra
# \D - lubaia ne cifra
# \s - luboi probelnii simvol
# \S - luboi ne prbelnii simvol
# \w - lubaia bukva cifra ili _

# diapazoni simvolov - []
# [02468] - rovno odin iz ukazannih simvolov
# [a-z] - vse malenkie bukvi
# [1-5A-K]
# ^ - iskluchenie simvolov
# [^02468] - nechetnie cifri

# kvantifikatori
# {m,n} kolichestvo povtorenii ot m do n
# + - hotuabi odno vhozhdenie
# * -luboe kolichestvo vhozhdenii
# ? - libo 0 libo 1 raz
# | - ili
# () - svuazivaet blok

from re import *

data = "+7 999 999 99 99 89999999999 79999999999"
pattern = r"(\+7|7|8)(\s?\d{3}){2}(\s?\d{2}){2}"

# matches = finditer(pattern, data)
# for i in matches:
#     print(i.group())
#
# matches = [match.group() for match in finditer(pattern, data)]
# print(matches)

data = "https://test.ru http://test.ru https://telemost.yandex.ru/"
pattern = r"(https|http)://\D+"
matches = [match.group() for match in finditer(pattern, data)]
print(matches)

data = "aleksandr@gmail.com pavel431@mail.ru vladislav@ug.s"
pattern = r"\S+@\S+\.(ru|com)"
matches = [match.group() for match in finditer(pattern, data)]
print(matches)


