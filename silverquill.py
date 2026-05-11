import random
import bonus_card
class Silverquill():
    def __init__(self):
        #Inital cardpool containing 3 guaranteed cards, they are removed from other card pools to prevent repetition
        self.card_list = ["Forum of Amity (SOS) 256", "Inkling Mascot (SOS) 196", "Silverquill Charm (SOS) 225"]
        self.common = ["Ajani's Response (SOS) 6", "Ascendant Dustspeaker (SOS) 8", "Eager Glyphmage (SOS) 11", "Elite Interceptor // Rejoinder (SOS) 12", "Honorbound Page // Forum's Favor (SOS) 19", "Interjection (SOS) 22", "Owlin Historian (SOS) 24", "Rapier Wit (SOS) 28", "Rehearsed Debater (SOS) 29", "Shattered Acolyte (SOS) 31", "Stone Docent (SOS) 36", "Adventurous Eater // Have a Bite (SOS) 72", "Burrog Banemaker (SOS) 75", "Cheerful Osteomancer // Raise Dead (SOS) 76", "Cost of Brilliance (SOS) 77", "Last Gasp (SOS) 86", "Masterful Flourish (SOS) 89", "Melancholic Poet (SOS) 90", "Pull from the Grave (SOS) 95", "Sneering Shadewriter (SOS) 101", "Wander Off (SOS) 104", "Imperious Inkmage (SOS) 195", "Render Speechless (SOS) 220", "Terramorphic Expanse (SOS) 265"]
        self.uncommon = ["Ennis, Debate Moderator (SOS) 14", "Graduation Day (SOS) 16", "Harsh Annotation (SOS) 18", "Inkshape Demonstrator (SOS) 21", "Primary Research (SOS) 26", "Quill-Blade Laureate // Twofold Intent (SOS) 27", "Soaring Stoneglider (SOS) 32", "Spiritcall Enthusiast // Scrollboost (SOS) 33", "Stand Up for Yourself (SOS) 34", "Summoned Dromedary (SOS) 37", "Arcane Omens (SOS) 73", "Dissection Practice (SOS) 79", "End of the Hunt (SOS) 81", "Eternal Student (SOS) 82", "Forum Necroscribe (SOS) 84", "Lecturing Scornmage (SOS) 87", "Leech Collector // Bloodletting (SOS) 88", "Rabid Attack (SOS) 96", "Scathing Shadelock // Venomous Words (SOS) 98", "Abigale, Poet Laureate // Heroic Stanza (SOS) 170", "Killian's Confidence (SOS) 197", "Scolding Administrator (SOS) 224", "Snooping Page (SOS) 227", "Social Snub (SOS) 228", "Stirring Honormancer (SOS) 234"]
        self.rare = ["Erode (SOS) 15", "Informed Inkwright (SOS) 20", "Joined Researchers // Secret Rendezvous (SOS) 23", "Stirring Hopesinger (SOS) 35", "Grave Researcher // Reanimate (SOS) 85", "Postmortem Professor (SOS) 93", "Pox Plague (SOS) 94", "Scheming Silvertongue // Sign in Blood (SOS) 99", "Conciliator's Duelist (SOS) 182", "Fix What's Broken (SOS) 188", "Moment of Reckoning (SOS) 205", "Nita, Forum Conciliator (SOS) 206", "Shattered Sanctum (SOS) 260"]
        self.mythic = ["Emeritus of Truce // Swords to Plowshares (SOS) 13", "Restoration Seminar (SOS) 30", "Decorum Dissertation (SOS) 78", "Emeritus of Woe // Demonic Tutor (SOS) 80", "Ral Zarek, Guest Lecturer (SOS) 97", "Silverquill, the Disputant (SOS) 226"]
        #0.125% of the time a rare will be upshifted to a mythic
        self.mythic_rate = 0.125

    def generate(self):
       #Generate 8 random, unique, common cards
        for common_card in range(7):
            random.shuffle(self.common)
            self.card_list.append(self.common.pop())
       #Generate 3 random, unique, uncommon cards
        for uncommon_card in range(3):
            random.shuffle(self.uncommon)
            self.card_list.append(self.uncommon.pop())
        # 0.125 chance of generating a random mythic, otherwise, a random rare
        if random.random() < self.mythic_rate:
            random.shuffle(self.mythic)
            self.card_list.append(self.mythic.pop())
        else:
            random.shuffle(self.rare)
            self.card_list.append(self.rare.pop())
        
        #Add a bonus rare or mythic from *ANY SCHOOL*
        get_bonus = bonus_card.BonusCard()
        self.card_list.append(get_bonus.get_bonus_card())

        #Print final card list formatted
        for card in self.card_list:
            print(f"1 {card}")
  
    def card_list_all(self):
        all_cards = []
        all_cards.append(self.card_list)
        all_cards.append(self.common)
        all_cards.append(self.uncommon)
        all_cards.append(self.rare)
        all_cards.append(self.mythic)
        for i in all_cards:
            for j in i:
                print(j)