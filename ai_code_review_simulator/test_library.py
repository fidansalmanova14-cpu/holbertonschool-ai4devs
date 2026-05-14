import unittest
from library_manager import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("Test Book", "Author", "111")

    def test_add_book(self):
        self.assertEqual(len(self.lib.books), 1)

    def test_search(self):
        results = self.lib.search_books("Test")
        self.assertEqual(len(results), 1)

    def test_checkout(self):
        msg = self.lib.checkout_book(1)
        self.assertIn("Success", msg)
        self.assertFalse(self.lib.books[1].is_available)

    def test_return(self):
        self.lib.checkout_book(1)
        self.lib.return_book(1)
        self.assertTrue(self.lib.books[1].is_available)

    def test_invalid_checkout(self):
        msg = self.lib.checkout_book(999)
        self.assertEqual(msg, "Book not found.")

if __name__ == "__main__":
    unittest.main()
