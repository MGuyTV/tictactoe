array = [["-1", "-1", "-1"], ["-1", "-1", "-1"], ["-1", "-1", "-1"]]




def run():
	boolean = True
	while(boolean)

		response = input()
		

#There is probably a way to do the below better, but it's good for now
def checkWin():
	#Horizontal rows
	if array[0][0] == "x" or array[0][0] == "O" and array[0][1] == "X" or array[0][1] == "O" and array[0][2] == "X" or array[0][2] == "O":
		return True

	if array[1][0] == "x" or array[1][0] == "O" and array[1][1] == "X" or array[1][1] == "O" and array[1][2] == "X" or array[1][2] == "O":
		return True

	if array[2][0] == "x" or array[2][0] == "O" and array[2][1] == "X" or array[2][1] == "O" and array[2][2] == "X" or array[2][2] == "O":
		return True


	#vertical columns
	if array[0][0] == "x" or array[0][0] == "O" and array[1][0] == "X" or array[1][0] == "O" and array[2][0] == "X" or array[2][0] == "O":
		return True

	if array[1][0] == "x" or array[1][0] == "O" and array[1][1] == "X" or array[1][1] == "O" and array[1][2] == "X" or array[1][2] == "O":
		return True

	if array[2][0] == "x" or array[2][0] == "O" and array[2][1] == "X" or array[2][1] == "O" and array[2][2] == "X" or array[2][2] == "O":
		return True


	#Criss-cross cases
	if array[0][0] == "x" or array[0][0] == "O" and array[1][1] == "X" or array[1][1] == "O" and array[2][2] == "X" or array[2][2] == "O":
		return True

	if array[0][2] == "x" or array[0][2] == "O" and array[1][1] == "X" or array[1][1] == "O" and array[2][0] == "X" or array[2][0] == "O":
		return True
	return False
