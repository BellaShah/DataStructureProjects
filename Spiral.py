def make_Spiral(dimension):
	#initialize variables
	spiral = []
	#dim and dim count track the squares in the spiral
	dim = dimension
	#dim2 creates the bottom half of the spiral
	dim2 = (dim // 2 + 1)
	dim_count = dim - 1

	#fills in number of rows to be made
	for i in range (dim):
		a = []

		#fills in spiral points that are not part of odd square sequence on the left side
		if (i < dim2):
			for k in range (i):
				if i == 0:
					break
				else:
					a.append(spiral[i-1][k] - 1)

		#fills in middle odd square spiral points
		for j in range (dim):
			#fills in spiral points part of odd square sequence
			a.append((dim * dim) - (dim_count))
			dim_count -= 1

		#fills in top right portion of spiral
		if (i < dim2):
			for k in range (i, 0, -1):
				if i == 0:
					break
				if k == i:
					a.append(a[-1] +1)
				else:
					a.append(spiral[i-1][-k] + 1)


		#fills in bottom left portion of spiral
		if (i >= dim2):
			for k in range(i + dim_count):
				a.append(spiral[i-1][k] - 1 )
			

		#fill in the middle bottom, even square sequence
		if (i >= dim2):
			for x in range(1, dim -1, -1):
				a.append(dim_count * dim_count + x)

		#fills in bottom right portion of spiral
		if (i >= dim2):
			for k in range(i + dim_count, 0, -1):
				a.append(spiral[i-1][-k] + 1)

		#decrease the odd square number for the next row's calculation
		dim -= 2
		#decrease the dimension counter so that the first number in the new odd square sequence is subtracted by the correct amount
		dim_count = dim - 1

		#add list a to the spiral
		spiral.append(a)

	return(spiral)	

def main():
	#open the file, read the basic dimension and target
	spiral_Input = open("./spiral.txt", 'r')
	dimension = int(spiral_Input.readline().strip())
	target = int(spiral_Input.readline().strip())
	spiral_Input.close()

	#check that the dimension is odd, increment if not
	if (dimension % 2 != 1):
		dimension += 1

	#check if the target number is in the spiral of given dimension
	if (target < 1) or (target > dimension**2):
		print('Number not in Range.')
		return

	#create spiral
	spiral = make_Spiral(dimension)

	#test if the target number is on the edge 
	for row in spiral:
		if (target == row[-1] or target == row[0]):
			print ('Number on Outer Edge.')
			return
	if ((target in spiral[0]) or (target in spiral[-1])):
		print ('Number on Outer Edge.')
		return

	#output
	for i in range(len(spiral)):
		for j in range(len(spiral[i])):
			if target == spiral[i][j]:
				cen_col = j
				cen_row = i
				
	#assign variables for grid output
	top_l = spiral[cen_row - 1][cen_col - 1]
	top_m = spiral[cen_row - 1][cen_col]
	top_r = spiral[cen_row - 1][cen_col + 1]
	mid_l = spiral[cen_row][cen_col - 1]
	mid_m = spiral[cen_row][cen_col]
	mid_r = spiral[cen_row][cen_col + 1]
	bot_l = spiral[cen_row + 1][cen_col - 1]
	bot_m = spiral[cen_row + 1][cen_col]
	bot_r = spiral[cen_row + 1][cen_col + 1]

	print (str(top_l) + " " + str(top_m) + " " + str(top_r))
	print (str(mid_l)+ " " + str(mid_m) + " " +  str(mid_r))
	print (str(bot_l) + " " +  str(bot_m) + " " +  str(bot_r))

main()