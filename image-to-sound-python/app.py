from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import pytesseract

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

def image_to_sound(path_to_image, output_sound="sound.mp3"):
    """
    Function for converting an image to sound
    """
    try:
        # Load and decode image to text
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        
        # Clean the text: Remove empty lines and join
        cleaned_text = " ".join(line.strip() for line in decoded_text.splitlines() if line.strip())
        print("Decoded Text:\n", cleaned_text)
        
        # Convert text to speech
        if cleaned_text:
            sound = gTTS(cleaned_text, lang="en")
            sound.save(output_sound)
            print(f"Sound saved as {output_sound}")
            return True
        else:
            print("No text found in the image.")
            return False
        
    except Exception as bug:
        print("The bug thrown while executing the code:\n", bug)
        return


if __name__ == "__main__":
    # Convert image.jpg to sound.mp3
    image_to_sound("image.jpg", "output.mp3")
    input("Press Enter to exit...")
