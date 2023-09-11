class Utils:
    @staticmethod
    def reversed(number):
        return int(str(number)[::-1])

    @staticmethod
    def formatter(number):
        binary = bin(number)[2:]
        octal = oct(number)[2:]
        return {
            "binary": binary,
            "octal": octal
        }
