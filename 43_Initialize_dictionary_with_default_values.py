employs = ['kelly', 'emma']
defults = {"designation": "developer", "salary": 8000}

p = dict.fromkeys(employs, defults)

print(p)

print(p["kelly"])