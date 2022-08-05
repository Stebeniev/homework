#Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.
year_of_birth = [1982, 1982, 2004, 2010, 2013]
family_members = ['Dmitriy', 'Maria', 'Andrey', 'Yaroslava', 'Matvey']
s = zip(year_of_birth, family_members)
print(list(s))
