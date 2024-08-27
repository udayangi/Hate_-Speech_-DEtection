from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import subprocess
import tkinter as tk
from tkinter import messagebox

def get_transcript_and_check_hate():
    vid_id = entry.get()

    try:
        data = yta.get_transcript(vid_id)

        transcript = ''
        for value in data:
            for key, val in value.items():
                if key == 'text':
                    transcript += val

        lines = transcript.splitlines()
        final_tra = " ".join(lines)

        with open("ConvertText.txt", 'w') as file:
            file.write(final_tra)

        messagebox.showinfo("Success", "Transcript saved successfully.")

        # Run the hate.py script
        subprocess.run(["python", "hate.py"])

        # Read results from HateResults.txt
        with open("HateResults.txt", 'r') as result_file:
            result_text = result_file.read()

        # Display results in a message box
        messagebox.showinfo("Hate Check Results", result_text)

    except Exception as e:
        if "TranscriptsDisabled" in str(e):
            messagebox.showerror("Error", "Transcripts are disabled for this video.")
        else:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create a simple Tkinter GUI
root = tk.Tk()
root.title("VideoToText-Only Convert cc video")

label = tk.Label(root, text="Paste URL after '=' Symbol:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Convert and Check Hate", command=get_transcript_and_check_hate)
button.pack(pady=20)

root.mainloop()