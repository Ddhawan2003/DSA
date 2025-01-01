class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or the string length is less than numRows, return the original string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list to hold the rows
        rows = ["" for _ in range(numRows)]

        # Variables to track the current row and direction
        current_row = 0
        going_down = False

        # Iterate through the characters in the string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char

            # If we are at the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Update the current row based on the direction
            current_row += 1 if going_down else -1

        # Combine all rows to form the final string
        return "".join(rows)