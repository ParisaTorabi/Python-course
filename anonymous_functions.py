# %% On map


def power_2(x):
    return x**2


a = [3, 4, 5, 6]
a_power_2 = map(power_2, a)
print(a_power_2)  # an object!
print(list(a_power_2))  # calculated!


# %% Anonymous function using lambda
a = [3, 4, 5, 8]
a_power_2 = map(lambda x: x**2, a)

print(list(a_power_2))


# %% On filter!


def is_decimal_number(x):
    return not isinstance(x, int)


my_list = [1, 2, 3, 4.5, 6.7, 8.9]
print(list(filter(is_decimal_number, my_list)))

# %% Using lambda:

my_list = [1, 2, 3, 4.5, 6.7, 8.9]
print(list(filter(lambda x: not isinstance(x, int), my_list)))

# %%
multiply = lambda x, y: x * y
print(multiply(3, 4))
