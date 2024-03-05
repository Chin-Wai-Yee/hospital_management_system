# Give a proper name for the decorator that contain this funct
def idValidation(length : int, n : int):
    # This function check if the id is valid
    # The id must be a string with the length
    # The first n characters must be letters and the rest must be numbers
    def isValidId(id : str) -> bool:
        
        # Check if id length is correct
        if len(id) != length:
            return False

        # Check if the first n characters are letters
        for i in range(n):
            if not id[i].isalpha():
                return False
        
        # Check if the rest of the characters are numbers
        for i in range(n, length):
            if not id[i].isdigit():
                return False

        return True
    
    return isValidId

def addrValidation(address : str):
    addr = [a.strip() for a in address.split(",")]
    if len(addr) != 5:
        return False
    if not addr[0].isdigit():
        return False
    
    return True

# Test
if __name__ == "__main__":
    validation = idValidation(5, 3)
    print(validation("abc12")) # True
    print(validation("abc123")) # False
    print(validation("22abd")) # False
    print(validation("ac123")) # False