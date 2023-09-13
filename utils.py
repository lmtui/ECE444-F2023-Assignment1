class Utils:
    def reversed(number):
        str(number)[::-1]
        return int(number)

    def formatter(number):
        binary =  (bin(number)[2:])
        octal =  (oct(number)[2:])
        return binary, octal
