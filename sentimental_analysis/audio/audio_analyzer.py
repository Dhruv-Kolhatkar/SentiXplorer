import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

## Audio Analyzer class for Audio Sentiment Analysis
class AudioAnalyzer:

    def __init__(self):
        pass

    ## method takes in param file path of .wav audio file and returns corresponding text
    def speech_to_text(self, filename):
        r = sr.Recognizer()

        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            # print(text)
            return text

    ## methods takes in param sentence text and returns python dictionary containing pos, neg, neutral sentiment
    def sentiment_analyzer_scores(self, sentence):
        analyser = SentimentIntensityAnalyzer()

        score = analyser.polarity_scores(sentence)
        # print("{:-<40} {}".format(sentence, str(score)))
        return score





## Usage
'''
aa = AudioAnalyzer()
text = aa.speech_to_text("test_wv.wav")
print(aa.sentiment_analyzer_scores(text))
'''
