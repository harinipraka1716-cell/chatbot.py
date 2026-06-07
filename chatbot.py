import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Chatbot Response Function
def chatbot_response(message):
    message = message.lower()

    # Greetings
    if message in ["hi", "hello", "hey"]:
        return "Hello! Welcome to Smart Assistant. How can I help you today?"

    # Bank Services
    elif "open account" in message:
        return """To open a bank account:
1. Submit Aadhaar Card
2. Submit PAN Card
3. Passport Size Photo
4. Initial Deposit Amount"""

    elif "balance" in message:
        return "Your account balance is ₹25,000 (Demo Response)."

    elif "loan" in message:
        return "We offer Home Loans, Personal Loans, and Education Loans."

    # Ticket Booking
    elif "book ticket" in message:
        return "Please provide your destination and travel date."

    elif "chennai to bangalore" in message:
        return """Available Trains:
1. Shatabdi Express - ₹550
2. Double Decker - ₹450
3. Intercity Express - ₹400"""

    elif "flight" in message:
        return "Flights are available. Please provide source and destination."

    # General Queries
    elif "time" in message:
        return datetime.now().strftime("Current Time: %H:%M:%S")

    elif "help" in message:
        return """
Available Services:
• Open Bank Account
• Check Balance
• Loan Information
• Ticket Booking
• Time
• Greetings
"""

    elif "bye" in message:
        return "Thank you for visiting. Have a great day!"

    return "Sorry, I couldn't understand. Type 'help' to see available services."


# Send Message Function
def send_message():
    user_msg = entry.get()

    if user_msg.strip() == "":
        return

    chat_area.insert(tk.END, f"\n🧑 You: {user_msg}\n", "user")

    bot_reply = chatbot_response(user_msg)

    chat_area.insert(tk.END, f"🤖 Bot: {bot_reply}\n", "bot")

    chat_area.yview(tk.END)
    entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Smart Assistant Chatbot")
root.geometry("700x550")
root.configure(bg="#EAF4FC")

# Header
header = tk.Label(
    root,
    text="🤖 Smart Assistant Chatbot",
    font=("Arial", 18, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
header.pack(fill=tk.X)

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11),
    bg="white"
)
chat_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

chat_area.insert(
    tk.END,
    "🤖 Bot: Hello! Welcome to Smart Assistant.\nType 'help' to see available services.\n\n",
    "bot"
)

# Bottom Frame
bottom_frame = tk.Frame(root, bg="#EAF4FC")
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12),
    width=50
)
entry.pack(side=tk.LEFT, padx=5)

send_btn = tk.Button(
    bottom_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#1565C0",
    fg="white",
    command=send_message
)
send_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
