import random

class QuickBot:
    def __init__(self):
        self.emotions = {
            'happy': ['happy', 'great', 'awesome', 'wonderful', 'excited'],
            'sad': ['sad', 'depressed', 'lonely', 'down', 'miserable'],
            'anxious': ['anxious', 'worried', 'nervous', 'stressed', 'scared'],
            'angry': ['angry', 'mad', 'furious', 'frustrated', 'annoyed'],
            'crisis': ['suicide', 'kill myself', 'want to die', 'end it all', 'die']
        }
        
        self.replies = {
            'happy': ["That's wonderful!", "Great to hear!", "I'm glad you're feeling good!"],
            'sad': ["I'm sorry you're feeling sad.", "Want to talk about it?", "I understand."],
            'anxious': ["Take a deep breath.", "Let's work through this.", "You're safe."],
            'angry': ["I hear you.", "What happened?", "Let's talk."],
            'crisis': ["CALL 988 NOW! Your life matters."],
            'neutral': ["I'm listening.", "Tell me more.", "How can I help?"]
        }
    
    def detect_emotion(self, text):
        text_lower = text.lower()
        for word in self.emotions['crisis']:
            if word in text_lower:
                return 'crisis'
        for emotion, words in self.emotions.items():
            if emotion == 'crisis':
                continue
            for word in words:
                if word in text_lower:
                    return emotion
        return 'neutral'
    
    def get_response(self, text):
        emotion = self.detect_emotion(text)
        response = random.choice(self.replies[emotion])
        return response, emotion
