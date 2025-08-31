Meatpie = '{"cursedKnown":false,"quantity":10,"levelKnown":false,"cursed":false,"level":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.food.MeatPie","kept_lost":false}'

ScrollOfUpgrade = '{"cursedKnown":false,"quantity":3,"levelKnown":false,"cursed":false,"level":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.scrolls.ScrollOfUpgrade","kept_lost":false}'
ScrollOfIdentify = '{"cursedKnown":false,"quantity":5,"levelKnown":false,"cursed":false,"level":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.scrolls.ScrollOfIdentify","kept_lost":false}'

PotionOfHealing = '{"cursedKnown":true,"quantity":5,"levelKnown":true,"cursed":false,"level":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.potions.PotionOfHealing"}'

WandOfLivingEarth = '{"cursedKnown":true,"quantity":1,"levelKnown":true,"cursed":false,"level":2,"uses_left_to_id":0,"curCharges":4,"quickslotpos":2,"resin_bonus":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.wands.WandOfLivingEarth","kept_lost":false,"curse_infusion_bonus":false,"partialCharge":0,"available_uses":0.6499998569488525,"curChargeKnown":true}'
WandOfBlastWave = '{"cursedKnown":true,"quantity":1,"levelKnown":true,"cursed":false,"level":2,"uses_left_to_id":10,"curCharges":4,"quickslotpos":1,"resin_bonus":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.wands.WandOfBlastWave","kept_lost":false,"curse_infusion_bonus":false,"partialCharge":0,"available_uses":5,"curChargeKnown":true}'
WandOfDisintegration = '{"cursedKnown":true,"quantity":1,"levelKnown":true,"cursed":false,"level":2,"uses_left_to_id":10,"curCharges":2,"quickslotpos":5,"resin_bonus":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.wands.WandOfDisintegration","kept_lost":false,"curse_infusion_bonus":false,"partialCharge":0.7437540292739868,"available_uses":5,"curChargeKnown":true},'
WandOfFireBlast = '{"cursedKnown":true,"quantity":1,"levelKnown":false,"cursed":false,"level":0,"uses_left_to_id":3,"curCharges":2,"resin_bonus":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.wands.WandOfFireblast","kept_lost":false,"curse_infusion_bonus":false,"partialCharge":0,"available_uses":0,"curChargeKnown":false}'


MissileShuriken = '{"cursedKnown":false,"quantity":2,"levelKnown":true,"cursed":false,"level":4,"uses_left_to_id":20,"quickslotpos":2,"durability":100,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.weapon.missiles.Shuriken","kept_lost":false,"curse_infusion_bonus":false,"augment":"NONE","mastery_potion_bonus":false,"available_uses":10,"enchant_hardened":false}'

RingOfWealth = '{"cursedKnown":true,"quantity":1,"levelKnown":true,"cursed":false,"drops_to_rare":-2147483648,"level":0,"tries_to_drop":1.401298464324817E-45,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.rings.RingOfWealth","levels_to_ID":0,"kept_lost":false}'
RingOfEnergy = '{"cursedKnown":true,"quantity":1,"levelKnown":true,"cursed":false,"level":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.rings.RingOfEnergy","levels_to_ID":0,"kept_lost":false}'


HornOfPlenty = '{"cursedKnown":true,"quantity":1,"charge":0,"levelKnown":true,"cursed":false,"level":0,"stored":0,"partialcharge":0,"__className":"com.shatteredpixel.shatteredpixeldungeon.items.artifacts.HornOfPlenty","exp":0,"kept_lost":false}'

WaterSkin = '"__className":"com.shatteredpixel.shatteredpixeldungeon.items.Waterskin","kept_lost":false}'


def main() -> None:
	items_to_add = [Meatpie, ScrollOfUpgrade, ScrollOfIdentify, PotionOfHealing, WandOfLivingEarth, WandOfBlastWave, MissileShuriken, RingOfWealth, RingOfEnergy]
		
		
	file = open("game", "r")
	game_file = file.read()
	
	string_to_add = ","
	for item in items_to_add:
		string_to_add += (item + ',')
	
	string_to_add_no_final_comma = string_to_add[:-1]
	
	game_buffed_str = game_file.replace(WaterSkin, WaterSkin + string_to_add_no_final_comma)
	
	with open("game.dat", "w") as file:
		file.write(game_buffed_str)


if __name__ == "__main__":
	main()
