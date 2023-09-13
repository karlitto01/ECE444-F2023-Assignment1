
class utils:
    @staticmethod
    def reversed(num):
        if isinstance(num, int):
            return int(str(num)[::-1])
        else:
            raise ValueError("Input must be an integer")

    @staticmethod
    def formatter(num):
        if isinstance(num, int):
            binary = bin(num)[2:]  # Convert to binary and remove '0b' prefix
            octal = oct(num)[2:]  # Convert to octal and remove '0o' prefix
            return binary, octal
        else:
            raise ValueError("Input must be an integer")
