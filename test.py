# function to create uniqe combinations of a nested list
abc = [[1,2,3],[4,5,6],[7,8,9]]
def uniqe_combinations(arr):
    # create a list to hold all the uniqe combinations
    result = []
    # create a list to hold the current combination
    current = []
    # loop through all the elements in the list
    for i in range(len(arr)):
        # loop through all the elements in the sublist
        for j in range(len(arr[i])):
            # add the element to the current list
            current.append(arr[i][j])
            # add the current list to the result list
            result.append(current[:])
            # remove the last element from the current list
            current.pop()
    return result
test = uniqe_combinations(abc)
print(test)