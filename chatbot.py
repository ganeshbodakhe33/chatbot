import tkinter as tk
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Function to send a message to the chatbot
def send_message(event=None):  # Added the 'event' parameter
    message = input_box.get()
    if message:
        conversation_window.config(state=tk.NORMAL)
        conversation_window.insert(tk.END, "You: " + message + "\n")

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="User: " + message + "\n",
            max_tokens=50
        )

        bot_response = response.choices[0].text

        conversation_window.insert(tk.END, "Chatbot: " + bot_response + "\n")
        conversation_window.config(state=tk.DISABLED)

        input_box.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("FastGPT")
app.geometry("400x700")
app.configure(bg="purple")

# Label for the chatbot's name
chatbot_name = tk.Label(app, text="FastGPT", font=("Arial", 20), bg="purple" ,fg="white")
chatbot_name.pack(pady=10)

# Horizontal line separator
line_frame = tk.Frame(app, bg="black", height=2)
line_frame.pack()

# Frame for the conversation window
conversation_frame = tk.Frame(app)
conversation_frame.pack(fill=tk.BOTH, expand=True)

# Text widget for displaying the conversation
conversation_window = tk.Text(conversation_frame, wrap=tk.WORD, state=tk.DISABLED)
conversation_window.pack(fill=tk.BOTH, expand=True)

# Frame for the input box and send button
bottom_frame = tk.Frame(app, bg="purple")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Style for the input box
input_style = {"bg": "lightgray", "font": ("Arial", 12)}
input_box = tk.Entry(bottom_frame, width=30, **input_style)
input_box.pack(pady=10, padx=10, side=tk.LEFT)

# Style for the send button
button_style = {"bg": "blue", "fg": "white", "font": ("Arial", 12)}
send_button = tk.Button(bottom_frame, text="Send", command=send_message, **button_style)
send_button.pack(pady=10, padx=10, side=tk.LEFT)

# Bind the Enter key to the send_message function
input_box.bind("<Return>", send_message)

# Start the Tkinter main loop
app.mainloop()
