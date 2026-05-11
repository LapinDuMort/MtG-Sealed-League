import lorehold, prismari, quandrix, silverquill, witherbloom

print("Welcome to the MtG Seeded Pack Generator!")
while True:
    response = input("Please input the school you would like to generate a pack for: [L]orehold, [P]rismari, [Q]uandrix, [S]ilverquill or [W]itherbloom: ").lower()
    print(response)
    if response in ["lorehold","l","prismari", "p", "quandrix", "q", "silverquill", "s", "witherbloom", "w"]:
        break
    else:
        print(f"{response} does not appear in this list, please enter one of the following schools- [L]orehold, [P]rismari, [Q]uandrix, [S]ilverquill or [W]itherbloom: ")

if response == "lorehold" or response == "l":
    print("=== Generating a pack for Lorehold! ===")
    lorehold_pack = lorehold.Lorehold()
    lorehold_pack.generate()
    
elif response == "prismari" or response == "p":
    print("=== Generating a pack for Prismari! ===")
    prismari_pack = prismari.Prismari()
    prismari_pack.generate()
    
elif response == "quandrix" or response == "q":
    print("=== Generating a pack for Quandrix! ===")
    quandrix_pack = quandrix.Quandrix()
    quandrix_pack.generate()
    
elif response == "silverquill" or response == "s":
    print("=== Generating a pack for Silverquill! ===")
    silverquill_pack = silverquill.Silverquill()
    silverquill_pack.generate()
    
elif response == "witherbloom" or response == "w":
    print("=== Generating a pack for Witherbloom! ===")
    witherbloom_pack = witherbloom.Witherbloom()
    witherbloom_pack.generate()

else:
    print("Oops! You broke something! Begone!")
    quit()
    