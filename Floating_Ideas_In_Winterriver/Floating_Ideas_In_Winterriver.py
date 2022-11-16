# Floating Ideas in Winterriver
#
# Finding the most common / rare character in the list:
# - put the text in a variable (multiline string or a list of strings)
# - if necessary, split the text by end of line (\n)
# - go through each line of the text
# - split each line by colon, the left part being the company name, the right one the category
# - go through each character in the company name
# - create a dictionary (map) of all characters, using the character as the key and the occurrences as the value
# - sort the dictionary by the values
# - take the top / bottom three entries
#
# Sorting the companies by category:
# - use the company and category as read in the first part of this exercise
# - create a dictionary (map) with the category as the key and a list of companies as the value
# - go through each line and put each company in a category of the dictionary
#
# Company Names: Categories
text = """Inspiration Alley: Education
Love Homework Ideas: Education
Winterriver City : State
Sugarless Berries: Health
Soul of Climate: Environment
Feed the Feedback: Tech
Demonetize Money: Business
Digital Pills: Health
Greenish Streets: Umwelt
Happitize Happiness: Health
Government Ambition: State
Life Long Sharing: Education
Efficiently Codified: Tech
Stating Statements: State
Water Falling: Environment
StoryCoder.dev: Tech
Office Friends: Business
The Scabby Cockroach: Environment
Spaces and Cows: Environment
Guess or Code? : Tech
Accounting without Counting: Business
Gramming a Pro: Tech"""

occurrences = {}
categories = {}

for line in text.split('\n'):
    items = line.split(':')
    company, category = line.split(':')
    category = category.strip()
    company = company.strip()
    for c in company.lower():
        if c == ' ' or c == '?' or c == '.':
            continue
        if c not in occurrences:
            occurrences[c] = 1
        else:
            occurrences[c] += 1
    if category not in categories:
        categories[category] = [company]
    else:
        categories[category].append(company)
    
# print(occurrences)
print(sorted(occurrences, key=occurrences.get, reverse=True)[:3])
print(sorted(occurrences, key=occurrences.get, reverse=False)[:3])
// if you look well at the results, you might notice that s and t might both be the third top result:
// discuss what options you have to solve this.

print(categories)
