

Class Game:

    image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
    challenges = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "How many continents are there?", "answer": "7"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
    ]

    current_image_index = 0


    def get_current_image_path():
        return image_paths[current_image_index]

    def get_current_challenge():
        return challenges[current_image_index]

    def next_content():
        global current_image_index
        if current_image_index < len(image_paths) - 1:
            current_image_index += 1

    def prev_content():
        global current_image_index
        if current_image_index > 0:
            current_image_index -= 1

    def is_answer_correct(answer):
        return answer.lower() == challenges[current_image_index]["answer"].lower()