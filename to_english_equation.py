# another pig_latin to english translator

def to_english(raw_pig_latin):
    if raw_pig_latin[-3:].lower() == "yay":
        non_pig = raw_pig_latin[:-3]
        return correct_cap(raw_pig_latin[-3:], non_pig)

    if raw_pig_latin[-2:].lower() != "ay":
        print()
        raise TypeError()

    raw_pig_latin = raw_pig_latin[:-2]
    last_two = raw_pig_latin[-2:]

    constant_clusters = set(["br", "cr", "dr", "fr", "gr", "pr", "tr", "sc",
                             "sk", "sl", "sm", "sn", "sp", "st", "sw", "bl",
                             "cl", "fl", "gl", "pl", "sh", "ch", "th", "wh",
                             "ph", "gh", "ng"])
    if last_two in constant_clusters:
        non_pig = raw_pig_latin[-2:] + raw_pig_latin[:-2]
        return correct_cap(raw_pig_latin, non_pig)

    tripple_constant = set(["str", "spr", "thr", "chr", "phr", "shr"])

    last_three = raw_pig_latin[-3:]

    if last_three in tripple_constant:
        non_pig = raw_pig_latin[-3:] + raw_pig_latin[:-3]
        return correct_cap(raw_pig_latin, non_pig)

    non_pig = raw_pig_latin[-1:] + raw_pig_latin[:-1]
    return correct_cap(raw_pig_latin, non_pig)


def correct_cap(pig_string, non_pig):
    if pig_string.islower():
        return non_pig.lower()
    if pig_string.isupper():
        return non_pig.isupper()
    return non_pig.title()


