from vehicle import ElectricVehicle, SportsCar
from bintree import BinaryTree

tree = BinaryTree()

vehicles = [
    ElectricVehicle("Tesla", "Model 3", 85.0, 75, 500),
    SportsCar("BMW", "M3", 90.0, 480, 3.9),
    ElectricVehicle("Ford", "F-150 Lightning", 80.0, 120, 400),
    SportsCar("Porsche", "911", 95.0, 520, 3.2)
]

for v in vehicles:
    tree.insert(v)

print("In-order traversal:")
for v in tree:
    print(v)

tree.serialize("vehicles.pkl")
print("\nTree serialized successfully.")
