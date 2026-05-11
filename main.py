import lorehold, prismari, quandrix, silverquill, witherbloom

print("Welcome to the MtG Seeded Pack Generator!")
while True:
    response = input("Please input the school you would like to generate a pack for: [L]orehold, [P]rismari, [Q]uandrix, [S]ilverquill or [W]itherbloom: ").lower()
    print(response)
    if response in ["lorehold","l","prismari", "p", "quandrix", "q", "silverquill", "s", "witherbloom", "w"]:
        print(f"Generating a pack for {response}!")
        break
    else:
        print(f"{response} does not appear in this list, please enter one of the following schools- [L]orehold, [P]rismari, [Q]uandrix, [S]ilverquill or [W]itherbloom: ")

if response == "lorehold" or response == "l":
    lorehold_pack = lorehold.Lorehold()
    lorehold_pack.generate()
    
elif response == "prismari" or response == "p":
    prismari_pack = prismari.Prismari()
    prismari_pack.generate()
    
elif response == "quandrix" or response == "q":
    quandrix_pack = quandrix.Quandrix()
    quandrix_pack.generate()
    
elif response == "silverquill" or response == "s":
    silverquill_pack = silverquill.Silverquill()
    silverquill_pack.generate()
    
elif response == "witherbloom" or response == "w":
    witherbloom_pack = witherbloom.Witherbloom()
    witherbloom_pack.generate()

else:
    print("Oops! You broke something! Begone!")
    quit()
    