from textblob import TextBlob
def correct_spelling(input_text):
    """
    Corrects spelling in the given input text using TextBlob.

    Parameters:
    - input_text (str): The input text with potential spelling errors.

    Returns:
    - corrected_text (str): The input text with corrected spelling.

    """
    # Create a TextBlob object
    blob = TextBlob(input_text)


    # Correct spelling using the correct() method
    corrected_text = str(blob.correct())

    return corrected_text
