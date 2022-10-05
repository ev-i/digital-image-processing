def two_d_expander(array, scale_factor):
    # expanded = [[None] * int(len(array)*scale_factor)]* int(len(array[0])*scale_factor)    ### WRONG! REUSES STRINGS AS OBJECTS
    expanded = [[None for _ in range (int(len(array[0])*scale_factor))] for _ in range (int(len(array)*scale_factor))]
    for expanded_row in range(len(expanded)):
        for expanded_column in range(len(expanded[expanded_row])):
            # print('---------------------')
            # print('expanded_row ' + str(expanded_row))
            # print('expanded_column ' + str(expanded_column))
            if expanded_row % scale_factor == 0 and expanded_column % scale_factor == 0:
                # print(expanded_row % scale_factor == 0 and expanded_column % scale_factor == 0)
                expanded[expanded_row][expanded_column] = array[int(expanded_row / scale_factor)][int(expanded_column / scale_factor)]
                # print('int(expanded_row / scale_factor) ' + str(int(expanded_row / scale_factor)))
                # print('int(expanded_column / scale_factor) ' + str(int(expanded_column / scale_factor)))
                # print('array[][]: ' + str(array[int(expanded_row / scale_factor)][int(expanded_column / scale_factor)]))
                # print('expanded[][]: ' + str(expanded[expanded_row][expanded_column]))
    return expanded






