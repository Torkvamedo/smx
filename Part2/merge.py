def merge(right, left, result):
    result.append((left if left[0] < right[0] else right).pop(0))
    return merge(right=right, left=left, result=result) if left and right else result+left+right

merge_sort = (lambda arr: arr if len(arr) == 1 else merge(merge_sort(arr[len(arr)/2:]),
                                                          merge_sort(arr[:len(arr)/2]), []))

