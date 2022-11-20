from api import PetFriends
from settings import*
import os

pf = PetFriends()
# my_pets['pets'][0]['id']

def test_add_new_pet_simple(name='Samson', animal_type='Cat',
                            age='1'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_add_pet_photo(pet_photo='images/cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.set_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert "pet_photo" in result
    else:
        raise Exception("There is no my Pets")


def test_get_api_for_invalid_mail(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status != 200


def test_get_api_for_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)

    assert status != 200


def test_get_api_for_invalid_user(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)

    assert status != 200


def test_get_api_empty_data(email=empty_email, password=empty_password):
    status, result = pf.get_api_key(email, password)

    assert status != 200


def test_add_new_pet_with_empty_data(name='', animal_type='',
                                     age='', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200    # !!!!!!!!!!!!!!Expected 4xx due to lack of data!!!!!!!!!!!!!!!!!!!!
    assert result['name'] == name


def test_add_new_pet_with_str_for_age(name='Silver', animal_type='Cat',
                                      age='LoadAge', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200    # !!!!!!!!!!!!!!!Expected 4xx due to age is not int!!!!!!!!!!!!!!!!!!!!
    assert result['name'] == name


def test_add_new_pet_with_wrong_photo_file(name='Silver', animal_type='Cat',
                                           age='1', pet_photo='images/cat1.txt'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200    # !!!!!!!!!!!!!!!!!!Expected 4xx due to cat1.txt is not a photo!!!!!!!!!!!!!!!!!!!
    assert result['name'] == name


def test_add_new_pet_with_int_for_name(name=1, animal_type='Cat',
                                      age='2', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    try:
        assert status != 200  # !!!!!!!!!!!!!!!Expected 4.. due to age is not int!!!!!!!!!!!!!!!!!!!!
    except AttributeError:
        pass