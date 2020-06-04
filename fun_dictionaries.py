def player(name, *scores, **about):
    print("Player:", name)
    for score in scores:
        print(score)
    for kw in about:
        print(kw, ":", about[kw])

player("John Smith", 
        "12", "8", "32", "0",
        number="22", position="WR", team="DAL")