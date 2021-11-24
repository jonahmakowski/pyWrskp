def sudoku(size):
    import time
    start_time=time.time()

    import sys
    import random as rn
    mydict = {}
    n = 0
    print '--started calculating--'
    while len(mydict) < 9:
        n += 1
        x = range(1, size+1)
        testlist = rn.sample(x, len(x))

        isgood = True
        for dictid,savedlist in mydict.items():
            if isgood == False:
                break
            for v in savedlist:
                if testlist[savedlist.index(v)] == v:
                    isgood = False
                    break

        if isgood == True:
            isgoodafterduplicatecheck = True
            mod = len(mydict) % 3
            dsavedlists = {}
            dtestlists = {}
            dcombindedlists = {}
            for a in range(1,mod + 1):
                savedlist = mydict[len(mydict) - a]               
                for v1 in savedlist:
                    modsavedlists = (savedlist.index(v1) / 3) % 3
                    dsavedlists[len(dsavedlists)] = [modsavedlists,v1]
                for t1 in testlist:
                    modtestlists = (testlist.index(t1) / 3) % 3
                    dtestlists[len(dtestlists)] = [modtestlists,t1]
                for k,v2 in dsavedlists.items():
                    dcombindedlists[len(dcombindedlists)] = v2
                    dcombindedlists[len(dcombindedlists)] = dtestlists[k]
            vsave = 0
            lst1 = []
            for k, vx in dcombindedlists.items():
                vnew = vx[0]
                if not vnew == vsave:
                    lst1 = []
                    lst1.append(vx[1])
                else:
                    if vx[1] in lst1:
                        isgoodafterduplicatecheck = False
                        break
                    else:
                        lst1.append(vx[1])
                vsave = vnew

            if isgoodafterduplicatecheck == True:

                mydict[len(mydict)] = testlist
                print 'success found', len(mydict), 'row'   

    print '--finished calculating--'
    total_time = time.time()-start_time
    return mydict, n, total_time

return_dict, total_tries, amt_of_time = sudoku(9)
print ''
print '--printing output--'
for n,v in return_dict.items():
    print n,v
print 'process took',total_tries,'tries in', round(amt_of_time,2), 'secs'
print '-------------------'