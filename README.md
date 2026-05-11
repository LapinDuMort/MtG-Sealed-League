I couldn't find a way to generate Secrets of Strixhaven seeded packs, so, I made my own.
First run `python3 main.py` in the terminal, or run `/main.py` directly.
The prompt will ask which of the five schools you would like to generate a pack for.

- Type 'l' or 'lorehold' for Lorehold;
- Type 'p' or 'prismari' for Prismari;
- Type 'q' or 'quandrix' for Quandrix;
- Type 's' or 'silverquill' for Silverquill; OR
- Type 'w' or 'witherbloom' for Witherbloom.

These are NOT case sensitive.

This will generate a pack in plain text in the terminal, which can be copied and pasted directly into Moxfield.

Note on contents of packs:
Each pack contains one copy of the charm, mascot and common tapland for that college.
It will contain 7 random common cards from that college, 3 random uncommon cards and 1 random rare/mythic from that college.
It will also contain 1 random rare/mythic from the entire set.

There is a 0.125 (1/8) chance of rares to be upgraded to mythics.

Each card pool is made up of all on colour cards from that college, but exclude any cards with college stamps for the others, e.g. Antiquities on the Loose (SOS) #7 shows up in the Lorehold rare pool, and the set rare pool, but not in Silverquill despite being mono-white as it features the Lorehold stamp.

College stamps are associated with mechanics and tokens, so cards that have flashback will be in Lorehold, cards that create pests will be in Witherbloom etc...

If you have any questions, suggestions or notice any bugs, feel free to contact @LapinDuMort on Discord or robynjarcher96@gmail.com <3
