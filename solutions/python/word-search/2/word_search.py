class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.puzzle_word_length = len(puzzle[0])
        self.puzzle_row_number = len(puzzle)

    def search(self, word):
        # self.word = word

        def top_to_bottom_locate(word):

            for column in range(self.puzzle_word_length):
                sample_vertical_string = "".join(
                    [element[column] for element in self.puzzle]
                )

                if word in sample_vertical_string:
                    # Returning the first element and last element
                    first_letter_column_axis = last_letter_column_axis = column
                    first_letter_row_axis = sample_vertical_string.find(word)
                    last_letter_row_axis = (
                        sample_vertical_string.find(word) + len(word) - 1
                    )

                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        def bottom_to_top_locate(word):

            for column in range(self.puzzle_word_length):
                sample_vertical_string = "".join(
                    [element[column] for element in self.puzzle]
                )

                sample_reversed_vertical_string = sample_vertical_string[::-1]

                if word in sample_reversed_vertical_string:
                    # Returning the first element and last element
                    first_letter_column_axis = last_letter_column_axis = column
                    first_letter_row_axis = (
                        len(sample_vertical_string)
                        - sample_reversed_vertical_string.find(word)
                        - 1
                    )

                    last_letter_row_axis = len(sample_vertical_string) - (
                        sample_reversed_vertical_string.find(word) + len(word)
                    )

                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        def left_to_right_locate(word):

            for element in self.puzzle:
                sample_horizontal_string = element

                if word in sample_horizontal_string:
                    # first and last character value
                    index = sample_horizontal_string.find(word)
                    first_letter_column_axis = index
                    last_letter_column_axis = index + len(word) - 1

                    # the row value is constant and equal in each character of 'word'
                    first_letter_row_axis = last_letter_row_axis = self.puzzle.index(
                        element
                    )

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        def right_to_left_locate(word):

            for element in self.puzzle:
                sample_reversed_horizontal_string = element[::-1]

                if word in sample_reversed_horizontal_string:
                    # first and last character value
                    index = sample_reversed_horizontal_string.find(word)
                    first_letter_column_axis = (
                        len(sample_reversed_horizontal_string) - index - 1
                    )
                    last_letter_column_axis = len(sample_reversed_horizontal_string) - (
                        index + len(word)
                    )

                    # the row value is constant and equal in each character of 'word'
                    first_letter_row_axis = last_letter_row_axis = self.puzzle.index(
                        element
                    )

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        def top_left_to_bottom_right(word):

            # defining moving vector
            dx, dy = 1, 1

            for column_start in range(self.puzzle_word_length):
                sample_string_diagonal = ""
                row_init = 0
                column_init = column_start

                row, col = row_init, column_init

                while (row < self.puzzle_row_number) and (
                    col < self.puzzle_word_length
                ):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                if word in sample_string_diagonal:
                    # first and last character value
                    index = sample_string_diagonal.find(word)
                    first_letter_column_axis = column_init + index * dy
                    first_letter_row_axis = row_init + index * dx
                    last_letter_column_axis = first_letter_column_axis + len(word) - 1
                    last_letter_row_axis = first_letter_row_axis + len(word) - 1
                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)
                    return (first_point, second_point)

            for row_start in range(1, self.puzzle_row_number):
                sample_string_diagonal = ""
                row_init = row_start
                column_init = 0

                row, col = row_init, column_init

                while (row < self.puzzle_row_number) and (
                    col < self.puzzle_word_length
                ):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                if word in sample_string_diagonal:
                    # first and last character value
                    index = sample_string_diagonal.find(word)
                    first_letter_column_axis = column_init + index * dy
                    first_letter_row_axis = row_init + index * dx
                    last_letter_column_axis = first_letter_column_axis + len(word) - 1
                    last_letter_row_axis = first_letter_row_axis + len(word) - 1
                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)
                    return (first_point, second_point)

        def top_left_to_bottom_right_reversed(word):

            # defining moving vector
            dx, dy = 1, 1

            for column_start in range(self.puzzle_word_length):
                sample_string_diagonal = ""
                sample_reversed_string_diagonal = ""
                row_init = 0
                column_init = column_start

                row, col = row_init, column_init

                while (row < self.puzzle_row_number) and (
                    col < self.puzzle_word_length
                ):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                sample_reversed_string_diagonal = sample_string_diagonal[::-1]

                if word in sample_reversed_string_diagonal:
                    # first and last character value
                    index = sample_reversed_string_diagonal.find(word)

                    origin_index = len(sample_reversed_string_diagonal) - index - 1
                    first_letter_column_axis = column_init + origin_index * dy
                    first_letter_row_axis = row_init + origin_index * dx

                    last_letter_column_axis = first_letter_column_axis - (len(word) - 1)
                    last_letter_row_axis = first_letter_row_axis - (len(word) - 1)

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

            for row_start in range(1, self.puzzle_row_number):
                sample_string_diagonal = ""
                sample_reversed_string_diagonal = ""
                row_init = row_start
                column_init = 0

                row, col = row_init, column_init

                while (row < self.puzzle_row_number) and (
                    col < self.puzzle_word_length
                ):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                sample_reversed_string_diagonal = sample_string_diagonal[::-1]

                if word in sample_reversed_string_diagonal:
                    # first and last character value
                    index = sample_reversed_string_diagonal.find(word)

                    origin_index = len(sample_reversed_string_diagonal) - index - 1
                    first_letter_column_axis = column_init + origin_index * dy
                    first_letter_row_axis = row_init + origin_index * dx

                    last_letter_column_axis = first_letter_column_axis - (len(word) - 1)
                    last_letter_row_axis = first_letter_row_axis - (len(word) - 1)

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        def bottom_left_to_top_right(word):

            # defining moving vector
            dx, dy = -1, 1

            for column_start in range(self.puzzle_word_length):
                sample_string_diagonal = ""
                row_init = self.puzzle_row_number - 1
                column_init = column_start

                row, col = row_init, column_init

                while (row >= 0) and (col < self.puzzle_word_length):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                if word in sample_string_diagonal:
                    # first and last character value
                    index = sample_string_diagonal.find(word)

                    first_letter_column_axis = column_init + index * dy
                    first_letter_row_axis = row_init + index * dx

                    last_letter_column_axis = first_letter_column_axis + (len(word) - 1)
                    last_letter_row_axis = first_letter_row_axis - (len(word) - 1)

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

            for row_start in range(self.puzzle_row_number):
                sample_string_diagonal = ""
                row_init = self.puzzle_row_number - row_start - 1
                column_init = 0

                row, col = row_init, column_init

                while (row >= 0) and (col < self.puzzle_word_length):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                if word in sample_string_diagonal:
                    # first and last character value
                    index = sample_string_diagonal.find(word)

                    first_letter_column_axis = column_init + index * dy
                    first_letter_row_axis = row_init + index * dx

                    last_letter_column_axis = first_letter_column_axis + (len(word) - 1)
                    last_letter_row_axis = first_letter_row_axis - (len(word) - 1)

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        def bottom_left_to_top_right_reversed(word: str):

            # defining moving vector
            dx, dy = -1, 1

            # finding in beneath of main diagonal
            for column_start in range(self.puzzle_word_length):
                sample_string_diagonal = ""
                row_init = self.puzzle_row_number - 1
                column_init = column_start

                row, col = row_init, column_init

                while (row >= 0) and (col < self.puzzle_word_length):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                sample_reversed = sample_string_diagonal[::-1]

                if word in sample_reversed:
                    index = sample_reversed.find(word)
                    origin_index = len(sample_string_diagonal) - index - 1

                    first_letter_column_axis = column_init + origin_index * dy
                    first_letter_row_axis = row_init + origin_index * dx

                    last_letter_column_axis = first_letter_column_axis - (len(word) - 1)
                    last_letter_row_axis = first_letter_row_axis + (len(word) - 1)

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

            # finding in top of main diagonal
            for row_start in range(self.puzzle_row_number):
                sample_string_diagonal = ""
                row_init = self.puzzle_row_number - row_start - 1
                column_init = 0

                row, col = row_init, column_init

                while (row >= 0) and (col < self.puzzle_word_length):
                    sample_string_diagonal += self.puzzle[row][col]
                    row += dx
                    col += dy

                sample_reversed = sample_string_diagonal[::-1]

                if word in sample_reversed:
                    index = sample_reversed.find(word)
                    origin_index = len(sample_string_diagonal) - index - 1

                    first_letter_column_axis = column_init + origin_index * dy
                    first_letter_row_axis = row_init + origin_index * dx

                    last_letter_column_axis = first_letter_column_axis - (len(word) - 1)
                    last_letter_row_axis = first_letter_row_axis + (len(word) - 1)

                    # returning the first element and last element
                    first_point = Point(first_letter_column_axis, first_letter_row_axis)
                    second_point = Point(last_letter_column_axis, last_letter_row_axis)

                    return (first_point, second_point)

        # executing all functions
        result1 = top_to_bottom_locate(word)
        result2 = bottom_to_top_locate(word)
        result3 = left_to_right_locate(word)
        result4 = right_to_left_locate(word)
        result5 = top_left_to_bottom_right(word)
        result6 = top_left_to_bottom_right_reversed(word)
        result7 = bottom_left_to_top_right(word)
        result8 = bottom_left_to_top_right_reversed(word)

        if result1:
            return result1
        elif result2:
            return result2
        elif result3:
            return result3
        elif result4:
            return result4
        elif result5:
            return result5
        elif result6:
            return result6
        elif result7:
            return result7
        elif result8:
            return result8
        else:
            return None
