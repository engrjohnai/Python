

def object_with_beautiful_identity():
    for i in range(0, 10000):
        address = id(i)
        if address % 1000 == 888:
            return i
            
            
                         
object_with_beautiful_identity()