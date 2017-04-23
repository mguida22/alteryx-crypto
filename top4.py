import operator
import json

x = "allCay emay Ishmaelyay. omeSay yearsyay agoyay- evernay indmay owhay onglay eciselypray- avinghay ittlelay oryay onay oneymay inyay ymay ursepay, andyay othingnay articularpay otay interestyay emay onyay oreshay, Iyay oughtthay Iyay ouldway ailsay aboutyay ayay ittlelay andyay eesay ethay ateryway artpay ofyay ethay orldway. Ityay isyay ayay ayway Iyay avehay ofyay ivingdray offyay ethay eensplay andyay egulatingray ethay irculationcay. eneverWhay Iyay indfay yselfmay owinggray imgray aboutyay ethay outhmay; eneverwhay ityay isyay ayay ampday, izzlydray ovemberNay inyay"

most_common = {}

for i in range(len(x) - 3):
    item = x[i:i + 4]

    if item in most_common.keys():
        most_common[item] += 1
    else:
        most_common[item] = 1


sorted_x = sorted(most_common.items(), key=operator.itemgetter(1))


print(json.dumps(sorted_x, indent=1))
