# Example solution: dictionary methods
data = {"a": 1, "b": 2, "c": 3}
print("Keys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())
print("get b:", data.get("b"))
print("get z:", data.get("z"))
data.update({"b": 20, "d": 4})
print("After update:", data)
removed = data.pop("a")
print("Removed:", removed)
print("After pop:", data)