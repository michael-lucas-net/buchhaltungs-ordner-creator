import unittest
import tempfile
import shutil
import os
from unittest.mock import patch, MagicMock
from helper import functions, folders, names

class TestFunctions(unittest.TestCase):
    def test_validate_year_valids(self):
        """Testet gültige Jahreszahlen."""
        # A valid year must be 4 digits string and between 1901 and 2099
        # Test if functions.validate_year(year) returns True for valid years
        self.assertTrue(functions.validate_year('2000'))
        self.assertTrue(functions.validate_year('2050'))
        self.assertTrue(functions.validate_year('2099'))
        self.assertTrue(functions.validate_year('1901'))
        self.assertTrue(functions.validate_year('2024'))
        self.assertTrue(functions.validate_year('1999'))

    def test_validate_year_invalids(self):
        """Testet ungültige Jahreszahlen."""
        # A valid year must be 4 digits string and between 1901 and 2099
        # Test if functions.validate_year(year) returns False for invalid years
        self.assertFalse(functions.validate_year('0000'))
        self.assertFalse(functions.validate_year('2100'))
        self.assertFalse(functions.validate_year('2500'))
        self.assertFalse(functions.validate_year('1830'))
        self.assertFalse(functions.validate_year('1900'))
        self.assertFalse(functions.validate_year('999'))
        self.assertFalse(functions.validate_year('10000'))

    def test_validate_year_non_strings(self):
        """Testet nicht-String Eingaben."""
        # A valid year must be 4 digits string and between 1901 and 2099
        # Test if functions.validate_year(year) returns False for non-strings
        self.assertFalse(functions.validate_year(''))
        self.assertFalse(functions.validate_year(None))
        self.assertFalse(functions.validate_year(1))
        self.assertFalse(functions.validate_year(1.0))
        self.assertFalse(functions.validate_year([]))
        self.assertFalse(functions.validate_year({}))
        self.assertFalse(functions.validate_year(True))
        self.assertFalse(functions.validate_year(False))

    def test_validate_year_edge_cases(self):
        """Testet Grenzfälle bei der Jahresvalidierung."""
        # Test non-numeric strings
        self.assertFalse(functions.validate_year('abcd'))
        self.assertFalse(functions.validate_year('20ab'))
        self.assertFalse(functions.validate_year('ab20'))
        self.assertFalse(functions.validate_year('2.0'))
        self.assertFalse(functions.validate_year('-2000'))
        self.assertFalse(functions.validate_year(' 2000 '))
        self.assertFalse(functions.validate_year('2000.0'))

    @patch('builtins.input')
    def test_ask_function(self, mock_input):
        """Testet die ask-Funktion."""
        # Test normal input
        mock_input.return_value = "2024"
        result = functions.ask("Jahr eingeben: ")
        self.assertEqual(result, "2024")
        mock_input.assert_called_once_with("Jahr eingeben: ")

        # Test empty input
        mock_input.return_value = ""
        result = functions.ask("Leere Eingabe: ")
        self.assertEqual(result, "")

        # Test special characters
        mock_input.return_value = "Test@123!"
        result = functions.ask("Sonderzeichen: ")
        self.assertEqual(result, "Test@123!")

