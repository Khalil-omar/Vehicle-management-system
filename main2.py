from bintree import BinaryTree

tree = BinaryTree()
tree.deserialize("vehicles.pkl")

print("All vehicles (in-order):")
for v in tree:
    print(v)

print("\nVehicles with performance > 135:")
for v in tree.filter_by_performance(135):
    print(v)
