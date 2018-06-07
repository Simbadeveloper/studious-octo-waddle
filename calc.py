

def add(x ,y):
    """Add Function"""
    return x + y

def subtract(x , y):
     """subtract Function"""
     return x - y
def multiply(x, y):
     """multiplyFunction"""
     return x*y

def divide(x, y):
     """divide Function"""
     if y==0:
        raise ValueError ('can not divide by zero!')
     return x/y