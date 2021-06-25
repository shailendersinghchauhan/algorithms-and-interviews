def definition():
    print("list() - list stores a series of items in a particular order. You access items using an index, or within a loop.\n        you can have different data types in list, sublist")
    print("dict() - Dictionaries store connections between pieces of information. Each item in a dictionary is a key-value pair")
    print("tuple() - Tuples are similar to lists, but the items in a tuple can't be modified. \n       But we if element is mutable then we can modify elemement. \n       Tuples can be reassigned")
    print("set() - The order of elements in a set is undefined. You can add and delete elements of a set,\n       You can iterate the elements of the set, you can perform standard operations on sets (union, intersection, difference).\n        Set contains unique values where as list don't\n       Elements are immutable but set itself is mutable")
    print("      - A set is a collection which is both unordered and unindexed \n Sets are used to store multiple items in a single variable \n Set items are unordered, unchangeable, and do not allow duplicate values.")
def list():
    bikes = ['trek', 'redline', 'giant']
    for bike in bikes: print(bike)
    bikes.append('trek')
    bikes.append('redline')
    bikes.append('giant')
    #for bike in bikes: print(bike)
    if 'shailender' in bikes:
        print("shailender is in list")
    a = bikes.count('trek')
    print(a)
    print("Count is:{0}".format(bikes.count('trek')))
    print("Lenght is:{0}".format(len(bikes)))
    print("Index value is:{0}".format(bikes.index('trek')))
    bikes.sort(reverse=True)
    print("Softed list:{0}".format(bikes))
    print("---List End----")

def dict():
    pass
    alien = {'color': 'green', 'points': 5}
    fav_numbers = {'eric': 17, 'ever': 4}
    for name, number in fav_numbers.items(): print(name + ' loves ' + str(number))

    print("---Dict End----")
def tuple():
    pass
    dimensions = (1920, 1080)

    print("---Tuple End----")
def set():
    #pass
    set1 = {1,2,3,6,10}
    print("--- Set End----")

def main():
    print("In main")

if __name__ == "__main__":
    definition()
    list()
    dict()
    tuple()
    set()