# website: https://www.coinlore.com/cryptocurrency-data-api#ticker
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_cryptomulti.lock"
# Check lock file
try:
    open(lock_file, 'w').close()
    import os, sys
    import requests
    import math
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set the temporary paths
    home = '/home/'
    conky = '/.conky/'
    ptemp = 'multicrypto/'    
    ################################ paths
    pconky = home + homename + conky + ptemp + 'conky.txt'
    soundmulti2 = home + homename + conky + ptemp + "alarms/"
    pathlist = home + homename + conky + ptemp + "list.txt"
    soundfake = ''
    psearch_lock = home + homename + conky + ptemp + "search.lock"
    ################################ variables
    news = ''
    ################################ rows
    row1 = '${color6}Target reached. ${color}'
    row2 = '${color}'
    # insert the coins you want to search, the order in the following row doesn't affect the script.
    cointosearch = ["BTC", "DOGE", "SOL"] # use the coin symbol
    # how many symbol in the list 
    symbolnum = len(cointosearch)
    ################################################################ SEARCH FUNCTION
    # the coins searched and saved by the following function, is the order you have to follow for the script
    def searchcrypto(fcointosearch, fpathlist):
        # Check lock file
        try:
            if not os.path.exists(psearch_lock):
                # Lock file to tell python to create var only the first time
                lock_search_file = psearch_lock   
            else:
                return
            open(lock_search_file, 'w').close()
            page = 0
            numcoins = 14380
            numcoinsmod = math.floor((numcoins/100) + 1)
            with open(fpathlist, "w") as fo:
                for i in range(0, numcoinsmod):
                    if i == 0:
                        urllist1 = 'https://api.coinlore.net/api/tickers/'
                        reslist1 = requests.get(urllist1).json()
                        datalist1 = reslist1
                        data = datalist1
                        for j in range (0, 100):
                            tempid = data['data'][j]['id']
                            tempsymbol = data['data'][j]['symbol']
                            if tempsymbol in fcointosearch:
                                fo.write('{}\n'.format(tempid))
                                fo.write('{}\n'.format(tempsymbol))
                    else:
                        if i == 1:
                            page = 100
                        urllist2 = 'https://api.coinlore.net/api/tickers/?start=' + str(page) + '&limit=100'
                        reslist2 = requests.get(urllist2).json()
                        datalist2 = reslist2
                        if i == 143:
                            for z in range(0, 79):
                                data = datalist2
                                tempid = data['data'][z]['id']
                                tempsymbol = data['data'][z]['symbol']
                                if tempsymbol in fcointosearch:
                                    fo.write('{}\n'.format(tempid))
                                    fo.write('{}\n'.format(tempsymbol))
                        else:
                            for z in range(0, 100):
                                data = datalist2
                                tempid = data['data'][z]['id']
                                tempsymbol = data['data'][z]['symbol']
                                if tempsymbol in fcointosearch:
                                    fo.write('{}\n'.format(tempid))
                                    fo.write('{}\n'.format(tempsymbol))
                    page = page + 100
        except Exception as e:
            # Manage exceptions (optional)
            filelockerror = (f"Error during script execution: {e}")
    ################################ write conky.txt file
    def fconky(fsymbol, fname, fpath, fprice, fpriceUp, fpriceDown, frow, fnews, fsound):
        fo.write('${color2} ' + fsymbol + ' - ' + fname + '${color}\n')
        fo.write('${color2}Actual price (USD): ${color}' + str(fprice) + '\n')
        fo.write('\n')
        fo.write('${color2}${ALIGNC}TARGETS\n')
        if isinstance(fpriceUp, (int, float)):
            fo.write('${color2}Limit Up: ${color6}' + f"{fpriceUp}" + '${color}')
        else:
            fo.write('${color2}Limit Up: ${color6}' + str(fpriceUp) + '${color}')
        if isinstance(fpriceDown, (int, float)):
            fo.write('${ALIGNR}${color2}Limit Down: ${color9}' + f"{fpriceDown}" + '${color}\n')
        else:
            fo.write('${ALIGNR}${color2}Limit Down: ${color9}' + str(fpriceDown) + '${color}\n')
        fo.write('\n')
        fo.write(frow + fnews + fsound +'\n')
        fo.write('${alignc}--------------------------------------------\n')
    ################################ Call search function    
    searchcrypto(cointosearch, pathlist)
    ################################ SET TARGETS variables
    # give the number of coins found (you can find more than the 'symbolnum', cause a single symbol can have more than 1 coin, example: XCN)
    coinnum = int(sum(1 for riga in open(pathlist) if riga.strip()) / 2)
    tUp = [0] * (coinnum)
    tDown = [0] * (coinnum)
    # SET THE FOLLOWING TARGETS BASED ON THE ORDER OF THE list.txt file
    # add or remove the following rows based on how many coins (coinnum) you are searching for. (2 values for 1 coin: "tUp" and "tDown")
    # copy and paste if you need more rows and edit the index
    tUp[0] = 0
    tDown[0] = 0
    tUp[1] = 0
    tDown[1] = 0
    tUp[2] = 0
    tDown[2] = 0
    ################################ swap targets variables
    targetUp = [0] * (coinnum + 1)
    targetDown = [0] * (coinnum + 1)
    for i in range(0, coinnum):
        targetUp[i] = tUp[i]
        targetDown[i] = tDown[i]
    # set rows for the audio bash file
    with open(pathlist, "r") as f:
        rownum = 1
        lines = lines = [line.strip() for line in f if line.strip()]
        soundcoins = [0] * (coinnum + 1)
        for i in range(0, coinnum):
            namecoin = lines[rownum].strip()
            soundcoins[i] = "${exec " + home + homename + "/.conkyrc_cryptomulti_audio.sh " + soundmulti2 + namecoin + ".mp3}"
            rownum = rownum + 2
    ################################ API variables 
    aid = []
    asymbol = []
    aname = []
    anameid = []
    arank = []
    aprice_usd = []
    apercent_change_24h = []
    apercent_change_1h = []
    apercent_change_7d = []
    aprice_btc = []
    amarket_cap_usd = []
    avolume24 = []
    avolume24a = []
    acsupply = []
    atsupply = []
    amsupply = []
    ################################ get data
    with open(pathlist, "r") as f:
        rownum = 0
        lines = lines = [line.strip() for line in f if line.strip()]
        for i in range(0, coinnum):
            idcoin = lines[rownum].strip()
            url1 = 'https://api.coinlore.net/api/ticker/?id=' + str(idcoin)
            res1 = requests.get(url1).json()
            data1 = res1
            data = data1
            ################################ get data
            aid.append(data[0]['id'])
            asymbol.append(data[0]['symbol'])
            aname.append(data[0]['name'])
            anameid.append(data[0]['nameid'])
            arank.append(data[0]['rank'])
            aprice_usd.append(data[0]['price_usd'])
            apercent_change_24h.append(data[0]['percent_change_24h'])
            apercent_change_1h.append( data[0]['percent_change_1h'])
            apercent_change_7d.append(data[0]['percent_change_7d'])
            aprice_btc.append(data[0]['price_btc'])
            amarket_cap_usd.append(data[0]['market_cap_usd'])
            avolume24.append( data[0]['volume24'])
            avolume24a.append(data[0]['volume24a'])
            acsupply.append(data[0]['csupply'])
            atsupply.append( data[0]['tsupply'])
            amsupply.append( data[0]['msupply'])
            rownum = rownum + 2
    ################################ write raw data
    pbtc = home + homename + conky + ptemp + '-raw.txt'
    fo = open(pbtc, 'w')
    for i in range(0,coinnum):
        fo.write('id: {}\n'.format(aid[i]))
        fo.write('symbol: {}\n'.format(asymbol[i]))
        fo.write('name: {}\n'.format(aname[i]))
        fo.write('nameid: {}\n'.format(anameid[i]))
        fo.write('rank: {}\n'.format(arank[i]))
        fo.write('price_usd: {}\n'.format(aprice_usd[i]))
        fo.write('percent_change_24h: {}\n'.format(apercent_change_24h[i]))
        fo.write('percent_change_1h: {}\n'.format(apercent_change_1h[i]))
        fo.write('percent_change_7d: {}\n'.format(apercent_change_7d[i]))
        fo.write('price_btc: {}\n'.format(aprice_btc[i]))
        fo.write('market_cap_usd: {}\n'.format(amarket_cap_usd[i]))
        fo.write('volume24: {}\n'.format(avolume24[i]))
        fo.write('volume24a: {}\n'.format(avolume24a[i]))
        fo.write('csupply: {}\n'.format(acsupply[i]))
        fo.write('tsupply: {}\n'.format(atsupply[i]))
        fo.write('msupply: {}\n'.format(amsupply[i]))
    fo.close()
    ################################ write clean data
    pbtc = home + homename + conky + ptemp + 'clean.txt'
    fo = open(pbtc, 'w')
    for i in range(0,coinnum):
        fo.write('{}\n'.format(aid[i]))
        fo.write('{}\n'.format(asymbol[i]))
        fo.write('{}\n'.format(aname[i]))
        fo.write('{}\n'.format(anameid[i]))
        fo.write('{}\n'.format(arank[i]))
        fo.write('{}\n'.format(aprice_usd[i]))
        fo.write('{}\n'.format(apercent_change_24h[i]))
        fo.write('{}\n'.format(apercent_change_1h[i]))
        fo.write('{}\n'.format(apercent_change_7d[i]))
        fo.write('{}\n'.format(aprice_btc[i]))
        fo.write('{}\n'.format(amarket_cap_usd[i]))
        fo.write('{}\n'.format(avolume24[i]))
        fo.write('{}\n'.format(avolume24a[i]))
        fo.write('{}\n'.format(acsupply[i]))
        fo.write('{}\n'.format(atsupply[i]))
        fo.write('{}\n'.format(amsupply[i]))
    fo.close()
    ################################ compare actual price with targets
    with open(pconky, "w") as fo:
        for i in range(0, coinnum):
            if (float(aprice_usd[i]) >= targetUp[i]):
                tempprice = targetDown
                tempprice = '-'
                news = '${color4}Actual price is above this value.${color}'
                fconky(asymbol[i], aname[i].upper(), fo, aprice_usd[i], targetUp[i], tempprice, row1, news, soundcoins[i])
            elif (float(aprice_usd[i]) <= targetDown[i]):
                tempprice = targetUp
                tempprice = '-'
                news = '${color4}Actual price is under this value.${color}'
                fconky(asymbol[i], aname[i].upper(), fo, aprice_usd[i], tempprice, targetDown[i], row1, news, soundcoins[i])
            else:
                news = 'Actual price is between the targets.'
                fconky(asymbol[i], aname[i].upper(), fo, aprice_usd[i], targetUp[i], targetDown[i], row2, news, soundfake)
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed