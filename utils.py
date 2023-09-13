class Utils:
    def reversed(number):
        str(number)[::-1]
        return int(number)

    def formatter(number):
        binary = int (bin(number)[2:])
        octal = int (oct(number)[2:])
        return binary, octal
