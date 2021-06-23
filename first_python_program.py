def sentence_maker(phrase):
    iterrogatives = ("who", "what", "where", "when", "why", "how")
    capitalized = phrase.capitalize()
    if phrase.startswith(iterrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


paragraph = []
while True:
    sentence = input("Say something: ")
    if sentence == "\end":
        break
    else:
        paragraph.append(sentence_maker(sentence))

print(" ".join(paragraph))
