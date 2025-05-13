from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]: 
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace ("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements: 
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = "crop_yield_prediction", 
    version = "0.0.1", 
    author = "Xasanov Dilmurod, Abdulhakimov Hojiakbar, Raximov Nodir", 
    description= "Donli ekinlar hosilini oldindan aytish uchun mo'ljallangan loyiha",
    long_description= "Bu loyiha O'zbekistonning turli viloyatlarida donli ekinlar hosilini oldindan aytish uchun mo'ljallangan. Ushbu loyiha ma'lumotlarni to'plash, tozalash, o'zgartirish va mashinani o'rganish modellarini yaratishni o'z ichiga oladi. Ushbu loyiha yordamida fermerlar hosilni oldindan bilib olishlari va resurslarni samarali ravishda boshqarishlari mumkin.",
    author_email= "Abdulhakimovhojiakbar@gmail.com", 
    install_requires = get_requirements("requirements.txt"),
    packages= find_packages()
    )