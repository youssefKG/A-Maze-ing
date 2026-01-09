

class CellGenerator:
    
    @classmethod
    def wall_generator(cls, hexa: int):
        bin_hexa = bin(hexa)[2:]
        i = len(bin_hexa)
        while i < 4:
            bin_hexa = "0" + bin_hexa
            i += 1
        north = True if bin_hexa[0] == '1' else False
        east = True if bin_hexa[1] == '1' else False
        south = True if bin_hexa[2] == '1' else False
        west = True if bin_hexa[3] == '1' else False
        return (north, east, south, west)

print(CellGenerator.wall_generator(4))
