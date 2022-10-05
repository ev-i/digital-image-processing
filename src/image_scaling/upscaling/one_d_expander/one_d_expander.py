def one_d_expander(array, scale_factor):
    expanded = [None] * int(len(array)*scale_factor)
    for j in range(len(expanded)):
        if j % scale_factor == 0:
            expanded[j]=array[int(j / scale_factor)]
    return expanded


