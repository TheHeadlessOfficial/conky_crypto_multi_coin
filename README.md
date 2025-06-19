# Conky Multi Crypto Alert (multi coins) (by CoinLore)
 
A conky (with a script written in Python) which sets 2 targets, one higher and one lower than the current price of a given crypto. When one of the two targets is reached, the conky emits a sound. Using [CoinLore API](https://www.coinlore.com/cryptocurrency-data-api#ticker) website.<br>

<br>
Inside the Coinlore website, you can search the symbol, the id, the name etc of the coins.
<br>


## **WIKI**<br>

Download the .zip file, extract the file, copy the file `.conkyrc_cryptomulti`, `.conkyrc_cryptomulti_audio.sh`, `.conkyyrc_cryptomulti_bash.sh` and the folder `.conky` inside your Linux `home`.
If your `home` is named pippo, copy inside pippo so you get: `/home/pippo/.conky` and `/home/pippo/.conkyrc_cryptomulti`, etc.

**0-** go to `/home/YOURHOMENAME/.conky/multicrypto/` and open the `crypto_multialert.py` file with a text editor, go to row 30 and insert the coins you want to search (using the coin symbol), following the scheme you found (["BTC", "DOGE", "SOL"]);<br>
**1-** open a terminal and run `.conkyrc_cryptomulti_bash.sh` (you can also just load the normal conky, `.conkyrc_cryptomulti`) and wait until the conky shows on screen;<br>
**2-** once conky shows the info, go to `/home/YOURHOMENAME/.conky/multicrypto/` and open the `list.txt` file with a text editor. Check if the coins found are as you wanted (check the Coinlore website). It's possible that the script finds more than 1 coin with the same symbol: for example XCN. If you don't need some doubled coin, just delete it/them, without leaving empty rows in the file;<br>
**3-** go to `/home/YOURHOMENAME/.conky/multicrypto/` and open the `crypto_multialert.py` file with a text editor, go to rows 112-following until the first character # and set the targets for the coins. You have 2 targets for every coin and you need to follow the `list.txt` file order. You can add or remove targets based on how many coins you have in the `list.txt` file. So if you have just 1 coin keep only rows 112 and 113, if you have more coins, copy and paste rows 112-113 and edit the index between square brackets. Save the script. Give time to conky to update the info;<br>
**4-** go to `/home/YOURHOMENAME/.conky/multicrypto/alarms` open the `readme.txt` file and you find a website where you can create the audio alarms for your coins. Once you create the file save it with the symbol name of the coin, as the examples you can see inside the folder.<br>

If you don't know how to do all that, follow this video instructions: [Video guide](https://www.youtube.com/watch?v=4h0ybJiIHgI)<br>

In the font folder, you can find some fonts you need.<br>
The python script saves data in file so you can build your conky as you wish.<br>
Edit `.conkyrc_cryptomulti` to build your conky.<br>
The `.conkyrc_cryptomulti` file i attach, works.<br>
Run the file `.conkyrc_cryptomulti` or `.conkyrc_cryptomulti_bash.sh` from terminal (the first time you run this conky), so you can get possible errors.
<br>
<br>

## Screenshot

![](https://github.com/TheHeadlessOfficial/conky_crypto_multi_coin/blob/main/.conky/multicrypto/docs/screenshot.png)<br>

<br>
<br>

<br>

---
[Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


