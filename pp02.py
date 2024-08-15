try:
    import nltk
    import random
    import string
    import warnings
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError as e:
    import os
    os.system('pip install nltk scikit-learn')
    import nltk
    import random
    import string
    import warnings
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings("ignore", category=UserWarning, module='nltk')

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Sample data for the chatbot
data = """
Hello! How can I help you today?
I am a chatbot designed to assist you with basic queries.
You can ask me about the weather, general knowledge, or just have a casual conversation.
I'm here to help you.
"""

# Preprocessing the data
def preprocess(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    return text

# Tokenize the raw data
sent_tokens = nltk.sent_tokenize(data)
word_tokens = nltk.word_tokenize(data)

# Lemmatizer to normalize text
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Generate responses
def response(user_response):
    chatbot_response = ''
    sent_tokens.append(user_response)
    
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if(req_tfidf == 0):
        chatbot_response = "I am sorry! I don't understand you."
    else:
        chatbot_response = sent_tokens[idx]
    
    sent_tokens.pop()
    return chatbot_response

# Greeting function
def greeting(sentence):
    greetings = ["hi", "hello", "hey", "hola", "greetings", "wassup", "hi there"]
    responses = ["hi", "hey", "hello", "hola", "greetings", "hi there"]
    
    for word in sentence.split():
        if word.lower() in greetings:
            return random.choice(responses)
    
    return None

# Main chatbot function
def chatbot():
    print("Chatbot: Hi! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_response = input("You: ")
        user_response = user_response.lower()
        
        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you':
                print("Chatbot: You're welcome!")
                break
            else:
                if greeting(user_response) is not None:
                    print("Chatbot:", greeting(user_response))
                else:
                    print("Chatbot:", response(user_response))
        else:
            print("Chatbot: Bye! Take care.")
            break

# Run the chatbot
chatbot()
