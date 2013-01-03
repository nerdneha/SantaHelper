import random
import pprint
PARTICIPANTS = [
    "Neha",
    "Damon",
    "Adam",
    "David",
    "Karen",
    "Scott",
    "Javi",
    "Faria",
    "Kyle",
    "Yuting",
    "Spam",
    "Hassan",
]

BLACKLIST = {
   ("Javi", "Scott"),
   ("Karen", "Faria")
   }

def shuffle_list(participants):
  gifters = participants[:]
  random.shuffle(gifters)
  return gifters

def create_loop(participants):
  gifters = shuffle_list(participants)
  #print gifters
  gift_dict= {}
  gifters.append(gifters[0])
  for index in range(1,len(gifters)):
    gift_dict[gifters[index-1]] = gifters[index]
  return gift_dict

def check_dict(gift_dict):
  givers = gift_dict.keys()
  receivers = gift_dict.values()
  #check if any people in blacklist have each other
  for jack, jill in BLACKLIST:
    if gift_dict[jack] == jill or gift_dict[jill] == jack:
      print "Blacklist hit, trying again...."
      print ""
      return False
  #checking to see if everyone is giving a present
  for name in PARTICIPANTS:
    if name in givers:
      givers.remove(name)
    else:
     print "Missing " + name + " in givers"
     return False
  #checking to see if everyone is receiving a present
  for name in PARTICIPANTS:
    if name in receivers:
      receivers.remove(name)
    else:
      print "Missing " + name + " in receivers"
      return False
  #checks if anyone is left out in giving/receiving
  if len(givers) == 0 and len(receivers) == 0:
    return True
  else:
    print "Givers is " + str(givers) + " receivers is " + str(receivers)
    return False

def create_santa_list(participants):
  good_list = False
  while (not good_list):
    pp = pprint.PrettyPrinter(indent=4)
    gift_dict = create_loop(participants)
    pp.pprint(gift_dict)
    good_list = check_dict(gift_dict)
  return gift_dict

def print_out_ss_dict (participants):
  gift_dict = create_santa_list(participants)
  list_length = len(gift_dict.keys())
  value = "Neha"
  for index in range(list_length):
    print value + " has " + gift_dict[value]
    value = gift_dict[value]


#print PARTICIPANTS
print_out_ss_dict(PARTICIPANTS)
