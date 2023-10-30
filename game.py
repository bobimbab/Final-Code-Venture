import os
from PIL import Image
"""
Game Class

A class representing a game that allows the user to browse through modules of images and answer challenges.

Attributes:
- modules (dict): A dictionary storing the modules and their corresponding image paths.
- current_module (str): The name of the current module being viewed.
- current_image_index (int): The index of the current image being viewed.
- questions (dict): A dictionary storing the challenges for each module.

Methods:
- load_modules_and_images(): Loads the modules and their image paths from a file.
- load_challenges_and_answers(): Loads the challenges and their answers from a file.
- set_current_module(module_name): Sets the current module to the specified module.
- get_current_image(): Returns the current image being viewed.
- get_current_challenge(): Returns the challenge for the current module.
- has_next_image(): Checks if there is a next image in the current module.
- has_previous_image(): Checks if there is a previous image in the current module.
- get_current_image_index(): Returns the index of the current image.
- set_current_image_index(index): Sets the index of the current image.
- check_answer(user_answer): Checks if the user's answer matches the correct answer for the current challenge.

"""


class Game:
    def __init__(self):
        self.modules = {}  # Use a dictionary to store modules
        self.current_module = None
        self.current_image_index = 0
        self.questions = {}
        self.load_modules_and_images()
        self.load_challenges_and_answers()

    def load_modules_and_images(self):
        data_directory = "data"
        module_content_directory = "module_content"
        modules_file_path = os.path.join(data_directory, 'modules.txt')

        with open(modules_file_path, 'r') as file:
            for line in file:
                module_name, image_names = line.strip().split(': ')
                image_names = image_names.split(', ')
                image_paths = [os.path.join(data_directory, module_content_directory, module_name, name) for name in
                               image_names]
                self.modules[module_name] = image_paths  # Store image paths in the dictionary

    def load_challenges_and_answers(self):
        data_directory = "data"
        challenges_file_path = os.path.join(data_directory, 'challenges.txt')
        with open(challenges_file_path, 'r') as file:
            for line in file:
                module_name, question, answer = line.strip().split(': ')
                self.questions[module_name] = (question, answer)

    def set_current_module(self, module_name):
        self.current_module = module_name
        self.current_image_index = 0

    def get_current_image(self):
        if self.current_module is not None:
            image_paths = self.modules.get(self.current_module)
            if image_paths and 0 <= self.current_image_index < len(image_paths):
                image_path = image_paths[self.current_image_index]
                return Image.open(image_path)
        return None

    def get_current_challenge(self):
        if self.current_module is not None:
            return self.questions.get(self.current_module, ("No question", "No answer"))

    def has_next_image(self):
        if self.current_module is not None:
            image_paths = self.modules.get(self.current_module)
            if image_paths and self.current_image_index < len(image_paths) - 1:
                return True
        return False

    def has_previous_image(self):
        return self.current_image_index > 0

    def get_current_image_index(self):
        return self.current_image_index

    def set_current_image_index(self, index):
        self.current_image_index = index

    def check_answer(self, user_answer):
        _, correct_answer = self.get_current_challenge()

        if user_answer.lower() == correct_answer.lower():
            return "Correct!"
        else:
            return "Incorrect!"
