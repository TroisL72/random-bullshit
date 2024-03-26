z = 13
for x in range(0, z):
    arr = []
    count_one = 0
    for y in range(0, z):
        dap = (x**y)%z
        """
        if dap == 1:
            count_one += 1
            if count_one == 2:
                break
        """
        print(f"x: {x}")
        print(f"y: {y}")
        arr.append(dap)
        arr.sort()
        
    print(f"Element {x}: {arr}")