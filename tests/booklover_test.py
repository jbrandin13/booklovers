import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.

        #Create BookLover instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        #Add book to list
        test_object.add_book("War of the Worlds", 4)
        #Test if book in list
        self.assertTrue("War of the Worlds" in list(test_object.book_list.book_name), "Test 1 failed: Book not in list.")

    def test_2_add_book(self):
        # add a book and test if it is in `book_list`.

        #Create BookLover instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        #Add book to list
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        #Test if book in list once
        self.assertTrue(list(test_object.book_list.book_name).count("War of the Worlds") == 1, "Test 2 failed: The book has been added more than once, or not at all.")

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.

        #Create BookLover instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        #Add book to list
        test_object.add_book("War of the Worlds", 4)
        #Test if reader has read the book
        self.assertTrue(test_object.has_read("War of the Worlds"),"Test 3 failed: The book lover has not read this book when they should have.")

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
        #Create BookLover instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        #Add book to list
        test_object.add_book("War of the Worlds", 4)
        #Test if reader has read a book
        self.assertFalse(test_object.has_read("Dune"), "Test 4 failed: The book lover has read this book when they should not have.")

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        
        #Create BookLover instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        #Add book to list
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Dune", 5)
        test_object.add_book("Dune", 5)
        test_object.add_book("The Moon is a Harsh Mistress", 3)
        test_object.add_book("Ubik", 3)
        #Test number of books read
        self.assertTrue(test_object.num_books_read() == 4, "Test 5 failed: The number of books read is incorrect.")

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        
        #Create BookLover instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        #Add book to list
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Dune", 5)
        test_object.add_book("The Moon is a Harsh Mistress", 3)
        test_object.add_book("Ubik", 3)
        #Test number of books read
        self.assertTrue(all(test_object.fav_books().book_rating > 3) == True, "Test 6 failed: Not all favorite books have a rating above 3.")

if __name__ == '__main__':
    unittest.main(verbosity=3)



