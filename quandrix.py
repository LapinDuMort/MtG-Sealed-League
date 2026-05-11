import random
import bonus_card
class Quandrix():
    def __init__(self):
        #Inital cardpool containing 3 guaranteed cards, they are removed from other card pools to prevent repetition
        self.card_list = ["Fractal Mascot (SOS) 189", "Paradox Gardens (SOS) 258", "Quandrix Charm (SOS) 217"]
        self.common = ["Banishing Betrayal (SOS) 38", "Chase Inspiration (SOS) 41", "Essence Scatter (SOS) 47", "Hydro-Channeler (SOS) 54", "Landscape Painter // Vibrant Idea (SOS) 56", "Procrastinate (SOS) 64", "Quick Study (SOS) 65", "Run Behind (SOS) 66", "Spellbook Seeker // Careful Study (SOS) 68", "Textbook Tabulator (SOS) 70", "Burrog Barrage (SOS) 141", "Glorious Decay (SOS) 150", "Hungry Graffalon (SOS) 151", "Mindful Biomancer (SOS) 154", "Noxious Newt (SOS) 155", "Oracle's Restoration (SOS) 156", "Shopkeeper's Bane (SOS) 159", "Studious First-Year // Rampant Growth (SOS) 162", "Wild Hypothesis (SOS) 167", "Embrace the Paradox (SOS) 186", "Pterafractyl (SOS) 215", "Terramorphic Expanse (SOS) 265"]
        self.uncommon = ["Brush Off (SOS) 39", "Campus Composer // Aqueous Aria (SOS) 40", "Divergent Equation (SOS) 43", "Encouraging Aviator // Jump (SOS) 46", "Flow State (SOS) 49", "Fractal Anomaly (SOS) 50", "Fractalize (SOS) 51", "Homesickness (SOS) 53", "Matterbending Mage (SOS) 59", "Tester of the Tangential (SOS) 69", "Aberrant Manawurm (SOS) 138", "Additive Evolution (SOS) 139", "Chelonian Tackle (SOS) 142", "Emil, Vastlands Roamer (SOS) 146", "Environmental Scientist (SOS) 147", "Infirmary Healer // Stream of Life (SOS) 152", "Snarl Song (SOS) 161", "Topiary Lecturer (SOS) 165", "Zimone's Experiment (SOS) 169", "Cuboid Colony (SOS) 183", "Fractal Tender (SOS) 190", "Growth Curve (SOS) 193", "Paradox Surveyor (SOS) 208", "Proctor's Gaze (SOS) 213", "Tam, Observant Sequencer // Deep Sight (SOS) 237"]
        self.rare = ["Harmonized Trio // Brainstorm (SOS) 52", "Jadzi, Steward of Fate // Oracle's Gift (SOS) 55", "Mana Sculpt (SOS) 57", "Pensive Professor (SOS) 63", "Skycoach Conductor // All Aboard (SOS) 67", "Wisdom of Ages (SOS) 71", "Ambitious Augmenter (SOS) 140", "Comforting Counsel (SOS) 143", "Planar Engineering (SOS) 158", "Slumbering Trudge (SOS) 160", "Vastlands Scavenger // Bind to Life (SOS) 166", "Wildgrowth Archaic (SOS) 168", "Applied Geometry (SOS) 172", "Berta, Wise Extrapolator (SOS) 175", "Geometer's Arthropod (SOS) 191", "Mind into Matter (SOS) 202", "Dreamroot Cascade (SOS) 254"]
        self.mythic = ["Echocasting Symposium (SOS) 44", "Emeritus of Ideation // Ancestral Recall (SOS) 45", "Mathemagics (SOS) 58", "Emeritus of Abundance // Regrowth (SOS) 145", "Germination Practicum (SOS) 149", "Quandrix, the Proof (SOS) 218"]
        #0.125% of the time a rare will be upshifted to a mythic
        self.mythic_rate = 0.125

    def generate(self):
       #Generate 8 random, unique, common cards
        for common_card in range(8):
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