

def bubbleSort(inputArray):

    # Copy the array so we are not messing up any data
    workingArray = inputArray.copy()
    length = len(inputArray)

    for i in range(length -1):
        for j in range(length -1 - i):
            leftN = workingArray[j]
            rightN = workingArray[j+1]

            if(leftN > rightN):
                workingArray[j] = rightN
                workingArray[j+1] = leftN

    return workingArray


def main():
    arr1 = [2,3,4,23,9,443,856,343,48,2,1,0,34,65,98,38,23,12]

    arr2 = bubbleSort(arr1)

    print(arr1)
    print(arr2)

if __name__ == "__main__":
    main()