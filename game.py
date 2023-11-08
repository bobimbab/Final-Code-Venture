import os
import json
from PIL import Image


class Game:
    """
    Game Class

    A class representing a game that allows the user to browse through modules of images and answer challenges.
    """

    def __init__(self, username):
        """
        Initialize a Game instance.

        Args:
            username (str): The username of the player.
        """
        self.modules = {}  # Use a dictionary to store modules
        self.current_module = None # The current module the player is viewing
        self.current_image_index = 0
        self.questions = {}
        self.progress = {}
        self.completion = None
        self.username = username
        self.current_page = 0
        self.load_modules_and_images()
        self.load_challenges_and_answers()
        self.load_progress(username)

    def get_all_progress(self) -> dict:
        return self.progress

    def go_next_page(self):
        image_paths = self.modules.get(self.current_module)
        user_current_page = self.progress[self.current_module]["page"]
        print(self.current_page,"current_page")
        print(user_current_page,"user_current_page")
        if self.current_page >= user_current_page and self.has_next_image():
            print("yes")
            self.current_page += 1
            self.current_image_index += 1
            self.progress[self.current_module]["page"] += 1
        else:
            self.current_page += 1
            self.current_image_index += 1

    def go_previous_page(self):
        user_current_page = self.progress[self.current_module]["page"]
        self.current_page -= 1
        self.current_image_index -= 1

    def load_modules_and_images(self):
        """
        Load modules and their associated image paths from 'modules.txt'.
        """
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
        """
        Load challenges and their answers from 'challenges.txt'.
        """
        data_directory = "data"
        challenges_file_path = os.path.join(data_directory, 'challenges.txt')
        with open(challenges_file_path, 'r') as file:
            for line in file:
                module_name, question, answer = line.strip().split(': ')
                self.questions[module_name] = (question, answer)

    def save_progress(self):
        """
        Save the player's progress and completion status to 'progress.json'.
        """
        print(self.username)
        new_progress = self.progress
        new_completion = self.completion
        updated_module = self.current_module
        print(new_progress,"new progress")
        print(new_completion,"new completion")
        print(updated_module,"updated module")

        # we need to now update the progress in the json file
        data_directory = "data"
        progress_file_path = os.path.join(data_directory, "progress.json")
        user_found = False
        # so first we need to load the json file
        with open(progress_file_path,'r') as file:
            data = json.load(file)
            for user_data in data:
                # locate the user
                if user_data["username"] == self.username:
                    user_found = True
                    if self.current_module in user_data["progress"]:
                        module_progress = user_data["progress"][self.current_module]
                        module_progress["page"] = new_progress[self.current_module]["page"]
                        module_progress["completed"] = new_completion
                    else:
                        user_data["progress"][self.current_module] = {"page":self.current_image_index,"completed": new_completion}

        if not user_found:
            with open(progress_file_path, 'r') as file:
                data = json.load(file)
                new_user_data = {
                    "username": self.username,
                    "progress": {
                        "introduction to python": {
                            "page": 0,
                            "completed": False
                        }
                    }
                }
                data.append(new_user_data)

        with open(progress_file_path,'w') as file:
            json.dump(data,file,indent=4)

    def load_progress(self, username):
        data_directory = "data"
        progress_file_path = os.path.join(data_directory, "progress.json")
        if os.path.exists(progress_file_path):
            if os.path.getsize(progress_file_path) > 0:  # Check if the file is not empty
                with open(progress_file_path, 'r') as file:
                    data = json.load(file)
                    for user_data in data:
                        if user_data["username"] == username:
                            for module_name, progress in user_data["progress"].items():
                                self.progress[module_name] = progress

    def update_progress(self):
        """
        Update the player's progress and completion status.
        """
        if not self.has_next_image():
            self.completion = True

        self.save_progress()

    def set_current_module(self, module_name):
        """
        Set the current module and reset image index and progress for the player.

        Args:
            module_name (str): The name of the module to set as the current module.
        """
        self.current_module = module_name
        if self.current_module in self.progress:
            print(self.progress)
            load_page, load_completion = self.progress[self.current_module]["page"],self.progress[self.current_module]["completed"]
        else:
            load_page, load_completion = 0, False
            self.progress[self.current_module] = {"page": load_page, "completed": load_completion}

        self.completion = load_completion
        self.current_image_index = load_page
        self.current_page = load_page
        print(self.progress)
        self.save_progress()  # save the progress

    def get_current_image(self):
        """
        Get the current image to display.

        Returns:
            PIL.Image.Image or None: The current image as a PIL Image, or None if there are no images.
        """
        if self.current_module is not None:
            image_paths = self.modules.get(self.current_module)
            if image_paths and 0 <= self.current_image_index < len(image_paths):
                image_path = image_paths[self.current_image_index]
                self.save_progress()
                return Image.open(image_path)
        return None

    def get_current_challenge(self):
        """
        Get the challenge associated with the current module.

        Returns:
            tuple: A tuple containing the question and correct answer for the challenge.
        """
        if self.current_module is not None:
            return self.questions.get(self.current_module, ("No question", "No answer"))

    def has_next_image(self):
        """
        Check if there is a next image in the current module.

        Returns:
            bool: True if there is a next image, False otherwise.
        """
        if self.current_module is not None:
            image_paths = self.modules.get(self.current_module)
            if image_paths and self.current_image_index < len(image_paths) - 1:
                return True
        return False

    def has_previous_image(self):
        """
        Check if there is a previous image in the current module.

        Returns:
            bool: True if there is a previous image, False otherwise.
        """
        return self.current_image_index > 0

    def get_current_image_index(self):
        """
        Get the current image index.

        Returns:
            int: The current image index.
        """
        return self.current_image_index

    def set_current_image_index(self, index):
        """
        Set the current image index.

        Args:
            index (int): The index to set as the current image index.
        """
        self.current_image_index = index

    def check_answer(self, user_answer):
        """
        Check if the user's answer matches the correct answer for the current challenge.

        Args:
            user_answer (str): The user's answer to check.

        Returns:
            str: "Correct!" if the answer is correct, "Incorrect!" otherwise.
        """
        _, correct_answer = self.get_current_challenge()

        if user_answer.lower() == correct_answer.lower():
            return "Correct!"
        else:
            return "Incorrect!"
