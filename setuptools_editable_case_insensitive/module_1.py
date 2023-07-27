print(f"Hello from {__name__}!")

if __name__.endswith("module_1"):
    print("Hooray, I was imported with the correct name!")
else:
    print("Oh no, I was imported with the wrong name!")


print(f"\t{__name__=}")
print(f"\t{__file__=}")
print()
