def longest_series_of_neighbours(items):
    if not items:
        return 0

    max_length = 1
    current_length = 1

    # Loop from the second item to the end
    for i in range(1, len(items)):
        # Check if the current item is a neighbor to the previous item
        if abs(items[i] - items[i - 1]) == 1:
            current_length += 1
        else:
            # The streak broke; reset the counter to 1
            current_length = 1
        
        # Keep track of the highest streak we've ever seen
        if current_length > max_length:
            max_length = current_length

    return max_length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))  # Expected Output: 4 (for [7, 6, 5, 6] or [3, 4] or [1, 0])