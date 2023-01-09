#!/usr/bin/python3
"""A class Mylist that inherits from list:"""


class MyList(list):

    def print_sorted(self):
        """ Create a copy of the list and sort it """
        sorted_list = self.copy()
        sorted_list.sort()

        # Print the sorted list
        print(sorted_list)
