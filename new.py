#Arya Venkat and Donavan Tse
import tkinter as tk
import requests

API_TOKEN = "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"

def translator(original_text, original_language, new_language):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}"}
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a user",
            },
            {
                "role": "user",
                "content": f"Translate the following text from {original_language} to {new_language}: {original_text}",
            }
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_data = response.json()

    if "choices" in response_data and len(response_data["choices"]) > 0:
        return response_data["choices"][0]["message"]["content"]

    return "No response from the API"

def click_button():
    original_text = original_text_entry.get()
    original_language = original_language_entry.get()
    new_language = new_language_entry.get()

    translation = translator(original_text, original_language, new_language)
    translated_text_label.configure(text=translation)

#Main Tkinter Window
window = tk.Tk()
window.title("Language Translator")

#Original Text
original_text_label = tk.Label(window, text="Word:")
original_text_label.pack()
original_text_entry = tk.Entry(window, width=50)
original_text_entry.pack()

#Original Language
original_language_label = tk.Label(window, text="Translate From:")
original_language_label.pack()
original_language_entry = tk.Entry(window, width=30)
original_language_entry.pack()

#New Language
new_language_label = tk.Label(window, text="Translate To:")
new_language_label.pack()
new_language_entry = tk.Entry(window, width=30)
new_language_entry.pack()

#Button to operate app is created
button = tk.Button(window, text="Translate", command=click_button)
button.pack()

translated_text_label = tk.Label(window, text="")
translated_text_label.pack()

#Main Loop
window.mainloop()

#ChatGPT was used to build this program
