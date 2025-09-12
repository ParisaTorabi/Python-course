"""A store offers special discounts to its customers. The discount rules are as follows:

If the purchase amount is more than 50,000 Tomans, a 20% discount is applied.

If the purchase amount is between 20,000 and 50,000 Tomans, a 10% discount is applied.

If the purchase amount is less than 20,000 Tomans, no discount is applied.

Write a program that receives the purchase amount from the user and displays the final amount.
"""

if __name__ == "__main__":
    purchase_amount = int(input("Enter your purchase amount:"))
    if purchase_amount > 50_000:
        print(0.8 * purchase_amount)
    elif 20_000 <= purchase_amount < 50_000:
        print(0.9 * purchase_amount)
    else:
        print(purchase_amount)
