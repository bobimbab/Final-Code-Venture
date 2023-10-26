import os


class GameLogic:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.images = []
        self.current_image_index = 0
        self.questions = []
        self.progress = 0

    def load_images(self):
        # Load the series of images based on the difficulty chosen
        module_folder = os.path.join(os.path.dirname(__file__), "data")
        image_folder = os.path.join(module_folder, "module_content")
        image_txt_path = os.path.join(module_folder, "modules.txt")

        with open(image_txt_path, "r") as file:
            image_lines = file.readlines()
            images_by_difficulty = {}

            for line in image_lines:
                line = line.strip()
                difficulty, images = line.split(":")
                images_by_difficulty[difficulty] = [os.path.join(image_folder, image.strip()) for image in images.split(",")]

            self.images = images_by_difficulty.get(self.difficulty, [])

    def load_questions(self):
        # Load the questions after each series of images
        with open("data/challenges.txt", "r") as file:
            question_lines = file.readlines()
            for line in question_lines:
                question = line.strip()
                self.questions.append(question)

    def save_progress(self):
        # Save the progress to a text file
        with open("data/progress.txt", "w") as file:
            file.write(str(self.progress))

    def get_current_image(self):
        # Get the current image based on the current_image_index
        return self.images[self.current_image_index]

    def get_current_question(self):
        # Get the current question based on the current_image_index
        return self.questions[self.current_image_index]

    def next_image(self):
        # Move to the next image
        if self.current_image_index < len(self.images) - 1:
            self.current_image_index += 1
            self.progress += 1

    def previous_image(self):
        # Move to the previous image
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.progress -= 1

    def answer_question(self, answer):
        # Handle the user's answer to the question
        # You can implement your own logic here
        pass