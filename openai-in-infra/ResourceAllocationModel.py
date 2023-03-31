class Resource:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.allocated = 0

    def allocate(self, amount):
        if amount <= self.capacity - self.allocated:
            self.allocated += amount
            return True
        else:
            return False

    def deallocate(self, amount):
        if amount <= self.allocated:
            self.allocated -= amount
            return True
        else:
            return False


class ResourceManager:
    def __init__(self):
        self.resources = {}

    def add_resource(self, name, capacity):
        if name in self.resources:
            raise ValueError("Resource with name '{}' already exists".format(name))
        self.resources[name] = Resource(name, capacity)

    def allocate_resources(self, resource_allocations):
        for name, amount in resource_allocations.items():
            if name not in self.resources:
                raise ValueError("Unknown resource: '{}'".format(name))
            if not self.resources[name].allocate(amount):
                raise ValueError("Not enough capacity for resource '{}'".format(name))

    def deallocate_resources(self, resource_allocations):
        for name, amount in resource_allocations.items():
            if name not in self.resources:
                raise ValueError("Unknown resource: '{}'".format(name))
            if not self.resources[name].deallocate(amount):
                raise ValueError("Trying to deallocate more resources than allocated for '{}'".format(name))


# Example usage:
if __name__ == "__main__":
    rm = ResourceManager()
    rm.add_resource("CPU", 8)
    rm.add_resource("Memory", 16)

    # Allocate resources:
    rm.allocate_resources({
        "CPU": 3,
        "Memory": 8
    })

    # Try to allocate too much CPU:
    try:
        rm.allocate_resources({
            "CPU": 6,
            "Memory": 4
        })
    except ValueError as e:
        print(e)  # Not enough capacity for resource 'CPU'

    # Deallocate resources:
    rm.deallocate_resources({
        "CPU": 1,
        "Memory": 4
    })
