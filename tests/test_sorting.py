import unittest
from sorting_algorithms import bubble_sort
from ds import convert_to_linked_list

class TestSorting(unittest.TestCase):

    def test_bubble_sort_list(self):
        l1 = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(bubble_sort(l1), [1,2,3,4,5,6,7,8,9])

    def test_bubble_sort_linked_list(self):
        l2 = [9,8,7,6,5,4,3,2,1]
        linked_list = convert_to_linked_list(l2)
        sorted_ll = bubble_sort(linked_list)
        self.assertEqual(list(sorted_ll), sorted(l2))

if __name__ == "__main__":
    unittest.main()
