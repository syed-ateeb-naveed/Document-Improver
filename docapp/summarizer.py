import time
from docx import Document
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def count_words_in_docx(file_path):
    doc = Document(file_path)
    total_words = 0

    for paragraph in doc.paragraphs:
        total_words += len(paragraph.text.split())

    return total_words

def calculate_sentences_count(file_path):
    
    return max(1, count_words_in_docx(file_path)//100)


def summarize(text, language="english", sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

def read_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'

    return text.strip()

if __name__ == "__main__":
    start_time = time.time()
    doc = Document("Sample.docx")
    sentences = calculate_sentences_count("Sample.docx")
    text = read_text_from_docx("Sample.docx")
    summary = summarize(text, sentences_count=sentences)
    print(summary)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")