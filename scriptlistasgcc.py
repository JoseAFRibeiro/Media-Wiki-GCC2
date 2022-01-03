import rapidminer
from pageCreater import createPageFile
minerhome = "C:\Program Files\RapidMiner\RapidMiner Studio"


def main():
    ogtittle = []
    ogdesc = []
    ograting = []
    mediastrings = []
    miner = rapidminer.Studio(minerhome)
    minerinput = miner.run_process("//Local Repository/processes/Select movies")

    minerinput = minerinput.__getitem__(['original_title', 'description', 'avg_vote'])

    for i in minerinput['original_title']:
        ogtittle.append(i)

    for i in minerinput['description']:
        ogdesc.append(i)

    for i in minerinput['avg_vote']:
        ograting.append(i)

    createPageFile(ogtittle[0], ogdesc[0], ograting[0])

    # for i in ogtittle:
    #     mediastrings.append("{{%s}}" % (i))


if __name__ == '__main__':
    main()