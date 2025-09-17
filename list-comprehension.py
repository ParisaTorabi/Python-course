my_list = [0, 0.45, 9, -1]

new_list = [2 * n for n in my_list]

print(new_list)


# %%

a = int(input())

result = "even" if a % 2 == 0 else "odd"

print(result)

# %% put the two together

my_list = [0, 0.45, 9, -1]

new_list = [n for n in my_list if n % 2 == 0]

print(new_list)
# %%

int_list = [1, 3, 6, 7, 9, 10, 23]

oddities = ["even" if n % 2 == 0 else "odd" for n in int_list]
print(oddities)
