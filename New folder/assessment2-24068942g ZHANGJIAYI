from PIL import Image

# Dictionary to map words to image file paths
word_to_image = {
    "1": r"C:\\Users\sdit\Desktop\\New folder\\pic\\1 (1).jpeg",
    "2": r"C:\\Users\sdit\Desktop\\New folder\\pic\\1 (2).jpeg",
    "3": r"C:\\Users\sdit\Desktop\\New folder\\pic\\1 (3).jpeg",
}

# Function to display image based on user input
def show_image(word):
    image_path = word_to_image.get(word)  # Get the corresponding image path
    if image_path:
        try:
            img = Image.open(image_path)
            img.show()  # This will open the image in the default image viewer
        except FileNotFoundError:
            print(f"Error: The image for '{word}' was not found.")
    else:
        print("The word you entered doesn't have a corresponding image.")

# Main loop to get user input
while True:
    user_input = input("Enter a word (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    show_image(user_input)