class TestNames(unittest.TestCase):
    def test_folder_names(self):
        """Testet die Ordner-Namen-Konstanten."""
        self.assertEqual(len(names.folder_names), 2)
        self.assertIn("Eingehend", names.folder_names)
        self.assertIn("Ausgehend", names.folder_names)
        self.assertEqual(names.folder_names, ["Eingehend", "Ausgehend"])

    def test_quarters_structure(self):
        """Testet die Quartale-Struktur."""
        self.assertEqual(len(names.quarters), 4)
        
        # Test first quarter
        self.assertEqual(names.quarters[0][0], "1 Quartal")
        self.assertEqual(len(names.quarters[0][1]), 3)
        self.assertIn("1 Januar", names.quarters[0][1])
        self.assertIn("2 Februar", names.quarters[0][1])
        self.assertIn("3 Maerz", names.quarters[0][1])

        # Test all quarters have correct structure
        for i, quarter in enumerate(names.quarters, 1):
            self.assertEqual(quarter[0], f"{i} Quartal")
            self.assertEqual(len(quarter[1]), 3)

    def test_find_quarter_valid(self):
        """Testet find_quarter mit gültigen Eingaben."""
        # Test all quarters
        for i in range(1, 5):
            quarter_name = f"{i} Quartal"
            result = names.find_quarter(quarter_name)
            self.assertIsNotNone(result)
            self.assertEqual(result[0], quarter_name)
            self.assertEqual(len(result[1]), 3)

    def test_find_quarter_invalid(self):
        """Testet find_quarter mit ungültigen Eingaben."""
        invalid_quarters = [
            "0 Quartal",
            "5 Quartal", 
            "Quartal 1",
            "1. Quartal",
            "Erstes Quartal",
            "",
            None,
            "Random Text"
        ]
        
        for invalid_quarter in invalid_quarters:
            result = names.find_quarter(invalid_quarter)
            self.assertIsNone(result)

    def test_find_quarter_case_sensitivity(self):
        """Testet find_quarter mit verschiedenen Groß-/Kleinschreibungen."""
        # Should be case sensitive
        self.assertIsNone(names.find_quarter("1 quartal"))
        self.assertIsNone(names.find_quarter("1 QUARTAL"))
        self.assertIsNone(names.find_quarter(" 1 Quartal "))
        self.assertIsNone(names.find_quarter("1Quartal"))

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

    def test_create_folder_already_exists(self):
        """Testet Ordnererstellung wenn Ordner bereits existiert."""
        # Create folder first time
        result1 = folders.create_folder(self.test_dir, 'existing')
        self.assertTrue(result1)
        
        # Try to create same folder again
        result2 = folders.create_folder(self.test_dir, 'existing')
        self.assertTrue(result2)  # Should not fail, just return True
        
        # Verify folder still exists
        self.assertTrue(folders.folder_exists(os.path.join(self.test_dir, 'existing')))

    def test_create_folder_nested(self):
        """Testet verschachtelte Ordnererstellung."""
        nested_path = os.path.join(self.test_dir, 'level1', 'level2', 'level3')
        result = folders.create_folder(self.test_dir, 'level1/level2/level3')
        self.assertTrue(result)
        self.assertTrue(folders.folder_exists(nested_path))

    def test_create_folder_invalid_path(self):
        """Testet Ordnererstellung mit ungültigen Pfaden."""
        # Test with None path
        result = folders.create_folder(None, 'test')
        self.assertFalse(result)
        
        # Test with None name
        result = folders.create_folder(self.test_dir, None)
        self.assertFalse(result)
        
        # Test with empty name
        result = folders.create_folder(self.test_dir, '')
        self.assertFalse(result)

    def test_folder_exists(self):
        """Testet die Ordner-Existenz-Prüfung."""
        # Test with non-existent folder
        self.assertFalse(folders.folder_exists(os.path.join(self.test_dir, 'non_existent')))
        
        # Test with existing folder
        test_folder = os.path.join(self.test_dir, 'test_folder')
        os.makedirs(test_folder)
        self.assertTrue(folders.folder_exists(test_folder))

        # Test with file (should return False)
        test_file = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        self.assertFalse(folders.folder_exists(test_file))

    def test_folder_exists_edge_cases(self):
        """Testet Grenzfälle bei der Ordner-Existenz-Prüfung."""
        # Test with None
        self.assertFalse(folders.folder_exists(None))
        
        # Test with empty string
        self.assertFalse(folders.folder_exists(''))
        
        # Test with current directory
        self.assertTrue(folders.folder_exists('.'))

    def test_delete_folder(self):
        """Testet das Löschen von Ordnern."""
        # Create a folder to delete
        test_folder = os.path.join(self.test_dir, 'to_delete')
        os.makedirs(test_folder)
        self.assertTrue(folders.folder_exists(test_folder))
        
        # Delete it
        result = folders.delete_folder(test_folder)
        self.assertTrue(result)
        self.assertFalse(folders.folder_exists(test_folder))

    def test_delete_folder_not_exists(self):
        """Testet das Löschen nicht existierender Ordner."""
        non_existent = os.path.join(self.test_dir, 'non_existent')
        result = folders.delete_folder(non_existent)
        self.assertFalse(result)

    def test_delete_folder_with_content(self):
        """Testet das Löschen von Ordnern mit Inhalt."""
        # Create folder with content
        test_folder = os.path.join(self.test_dir, 'with_content')
        os.makedirs(test_folder)
        test_file = os.path.join(test_folder, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        # Try to delete (should fail because not empty)
        result = folders.delete_folder(test_folder)
        self.assertFalse(result)
        self.assertTrue(folders.folder_exists(test_folder))

    @patch('pathlib.Path.mkdir')
    def test_create_folder_permission_error(self, mock_mkdir):
        """Testet Ordnererstellung bei Berechtigungsfehlern."""
        mock_mkdir.side_effect = PermissionError("Permission denied")
        result = folders.create_folder(self.test_dir, 'permission_test')
        self.assertFalse(result)

    @patch('os.rmdir')
    def test_delete_folder_permission_error(self, mock_rmdir):
        """Testet Ordnerlöschung bei Berechtigungsfehlern."""
        mock_rmdir.side_effect = PermissionError("Permission denied")
        result = folders.delete_folder(self.test_dir)
        self.assertFalse(result)

class TestBhFolders(unittest.TestCase):
    def setUp(self):
        """Erstellt ein temporäres Verzeichnis für Tests."""
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        
    def tearDown(self):
        """Räumt das temporäre Verzeichnis auf."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_create_bh_folders_structure(self):
        """Testet die vollständige Buchhaltungs-Ordnerstruktur."""
        year = "2024"
        result = folders.create_bh_folders(year)
        self.assertTrue(result)
        
        # Check year folder exists
        self.assertTrue(folders.folder_exists(year))
        
        # Check all quarters exist
        for i in range(1, 5):
            quarter_name = f"{i} Quartal"
            quarter_path = os.path.join(year, quarter_name)
            self.assertTrue(folders.folder_exists(quarter_path))
            
            # Check Konto folder exists
            konto_path = os.path.join(quarter_path, "Konto")
            self.assertTrue(folders.folder_exists(konto_path))
            
            # Check months exist
            quarter_data = names.find_quarter(quarter_name)
            for month in quarter_data[1]:
                month_path = os.path.join(quarter_path, month)
                self.assertTrue(folders.folder_exists(month_path))
                
                # Check inbox/outbox folders exist
                for folder_name in names.folder_names:
                    subfolder_path = os.path.join(month_path, folder_name)
                    self.assertTrue(folders.folder_exists(subfolder_path))

    def test_create_bh_folders_invalid_year(self):
        """Testet Buchhaltungs-Ordnererstellung mit ungültigem Jahr."""
        # This should not happen in normal flow due to validation,
        # but we test the function's robustness
        result = folders.create_bh_folders("")
        self.assertFalse(result)

    def test_create_bh_folders_existing_structure(self):
        """Testet Buchhaltungs-Ordnererstellung wenn Struktur bereits existiert."""
        year = "2024"
        
        # Create structure first time
        result1 = folders.create_bh_folders(year)
        self.assertTrue(result1)
        
        # Create structure second time (should not fail)
        result2 = folders.create_bh_folders(year)
        self.assertTrue(result2)

class TestIntegration(unittest.TestCase):
    def setUp(self):
        """Erstellt ein temporäres Verzeichnis für Tests."""
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        
    def tearDown(self):
        """Räumt das temporäre Verzeichnis auf."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_full_workflow(self):
        """Testet den vollständigen Arbeitsablauf."""
        # Simulate user input
        test_year = "2024"
        
        # Validate year
        self.assertTrue(functions.validate_year(test_year))
        
        # Create folder structure
        result = folders.create_bh_folders(test_year)
        self.assertTrue(result)
        
        # Verify structure
        self.assertTrue(folders.folder_exists(test_year))
        
        # Check a specific path
        specific_path = os.path.join(test_year, "1 Quartal", "1 Januar", "Eingehend")
        self.assertTrue(folders.folder_exists(specific_path))

    @patch('builtins.input')
    def test_user_interaction_flow(self, mock_input):
        """Testet den Benutzerinteraktions-Fluss."""
        mock_input.return_value = "2024"
        
        # Simulate asking for year
        year = functions.ask("Jahr eingeben: ")
        self.assertEqual(year, "2024")
        
        # Validate the input
        self.assertTrue(functions.validate_year(year))
        
        # Create folders
        result = folders.create_bh_folders(year)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
        
