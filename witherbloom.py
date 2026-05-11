import random
import bonus_card
class Witherbloom():
    def __init__(self):
        #Inital cardpool containing 3 guaranteed cards, they are removed from other card pools to prevent repetition
        self.card_list = ["Pest Mascot (SOS) 209", "Titan's Grave (SOS) 266", "Witherbloom Charm (SOS) 244"]
        self.common = ["Bogwater Lumaret (SOS) 177", "Burrog Barrage (SOS) 141", "Efflorescence (SOS) 144", "Follow the Lumarets (SOS) 148", "Glorious Decay (SOS) 150", "Grapple with Death (SOS) 192", "Mindful Biomancer (SOS) 154", "Noxious Newt (SOS) 155", "Oracle's Restoration (SOS) 156", "Shopkeeper's Bane (SOS) 159", "Studious First-Year // Rampant Growth (SOS) 162", "Tenured Concocter (SOS) 163", "Adventurous Eater // Have a Bite (SOS) 72", "Burrog Banemaker (SOS) 75", "Cheerful Osteomancer // Raise Dead (SOS) 76", "Cost of Brilliance (SOS) 77", "Last Gasp (SOS) 86", "Masterful Flourish (SOS) 89", "Pull from the Grave (SOS) 95", "Send in the Pest (SOS) 100", "Sneering Shadewriter (SOS) 101", "Ulna Alley Shopkeep (SOS) 103", "Wander Off (SOS) 104", "Terramorphic Expanse (SOS) 265"]
        self.uncommon = ["Aberrant Manawurm (SOS) 138", "Chelonian Tackle (SOS) 142", "Environmental Scientist (SOS) 147", "Infirmary Healer // Stream of Life (SOS) 152", "Lluwen, Exchange Student // Pest Friend (SOS) 199", "Lumaret's Favor (SOS) 153", "Mind Roots (SOS) 203", "Old-Growth Educator (SOS) 207", "Pestbrood Sloth (SOS) 157", "Root Manipulation (SOS) 222", "Snarl Song (SOS) 161", "Teacher's Pest (SOS) 238", "Thornfist Striker (SOS) 164", "Zimone's Experiment (SOS) 169", "Arcane Omens (SOS) 73", "Arnyn, Deathbloom Botanist (SOS) 74", "Dissection Practice (SOS) 79", "End of the Hunt (SOS) 81", "Essenceknit Scholar (SOS) 187", "Foolish Fate (SOS) 83", "Leech Collector // Bloodletting (SOS) 88", "Poisoner's Apprentice (SOS) 92", "Rabid Attack (SOS) 96", "Scathing Shadelock // Venomous Words (SOS) 98"]
        self.rare = ["Blech, Loafing Pest (SOS) 176", "Cauldron of Essence (SOS) 179", "Comforting Counsel (SOS) 143", "Dina's Guidance (SOS) 184", "Planar Engineering (SOS) 158", "Slumbering Trudge (SOS) 160", "Vastlands Scavenger // Bind to Life (SOS) 166", "Wildgrowth Archaic (SOS) 168", "Grave Researcher // Reanimate (SOS) 85", "Moseo, Vein's New Dean (SOS) 91", "Tragedy Feaster (SOS) 102", "Vicious Rivalry (SOS) 241", "Postmortem Professor (SOS) 93", "Pox Plague (SOS) 94", "Scheming Silvertongue // Sign in Blood (SOS) 99", "Deathcap Glade (SOS) 253"]
        self.mythic = ["Emeritus of Abundance // Regrowth (SOS) 145", "Germination Practicum (SOS) 149", "Professor Dellian Fel (SOS) 214", "Witherbloom, the Balancer (SOS) 245", "Decorum Dissertation (SOS) 78", "Emeritus of Woe // Demonic Tutor (SOS) 80", "Withering Curse (SOS) 105"]
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