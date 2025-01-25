def pascal_triangle(rows) :
    arr = [1]
    while True:
        if len(arr) is rows+1:
            break
        new_arr = [1]
        for count in range(0, len(arr) - 1):
            new_arr.append(arr[count] + arr[count+1])
        new_arr.append(1)
        arr = new_arr
    return arr
for n in range(0, 6):
    print(pascal_triangle(n))

            #       <- Output ->  
            #           [1]
            #           [1, 1]
            #           [1, 2, 1]
            #           [1, 3, 3, 1]
            #           [1, 4, 6, 4, 1]
            #           [1, 5, 10, 10, 5, 1]
