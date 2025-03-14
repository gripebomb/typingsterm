import curses
import time
import random

# List of words provided
WORDS = [
    "the", "be", "of", "and", "a", "to", "in", "he", "have", "it", "that",
    "for", "they", "I", "with", "as", "not", "on", "she", "at", "by", "this",
    "we", "you", "do", "but", "from", "or", "which", "one", "would", "all",
    "will", "there", "say", "who", "make", "when", "can", "more", "if", "no",
    "man", "out", "other", "so", "what", "time", "up", "go", "about", "than",
    "into", "could", "state", "only", "new", "year", "some", "take", "come",
    "these", "know", "see", "use", "get", "like", "then", "first", "any",
    "work", "now", "may", "such", "give", "over", "think", "most", "even",
    "find", "day", "also", "after", "way", "many", "must", "look", "before",
    "great", "back", "through", "long", "where", "much", "should", "well",
    "people", "down", "own", "just", "because", "good", "each", "those",
    "feel", "seem", "how", "high", "too", "place", "little", "world", "very",
    "still", "nation", "hand", "old", "life", "tell", "write", "become",
    "here", "show", "house", "both", "between", "need", "mean", "call",
    "develop", "under", "last", "right", "move", "thing", "general", "school",
    "never", "same", "another", "begin", "while", "number", "part", "turn",
    "real", "leave", "might", "want", "point", "form", "off", "child", "few",
    "small", "since", "against", "ask", "late", "home", "interest", "large",
    "person", "end", "open", "public", "follow", "during", "present",
    "without", "again", "hold", "govern", "around", "possible", "head",
    "consider", "word", "program", "problem", "however", "lead", "system",
    "set", "order", "eye", "plan", "run", "keep", "face", "fact", "group",
    "play", "stand", "increase", "early", "course", "change", "help", "line"
]

def run_test(stdscr):
    # Generate random text from 20 random words
    num_words = 20
    target_words = [random.choice(WORDS) for _ in range(num_words)]
    target_text = " ".join(target_words)

    # Clear screen and display the test instructions and text
    stdscr.clear()
    stdscr.addstr(0, 0, "Type the following text:")
    stdscr.addstr(2, 0, target_text, curses.color_pair(3))
    stdscr.addstr(4, 0, "Your input:")
    stdscr.refresh()

    typed = ""
    start_time = None

    # Main loop to capture keystrokes for this test
    while True:
        if start_time is None:
            start_time = time.time()

        key = stdscr.getch()

        # Handle backspace (several possible codes)
        if key in (curses.KEY_BACKSPACE, 127, 8):
            typed = typed[:-1]
        # Only add characters if we haven't reached the target length
        elif len(typed) < len(target_text):
            try:
                typed += chr(key)
            except ValueError:
                continue
            # If the user just typed the last character, end the test.
            if len(typed) == len(target_text):
                # Redraw the final state before finishing
                stdscr.move(2, 0)
                for i, ch in enumerate(target_text):
                    if typed[i] == ch:
                        stdscr.addch(ch, curses.color_pair(1))
                    else:
                        stdscr.addch(ch, curses.color_pair(2))
                stdscr.clrtoeol()
                stdscr.addstr(4, 0, "Your input: " + typed)
                stdscr.clrtoeol()
                stdscr.refresh()
                break
        else:
            continue

        # Redraw target text with letter-by-letter color feedback.
        stdscr.move(2, 0)
        for i, ch in enumerate(target_text):
            if i < len(typed):
                if typed[i] == ch:
                    stdscr.addch(ch, curses.color_pair(1))
                else:
                    stdscr.addch(ch, curses.color_pair(2))
            else:
                stdscr.addch(ch, curses.color_pair(3))
        stdscr.clrtoeol()

        # Update the user's input display
        stdscr.addstr(4, 0, "Your input: " + typed)
        stdscr.clrtoeol()
        stdscr.refresh()

    # Calculate elapsed time and words per minute (WPM)
    elapsed = time.time() - start_time
    word_count = len(target_text.split())
    wpm = word_count / (elapsed / 60)
    stdscr.addstr(6, 0, f"Time: {elapsed:.2f} seconds, WPM: {wpm:.2f}")
    stdscr.refresh()

def main(stdscr):
    # Initialize colors: green for correct, red for incorrect, cyan for untyped
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_CYAN, -1)

    while True:
        run_test(stdscr)
        # Display prompt after finishing the test
        stdscr.addstr(8, 0, "Press Enter to start another test or Escape to quit.")
        stdscr.clrtoeol()
        stdscr.refresh()

        # Wait until user presses only Enter or Escape
        while True:
            key = stdscr.getch()
            if key in (10, 13):  # Enter key
                break  # Start a new test
            elif key == 27:  # Escape key
                return  # Exit the program
            # Ignore any other keys

curses.wrapper(main)
