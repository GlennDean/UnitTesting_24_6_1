import unittest

from AModule import Sort_Tuple
from AModule import get_index_for_book
from AModule import get_first_index_closes_to_name
from AModule import get_books_close_by_in_name
from AModule import get_ordered_list_for_book

class OptionsTestCases(unittest.TestCase):
    
    def test_sort_tuple(self):
        print("running unit test 'test_option1'")
        mylist = [('z',17.2),('a',24.15)]
        ordered_list = Sort_Tuple(mylist)
        # did it work
        self.assertEqual('a',ordered_list[0][0])
        self.assertEqual('z',ordered_list[1][0])
        self.assertEqual(24.15,ordered_list[0][1])
        self.assertEqual(17.2,ordered_list[1][1])
        
    def test_get_index_for_book(self):
        print("running unit test 'test_get_index_for_book'")
        idx = get_index_for_book("Eye of The Needle")
        self.assertEqual(-1,idx)
        idx = get_index_for_book("Eye of the Needle")
        self.assertEqual(481,idx)
        # Test the edge case - idx = 1
        idx = get_index_for_book("'Tis (Frank McCourt, #2)")
        self.assertEqual(1,idx)

    def test_get_first_index_closes_to_name(self):
        # 'Eat, Pray, Love' has idx 440
        # 'Eats, Shoots & Leaves' should have idx 441
        # 'Echo Burning' has idx 442
        idx = get_first_index_closes_to_name("Eats, Shoots & Leaves")
        self.assertEqual(441,idx)

    def test_get_books_close_by_in_name(self):
        bookname = "Eats, Shoots & Leaves"
        close_by_list = get_books_close_by_in_name(bookname)
        #IMPORTANT - it should return exactly 20 books, with the
        # 10th element the closest in name
        self.assertEqual(20,len(close_by_list))
        self.assertEqual(bookname,close_by_list[10][0][0:len(bookname)])

    def test_get_ordered_list_for_book(self):
        bookname = "Eye of the Needle"
        ord_list = get_ordered_list_for_book(bookname)
        # the list should have
        # 1st entry: 'Gorky Park (Arkady Renko, #1)'
        # 18th entry: 'Clear and Present Danger (Jack Ryan Universe, #6)'
        book1 = "Gorky Park (Arkady Renko, #1)"
        book19 = "Clear and Present Danger (Jack Ryan Universe, #6)"
        self.assertEqual(book1,ord_list[1][0])
        self.assertEqual(book19,ord_list[19][0])
        
if __name__ == '__main__':
    unittest.main()

