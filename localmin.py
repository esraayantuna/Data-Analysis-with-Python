def localmin(a, low, high):
    mid = (low + high) // 2

    if mid == 0:
        return None

    if mid >= (len(a) - 1):
        return None

    xleft = a[mid-1]
    xmin= a[mid]
    xright = a [mid+1]

    # For xmin to be a local min, it should be smaller than the elements to its left and to its right
    if xmin < xleft and xmin < xright:
        return mid
    elif a[mid] > a[mid-1]:
        return localmin(a, low, mid-1)
    else:
        return localmin(a, mid+1, high)

a = [10, 8, 6, 4, 0, -2, 1, 3, 5, 7, 15]
localmin_index = localmin(a, 0, len(a) - 1)
if localmin_index is not None:
    print(localmin_index, a[localmin_index])
