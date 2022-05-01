test = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [None]]
# function that returns every first sub element of a nested array
def get_first_item_to_arr(arr):
    # create a new array
    new_arr = []
    # loop through the array
    for i in range(len(arr)):
        # add the first element to the new array
        # if arr[i][0] is empty
        if arr[i] == [None]:
            new_arr.append(None)
        else:
            new_arr.append(arr[i][0])
    return new_arr

testy = get_first_item_to_arr(test)
print(testy)

