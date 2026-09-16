class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine whether a partially filled Sudoku board is valid.

        Each row, column, and 3x3 sub-box may contain each digit from 1 to 9
        at most once. Empty cells, represented by ".", are ignored.

        A bitmask is used to track which digits have already appeared:
        - Bit 0 represents digit 1
        - Bit 1 represents digit 2
        - ...
        - Bit 8 represents digit 9

        For example, if digit 3 has appeared, bit 2 is set:
            mask |= (1 << 2)

        Args:
            board: A 9x9 Sudoku board containing digits "1"-"9" or ".".

        Returns:
            True if the board does not contain any duplicate digits in a
            row, column, or 3x3 sub-box; otherwise, False.
        """

        # Bitmasks for digits seen in each row, column, and 3x3 sub-box.
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                # Empty cells do not affect validity.
                if board[r][c] == ".":
                    continue

                # Convert the digit to a zero-based bit position.
                # Digit "1" maps to bit 0, digit "9" maps to bit 8.
                val = int(board[r][c]) - 1
                bit = 1 << val

                # Map the cell to one of the nine 3x3 sub-boxes.
                square_index = (r // 3) * 3 + (c // 3)

                # If the digit's bit is already set in any relevant
                # mask, the digit is duplicated.
                if bit & rows[r]:
                    return False
                if bit & cols[c]:
                    return False
                if bit & squares[square_index]:
                    return False

                # Mark the digit as seen in the row, column, and sub-box.
                rows[r] |= bit
                cols[c] |= bit
                squares[square_index] |= bit

        return True