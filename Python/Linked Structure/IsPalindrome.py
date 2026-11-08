from LinkedStack import *

def is_palindrome(text):
    cleaned = [char.lower() for char in text if char.isalnum()]
    stack = LinkedStack()

    for i in cleaned:
        stack.push(i)

    for ch in cleaned:
        if ch != stack.pop():
            return False
    return True

