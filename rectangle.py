class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the length and width of the rectangle
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield length followed by width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Create a rectangle instance
rect = Rectangle(10, 5)

# Iterating over the instance
for dim in rect:
    print(dim)