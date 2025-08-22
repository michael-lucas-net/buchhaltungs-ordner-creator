import unittest
import tempfile
import shutil
import os
from helper import functions, folders

class TestFunctions(unittest.TestCase):
    def test_validate_year_valids(self):
        """Testet gültige Jahreszahlen."""
        # A valid year must be 4 digits string and between 1901 and 2099
        # Test if functions.validate_year(year) returns True for valid years
        self.assertTrue(functions.validate_year('2000'))
        self.assertTrue(functions.validate_year('2050'))
        self.assertTrue(functions.validate_year('2099'))
        self.assertTrue(functions.validate_year('1901'))

    def test_validate_year_invalids(self):
        """Testet ungültige Jahreszahlen."""
        # A valid year must be 4 digits string and between 1901 and 2099
        # Test if functions.validate_year(year) returns False for invalid years
        self.assertFalse(functions.validate_year('0000'))
        self.assertFalse(functions.validate_year('2100'))
        self.assertFalse(functions.validate_year('2500'))
        self.assertFalse(functions.validate_year('1830'))

    def test_validate_year_non_strings(self):
        """Testet nicht-String Eingaben."""
        # A valid year must be 4 digits string and between 1901 and 2099
        # Test if functions.validate_year(year) returns False for non-strings
        self.assertFalse(functions.validate_year(''))
        self.assertFalse(functions.validate_year(None))
        self.assertFalse(functions.validate_year(1))
        self.assertFalse(functions.validate_year(1.0))

class TestFolders(unittest.TestCase):
    def setUp(self):
        """Erstellt ein temporäres Verzeichnis für Tests."""
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Räumt das temporäre Verzeichnis auf."""
        shutil.rmtree(self.test_dir)
        
    def test_create_folder(self):
        """Testet die Ordnererstellung."""
        # Test if folders.create_folder(path) returns True for valid paths
        result = folders.create_folder(self.test_dir, 'deleteMe')
        self.assertTrue(result)
        self.assertTrue(folders.folder_exists(os.path.join(self.test_dir, 'deleteMe')))

        # Delete the folder
        result = folders.delete_folder(os.path.join(self.test_dir, 'deleteMe'))
        self.assertTrue(result)

        # Test if folder is deleted
        self.assertFalse(folders.folder_exists(os.path.join(self.test_dir, 'deleteMe')))
        
    def test_folder_exists(self):
        """Testet die Ordner-Existenz-Prüfung."""
        # Test with non-existent folder
        self.assertFalse(folders.folder_exists(os.path.join(self.test_dir, 'non_existent')))
        
        # Test with existing folder
        test_folder = os.path.join(self.test_dir, 'test_folder')
        os.makedirs(test_folder)
        self.assertTrue(folders.folder_exists(test_folder))

if __name__ == '__main__':
    unittest.main()
        
