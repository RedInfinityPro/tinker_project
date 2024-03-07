import random
location = ''
object_found = ''
class Story():
    def __init__(self,text):
        super().__init__()
        global object_found,location
        self.text = text.lower().strip()
        self.story = ''
        # make the story
        story = ''
        if self.text == 'start story':
            locations = ['forest','mountains','desert','plains','valley','tundra','swamp','marsh']
            position = random.choice(locations)
            story = 'you open your eyes and you found your self in the middle of the {}'.format(position)
        elif 'drink' or 'sip' or 'eat' or 'consume' in self.text:
            if object_found == 'food' or 'water':
                story = 'you eat all of your food and dank all the water you could'
            else:
                story = 'you did not see any food or water on you.'
        elif 'analyze' or 'delve into' or 'examine' or 'probe' or 'research' or 'scrutinize' or 'search' or 'seek' or 'test' or 'try' or 'explore' in self.text:
            simple_objects = ['water','tools','a letter','a book','food','nothing']
            if location == 'forest' or 'plains':
                object_list = ['trees','rocks','rotten wood','ruins','lamp','boat','campfire']
            if location == 'mountains':
                object_list = ['trees', 'rocks', 'rotten wood', 'ruins', 'lamp', 'campfire']
            if location == 'desert':
                object_list = ['rocks','ruins','wood','cactus','foot prints','plaints']
            if location == 'tundra':
                object_list = ['trees', 'rocks', 'rotten wood','snow','ice']
            if location == 'swamp' or 'marsh':
                object_list = ['trees', 'rotten wood','boats']
            object_found = random.choice(object_list + simple_objects)
            story = 'you look around and you have found: {}'.format(object_found)
        elif 'analyze' or 'confirm' or 'correct' or 'find out' or 'go through' or 'investigate' or 'monitor' or 'probe' or 'review' or 'scrutinize' or 'study' or 'test' or 'try' or 'verify' in self.text:
            if object_found == 'a letter':
                letters = ['We are mammoth under the earth We stretch sticky knives among the water Whoa! The bastard shall fleeStrangely dazzling before the virginYou squeeze luminous devils against the mistAwaken! The King has died So sticky within the wind You grind green delusions beside the land Alass! The inspiration is dying opaque tired in another country a phone ringing somewhere Under what skies the god stop for a while unable to stop',
                           'So rabid above the vapors We prod invisible hooks below the mist Alass! The demon felt good Quite comely beside the fog We spread desirous toads over the mist Alass, Alack! The Fool is dying Sinister and electric below the fire I poke sinning snares within the light Intense! The bastard gets weird unsure nameless in the night sun on his face In whose heart the lost man make his way in a different light']
                information = random.choice(letters)
            if object_found == 'tools':
                tools = ['powertools','screw driver','hammers','pens','wrenches','pliers']
                information = random.choice(tools)
            if object_found == 'a book':
                book = ["this book will do two things. It will tell a story of how a couple got back together because there was love and joy in their lives, and it will tell a story of how I and I alone can do the same thing here. I'm glad I had both of these books.",
                        "this may not last loong.) The way the second page describes it, it's like the first page describing something like, An open packet, and a closed packet. Or An open packet that hasn't been closed yet that has a lot of data between it and its neighbors.Because of the way it describes it, the results often show a lot of data being sent through in the first place, which indicates the packet has been closed. At any rate, this makes it very difficult to test the theory that this is the only problem. If the packet has been closed it makes it impossible to tell if it had been opened by some other process, if there are many other processes behind the packet then it is likely that there are at least 100,000 connections. If there is one process in the world that did open the packet and sent it through, you can see one more connection from the top of the first page, so it makes it no less likely that a network could be open. That could be a reason if a lot of data was being closed, then there could be a bad memory where the packet could have been in read mode on a server, or a problem with a firewall. But if it comes down to it a closed packet will make it much harder than having a fully open one (or not). It is also less likely that a server would not respond to connections from outside its network. A very good way to check this is by looking at an open"]
                information = random.choice(book)
            else:
                information = 'nothing'
            story = 'you look at the {} at multiple angles and found: {}'.format(object_found,information)
        self.story = story.capitalize()
