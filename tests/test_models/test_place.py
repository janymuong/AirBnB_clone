#!/usr/bin/python3
"""
    test_place:
        This module contains the tests for the Place model
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """
        class contains the unit tests for the Place model
    """

    def test_place_inherits_from_base_model(self):
        """
            test that Place inherits from BaseModel
        """
        msg = "Expected Place to inherit from BaseModel"

        self.assertTrue(issubclass(Place, BaseModel), msg)

    def test_place_has_attribute_name(self):
        """
            test that Place has public class attr name
        """

        msg = "Expected Place to have public class attribute 'name'"
        self.assertTrue(hasattr(Place, 'name'), msg)

    def test_attribute_name_is_empty_string(self):
        """
            test that class attribute name is an empty string
        """
        msg = "Expected name to be an empty string"
        length = 0
        self.assertEqual(len(Place.name), length, msg)
        self.assertEqual(Place.name, "")

    def test_instance_has_default_name_value(self):
        """
            test that instances of Place get default name value
        """
        msg = "Expected object to have default name value"

        place = Place()
        self.assertEqual(len(place.name), 0)
        self.assertEqual(place.name, "")

    def test_instance_sets_own_name(self):
        """
            test that instance can set it own value
        """
        place = Place()
        name = "LOFT"
        place.name = name

        self.assertEqual(name, place.name)
        self.assertNotEqual(place.name, Place.name)

    def test_name_attribute_is_class_attribute(self):
        """
            test that name is a class attribute
        """
        place = Place()
        msg = "Expected name to be class attribute but got instance attribute"

        self.assertNotIn('name', place.__dict__.keys(), msg)

    def test_place_has_attribute_description(self):
        """
            test that Place has public class attr description
        """

        msg = "Expected Place to have public class attribute 'description'"
        self.assertTrue(hasattr(Place, 'description'), msg)

    def test_attribute_description_is_empty_string(self):
        """
            test that class attribute description is an empty string
        """
        msg = "Expected description to be an empty string"
        length = 0
        self.assertEqual(len(Place.description), length, msg)
        self.assertEqual(Place.description, "")

    def test_instance_has_default_description_value(self):
        """
            test that instances of Place get default decription value
        """
        msg = "Expected object to have default description value"

        place = Place()
        self.assertEqual(len(place.description), 0)
        self.assertEqual(place.description, "")

    def test_instance_sets_own_description(self):
        """
            test that instance can set it own value
        """
        place = Place()
        description = "Serene environment"
        place.description = description

        self.assertEqual(description, place.description)
        self.assertNotEqual(place.description, Place.description)

    def test_description_attribute_is_class_attribute(self):
        """
            test that description is a class attribute
        """
        place = Place()
        msg = "Expected description to be class\
                attribute but got instance attribute"

        self.assertNotIn('description', place.__dict__.keys(), msg)

    def test_place_has_attribute_number_rooms(self):
        """
            tests that Place has public class attr number_rooms
        """
        msg = "Expected Place to have public class attribute number_rooms"

        self.assertTrue(hasattr(Place, 'number_rooms'), msg)

    def test_number_rooms_is_class_attribute(self):
        """
            test that number_rooms is a public class attribute
        """
        place = Place()

        self.assertNotIn('number_rooms', place.__dict__.keys())

    def test_number_rooms_is_int(self):
        """
            test number_rooms is an integer
        """
        self.assertTrue(type(Place.number_rooms), int)

    def test_default_value_number_rooms(self):
        """
            tests the default value of number_rooms
        """

        rooms = 0

        self.assertEqual(Place.number_rooms, rooms)

    def test_instance_has_number_room_default_value(self):
        """
            test that instance of place get default values
        """
        place = Place()

        rooms = 0

        self.assertEqual(place.number_rooms, rooms)
        self.assertEqual(Place.number_rooms, place.number_rooms)

    def test_instance_sets_number_rooms(self):
        """
            test that instances can set their own number_rooms
        """
        place = Place()
        place.number_rooms = 3

        self.assertNotEqual(place.number_rooms, Place.number_rooms)

    def test_place_has_attribute_number_bathrooms(self):
        """
            tests that Place has public class attr number_bathrooms
        """
        msg = "Expected Place to have public class attribute number_bathrooms"

        self.assertTrue(hasattr(Place, 'number_bathrooms'), msg)

    def test_number_bathrooms_is_class_attribute(self):
        """
            test that number_bathrooms is a public class attribute
        """
        place = Place()

        self.assertNotIn('number_bathrooms', place.__dict__.keys())

    def test_number_bathrooms_is_int(self):
        """
            test number_bathrooms is integer
        """
        self.assertTrue(type(Place.number_bathrooms), int)

    def test_default_value_number_bathrooms(self):
        """
            tests the default value of number_bathrooms
        """

        bathrooms = 0

        self.assertEqual(Place.number_bathrooms, bathrooms)

    def test_instance_has_number_bathroom_default_value(self):
        """
            test that instance of place get default values
        """
        place = Place()

        bathrooms = 0

        self.assertEqual(place.number_bathrooms, bathrooms)
        self.assertEqual(Place.number_bathrooms, place.number_bathrooms)

    def test_instance_sets_number_bathrooms(self):
        """
            test that instances can set their own number_bathrooms
        """
        place = Place()
        place.number_bathrooms = 2

        self.assertNotEqual(place.number_bathrooms, Place.number_bathrooms)

    def test_place_has_attribute_max_guests(self):
        """
            tests that Place has public class attr max_guests
        """
        msg = "Expected Place to have public class attribute max_guests"

        self.assertTrue(hasattr(Place, 'max_guest'), msg)

    def test_max_guests_is_class_attribute(self):
        """
            test that max_guests is a public class attribute
        """
        place = Place()

        self.assertNotIn('max_guest', place.__dict__.keys())

    def test_max_guest_is_int(self):
        """
            test max_guest is int
        """

        self.assertTrue(type(Place.max_guest), int)

    def test_default_value_max_guests(self):
        """
            tests the default value of max_guests
        """

        guests = 0

        self.assertEqual(Place.max_guest, guests)

    def test_instance_has_max_guests_default_value(self):
        """
            test that instance of place get default values
        """
        place = Place()

        guests = 0

        self.assertEqual(place.max_guest, guests)
        self.assertEqual(Place.max_guest, place.max_guest)

    def test_instance_sets_max_guest(self):
        """
            test that instances can set their own max_guest
        """
        place = Place()
        place.max_guest = 3

        self.assertNotEqual(place.max_guest, Place.max_guest)

    def test_place_has_attribute_price_by_night(self):
        """
            tests that Place has public class attr price_by_night
        """
        msg = "Expected Place to have public class attribute price_by_night"

        self.assertTrue(hasattr(Place, 'price_by_night'), msg)

    def test_price_by_night_is_class_attribute(self):
        """
            test that price_by_night is a public class attribute
        """
        place = Place()

        self.assertNotIn('price_by_night', place.__dict__.keys())

    def test_price_by_night_is_int(self):
        """
            test price_by_night is integer
        """

        self.assertTrue(type(Place.price_by_night), int)

    def test_default_value_price_by_night(self):
        """
            tests the default value of price_by_night
        """

        price = 0

        self.assertEqual(Place.price_by_night, price)

    def test_instance_has_price_by_night_default_value(self):
        """
            test that instance of place get default values
        """
        place = Place()

        price = 0

        self.assertEqual(place.price_by_night, price)
        self.assertEqual(Place.price_by_night, place.price_by_night)

    def test_instance_sets_price_by_night(self):
        """
            test that instances can set their own price_by_night
        """
        place = Place()
        place.price_by_night = 15000

        self.assertNotEqual(place.price_by_night, Place.price_by_night)

    def test_place_has_long_lat(self):
        """
            test the Place has longitude and longitude
        """
        msg = "Expected place to have both longitude and latitude"

        self.assertTrue(hasattr(Place, 'longitude'), msg)
        self.assertTrue(hasattr(Place, 'latitude'), msg)

    def test_lat_and_long_are_class_attributes(self):
        """
            test that latitude and longitude are class attributes
        """
        place = Place()

        self.assertNotIn('longitude', place.__dict__.keys())
        self.assertNotIn('latitude', place.__dict__.keys())

    def test_lat_and_long_is_float(self):
        """
            test latitude and longitude are floats
        """

        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.latitude, float)

    def test_default_values_lat_long(self):
        """
            test default values of lat and long
        """
        lat = 0.0
        log = 0.0

        self.assertEqual(Place.longitude, log)
        self.assertEqual(Place.latitude, lat)

    def test_instance_has_default_values_lat_long(self):
        """
            test instances have class default values
        """
        lat = 0.0
        log = 0.0

        place = Place()

        self.assertEqual(place.longitude, Place.longitude)
        self.assertEqual(place.latitude, Place.latitude)
        self.assertEqual(place.longitude, log)
        self.assertEqual(place.latitude, lat)

    def test_place_has_class_attribute_city(self):
        """
            test that place has public class attribute city_id
        """
        msg = "Expected Place to have public class attribute city_id"
        self.assertTrue(hasattr(Place, 'city_id'), msg)

    def test_city_id_is_empty_string(self):
        """
            test that default value of city_id is empty string
        """
        length = 0

        self.assertEqual(len(Place.city_id), length)
        self.assertEqual(Place.city_id, "")

    def test_city_id_is_set_correct(self):
        """
            test that city_id is equivalent to city.id
        """

        city = City()
        place = Place()
        id_num = city.id
        place.city_id = id_num

        self.assertTrue(place.city_id == city.id)

    def test_city_id_set_incorrectly(self):
        """
            test incorrect city_id
        """
        city = City()
        place = Place()

        place.city_id = "123456"

        self.assertNotEqual(place.city_id, city.id)

    def test_city_id_is_string(self):
        """
            test that city_id is of type string
        """
        city = City()
        place = Place()
        place.city_id = city.id

        self.assertIsInstance(place.city_id, str)

    def test_city_id_not_empty_on_set(self):
        """
            test the instance city_id is not empty string
        """
        city = City()
        place = Place()

        place.city_id = city.id

        self.assertNotEqual(place.city_id, "")
        self.assertNotEqual(len(place.city_id), 0)
        self.assertFalse(place.city_id.isspace())

    def test_place_has_class_attribute_user(self):
        """
            test that place has public class attribute user_id
        """
        msg = "Expected Place to have public class attribute user_id"
        self.assertTrue(hasattr(Place, 'user_id'), msg)

    def test_user_id_is_empty_string(self):
        """
            test that default value of user_id is empty string
        """
        length = 0

        self.assertEqual(len(Place.user_id), length)
        self.assertEqual(Place.user_id, "")

    def test_user_id_is_set_correct(self):
        """
            test that user_id is equivalent to user.id
        """

        user = User()
        place = Place()
        id_num = user.id
        place.user_id = id_num

        self.assertTrue(place.user_id == user.id)

    def test_user_id_set_incorrectly(self):
        """
            test incorrect user_id
        """
        user = User()
        place = Place()

        place.user_id = "123456"

        self.assertNotEqual(place.user_id, user.id)

    def test_user_id_is_string(self):
        """
            test that user_id is of type string
        """
        user = User()
        place = Place()
        place.user_id = user.id

        self.assertIsInstance(place.user_id, str)

    def test_user_id_not_empty_on_set(self):
        """
            test the instance user_id is not empty string
        """
        user = User()
        place = Place()

        place.user_id = user.id

        self.assertNotEqual(place.user_id, "")
        self.assertNotEqual(len(place.user_id), 0)
        self.assertFalse(place.user_id.isspace())

    def test_place_has_class_attribute_amenity(self):
        """
            test that place has public class attribute amenity_ids
        """
        msg = "Expected Place to have public class attribute amenity_ids"
        self.assertTrue(hasattr(Place, 'amenity_ids'), msg)

    def test_amenity_ids_is_empty_list(self):
        """
            test that default value of amenity_id is empty list
        """
        length = 0

        self.assertEqual(len(Place.amenity_ids), length)


    def test_amenity_id_is_set_correct(self):
        """
            test that amenity_ids is equivalent to amenity.id
        """

        pool = Amenity()
        gym = Amenity()
        place = Place()

        place.amenity_ids.append(pool.id)
        place.amenity_ids.append(gym.id)

        self.assertTrue(place.amenity_ids[0] == pool.id)
        self.assertTrue(place.amenity_ids[1] == gym.id)
        Place.amenity_ids.clear()

    def test_amenity_id_set_incorrectly(self):
        """
            test incorrect amenity_id
        """
        am = Amenity()
        place = Place()

        place.amenity_ids.append("123456")

        self.assertNotEqual(place.amenity_ids[0], am.id)
        Place.amenity_ids.clear()

    def test_amenity_id_is_string(self):
        """
            test that amenity_id is of type string
        """
        am = Amenity()
        place = Place()
        place.amenity_ids.append(am.id)

        self.assertIsInstance(place.amenity_ids[0], str)
        Place.amenity_ids.clear()

    def test_amenity_id_not_empty_on_set(self):
        """
            test the instance amenity_id is not empty list
        """
        am = Amenity()
        place = Place()

        place.amenity_ids.append(am.id)

        self.assertNotEqual(len(place.amenity_ids), 0)
        Place.amenity_ids.clear()

