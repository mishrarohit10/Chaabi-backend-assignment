def sorting(list,sort_by):
    return (sorted(list, key=lambda x: x[sort_by]))

list = [
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
]

sortBy = "fruit"

print(sorting(list,sortBy))


