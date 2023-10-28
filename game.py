import os
from PIL import Image


class Game:
    def __init__(self):
        self.albums = {}  # Use a dictionary to store albums
        self.current_album = None
        self.current_image_index = 0
        self.questions = {}
        self.load_albums_and_images()
        self.load_challenges_and_answers()

    def load_albums_and_images(self):
        data_directory = "data"
        module_content_directory = "module_content"
        albums_file_path = os.path.join(data_directory, 'modules.txt')

        with open(albums_file_path, 'r') as file:
            for line in file:
                album_name, image_names = line.strip().split(': ')
                image_names = image_names.split(', ')
                image_paths = [os.path.join(data_directory, module_content_directory, album_name, name) for name in
                               image_names]
                self.albums[album_name] = image_paths  # Store image paths in the dictionary

    def load_challenges_and_answers(self):
        data_directory = "data"
        challenges_file_path = os.path.join(data_directory, 'challenges.txt')
        with open(challenges_file_path, 'r') as file:
            for line in file:
                album_name, question, answer = line.strip().split(': ')
                self.questions[album_name] = (question, answer)

    def set_current_album(self, album_name):
        self.current_album = album_name
        self.current_image_index = 0

    def get_current_image(self):
        if self.current_album is not None:
            image_paths = self.albums.get(self.current_album)
            if image_paths and 0 <= self.current_image_index < len(image_paths):
                image_path = image_paths[self.current_image_index]
                return Image.open(image_path)
        return None

    def get_current_challenge(self):
        if self.current_album is not None:
            return self.questions.get(self.current_album, ("No question", "No answer"))

    def has_next_image(self):
        if self.current_album is not None:
            image_paths = self.albums.get(self.current_album)
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
