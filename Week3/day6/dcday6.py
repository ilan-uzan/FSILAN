# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like "Today, is a happy day" or it can be an external text file.



# Part I
# First, we will analyze a simple string, like "A good book would sometimes cost as much as a good house."

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.



# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.

# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        if count > 0:
            return f"The word '{word}' appears {count} times in the text."
        else:
            return f"The word '{word}' does not appear in the text."
    
    def most_common_word(self):
        words = self.text.lower().split()
        word_count = {}
        
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        max_count = 0
        most_common = ""
        
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                most_common = word
                
        return most_common
    
    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))
    
    @classmethod
    def from_file(cls, file_path):
        import os
        # Get the current script directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Create absolute path to the file
        abs_file_path = os.path.join(current_dir, file_path)
        
        with open(abs_file_path, 'r') as file:
            text_content = file.read()
        return cls(text_content)


class TextModification(Text):
    def remove_punctuation(self):
        import string
        translator = str.maketrans('', '', string.punctuation)
        return self.text.translate(translator)
    
    def remove_stop_words(self):
        stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
                      'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 
                      'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 
                      'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 
                      'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 
                      'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
                      'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 
                      'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 
                      'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
                      'through', 'during', 'before', 'after', 'above', 'below', 'to', 
                      'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 
                      'again', 'further', 'then', 'once', 'here', 'there', 'when', 
                      'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
                      'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 
                      'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 
                      'just', 'don', 'should', 'now']
        
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)
    
    def remove_special_chars(self):
        import re
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)


# Example usage
if __name__ == "__main__":
    # Part I
    sample_text = "A good book would sometimes cost as much as a good house."
    text_instance = Text(sample_text)
    
    print("PART I: Analyzing a simple string")
    print("-" * 40)
    print(text_instance.word_frequency("good"))
    print(f"Most common word: {text_instance.most_common_word()}")
    print(f"Unique words: {text_instance.unique_words()}")
    print()
    
    # Part II - Using the_stranger.txt file
    print("PART II: Analyzing text from the_stranger.txt file")
    print("-" * 40)
    stranger_text = Text.from_file('the_stranger.txt')
    print(stranger_text.word_frequency("the"))
    print(stranger_text.word_frequency("mother"))
    print(f"Most common word in The Stranger: {stranger_text.most_common_word()}")
    print(f"Number of unique words: {len(stranger_text.unique_words())}")
    print()
    
    # Bonus
    print("BONUS: Text modification")
    print("-" * 40)
    text_mod = TextModification(sample_text)
    print(f"Text without punctuation: {text_mod.remove_punctuation()}")
    print(f"Text without stop words: {text_mod.remove_stop_words()}")
    print(f"Text without special characters: {text_mod.remove_special_chars()}")
    
    # Bonus with The Stranger
    print()
    print("BONUS: Text modification with The Stranger (first 100 characters)")
    print("-" * 40)
    stranger_mod = TextModification(stranger_text.text[:100])
    print(f"Original excerpt: {stranger_mod.text}")
    print(f"Without punctuation: {stranger_mod.remove_punctuation()}")
    print(f"Without stop words: {stranger_mod.remove_stop_words()}")
    print(f"Without special characters: {stranger_mod.remove_special_chars()}")

