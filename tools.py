import random

# -----------------------------
# JOKE DATABASE (10 per category)
# -----------------------------
JOKES = {
    "tech": [
        "Why do programmers prefer dark mode? Because light attracts bugs 🐛",
        "Why did the computer catch a cold? It left its Windows open 😂",
        "Why do developers hate meetings? Because they are always in a loop 🔁",
        "Why did the developer go broke? Because he used up all his cache 💸",
        "Why was the computer tired? It had too many tabs open 😴",
        "Why did the programmer quit his job? He didn’t get arrays 😆",
        "Why do coders love coffee? Because it helps them Java 😎",
        "Why was the JavaScript developer sad? Because he didn’t ‘null’ his feelings 😢",
        "Why did the phone need therapy? It lost its connection 📱",
        "Why do programmers hate nature? Too many bugs 🌿🐛"
    ],

    "school": [
        "Why did the student eat his homework? Because it was a piece of cake 🍰",
        "Why was the math book sad? Because it had too many problems 📘",
        "Why did the teacher wear sunglasses? Because her students were too bright 😎",
        "Why did the student bring a ladder to school? Because he wanted to go to high school 😂",
        "Why did the pencil go to therapy? It couldn’t draw boundaries ✏️",
        "Why was the history book always calm? Because it knew the past 📚",
        "Why did the student sit on the clock? He wanted to be on time ⏰",
        "Why did the teacher go to the beach? To test the waters 🌊",
        "Why did the student bring string to class? To tie up loose ends 🧵",
        "Why did the student get bad grades? Too many distractions 📱"
    ],

    "dad": [
        "I'm reading a book on anti-gravity. It's impossible to put down 😂",
        "Why don't eggs tell jokes? They’d crack each other up 🥚",
        "I used to play piano by ear, now I use my hands 🎹",
        "Why don’t skeletons fight? They don’t have the guts 💀",
        "I only know 25 letters of the alphabet. I don’t know y 🤔",
        "Did you hear about the restaurant on the moon? Great food, no atmosphere 🌕",
        "I would tell you a construction joke, but I’m still working on it 🚧",
        "Why did the scarecrow become a dad? He was outstanding in his field 🌾",
        "I used to hate facial hair, but then it grew on me 😂",
        "I’m on a seafood diet. I see food and I eat it 🍔"
    ],

    "funny": [
        "Why don’t skeletons fight each other? They don’t have the guts 💀",
        "What do you call fake spaghetti? An impasta 🍝",
        "Why did the scarecrow win an award? Because he was outstanding in his field 🌾",
        "Why did the chicken join a band? Because it had drumsticks 🥁",
        "Why can’t your nose be 12 inches long? Because then it would be a foot 😂",
        "Why did the banana go to the doctor? It wasn’t peeling well 🍌",
        "Why don’t scientists trust atoms? Because they make up everything ⚛️",
        "What do you call a bear with no teeth? A gummy bear 🐻",
        "Why did the coffee file a police report? It got mugged ☕",
        "Why did the math teacher break up? Too many problems 📘"
    ]
}

# -----------------------------
# GLOBAL MEMORY (NO REPEATS)
# -----------------------------
USED_JOKES = set()

# -----------------------------
# STRICT INTENT CHECK
# -----------------------------
def is_joke_request(text):
    text = text.lower()

    keywords = [
        "joke", "funny", "laugh",
        "make me laugh",
        "tell me a joke",
        "another joke",
        "jokes"
    ]

    return any(k in text for k in keywords)


# -----------------------------
# CATEGORY DETECTION
# -----------------------------
def detect_category(text):
    text = text.lower()

    if any(word in text for word in ["code", "computer", "program", "python", "java", "bug"]):
        return "tech"

    elif any(word in text for word in ["school", "teacher", "exam", "study", "student"]):
        return "school"

    elif any(word in text for word in ["dad", "father"]):
        return "dad"

    return "funny"


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def get_joke(text):

    # ❌ BLOCK NON-JOKE INPUTS
    if not is_joke_request(text):
        return "I can only tell jokes."

    # ✅ JOKE REQUEST
    category = detect_category(text)

    available_jokes = [
        joke for joke in JOKES[category]
        if joke not in USED_JOKES
    ]

    # reset if exhausted
    if not available_jokes:
        USED_JOKES.clear()
        available_jokes = JOKES[category]

    joke = random.choice(available_jokes)
    USED_JOKES.add(joke)

    return joke