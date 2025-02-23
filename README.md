<h1 align="left">About CardCrawler</h1>

###

<p align="left">CardCrawler is a (at the time) text-based dungeon crawler based on Zach Gage and Kurt Bieg's "Scoundrel", a singleplayer dungeon crawler that only uses a deck of playing cards. See original rules at: http://www.stfj.net/art/2011/Scoundrel.pdf <br><br>CardCrawler was made in just around 1:30h, but debugging and polishing the program took easily twice that.<br><br>I plan on expanding it in the future, adding a visual component and optional features such as a "real deck" mode where cards aren't completely random and instead are part of an ordered deck (and avoided cards are left at the bottom of the deck), or merchants that trade weapons for health.</p>

###

<h2 align="left">How to Play</h2>

###

<h3 align="left">Moving through The Dungeon</h3>

###

<p align="left">On your first and every turn, cards will be randomly generated until there are four of them. These four cards make up a Room.<br>You must face 3 of the four cards in every Room, one by one.<br><br>You can avoid from a Room if you wish, reshuffling all four cards.<br>You may avoid as many Rooms as you want, you can't avoid two Rooms in a row.<br><br>If there are no enemies left, it doesn't count as avoiding, so you can skip the next Room. The game only ends if your Health reaches 0.<br>This is different from the original Scoundrel, where you always have to either avoid a Room or face 3 cards. <br>The original game can also be "completed" once you discard all 52 cards, whereas CardCrawler is endless.</p>

###

<h3 align="left">Healing and Weapons</h3>

###

<p align="left">Choosing a weapon will replace your previous weapon (or equip it, if you have none).<br><br>Using a healing item simply adds your the item's level to your HP.<br>Your health may not exceed 20.<br>You cannot use healing items at 20 HP.</p>

###

<h3 align="left">Combat</h3>

###

<p align="left">Combat is possibly the hardest part of the game to explain.<br>It's intuitive and easy to understand, but difficult to put into words.<br>It follows three main rules:<br><br>1) If you have no equipped Weapon or the Enemy's level is higher than your Weapon's, you will fight barehanded.<br>This will defeat the Enemy, but you will lose Health equal to the Enemy's level.<br><br>2) If you have an effective Weapon, you will defeat the Enemy and lose Health equal to the level difference.<br>	For example, if you attack a level 7 Enemy with a Level 4 Weapon, you'd take 3 HP of damage (7-4 = 3).<br>	However, attacking a level 3 Enemy with a level 4 Weapon wouldn't make you lose any HP (3-4 < 0)<br><br>3) Once a Weapon is used on an Enemy, it can only be used to attack Enemies of equal or lower level.<br>	For example, if you use a level 5 Weapon to slay a level 6 Enemy, it wouldn't be able to attack level 7, 8, 9... Enemies.<br>	However, it would still be able to attack Enemies of level 6 and under.</p>

###
