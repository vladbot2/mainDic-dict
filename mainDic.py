# def count(string):
#     dict = {}
#     for char in string:
#         if char in dict:
#             dict[char] += 1
#         else:
#             dict[char] = 1
#     return dict

# string = "hello world"
# print(count(string))


#2
# def dicts(dict1, dict2):
#     dict = {dict1}
#     for key, value in dict2.items():
#         if key in dict:
#             if not isinstance(dict[key], list):
#                 dict[key] = [dict[key]]
#             dict[key].append(value)
#         else:
#             dict[key] = value
#     return dict

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# print(dicts(dict1, dict2))


#3
# def dict(dict):
#     inverted_dict = {v: i for i, v in dict.items()}
#     return inverted_dict

# unique_dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict)

#4
# def keys(d, descending=False):
#     dict = dict(sorted(d.items(), key=lambda item: item[0], reverse=descending))
#     return dict

# d = {'b': 2, 'c': 3, 'a': 1}
# print(keys(d))
# print(keys(d, descending=True))


#5
# def value(d, substring):
#     return [i for i, v in d.items() if substring in v]

# d = {'a': 'hello', 'b': 'world', 'c': 'hello world'}
# substring = 'world'
# print(value(d, substring))


#6
# def dict(list):
#     return dict(list)

# list = [(1, 'a'), (2, 'b'), (3, 'c')]
# print(dict(list))

#7
# def element(list):
#     dict = {}
#     for i, v in list:
#         if i in dict:
#             dict[i].append(v)
#         else:
#             dict[i] = [v]
#     return dict

# list = [(1, 'a'), (2, 'b'), (1, 'c')]
# print(element(list))


#8
# def values(dict1, dict2):
#     dict = {i: dict1 + dict2 for i in set(dict1) for i in set(dict2)}
#     return dict

# dict1 = {'a': [1, 2], 'b': [3, 4]}
# dict2 = {'a': [5], 'b': [6, 7]}
# print(values(dict1, dict2))

#9
# def keys(d):
#     key = min(d, key=d)
#     key = max(d, key=d)
#     return key, key

# d = {'a': 1, 'b': 2, 'c': 3}
# print(keys(d))

#10
# def dicts(d):
#     sum = sum(sum(inner) for inner in d)
#     return sum

# d = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
# print(dicts(d))







