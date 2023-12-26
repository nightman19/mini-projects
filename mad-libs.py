"""Mad Libs is a phrasal template word game consisting of one player prompting others for a list of words to substitute for blanks in a story before reading aloud."""


def mad_libs():
	"""The function takes prompt a user-input and insert the result into the story template and at the end of completing the template display a full story
	"""
	story_template = """Today I went to the zoo. I saw a(n) {adjective} {animal}\njumping up and down in its tree. He {verb}ed {adverb}\nthrough the large {noun}. I got a little scared when\na big {adjective} {animal} escaped from its cage and\n{verb}ed right past me!\n"""

	# Gets inputs from user
	print(story_template)
	words = {
        "adjective": input("Enter an adjective: "),
        "animal": input("Enter an animal: "),
        "verb": input("Enter a verb: "),
        "adverb": input("Enter an adverb: "),
        "noun": input("Enter a noun: "),
        "adjective2": input("Enter another adjective: "),
        "animal2": input("Enter another animal: "),
        "verb2": input("Enter another verb: "),
    }


	story = story_template.format(**words)

	# Print the complete story
	print('\nHere is your Mad-Libs story:\n')
	print(story)

if __name__ == '__main__':
 	mad_libs()
