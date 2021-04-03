#!/usr/bin/python3
""" Unittest for State """
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """ testing states"""
    @classmethod
    def setUpClass(cls):
        """ test """
        cls.state = State()
        cls.state.name = "Montevideo"

    @classmethod
    def teardown(cls):
        """ delete """
        del cls.state

    def tearDown(self):
        """ testing """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """ test """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_checking_for_docstring_State(self):
        """test"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """test"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """test"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """test State"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_State(self):
        """test"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
