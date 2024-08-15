import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch lyrics
def fetch_lyrics():
    artist = artist_entry.get()
    title = title_entry.get()
    
    if artist and title:
        url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            lyrics = data.get('lyrics', 'No lyrics found')
            lyrics_text.delete("1.0", tk.END)
            lyrics_text.insert(tk.END, lyrics)
        else:
            messagebox.showerror("Error", "Could not fetch lyrics. Please try again.")
    else:
        messagebox.showerror("Error", "Artist and song title are required fields.")

# Create the main window
root = tk.Tk()
root.title("Lyrics Fetcher")

# Create and place the artist label and entry
artist_label = tk.Label(root, text="Artist")
artist_label.grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the title label and entry
title_label = tk.Label(root, text="Song Title")
title_label.grid(row=1, column=0, padx=10, pady=10)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the fetch lyrics button
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=20)

# Create and place the text widget to display lyrics
lyrics_text = tk.Text(root, wrap='word', width=50, height=15)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
