# source: https://www.datacamp.com/community/tutorials/web-scraping-python-nlp
# función para sacar gráfico de frecuencia de palabras en texto (novelas en proyecto Gutenberg)

def plot_word_freq(url):
    """Takes a url (from Project Gutenberg) and plots a word frequency
    distribution"""
    # Make the request and check object type
    r = requests.get(url)
    # Extract HTML from Response object and print
    html = r.text
    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, "html5lib")
    # Get the text out of the soup and print it
    text = soup.get_text()
    # Create tokenizer
    tokenizer = RegexpTokenizer('\w+')
    # Create tokens
    tokens = tokenizer.tokenize(text)
    # Initialize new list
    words = []
    # Loop through list tokens and make lower case
    for word in tokens:
        words.append(word.lower())
    # Get English stopwords and print some of them
    sw = nltk.corpus.stopwords.words('english')
    # Initialize new list
    words_ns = []
    # Add to words_ns all words that are in words but not in sw
    for word in words:
        if word not in sw:
            words_ns.append(word)
    # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(25)

# Examples:

# Pride and Prejudice:
plot_word_freq('https://www.gutenberg.org/files/42671/42671-h/42671-h.htm')

# Robinson Crusoe
plot_word_freq('https://www.gutenberg.org/files/521/521-h/521-h.htm')

# The King James Bible
plot_word_freq('https://www.gutenberg.org/files/10/10-h/10-h.htm')
w
