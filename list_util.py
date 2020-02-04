
def stripArray(array):
    stripArray = []
    for item in array:
        stripArray.append(item.strip())
    return stripArray

 
def maxLength(array):
    length = 0
    for item in array:
        if len(item) > length:
            length = len(item)
    return length        
   