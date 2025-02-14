from textblob import TextBlob

def determine_sentiment(sentiment_score):
    if sentiment_score > 0.7:
        return "😄"
    elif 0.5 < sentiment_score <= 0.7:
        return "😊"
    elif 0.3 < sentiment_score <= 0.5:
        return "😃"
    elif 0.1 < sentiment_score <= 0.3:
        return "🙂"
    elif -0.1 <= sentiment_score <= 0.1:
        return "😐"
    elif -0.3 <= sentiment_score < -0.1:
        return "😕"
    elif -0.5 <= sentiment_score < -0.3:
        return "😞"
    elif -0.7 <= sentiment_score < -0.5:
        return "😢"
    else:
        return "😭"

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return determine_sentiment(sentiment_score)

def suggest_emoji(text, noun_emojis, verb_emojis):
    detected_emojis = []
    words = text.split()
    for i, word in enumerate(words):
        if word.lower() == "not" and i+1 < len(words):
            detected_emojis.append("❌" + noun_emojis.get(words[i+1].lower(), "") + verb_emojis.get(words[i+1].lower(), ""))
        elif word.lower() in noun_emojis:
            detected_emojis.append(noun_emojis[word.lower()])
        elif word.lower() in verb_emojis:
            detected_emojis.append(verb_emojis[word.lower()])
    return " ".join(detected_emojis)

def cricket_performance_statement(runs, balls):
    if balls == 0:
        return "No balls bowled, unable to determine performance."
    elif runs / balls >= 1.5:
        return "Excellent performance"
    elif runs / balls >= 1:
        return "Good performance"
    elif runs / balls >= 0.5:
        return "Okayish performance"
    else:
        return "Poor performance"

user_input = input("Enter your text: ")

noun_emojis = { 
    "cat": "😺", "dog": "🐶", "food": "🍔", "love": "❤️", "car": "🚗","hot" :"🥵♨️",
    "tree": "🌳", "house": "🏠", "book": "📚", "coffee": "☕", "sun": "☀️",
    "moon": "🌙", "star": "⭐", "heart": "💖", "guitar": "🎸", "flower": "🌸",
    "pizza": "🍕", "ice cream": "🍦", "computer": "💻", "phone": "📱","croissant" :"🥐","subject" : "📚",
    "money": "💰", "bird": "🐦", "fish": "🐟", "apple": "🍎", "banana": "🍌",
    "chocolate": "🍫", "cookie": "🍪", "football": "⚽", "basketball": "🏀", "cricket": "🏏",
    "globe": "🌍", "rocket": "🚀", "train": "🚂", "umbrella": "☔",
    "bicycle": "🚲", "camera": "📷", "microphone": "🎤", "paperclip": "📎",
    "pushpin": "📌", "flag": "🚩", "stop sign": "🛑", "traffic light": "🚦",
    "construction": "🚧", "barrier": "🚧", "cones": "🚧", "tool": "🛠️",
    "hammer": "🔨", "wrench": "🔧", "screwdriver": "🪛", "bolt": "🔩",
    "nut": "🔩", "ladder": "🪜", "stairs": "🪜", "elevator": "🪟","you": "🫵",
    "escalator": "🪟", "window": "🪟", "door": "🪟", "magnifying glass": "🔍",
    "telescope": "🔭", "microscope": "🔬", "test tube": "🧪", "thermometer": "🌡️",
    "scale": "⚖️", "ruler": "📏", "meter": "📏", "tape measure": "📏",
    "compass": "🧭", "protractor": "📐", "level": "📐", "laptop": "💻",
    "desktop": "💻", "screen": "💻", "monitor": "💻", "keyboard": "⌨️",
    "mouse": "🖱️", "trackball": "🖱️", "printer": "🖨️", "scanner": "🖨️",
    "fax": "🖨️", "telephone": "☎️", "cell phone": "📱", "smartphone": "📱",
    "mobile phone": "📱", "tablet": "📱", "remote": "📱", "watch": "⌚",
    "clock": "⏰", "alarm clock": "⏰", "hourglass": "⏳", "stopwatch": "⏱️",
    "timer": "⏱️", "calendar": "📅", "date": "📅", "date": "📆",
    "tear-off calendar": "📅", "spiral calendar": "🗓️", "memo": "📝",
    "notepad": "📝", "notebook": "📒", "journal": "📓", "diary": "📔",
    "ledger": "📒", "books": "📚", "book": "📖", "open book": "📖",
    "green book": "📗", "blue book": "📘", "orange book": "📙",
    "stack of books": "📚", "newspaper": "📰", "rolled-up newspaper": "🗞️",
    "magazine": "📖", "folder": "📁", "file folder": "📁",
    "open file folder": "📂", "clipboard": "📋", "board": "📋",
    "paper": "📃", "scroll": "📜", "page": "📄", "receipt": "🧾",
    "label": "🏷️", "bookmark": "🔖", "link": "🔗", "chains": "⛓️",
    "cog": "⚙️", "gear": "⚙️", "pick": "⛏️", "hammer and pick": "⛏️",
    "hammer and wrench": "🛠️", "dagger": "🗡️", "gun": "🔫",
    "bomb": "💣", "shield": "🛡️", "parasol": "🌂", "bed": "🛏️",
    "couch": "🛋️", "sofa": "🛋️", "chair": "🪑", "toilet": "🚽",
    "shower": "🚿", "bathtub": "🛁", "sink": "🚰", "mirror": "🪞","home": "🏠",
    "house": "🏠",
    "dog": "🐶",
    "cat": "🐱",
    "cricket": "🏏",
    "football": "⚽",
    "basketball": "🏀",
    "people": "👫",
    "person": "👤",
    "hot": "🔥",
    "seasons": "🌤️",
    "love": "❤️",
    "not": "❌",
    "go": "🚶",
    "cold": "❄️",
    "hate": "😡",
    "disagree": "👎",
    "adore": "😍",
    "hide": "🙈",
    "shy": "😳",
    "blush": "☺️",
    "cute": "🥰",
    "mind": "🤯",
    "excellent": "👍",
    "shock": "😱",
}

