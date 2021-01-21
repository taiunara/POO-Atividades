def printDecimal(x=0):
    print("   {}".format(int(x)), end=" ")


def printOctal(x):
    print("     {}".format(oct(x)[2:]), end=" ")

def printHexadecimal(x):
    print("       {}".format(hex(x)[2:]), end=" ")


def printBinario(x):
    print("        {}".format(bin(x)[2:]), end=" ")


def imprimirtabela():
  print("Decimal Octal Hexadecimal Binário")
  print("------- ----- ----------- -------")
  for x in range(301):
      printDecimal(x),
      printOctal(x),
      printHexadecimal(x),
      printBinario(x),
      print("\n")


imprimirtabela()
