import random
import bonus_card
class Lorehold():
    def __init__(self):
        #Inital cardpool containing 3 guaranteed cards, they are removed from other card pools to prevent repetition
        self.card_list = ["Lorehold Charm (SOS) 200", "Fields of Strife (SOS) 255", "Spirit Mascot (SOS) 230"]
        self.common = ["Ancestral Anger (SOS) 106", "Goblin Glasswright // Craft with Pride (SOS) 117", "Heated Argument (SOS) 118", "Rearing Embermare (SOS) 127", "Rubble Rouser (SOS) 128", "Seize the Spoils (SOS) 129", "Strife Scholar // Awaken the Ages (SOS) 131", "Unsubtle Mockery (SOS) 136", "Zealous Lorecaster (SOS) 137", "Wilt in the Heat (SOS) 243", "Tome Blast (SOS) 135", "Pursue the Past (SOS) 216", "Ajani's Response (SOS) 6", "Ascendant Dustspeaker (SOS) 8", "Dig Site Inventory (SOS) 10", "Elite Interceptor // Rejoinder (SOS) 12", "Honorbound Page // Forum's Favor (SOS) 19", "Interjection (SOS) 22", "Owlin Historian (SOS) 24", "Rapier Wit (SOS) 28", "Shattered Acolyte (SOS) 31", "Stone Docent (SOS) 36", "Terramorphic Expanse (SOS) 265"]
        self.uncommon = ["Archaic's Agony (SOS) 107", "Blazing Firesinger // Seething Song (SOS) 109", "Borrowed Knowledge (SOS) 178", "Charging Strifeknight (SOS) 110", "Colossus of the Blood Age (SOS) 181", "Duel Tactics (SOS) 112", "Garrison Excavator (SOS) 116", "Impractical Joke (SOS) 119", "Kirol, History Buff // Pack a Punch (SOS) 198", "Living History (SOS) 121", "Mica, Reader of Ruins (SOS) 124", "Molten Note (SOS) 204", "Pigment Wrangler // Striking Palette (SOS) 126", "Practiced Scrollsmith (SOS) 210", "Startled Relic Sloth (SOS) 233", "Tablet of Discovery (SOS) 132", "Daydream (SOS) 9", "Group Project (SOS) 17", "Primary Research (SOS) 26", "Quill-Blade Laureate // Twofold Intent (SOS) 27", "Soaring Stoneglider (SOS) 32", "Spiritcall Enthusiast // Scrollboost (SOS) 33", "Stand Up for Yourself (SOS) 34", "Summoned Dromedary (SOS) 37"]
        self.rare = ["Ark of Hunger (SOS) 173", "Aziza, Mage Tower Captain (SOS) 174", "Choreographed Sparks (SOS) 111", "Flashback (SOS) 115", "Hardened Academic (SOS) 194", "Maelstrom Artisan // Rocket Volley (SOS) 122", "Magmablood Archaic (SOS) 123", "Steal the Show (SOS) 130", "Suspend Aggression (SOS) 236", "Antiquities on the Loose (SOS) 7", "Erode (SOS) 15", "Joined Researchers // Secret Rendezvous (SOS) 23", "Practiced Offense (SOS) 25", "Sundown Pass (SOS) 264"]
        self.mythic = ["Emeritus of Conflict // Lightning Bolt (SOS) 113", "Improvisation Capstone (SOS) 120", "Lorehold, the Historian (SOS) 201", "Emeritus of Truce // Swords to Plowshares (SOS) 13", "Restoration Seminar (SOS) 30"]
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