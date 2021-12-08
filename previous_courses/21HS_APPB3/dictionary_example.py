eng2de = {}
eng2de["one"] = "eins"
eng2de["two"] = "zwei"


# print(eng2de['two'])

inventory = {
    "fruits": {"apples": 340, "bananas": 120},
    "vegetables": {"tomatoes": 12, "potatoes": 400},
}

for product, store in inventory.items():
    print(product, store)
    for item, in_store in store.items():
        print(f"There are {in_store} {item} in store")
