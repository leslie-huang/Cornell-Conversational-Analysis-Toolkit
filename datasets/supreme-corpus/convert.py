# convert into toolkit json format
import json

MaxUtterances = -1

KeyId = "id"
KeySpeaker = "speaker"
KeyConvoRoot = "conversation_id"
KeyReplyTo = "reply-to"
KeySpeakerInfo = "meta"  # can store any extra data
import time
import datetime

KeyText = "text"

with open("supreme.gender.txt", "r", encoding="utf-8") as f:
    genders = {}
    for line in f:
        line = line[:-1]
        name, gender = line.split(" +++$+++ ")
        genders[name.lower()] = gender

users_meta = {}

convo_id, root_id = 0, None
last_utterance_id = None
u = {}
with open("supreme.conversations.dat", "r", encoding="utf-8") as f:
    utterances = []
    count = 0
    for line in f:
        if count % 1000 == 0: print(count)
        line = line[:-1]
        if line:
            fields = line.split(" +++$+++ ")
            if len(fields) == 8:
                user = fields[3].strip().lower()
                if user == "justice roberts": user = "chief " + user # fix typo
                if user.endswith("kenned"): user += "y" # fix typo

                case = fields[0].strip() 
                is_justice = fields[4].strip() == "JUSTICE"

                #speaker += "(case:" + fields[0].strip() + ")"
                #is_justice = fields[4].strip() == "JUSTICE"
                #if is_justice:
                #    if fields[5].strip() == fields[6].strip(): # favorable justice
                #        speaker += "{justice-fav}"
                #    else:
                #        speaker += "{justice-unfav}"

                is_reply = fields[2].strip() == "TRUE"
                if not is_reply:
                    convo_id += 1
                    root_id = fields[1]

                users_meta[user] = {
                    "is-justice": is_justice,
                    "gender": genders[user],
                }
                if is_justice:
                    users_meta[user]["is-favorable"] = fields[5] == fields[6]

                d = {
                    KeyId: fields[1],
                    KeySpeaker: user,
                    KeyConvoRoot: root_id,#convo_id,
                    KeyText: fields[7],
                    KeySpeakerInfo: {
                        "case": case,
                        #"gender": genders[speaker],
                        #"is-justice": is_justice,
                        "side": fields[6].lower(),
                    }
                }
                if is_justice:
                    d[KeySpeakerInfo]["justice-vote"] = fields[5].lower()
                    d[KeySpeakerInfo]["justice-is-favorable"] = \
                            fields[5] == fields[6]

                if is_reply:
                    d[KeyReplyTo] = last_utterance_id
                    d[KeyConvoRoot] = root_id#convo_id#speaker # \
                        #+ "->" + (
                        #"[justices]" if \
                        #u[last_utterance_id][KeySpeaker].endswith("fav}") else \
                        #"[lawyers]")
                u[fields[1]] = d
                utterances.append(d)

                last_utterance_id = fields[1]
                
                count += 1
                #if MaxUtterances > 0 and count > MaxUtterances:
                #    break

#udict = {ut["id"]: ut for ut in utterances}
#for i, ut in enumerate(utterances):
#    if KeyReplyTo in ut:
#        target = udict[ut[KeyReplyTo]][KeySpeaker]
#        if target.endswith("{justice-fav}"):
#            ut[KeyConvoId] = ut[KeySpeaker] + "->{justice-fav}"
#        elif target.endswith("{justice-unfav}"):
#            ut[KeyConvoId] = ut[KeySpeaker] + "->{justice-unfav}"  # target groups
#        #ut[KeyConvoId] = target  # target groups -- experimental
#        #ut[KeyConvoId] = ut[KeySpeaker]  # speaker groups
#        utterances[i] = ut
#    else:
#        del utterances[i][KeyConvoId]

if MaxUtterances > 0:
    #import random
    #random.shuffle(utterances)
    utterances = utterances[-MaxUtterances:]
json.dump(utterances, open("supreme.json", "w"), indent=2,
          sort_keys=True)

with open("supreme-speakers.json", "w") as f:
    json.dump(users_meta, f, indent=2)
#print(len(usernames), len(usernames_cased))
print("Done")


