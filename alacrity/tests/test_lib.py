# Unittests for the lib.py functions to be placed here

import unittest
from alacrity import lib
import os


class TestParser(unittest.TestCase):
    """ Unittests for alacrity/lib.py """

    def test_rebuild_persistence(self):
        # Initialise paths
        self.path = 'test_persist.ini'

        # Test default values
        self.persist, test_attributes = lib.rebuild_persistence(self.path)
        self.assertEqual(test_attributes['invert'], False)
        self.assertEqual(test_attributes['build'], False)

        # Test creation of file
        self.assertTrue(os.path.isfile(self.persist))
        os.remove(self.persist)

    def test_read_from_paths(self):
        self.test_path = 'test_file'
        self.abs_path = os.path.abspath('test_file')

        with open(self.test_path, 'w') as obj:
            obj.write("#Testdata#")

        self.data = lib.read_from_paths(self.test_path, self.abs_path)
        self.assertEqual(self.data, "#Testdata#")

    def test_remove_package(self):
        self.test_path = 'test_dir'
        os.mkdir(self.test_path)
        lib.remove_package(self.test_path)

        self.assertFalse(os.path.isdir(self.test_path))

    # def test_create_package_structure(self):
    #     self.assertTrue(True)
    #
    # def test_create_docs(self):
    #     self.assertFalse(False)
    #
    # def test_create_tests(self):
    #     self.assertEqual(2+2, 4)
    #
    # def test_create_gitignore(self):
    #     self.assertTrue(True)
    #
    # def test_create_manifest(self):
    #     self.assertTrue(True)
    #
    # def test_create_requirements(self):
    #     self.assertTrue(True)
    #
    # def test_create_readme(self):
    #     self.assertTrue(True)
    #
    # def test_create_makefile(self):
    #     self.assertTrue(True)
    #
    # def test_create_setup(self):
    #     self.assertTrue(True)
    #
    # def test_mit(self):
    #     self.assertTrue(True)
    #
    # def test_apa(self):
    #     self.assertTrue(True)
    #
    # def test_gpl(self):
    #     self.assertTrue(True)
    #
    # def test_create_license(self):
    #     self.assertTrue(True)
    #
    # def test_create_starter_files(self):
    #     self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
