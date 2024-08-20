from collections import OrderedDict

n = int(input())
voting_results = OrderedDict()

for i in range(n):
    country = input()
    voting_results[country] = voting_results.get(country, 0) + 1

for country in sorted(voting_results.keys()):
    print(f"{country}: {voting_results[country]}")