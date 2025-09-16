# %%
# for loop on a list
my_list = [5, 3, 6, 8, 4, 0.5, 2.6]

for item in my_list:
    if item % 2 == 0:
        print(item)
    else:
        print(f"{item} is odd")

# %%
# for loop on string
for c in "Programming is fun":
    print(c)

# %%
# for loop on tuples

my_tuple = (1, 6, [3], "Parisa", 4.5)

for item in my_tuple:
    print(f"item tuple: {item}")
# %%

People = (("Parisa", 31), ("Jadi", 45), ("Mr.X", 120))

for name, age in People:
    print(f"{name} is {age} years old.")
# %%
# on dictionaries


People = {"Jadi": (45, 180), "Sina": (30, 171), "Parisa": (31, 162)}


for person in People:
    print(person)  # print keys

for person in People:
    print(person, People[person])

for person in People:
    print(person, People[person][0])  # print age

# %%

for person in People.items():
    print(person)  # the key,value tuples

for person, data in People.items():
    print(f"{person} -> age: {data[0]}, height: {data[1]}")  # the key,value tuples

for data in People.values():
    print(data)
# %%
# Exercise
"""A wizard has decided to increase the power of numbers by using a special spell! He chooses a number n and then does the following for n steps:

If the number is odd, double its value and subtract 1 unit.

If the number is even, halve its value.

The wizard performs this operation exactly n times.
📝 Input:

An integer n that specifies the number of steps (1 ≤ n ≤ 20).
An integer x that is the initial value (1 ≤ x ≤ 1000).

📤 Output: Finally, display the final value of x.
Input 1:

5
10

Output 1:

65"""

if __name__ == "__main__":
    n = int(input("insert number of steps, n:"))
    x = int(input("insert initial value, x:"))

    for _ in range(n):
        if x % 2 == 0:
            x = x / 2
        else:
            x = (2 * x) - 1

    print(f"Final value is {x}")
