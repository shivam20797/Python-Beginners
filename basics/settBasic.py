# empty set
emptySet = set()
print(type(emptySet))
emptySet.add("Test")
print(emptySet)
emptySet.update("Test")
emptySet.update(["Test","Test123"])
print(emptySet)


language = {"English","Hindi","Math","English"}
print(language)

# list convert into set
listLanguage = ["English","Hindi","Math","English"]
print(listLanguage)
print(set(listLanguage))