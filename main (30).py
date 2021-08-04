import wikipedia as wiki
print(wiki.search("Xiaomi"))
print(wiki.suggest("Tech"))
print(wiki.summary("Xiaomi"))

wiki.set_lang("en")
p = wiki.page("Xiaomi")
print(p.title)
print(p.url)
print(p.content)
print(p.images)
print(p.links)