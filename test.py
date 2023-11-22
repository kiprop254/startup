# def my_function(x=[]):
#     x.append(10)
#     return x

# a = my_function()
# b = my_function()
# c = my_function([])

# print(a, 'a')
# print(b, 'b')
# print(c, 'c')



# # def transform(data, my_func):
# #     return [my_func(item) for item in data]

# # values = [2, 4, 6, 8]
# # result = transform(values, lambda x : x // 2)

# # print(result) 

import math
def calculate1(numbers):
    return math.sqrt(sum(x*x for x in numbers if x ))