verb_emojis = { 
    "run": "🏃", "jump": "🤾", "eat": "🍽️", "sleep": "😴", "play": "🎮",
    "sing": "🎤", "dance": "💃", "read": "📖", "write": "✍️", "draw": "✏️",
    "swim": "🏊", "fly": "✈️", "drive": "🚗", "walk": "🚶", "talk": "🗣️",
    "listen": "👂", "laugh": "😂", "cry": "😢", "smile": "😊", "frown": "☹️",
    "clap": "👏", "wave": "👋", "hug": "🤗", "kiss": "💋", "fight": "🥊",
    "build": "🏗️", "cook": "👩‍🍳", "clean": "🧹", "study": "📚", "work": "💼",
    "exercise": "🏋️", "meditate": "🧘", "pray": "🙏", "celebrate": "🎉",
    "travel": "✈️", "explore": "🌍", "discover": "🔍", "create": "🎨",
    "teach": "👩‍🏫", "learn": "📚", "grow": "🌱", "help": "🤝", "serve": "🍽️",
    "give": "🎁", "receive": "🎁", "brush": "🖌️", "paint": "🎨", "wash": "🧼",
    "dry": "👕", "fold": "👕", "iron": "🔨", "scrub": "🧽", "sweep": "🧹",
    "mop": "🧹", "organize": "🪟", "tidy": "🪟", "fix": "🔨", "repair": "🔧",
    "maintain": "🔧", "assemble": "🔧", "construct": "🔨", "design": "🎨",
    "plan": "📝", "schedule": "📅", "prepare": "👩‍🍳", "bake": "👩‍🍳",
    "roast": "👩‍🍳", "grill": "👩‍🍳", "fry": "👩‍🍳", "stir": "👩‍🍳","not happy" :"😞",
    "mix": "👩‍🍳", "whisk": "👩‍🍳", "chop": "👩‍🍳", "slice": "👩‍🍳",
    "peel": "👩‍🍳", "pour": "👩‍🍳", "serve": "🍽️", "taste": "👅", "drink": "🍹",
    "sip": "🍹", "gulp": "🍹", "swallow": "🍹", "bite": "🍽️", "chew": "🍽️",
    "swallow": "🍽️", "digest": "🍽️", "absorb": "🍽️", "consume": "🍽️",
    "inhale": "💨", "exhale": "💨", "breathe": "💨", "nap": "😴", "doze": "😴",
    "rest": "😴", "dream": "💭", "snore": "💤", "sleepwalk": "😴",
    "awaken": "⏰", "rise": "⏰", "shine": "☀️", "wake": "⏰","not" :"❌",
    "light up": "💡", "glisten": "☀️","don't": "❌",
}

sentences = user_input.split(".")
output = ""

for sentence in sentences:
    sentiment_emoji = analyze_sentiment(sentence)
    emoji_suggestions = suggest_emoji(sentence, noun_emojis, verb_emojis)
    output += f"Analyzed sentiment = {sentiment_emoji}, {'  '}{emoji_suggestions}. "
    
    if "scored" in sentence.lower() and "runs" in sentence.lower() and "balls" in sentence.lower():
        words = sentence.split()
        runs_index = words.index("runs")
        balls_index = words.index("balls")
        runs = int(words[runs_index - 1])
        balls = int(words[balls_index - 1])
        performance_statement = cricket_performance_statement(runs, balls)
        performance_emoji = determine_sentiment(TextBlob(performance_statement).sentiment.polarity)
        
        if performance_emoji == "😄":
            output += f"{performance_statement} = {performance_emoji}👍. "
        if performance_emoji == "😊":
            output += f"{performance_statement} = {performance_emoji}👏."
        else:
            output += f"{performance_statement} = {performance_emoji}👎. "
    
print(output[:-2])
