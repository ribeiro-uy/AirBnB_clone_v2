#!/usr/bin/python3
""" Unittest for City """
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """ Test for City class """
    @classmethod
    def setUpClass(cls):
        """ create city """
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """ Test for City class """
        del cls.city

    def tearDown(self):
        """ test json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """ testing pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """ testing city docs """
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """ testing city """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """ testing city """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """ test city """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_City(self):
        """ test city """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """ testing city """
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
