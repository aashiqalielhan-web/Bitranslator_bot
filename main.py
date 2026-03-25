# Main Bot Code for Bitranslator Bot

class Bitranslator:
    def __init__(self):
        self.translations = {}

    def add_translation(self, word, translation):
        self.translations[word] = translation

    def get_translation(self, word):
        return self.translations.get(word, "Translation not found.")

    def run(self):
        print("Bitranslator Bot is running...")
        while True:
            word = input("Enter a word to translate (or 'exit' to quit): ")
            if word.lower() == 'exit':
                break
            translation = self.get_translation(word)
            print(f'Translation: {translation}')

if __name__ == '__main__':
    bot = Bitranslator()
    bot.add_translation('hello', 'hola')  # example translation
    bot.run()