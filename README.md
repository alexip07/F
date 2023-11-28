# Flash Card
Hi!

This is a flash card game designed for learning a new language in a fun and interactive way. Feel free to use and modify it as you like.

In the 'data' folder, you'll find a CSV file used for testing. Refer to the README file for information on where to get more files. Don't forget to thank @hermitdave for the help.

To change the language file, open 'main.py' and:
1. Navigate to the line where the file name is set (line 14) and replace "french_words.csv" with your desired file.
2. Go to the lines starting at - 26 - canvas.itemconfig(card_title, text="French", fill="black") and change "French" to the language you want to learn. Do the same for line - 27.

If you're learning from English, that's all you need to do. If you want to change the support language, repeat the steps for the lines starting at - 33 - canvas.itemconfig(card_title, text="English", fill="white") / canvas.itemconfig(card_word, text=current_card["English"], fill="white").

Now you can start learning a new language.

Thank you for your time, and have a great day!
