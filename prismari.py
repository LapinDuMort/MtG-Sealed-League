import random
import bonus_card
class Prismari():
    def __init__(self):
        #Inital cardpool containing 3 guaranteed cards, they are removed from other card pools to prevent repetition
        self.card_list =["Prismari Charm (SOS) 211", "Spectacle Summit (SOS) 262", "Elemental Mascot (SOS) 185"]
        self.common = ["Ancestral Anger (SOS) 106", "Expressive Firedancer (SOS) 114", "Goblin Glasswright // Craft with Pride (SOS) 117", "Heated Argument (SOS) 118", "Rearing Embermare (SOS) 127", "Rubble Rouser (SOS) 128", "Seize the Spoils (SOS) 129", "Strife Scholar // Awaken the Ages (SOS) 131", "Tackle Artist (SOS) 133", "Unsubtle Mockery (SOS) 136", "Zealous Lorecaster (SOS) 137", "Stadium Tidalmage (SOS) 232", "Visionary's Dance (SOS) 242", "Banishing Betrayal (SOS) 38", "Chase Inspiration (SOS) 41", "Deluge Virtuoso (SOS) 42", "Essence Scatter (SOS) 47", "Hydro-Channeler (SOS) 54", "Landscape Painter // Vibrant Idea (SOS) 56", "Muse's Encouragement (SOS) 61", "Procrastinate (SOS) 64", "Quick Study (SOS) 65", "Run Behind (SOS) 66", "Spellbook Seeker // Careful Study (SOS) 68", "Terramorphic Expanse (SOS) 265"]
        self.uncommon = ["Brush Off (SOS) 39", "Campus Composer // Aqueous Aria (SOS) 40", "Divergent Equation (SOS) 43", "Encouraging Aviator // Jump (SOS) 46", "Flow State (SOS) 49", "Homesickness (SOS) 53", "Matterbending Mage (SOS) 59", "Muse Seeker (SOS) 60", "Orysa, Tide Choreographer (SOS) 62", "Abstract Paintmage (SOS) 171", "Rapturous Moment (SOS) 219", "Sanar, Unfinished Genius // Wild Idea (SOS) 223", "Spectacular Skywhale (SOS) 229", "Stress Dream (SOS) 235", "Vibrant Outburst (SOS) 240", "Archaic's Agony (SOS) 107", "Artistic Process (SOS) 108", "Blazing Firesinger // Seething Song (SOS) 109", "Charging Strifeknight (SOS) 110", "Impractical Joke (SOS) 119", "Pigment Wrangler // Striking Palette (SOS) 126", "Tablet of Discovery (SOS) 132", "Thunderdrum Soloist (SOS) 134"]
        self.rare = ["Choreographed Sparks (SOS) 111", "Maelstrom Artisan // Rocket Volley (SOS) 122", "Magmablood Archaic (SOS) 123", "Molten-Core Maestro (SOS) 125", "Steal the Show (SOS) 130", "Colorstorm Stallion (SOS) 180", "Resonating Lute (SOS) 221", "Splatter Technique (SOS) 231", "Traumatic Critique (SOS) 239", "Zaffai and the Tempests (SOS) 246", "Exhibition Tidecaller (SOS) 48", "Harmonized Trio // Brainstorm (SOS) 52", "Jadzi, Steward of Fate // Oracle's Gift (SOS) 55", "Mana Sculpt (SOS) 57", "Skycoach Conductor // All Aboard (SOS) 67", "Wisdom of Ages (SOS) 71", "Stormcarved Coast (SOS) 263"]
        self.mythic = ["Echocasting Symposium (SOS) 44", "Emeritus of Ideation // Ancestral Recall (SOS) 45", "Mathemagics (SOS) 58", "Prismari, the Inspiration (SOS) 212", "Emeritus of Conflict // Lightning Bolt (SOS) 113", "Improvisation Capstone (SOS) 120"]        
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