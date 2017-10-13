import discord
import json

autoclears = {}
users = {}
warnings = {}
join_messages = {}
leave_messages = {}

spam_filter = []
profanity_filter = []

emails = {}
verif_servers = []

votes = []

try:
  with open('DATA/autoclears.json','r') as f:
    autoclears = json.load(f)

except FileNotFoundError:
  print('no autoclear file found')

try:
  with open('DATA/spamfilter.json','r') as f:
    spam = json.load(f)

except FileNotFoundError:
  print('no spam filter file found')

try:
  with open('DATA/profanityfilter.json','r') as f:
    profanity_filter = json.load(f)

except FileNotFoundError:
  print('no profanity filter file found')

try:
  with open('DATA/join_messages.json','r') as f:
    join_messages = json.load(f)

except FileNotFoundError:
  print('no join messages file found')

try:
  with open('DATA/leave_messages.json','r') as f:
    leave_messages = json.load(f)

except FileNotFoundError:
  print('no leave messages file found')

try:
  with open('DATA/verif_servers.json','r') as f:
    verif_servers = json.load(f)

except FileNotFoundError:
  print('no verif servers file found')

try:
  with open('DATA/emails.json','r') as f:
    emails = json.load(f)

except FileNotFoundError:
  print('no emails file found')
