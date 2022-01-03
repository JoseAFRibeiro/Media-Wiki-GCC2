
def createPageFile(title: str, description: str, rating: float):
    pagestr = "{{-start-}}\n ${description}\n ====Rating===\n ${rating}\n{{-stop-}}"
    f = open("%s" % (title), "w+")
    pagestr = pagestr.replace("${description}", description)
    pagestr = pagestr.replace("${rating}", str(rating))
    f.write(pagestr)
    f.close()
    return
