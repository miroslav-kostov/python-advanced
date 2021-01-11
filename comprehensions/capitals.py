country, capital = input().split(", "), input().split(", ")
dict_capitals = {country[x]: capital[x] for x in range(len(country))}
result = list(print(f"{pair} -> {dict_capitals[pair]}") for pair in dict_capitals)
