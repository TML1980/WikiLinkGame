import requests

print("\nWelcome to the Wiki-Links game.")
print("\nHere's how it works....write rules etc. here...yada yada...")

# Game start: player chooses a number between 1 and 10 (first time game, use 8)
# Game start: choose a starting page OR begin at the random link page:
# https://en.wikipedia.org/wiki/Special:Random
# 4 possible endings:
# Short Page Ending  (if your page doesn't have N links)
# Infinite Loop Ending (if you arrive at a page you have already visited during your run)
# Empty Link Ending  (if the Nth link is a red link to edit a page that doesn't exist)
# Off-sit Ending  (if you arrive at a non-Wikipedia page)

num = input("\nPlease choose a number between 1 and 10: ")
page = input("\nWould you like to begin on a specific page or a random page? ")

s = requests.session()
# resp = s.get("https://en.wikipedia.org/wiki/Special:Random")
resp = s.get("https://en.wikipedia.org/wiki/Wikipedia:Wiki-Link_Game#Wiki-Link_rules")

html = resp.text
html = html.lower()
links = html.split("href=")
allLinks = []
for l in links:
  parts = l.split("\"")
  if("http" in parts[1]):
    allLinks.append(parts[1])
    # if list more than num, stop adding links
    # if not enough links on page, stop
    # if new link same as prev, stop adding links
    # if new link is a red link, stop
    # if new link goes away from wikipedia, stop

# print all the pages visited
# print final page where game ends
# print type of ending
# ask if player wants to play again
print(allLinks[2])
