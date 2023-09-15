class Utils:
    @staticmethod
    def reversed(num):
        if not isinstance(num, int):
            raise TypeError("Input must be an integer, not a float")
        num_str = str(num)
        reversed_str = num_str[::-1]
        return int(reversed_str)  
    
    @staticmethod
    def formatter(num):
        if not isinstance(num, int):
            raise TypeError("Input must be an integer, not a float")
        binary_value = bin(num)[2:]
        octal_value = oct(num)
        return {"binary": binary_value, "octal": octal_value}
