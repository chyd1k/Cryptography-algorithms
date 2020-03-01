"""Just don't look here"""


def main():
	try:
		polynom = list(map(int, input("Input coefficients: ").split(" ")))
	except Exception:
		print("You can type only numbers separated by space")
		return

	for i in polynom:
		if i < 0:
			print("You can't input negatives")
			return

	adapt = ""
	polynom.sort(reverse = True)
	polynom = polynom[1:]
	for i, p in enumerate(polynom):
		if p == 0:
			if i == 0:
				adapt += "ShiftRegister"
			else:
				adapt += " ^ ShiftRegister"
		else:
			if i == 0:
				adapt += f" (ShiftRegister >> {p})"
			else:
				adapt += f" ^ (ShiftRegister >> {p})"

	root = int(input("Input initial value for scrembler: "))
	count = int(input("How many bits to generate: "))

	code = f'''
def get_bits(root, count):
	
	ShiftRegister = root
	states = []
	
	for i in range(count):
	
		yield ShiftRegister & 0x01
		states.append(bin(ShiftRegister)[2:])
		ShiftRegister = (
			(
				(
					{adapt}
				) & 0x01
			) << {max(polynom)}) | (ShiftRegister >> 1)
			
	print("Register states:")
	for state in states:
		print(f"{{state:0>{{max([len(i) for i in states])}}}}")
	root = ShiftRegister
		
bits = " ".join(map(str, list(get_bits(root, {count}))))
print(bits)
	'''
	exec(code, globals(), locals())


if __name__ == "__main__":
	main()
	input()
