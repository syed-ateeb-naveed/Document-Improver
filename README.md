# Document-Improver

## Overview
Document-Improver is a Django-based web application that allows users to upload documents in `.docx` or `.pdf` format to perform two main functions:
1. **Summarization**: Summarize long documents into concise versions.
2. **Spelling Correction**: Correct spelling errors in the uploaded documents.

This application uses various libraries to handle document processing, summarization, and spelling correction.

## Features
- **Upload Support**: Supports `.docx` and `.pdf` document uploads.
- **Summarization**: Uses the Latent Semantic Analysis (LSA) algorithm to provide concise summaries.
- **Spelling Correction**: Automatically detects and corrects spelling mistakes in documents.
- **Download**: Provides an option to download the corrected document with spelling corrections applied.

## Dependencies

### Core Dependencies
- **Django**: The web framework that powers the application.
  - To install Django, run:
    ```bash
    pip install django
    ```

### Document Handling
- **Fitz** (PyMuPDF): Used for reading and processing PDF files.
  - Install it using:
    ```bash
    pip install pymupdf
    ```
- **python-docx**: For reading and writing `.docx` files.
  - Install it using:
    ```bash
    pip install python-docx
    ```

### Summarization
- **Sumy**: Provides several summarization algorithms, including Latent Semantic Analysis (LSA).
  - Install Sumy:
    ```bash
    pip install sumy
    ```
- **nltk.punkt**: Used for sentence tokenization during summarization.
  - Install NLTK and the required Punkt package:
    ```bash
    pip install nltk
    ```
    Additionally, download the Punkt tokenizer models:
    ```python
    import nltk
    nltk.download('punkt')
    ```

### Spelling Correction
- **TextBlob** or other spell-checking libraries (if used) for spelling correction. If TextBlob is being used, you can install it using:
    ```bash
    pip install textblob
    ```

### Other Dependencies
- **Tempfile**: Used for creating temporary files during processing.
- **io**: Provides I/O operations for handling file streams.

### Additional Packages
- **time**: Used for timing operations.
- **NLTK**: Provides the `punkt` tokenizer required for summarization.

## Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd document-improver
   ```

2. **Install Required Dependencies**:
   Install all required dependencies using `pip`:
   ```bash
   pip install django pymupdf python-docx sumy nltk
   ```

3. **Run the Development Server**:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Usage
1. Upload a `.docx` or `.pdf` document.
2. Select whether you want to summarize or correct spelling in the document.
3. Click the respective button, and the app will process the document.
4. Download the summarized or corrected document.

## Screenshots

![image](https://github.com/user-attachments/assets/5bb840cf-b416-494c-b442-102811b37103)
![image](https://github.com/user-attachments/assets/d02a471b-c696-4e6a-b2ba-da697e5bec03)

