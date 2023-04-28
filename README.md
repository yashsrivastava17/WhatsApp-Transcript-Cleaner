# WhatsApp Transcript Cleaner
WhatsApp Transcript Cleaner is a Python program that allows you to clean up WhatsApp chat transcripts exported as text files by removing the timestamp and/or sender name. It is designed to make it easier to analyze WhatsApp chat data in bulk.

The program offers three options:

1. Remove both the timestamp and the sender name
2. Remove only the timestamp
3. Choose what to do with each individual file (option 1 or option 2)
With this program, you can quickly and easily clean up multiple WhatsApp chat transcripts at once, saving you time and effort. The cleaned chat files are saved in a new directory called Modified_Files, making it easy to keep them organized.

## Getting Started
Prerequisites
Before using WhatsApp Transcript Cleaner, make sure you have Python 3 installed on your computer. If you don't have it, you can download it from the official website: https://www.python.org/downloads/

## Installing
To get started with WhatsApp Transcript Cleaner, follow these steps:

Clone this repository to your local machine using the following command:
```
git clone https://github.com/yourusername/whatsapp-transcript-cleaner.git
```

Navigate to the repository directory:
```
cd whatsapp-transcript-cleaner
```

Install the required packages:
```
pip install -r requirements.txt
```

## Usage
To use WhatsApp Transcript Cleaner, follow these instructions:

1. Export the WhatsApp chat(s) you wish to clean as text files. Each chat should be saved in its own text file. For instructions on how to export a chat, see this WhatsApp support article.

2. Place all the exported text files in a single directory. Make sure there are no other text files in the directory that you do not want to clean.

3. Open a terminal window and navigate to the directory where you cloned the repository.

4. Run the program with the following command:
```
python whatsapp_transcript_cleaner.py
```

5. Follow the on-screen instructions to choose which option you want to use for each chat file. You can choose to remove the timestamp and/or sender name, or leave them as they are.

6. The cleaned chat files will be saved in a new directory called Modified_Filess inside the original directory.

## Contributing
Contributions are welcome! If you have any bug reports, feature requests, or code improvements, please submit them as issues or pull requests on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

