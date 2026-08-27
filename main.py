print("================================")
print("       THREE LAWS OF LOGIC")
print("================================")

statement = input("\nEnter a statement: ")
answer = input("Is it true? (yes/no): ").lower()

if answer == "yes":
    A = True
elif answer == "no":
    A = False
else:
    print("Please enter yes or no.")
    exit()



identity = (A == A)


non_contradiction = not (A and not A)


excluded_middle = A or not A

print("\n========== RESULTS ==========")

print("\n1. Law of Identity")
print("A = A")
print("Result:", identity)

print("\n2. Law of Non-Contradiction")
print("NOT (A AND NOT A)")
print("Result:", non_contradiction)

print("\n3. Law of Excluded Middle")
print("A OR NOT A")
print("Result:", excluded_middle)

print("\n=============================")

if identity and non_contradiction and excluded_middle:
    print("All three laws of logic are satisfied!")
else:
    print("There is a logical problem.")
