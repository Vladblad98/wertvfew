#!/usr/bin/env python3
"""
Simple Bot Implementation
A basic bot that responds to user input.
"""

def main():
    """Main bot function that interacts with users."""
    print("Bot: Hello! I'm a simple bot. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        elif user_input.lower() == 'hello':
            print("Bot: Hello there!")
        elif user_input.lower() == 'how are you':
            print("Bot: I'm doing great, thanks for asking!")
        elif user_input.lower() == 'help':
            print("Bot: Available commands: hello, how are you, help, exit")
        elif user_input:
            print(f"Bot: You said: {user_input}")
        else:
            print("Bot: Please say something!")

if __name__ == "__main__":
    main()
