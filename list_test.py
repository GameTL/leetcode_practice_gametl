# import timeit

# # Setup code: create a 20x20 2D list
# setup_code = '''
# my_2d_list = [[j for j in range(20)] for i in range(20)]
# '''

# # Code snippet using range(len())
# test_code_range = '''
# for i in range(len(my_2d_list)):
#     for j in range(len(my_2d_list[i])):
#         _ = my_2d_list[i][j]
# '''

# # Code snippet using enumerate()
# test_code_enumerate = '''
# for i, row in enumerate(my_2d_list):
#     for j, value in enumerate(row):
#         _ = value
# '''

# # Measure execution time
# time_range = timeit.timeit(setup=setup_code, stmt=test_code_range, number=1)
# time_enumerate = timeit.timeit(setup=setup_code, stmt=test_code_enumerate, number=1)

# print(f"Using range(len()): {time_range * 1000:.4f} ms")
# print(f"Using enumerate(): {time_enumerate * 1000:.4f} ms")
