import unittest

# from helper import functions
from helper import functions, folders

class TestFunctions(unittest.TestCase):
    def testValidateYearValids(self):
        # a valide year must be 4 digits string and between 1900 and 2100
        # test if functions.validateYear(year) returns True for valid years
        self.assertTrue(functions.validateYear('2000'))
        self.assertTrue(functions.validateYear('2050'))
        self.assertTrue(functions.validateYear('2099'))
        self.assertTrue(functions.validateYear('1901'))

    def testValidateYearInvalids(self):
        # a valide year must be 4 digits string and between 1900 and 2100
        # test if functions.validateYear(year) returns False for invalid years
        self.assertFalse(functions.validateYear('0000'))
        self.assertFalse(functions.validateYear('2100'))
        self.assertFalse(functions.validateYear('2500'))
        self.assertFalse(functions.validateYear('1830'))

    def testValidateYearNonStrings(self):
        # a valide year must be 4 digits string and between 1900 and 2100
        # test if functions.validateYear(year) returns False for non-strings
        self.assertFalse(functions.validateYear(''))
        self.assertFalse(functions.validateYear(None))
        self.assertFalse(functions.validateYear(1))
        self.assertFalse(functions.validateYear(1.0))

class TestFolders(unittest.TestCase):
    def testCreateFolder(self):
        # test if folders.createFolder(path) returns True for valid paths
        folders.createFolder('./', 'deleteMe')
        self.assertTrue(folders.folderExists('./deleteMe'))

        # delete the folder
        folders.deleteFolder('./deleteMe')

        # test if folder is deleted
        self.assertFalse(folders.folderExists('./deleteMe'))


      


        