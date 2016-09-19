#  File: Boxes.py

#  Description: This program will find the largest subset of boxes that nest inside each 
#  other starting with the inner most box to the outer most box

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 2, 2016

#  Date Last Modified: March 2, 2016

nestedBoxes = [] #global variable that stores all of the boxes

def All_Box():
    dimensions = [] 
    # Opens text file
    in_file = open("boxes.txt","r")

    # Reads number of boxes
    num_boxes = int(in_file.readline()) 

    # Parses through nestedBoxes list 
    for i in range(0, num_boxes):
        indiv_box = []
        box_dimension = (in_file.readline()).split()
        for entry in box_dimension:
            indiv_box.append(int(entry))
        indiv_box.sort()
        dimensions.append(indiv_box)
    sorted_box = dimensions.sort(key = lambda column: (column[2],column[1],column[0])) #Sorts the 2d list
    in_file.close()
    return dimensions

# Finds the correct order of the nested boxes
def nesting_boxes(box1, box2, lowwer):
    upper = len(box1)
    if (lowwer == upper):
        nestedBoxes.append(box2) 
        return
    else:
        c = box2[:]
        box2.append(box1[lowwer])
        nesting_boxes(box1, c, lowwer + 1)
        if len(box2) > 1:
            if box2[len(box2)-1][0] > box2[len(box2)-2][0] and box2[len(box2)-1][1] > box2[len(box2)-2][1] and box2[len(box2)-1][2] > box2[len(box2)-2][2]:
                nesting_boxes(box1, box2, lowwer + 1)
        else:
            nesting_boxes(box1, box2, lowwer + 1)
        
def main():
    boxes_list = All_Box() 
    subset_boxes = []
    nesting_boxes (boxes_list, subset_boxes, 0)
    max_length = 1
    for box in nestedBoxes:
        if len(box) > max_length:
            max_length = len(box)

    # Sorts nested Boxes smallest to biggest
    nestedBoxes.sort()

    # Prints largest subset of nesting boxes
    if max_length >= 2:
        print("Largest Subset of Nesting Boxes")
        for boxes in nestedBoxes:
            if len(boxes) == max_length:
                for box in boxes:
                    print(box)
                print()
    else:
        print("No Nesting Boxes")
    
main()
