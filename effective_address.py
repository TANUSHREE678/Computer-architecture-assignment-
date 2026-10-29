# Program to calculate Effective Address

address = 200
R1 = 40

memory = {
    200: 500,
    240: 900
}

# a) Immediate Addressing
operand = 25
print("a) Immediate Addressing")
print("Rule: Operand = Given value")
print("Operand =", operand)

# b) Direct Addressing
EA = address
print("\nb) Direct Addressing")
print("Rule: EA = Address field")
print("Effective Address =", EA)
print("Operand =", memory[EA])

# c) Indirect Addressing
EA = memory[address]
print("\nc) Indirect Addressing")
print("Rule: EA = Memory[Address field]")
print("Effective Address =", EA)

# d) Indexed Addressing
EA = address + R1
print("\nd) Indexed Addressing")
print("Rule: EA = Address field + R1")
print("Effective Address =", EA)
print("Operand =", memory[EA])
