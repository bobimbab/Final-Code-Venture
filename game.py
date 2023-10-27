import os
from PIL import Image


class Game:
    def __init__(self):
        self.albums = []
        self.current_album = None
        self.current_image_index = 0
        self.image_paths = []
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
                self.albums.append(album_name)
                image_names = image_names.split(', ')
                image_paths = [os.path.join(data_directory, module_content_directory, album_name, name) for name in image_names]
                self.image_paths.append(image_paths)

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
            if 0 <= self.current_image_index < len(self.image_paths[self.albums.index(self.current_album)]):
                image_path = self.image_paths[self.albums.index(self.current_album)][self.current_image_index]
                return Image.open(image_path)
        return None

    def get_current_challenge(self):
        if self.current_album is not None:
            return self.questions.get(self.current_album, ("No question", "No answer"))

    def check_answer(self, user_answer):
        _, correct_answer = self.get_current_challenge()

        if user_answer.lower() == correct_answer.lower():
            return "Correct!"
        else:
            return "Incorrect!"
