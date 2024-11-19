The goal of this project is to retrieve English words and their Hindi translations using Google Translate. Initially, I used the website **www.mso.anu.edu.au** to gather dictionary words from A to Z. The collected words, along with their definitions, were structured as key-value pairs and stored in a JSON file.

To automate the process, I initially created a **PyAutoGUI** script. The script manually opened a Chrome tab with Google Translate, iterated through the JSON file, and simulated `Ctrl + C` and `Ctrl + V` to input English words into the translation box. It then copied the Hindi translation by identifying the "copy" button using the `locateOnScreen` method. However, this approach was inefficient and made the computer unusable while the script was running.

To address these issues, I redeveloped the solution using **Selenium**, which significantly improved efficiency and usability.
