import tkinter as tk
import unittest

from .sorting_app import SortingApp


class TestSortingApp(unittest.TestCase):
    def test_bubble_sort(self):
        app = SortingApp(tk.Tk())
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        app.bubble_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_selection_sort(self):
        app = SortingApp(tk.Tk())
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        app.selection_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_insertion_sort(self):
        app = SortingApp(tk.Tk())
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        app.insertion_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
