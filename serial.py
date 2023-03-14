"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Class initializer which creates serial generator beginning from start which is an int"""
        self.start, self.current = start, start
    
    def __repr__(self):
        return f"<Test start: {self.start}>"
        
    def generate(self):
        """Class method which generates the next integer increasing by 1 from start which is an int"""
        self.current += 1
        return self.current
        
    def reset(self):
        """Class method which returns the generator the next back to the initial starting point"""
        self.current = self.start

if __name__ == "__main__":
    generator = SerialGenerator(start=1000)
    
    [print(generator.generate()) for i in range(10)]
    # 1001
    # 1002
    # 1003
    # 1004
    # 1005
    # 1006
    # 1007
    # 1008
    # 1009
    # 1010

    generator.reset()
    print(generator.generate())
    # 1001

# print(SerialGenerator serial = SerialGenerator(start=100))