test_data = {
    "untedhay": "hunted",
    "iestday": "diest",
    "acesfay": "faces",
    "Eyondbay": "Beyond",
    "Indfay": "Find",
    "icksay": "sick",
    "unsay": "sun",
    "awakeyay": "awake",
    "Illway": "Will",
    "Oremay": "More",
    "invitedyay": "invited",
    "iesday": "dies",
    "ixedmay": "mixed",
    "Eathedbray": "Breathed",
    "evernay": "never",
    "oneyhay": "honey",
    "earday": "dear",
    "ou'Thay": "'Thou",
    "is'tay": "'tis",
    "event'stpray": "prevent'st",
    "easontray": "treason",
    "ublicpay": "public",
    "onfoundedcay": "confounded",
    "owblay": "blow",
    "atwhay": "what",
    "Implysay": "Simply",
    "itsfay": "fits",
    "ivestray": "strive",
    "antonlyway": "wantonly",
    "Iiixxxay": "XXXIII",
    "imbeckslay": "limbecks",
    "ememberedray": "remembered",
    "ambushyay": "ambush",
    "acespay": "space",
    "ushhay": "hush",
    "Entay": "Ten",
    "ysicianphay": "physician",
    "ancay": "can",
    "illwrestingyay": "illwresting",
    "aloftyay": "aloft",
    "annedtay": "tanned",
    "Oundway": "Wound",
    "easonsray": "reasons",
    "extremeyay": "extreme",
    "ormsway": "worms",
    "eceaseday": "decease",
    "Eed'stfay": "Feed'st",
    "uprearyay": "uprear",
    "oilspay": "spoil",
    "Icxlay": "CXLI",
    "oughtsay": "sought",
    "ullensay": "sullen",
    "instinctyay": "instinct",
    "ashionfay": "fashion",
    "Elfsay": "Self",
    "assedpay": "passed",
    "airlyfay": "fairly",
    "iefsgray": "griefs",
    "evourday": "devour",
    "isdainday": "disdain",
    "urgingpay": "purging",
    "indedmay": "minded",
    "enurypay": "penury",
    "uchmay": "much",
    "O'Erchargedyay": "O'ercharged",
    "avitygray": "gravity",
    "eryvay": "very",
    "urdenbay": "burden",
    "olfway": "wolf",
    "ifeway": "wife",
    "ewelsjay": "jewels",
    "otenay": "note",
    "eclipsesyay": "eclipses",
    "ovidepray": "provide",
    "illway": "will",
    "augursyay": "augurs",
    "esagepray": "presage",
    "erethay": "there",
    "oubtingday": "doubting",
    "Icay": "CI",
    "Iixxvay": "XXVII",
    "eaplay": "leap",
    "Encewhay": "Whence",
    "eturnray": "return",
    "illhay": "hill",
    "isyay": "is",
    "earpurchasedday": "dearpurchased",
    "eignedray": "reigned",
    "oftyay": "oft",
    "aithsay": "saith",
    "ournfulmay": "mournful",
    "emalefay": "female",
    "iumphanttray": "triumphant",
    "ermilionvay": "vermilion",
    "Aymay": "May",
    "Othbay": "Both",
    "illion'dmay": "million'd",
    "earthay": "heart",
    "ersesvay": "verses",
    "eatsay": "seat",
    "oicesvay": "voices",
    "illedfay": "filled",
    "acultyfay": "faculty",
    "aysstay": "stays",
    "Oorpay": "Poor",
    "ereforethay": "therefore",
    "arstay": "star",
    "Xyay": "X",
    "eedway": "weed",
    "osay": "so",
    "ervantsay": "servant",
    "antway": "want",
    "earnedlay": "learned",
    "atherfay": "father",
    "ingthay": "thing",
    "Lvyay": "LV",
    "enemiesyay": "enemies",
    "Usicmay": "Music",
    "usuryyay": "usury",
    "ardway": "ward",
    "erfectpay": "perfect",
    "Ethay": "The",
    "oryglay": "glory",
    "earthyay": "earth",
    "ampstay": "stamp",
    "esmear'dbay": "besmear'd",
    "ot'nay": "'not",
    "adlyglay": "gladly",
    "iger'stay": "tiger's",
    "essingsdray": "dressings",
    "iescray": "cries",
    "eastyay": "east",
    "istanceday": "distance",
    "akeway": "wake",
    "aidyay": "aid",
    "entrecay": "centre",
    "oncordcay": "concord",
    "iftfootedsway": "swiftfooted",
    "orsakefay": "forsake",
    "udgment'sjay": "judgment's",
    "orbiddenfay": "forbidden",
    "erewhay": "where",
    "ieday": "die",
    "eessay": "sees",
    "appetitesyay": "appetites",
    "iewvay": "view",
    "enoughyay": "enough",
    "appealyay": "appeal",
    "extnay": "next",
    "eathbedday": "deathbed",
    "ontendcay": "contend",
    "akednay": "naked",
    "ow'styay": "ow'st",
    "uildingbay": "building",
    "inlythay": "thinly",
    "ontentcay": "content",
    "Ishay": "His",
    "ulytray": "truly",
    "Orgotfay": "Forgot",
    "eglectnay": "neglect",
    "udelyray": "rudely",
    "aysay": "say",
    "oanmay": "moan",
    "Eternalyay": "Eternal",
    "Onsumedcay": "Consumed",
    "aidsay": "said",
    "offence'syay": "offence's",
    "yranttay": "tyrant",
    "Eedsway": "Weeds",
    "inventyay": "invent",
    "affairsyay": "affairs",
    "akelessmay": "makeless",
    "ueshay": "hues",
    "orthierway": "worthier",
    "uehay": "hue",
    "Ativitynay": "Nativity",
    "Yetyay": "Yet",
    "ere'sthay": "there's",
    "Eath'Sday": "Death's",
    "iversthray": "thrivers",
    "ercymay": "mercy",
    "ightmay": "might",
    "ithalway": "withal",
    "abouringlay": "labouring",
    "ypray": "pry",
    "emoveray": "remove",
    "ualityqay": "quality",
    "o'eryay": "o'er",
    "owerstay": "towers",
    "ee'stsay": "see'st",
    "orwardsfay": "forwards",
    "acegray": "grace",
    "Ixlvay": "XLVI",
    "urlysay": "surly",
    "owardstay": "towards",
    "aightstray": "straight",
    "others'yay": "others'",
    "essaysyay": "essays",
    "Amen''Ay": "'Amen'",
    "Ixxxay": "XXXI",
    "Usthay": "Thus",
    "arrestyay": "arrest",
    "Antway": "Want",
    "onsetyay": "onset",
    "ancelledcay": "cancelled",
    "artherfay": "farther",
    "ookedlay": "looked",
    "Utyday": "Duty",
    "ookedcray": "crooked",
    "earlyyay": "early",
    "esidesbay": "besides",
    "Oudsclay": "Clouds",
    "istressmay": "mistress",
    "enancepay": "penance",
    "Lxxvyay": "LXXV",
    "essengersmay": "messengers",
    "orgetfay": "forget",
    "uesttray": "truest",
    "eepskay": "keeps",
    "ickle'ssay": "sickle's",
    "areshay": "share",
    "iscalledmay": "miscalled",
    "Itypay": "Pity",
    "eisurelay": "leisure",
    "eyeyay": "eye",
    "ickensay": "sicken",
    "earingsway": "swearing",
    "inefay": "fine",
    "eachesttay": "teachest",
    "oughtthay": "thought",
    "easantplay": "pleasant",
    "eemlysay": "seemly",
    "oppressedyay": "oppressed",
    "aceplay": "place",
    "ut'stpay": "put'st",
    "ereofwhay": "whereof",
    "useryay": "user",
    "artpay": "part",
    "ertaincay": "certain",
    "addingmay": "madding",
    "eliveredday": "delivered",
    "eardbay": "beard",
    "embassyyay": "embassy",
    "aitbay": "bait",
    "yramidspay": "pyramids",
    "Irredstay": "Stirred",
    "Aisingpray": "Praising",
    "Icvay": "CVI",
    "eefay": "fee",
    "unetay": "tune",
    "olestay": "stole",
    "Iiilxvay": "LXVIII",
    "universeyay": "universe",
    "endsay": "send",
    "ardonpay": "pardon",
    "Elltay": "Tell",
    "ander'sslay": "slander's",
    "onguestay": "tongues",
    "alliestay": "tallies",
    "Ehay": "He",
    "atelessday": "dateless",
    "inyay": "in",
    "oftenyay": "often",
    "oodblay": "blood",
    "eservepray": "preserve",
    "irectlyday": "directly",
    "Omwhay": "Whom",
    "inheritorsyay": "inheritors",
    "irefay": "fire",
    "Iftslay": "Lifts",
    "opsstay": "stops",
    "areray": "rare",
    "urlchay": "churl",
    "Iicay": "CII",
    "idow'dway": "widow'd",
    "Ivcxlay": "CXLIV",
    "amesshay": "shames",
    "ecayday": "decay",
    "o'erpressedyay": "o'erpressed",
    "Atehay": "Hate",
    "ingedway": "winged",
    "arcay": "car",
    "adsay": "sad",
    "ymnshay": "hymns",
    "Iicxay": "CXII",
    "acefay": "face",
    "akentay": "taken",
    "aciouslygray": "graciously",
    "ueday": "due",
    "otsblay": "blots",
    "Ilvay": "LVI",
    "other'smay": "mother's",
    "esidebay": "beside",
    "eadspray": "spread",
    "ewfay": "few",
    "absentyay": "absent",
    "iritspay": "spirit",
    "endingbay": "bending",
    "aritiesray": "rarities",
    "actyay": "act",
    "altshay": "shalt",
    "uchsay": "such",
    "ayerspray": "prayers",
    "overplusyay": "overplus",
    "itterbay": "bitter",
    "orrysay": "sorry",
    "Ivcxxay": "CXXIV",
    "entspay": "spent",
    "ightbray": "bright",
    "Ivxxay": "XXIV",
    "Iiilay": "LIII",
    "efiguringpray": "prefiguring",
    "eguil'dbay": "beguil'd",
    "accuseyay": "accuse",
    "Yselfmay": "Myself",
    "onourhay": "honour",
    "oughtnay": "nought",
    "iefchay": "chief",
    "Insay": "Sin",
    "or'tfay": "for't",
    "ayedplay": "played",
    "eetgray": "greet",
    "Admay": "Mad",
    "emovedray": "removed"
}


for key, value in test_data.items():
    if to_english(key) != value:
        print("error: wanted '{0}', got '{1}'".format(value, to_english(key)))