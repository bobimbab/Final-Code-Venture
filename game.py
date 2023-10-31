import os
import json
from PIL import Image
"""
Game Class

A class representing a game that allows the user to browse through modules of images and answer challenges.

"""


class Game:
    def __init__(self, username):
        self.modules = {}  # Use a dictionary to store modules
        self.current_module = None
        self.current_image_index = 0
        self.questions = {}
        self.progress = {}
        self.completion = False
        self.username = username
        self.load_modules_and_images()
        self.load_challenges_and_answers()
        self.load_progress()

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
                
    def save_progress(self):
        data_directory = "data"
        progress_file_path = os.path.join(data_directory, "progress.json")

        progress_data = {
            "username": self.username,
            "progress": self.progress,
            "completed": self.completion
        }

        with open(progress_file_path, 'w') as file:
            json.dump(progress_data, file)
                
    def load_progress(self):
        data_directory = "data"
        progress_file_path = os.path.join(data_directory, "progress.json")

        if os.path.exists(progress_file_path):
            if os.path.getsize(progress_file_path) > 0:  # Check if the file is not empty
                with open(progress_file_path, 'r') as file:
                    progress_data = json.load(file)
                    self.username = progress_data.get("username")
                    self.progress = progress_data.get("progress")
            else:
                print("Progress file is empty.")
        else:
            print("Progress file not found.")
            
    def update_progress(self):
        if Game.has_next_image(self) == False:
            self.completion = True

        self.save_progress()
                

    def set_current_module(self, module_name):
        self.current_module = module_name
        self.current_image_index = 0
        self.progress[module_name] = 0
        self.save_progress()  # save the progress

    def get_current_image(self):
        if self.current_module is not None:
            image_paths = self.modules.get(self.current_module)
            if image_paths and 0 <= self.current_image_index < len(image_paths):
                image_path = image_paths[self.current_image_index]
                self.progress[self.current_module] += 1
                self.save_progress()  # Add this line to save the progress
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
