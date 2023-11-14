def make_snippet(str):
    if len(str) <=5:
        return str[0:5]
    else:
        return '...'

print(make_snippet('James-Leigh'))