#!/usr/bin/python3

def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        # Return an empty list if n is not a positive integer
        return []

    # Initialize an empty list to store the rows of Pascal's Triangle
    triangle = []

    # Iterate through each row from 0 to n-1
    for i in range(n):
        # Create a new row with i + 1 elements, all initialized to 1
        row = [1] * (i + 1)

        # Check if the current row is not one of the first two rows
        if i > 1:
            # Iterate through the interior elements of the row
            for j in range(1, i):
                # Calculate the interior elements by summing elements from the previous row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the current row to the triangle list
        triangle.append(row)

    # Return the final Pascal's Triangle
    return triangle