import wikipedia
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

top50 = ["Jesus", "Napoleon", "Muhammad", "William Shakespeare", "Abraham Lincoln", "George Washington", "Adolf Hitler", "Aristotle", "Alexander the Great", "Thomas Jefferson", "Henry VIII of England", "Charles Darwin", "Elizabeth I of England", "Karl Marx", "Julius Caesar", "Queen Victoria", "Martin Luther", "Joseph Stalin", "Albert Einstein", "Christopher Columbus", "Isaac Newton", "Charlemagne", "Theodore Roosevelt", "Wolfgang Amadeus Mozart", "Plato", "Louis XIV of France", "Ludwig van Beethoven", "Ulysses S. Grant", "Leonardo da Vinci", "Augustus", "Carl Linnaeus", "Ronald Reagan", "Charles Dickens", "Paul the Apostle", "Benjamin Franklin", "George W. Bush", "Winston Churchill", "Genghis Khan", "Charles I of England", "Thomas Edison", "James I of England", "Friedrich Nietzsche", "Franklin D. Roosevelt", "Sigmund Freud", "Alexander Hamilton", "Mohandas Karamchand Gandhi", "Woodrow Wilson", "Johann Sebastian Bach", "Galileo Galilei", "Oliver Cromwell"]
wikiContent = []

for name in top50:
	page = wikipedia.page(name)
	wikiContent.append(page.content)

scores = []

for c in wikiContent:
	scores.append(SentimentIntensityAnalyzer().polarity_scores(c))

pos = []
neg = []

for s in scores:
	pos.append(s['pos'])
	neg.append(s['neg'])

plt.plot(pos, neg, 'bo')
plt.xlabel('pos')
plt.ylabel('neg')
plt.show()