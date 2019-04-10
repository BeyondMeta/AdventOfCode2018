# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:58:42 2018

@author: Sophie
"""


newList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/input5.txt", "r")
for line in file:
    newList.append(line)

polymerString = newList[0]

def polymerReaction(string):
    myStr =string
    for j in range(100000):
        stringreplaced = False
        for i in range(len(myStr) -1):
            if (myStr[i] != myStr[i + 1]) and ((myStr[i].lower()) == (myStr[i + 1].lower())):
                #print("this actually happens huzzah!")
                myStr = myStr.replace(myStr[i:i+2],"")
                #print("after the changes the string is now:", myStr)
                stringreplaced = True
                break
        if stringreplaced == False:
            break
            #print("This does get run")
        
    #if stringreplaced == True:
       # polymerReaction(myStr) 
        print("The length of the string:", len(myStr))
        return len(myStr)
    
def polymerReaction2(string):
    myStr =string
    stringreplaced = True
    while(stringreplaced):
        oldLen = len(myStr)
        myStr = stringReplacement(myStr)
        if len(myStr) == oldLen:
            for i in range(len(myStr) -1):
                if (myStr[i] != myStr[i + 1]) and ((myStr[i].lower()) == (myStr[i + 1].lower())):
                #print("this actually happens huzzah!")
                    myStr = myStr.replace(myStr[i:i+2],"")
                    stringreplaced = True
            else:
                stringreplaced = False
  
    print("The length of the string:", len(myStr))
    return myStr
       


    
replacementTuple = (("aA", ""), ("bB", ""), ("cC", ""), ("dD", ""), 
                    ("eE", ""), ("fF", ""), ("gG", ""), ("hH", ""),
                    ("iI", ""), ("jJ", ""), ("kK", ""), ("lL", ""), 
                    ("mM", ""), ("nN", ""), ("oO", ""), ("pP", ""),
                    ("qQ", ""), ("rR", ""), ("sS", ""), ("tT", ""), 
                    ("uU", ""), ("vV", ""), ("wW", ""), ("xX", ""),
                    ("yY", ""), ("zZ", ""), ("Aa", ""), ("Bb", ""), 
                    ("Cc", ""), ("Dd", ""), ("Ee", ""), ("Ff", ""), 
                    ("Gg", ""), ("Hh", ""), ("Ii", ""), ("Jj", ""), 
                    ("Kk", ""), ("Ll", ""), ("Mm", ""), ("Nn", ""), 
                    ("Oo", ""), ("Pp", ""), ("Qq", ""), ("Rr", ""),
                    ("Ss", ""), ("Tt", ""), ("Uu", ""), ("Vv", ""), 
                    ("Ww", ""), ("Xx", ""), ("Yy", ""), ("Zz", ""))
    
def stringReplacement(s):
    for r in replacementTuple:
        s = s.replace(*r)
    return s
    
def polymerReactionRecursive(string):
    myStr =string
    stringreplaced = False
    for i in range(len(myStr) -1):
        if (myStr[i] != myStr[i + 1]) and ((myStr[i].lower()) == (myStr[i + 1].lower())):
            #print("this actually happens huzzah!")
            myStr = myStr.replace(myStr[i:i+2],"")
            #print("after the changes the string is now:", myStr)
            stringreplaced = True
            break
            #print("This does get run")
        
    if stringreplaced == True:
        polymerReactionRecursive(myStr) 
    else:
        print("The length of the string:", len(myStr))
        #return myStr
    
alphabetString = "abcdefghijklmnopqrstuvwxyz"
    
def improvePolymer(string):
    for i in alphabetString:
        myStr = string.replace(i, "")
        myStr = myStr.replace(i.upper(), "")
        print("Letter :", i)
        polymerReaction2(myStr)

#improvePolymer(polymerString)

def proofOfConcept(string):
    myStr = string
    return (myStr)
    
#print(proofOfConcept("it's a thing"))
    
Test = "dabAcCaCBAcCcaDA"
polymerReaction2(Test)


#polymerReaction(polymerString)

print("Polymer Reaction 2")
polymerReaction2(polymerString)
#print("String length comparison")
#len(stringReplacement(polymerReaction2(polymerString)))
#print("Letter K")
#polymerStringG = polymerString.replace("k", "")
#polymerStringG = polymerStringG.replace("K", "")

#polymerReaction(polymerStringG)

newPolymer = "ipUerNGObhJsyGCBPfUBPiHBVmOXubDsFQQPGNphmlCTHIJYebKWAIKJzQUrkJioJWuhJMAkhMhCFztgwPbkhoXLLBptqnlvHSnsXPMYSZLWJMDEQMhCUrWXPHXKDbRthZpWFxpYiGtniBAErkNQZvxpZdfMiKZReHdwfZVHVaeaySfrJZNKdCxCiBoUrNfSnZeRITKXJksjYZbYidpMylDOMPAvRjrXAOOKRNYHvUlqoewuyeycZNdEDhRAzFPEnVkmNgdBGtCVbNSRLYOLUiuZPzflXpGhBpfYBTDAgjVGftjuGhqgUoCqeqrgeXrApeByuwMfikULPVopjnFGrkRTKsIxNRFtwBrASdBdyPeIjOOPaQUWeZazLPKnWjtdPLTXvRVpvkYukCuTxSuGXPSHGLEVYNEAFinpyHHRbOmYKVBhbCPXtYxTGZGlDljpmzqLdGVKbHbdULeAhEnjgVelWLnFNlqwtbHqYMiRpLhJQGrALbEJStzCflRFelqLDOhvtLCEqphlQxSwAmXtoMlMLohhAsHNTkAgvoEsjnOFkpvXZRbYtmpYWWpddTJRQPZyXLAIuYKxkMSvwdpNFcsaHBpHSuGDThsmrBJsOjSjeygFILotMUwdIHdJtcSgdwpVnVzehVTHVcUtvOVncWYCsoIFWRDXPOAeORjWOhJxOVoPFqqEFlpiuZxslpbnHkoeiCVzMQGWfZMxLFvOnYvwTkQVSQYGDArePzCndTXkaBPjXFrfBGOhTveeXjXUTFCtNHUZjXruXTUZIpRKceMPJXclFDPWVOAjGjOFAsAGQPnBkfwNYkAWTeuBQwMsmlctwBkrHrdnSEClTJMxFtoKRXuJPxrhjwvySpMSQLeCWEYXPNoAhEtPxVnxKGHqYcwoxjqSSFoqtwTovdLHKdnIvtdhdXqCpQfstJIbpfBeoPCJlYHRMRiRgMMKFWUeharKPJkjuqSCFFylcXtHDaeUPhRFAIkWoGFhChViCCOrUOpFvgkRxLmOkwxIjxhzoPPfhVzgXiFybJPMbwZnSUcuIwlGeNcVNUJtNqffaXQTWUeCstVWISaTyNAlPRMTeSMuCvsfWknyNlyRnGkLESiJtxcPXVyctCVGFlkVNmIyRTNzeiUpvgPrkLYPFvLOBNUFNSUyewTiuMaiTQQuzmaeKZjzSVODtsHTkRJFvKxtdjtHolCqbfDNlglJxgPzDSkzYqmeWvkGLBvvTmPGdTEFqqrNbrswUilCZrDWzDNELBCOEjsKiQRaOLpVcSGIptSgsTWMZhypqWkYWDYXdEXlwSUGEJbzNIxEIjiVakQpaNQHLIoakSBZnqSEOQwlylHLBzveCwKGOeudMLsMIBBVPfAlIoiNVDRcJLgXHxFJvfmiVMUaLUDQIrPspZMbTwRhPWxhakOCdrsZsskqUqZmuELpuLepMnntUCQJDvsrmoDJmkoZvMrLTgAldOZXBcGJZIfqExoDReyxWUNIPSeYYmoGZbtSylfhEApUFvuqCNyjaRkvrKlszpyddpzphbZKHLMzRsfGpwxRiPqtDMFdxmmpBaiGLgsasQtmBCRKSGMkgoWOdZPddaZWOtZiqKEvjXKHbTXZNRwCHuwbqvNtJXesgInEDwjwgdATysGbQGMCzXBsATaBRRPuSjcLOOIzTSYptPeufOzrGoDIpyAOgNLphfgYDPRYbyelVonZEzuVdOSNkxRiZapusQnXAJktDWaYbTVcqIqycrhVkMBWPhlKRYubbnrsRdimOdORFyccGYbEnZVLmrCSbHnmyFoVhgaSlQEmgBhaCZOFFaUtAAczhbpjDNWbVyxZtaLkTeClZyMVGjyKrEELwFqVDUPyTWVRHUKAiKRgfxkdayjdtlUgUKoQKbdGxkwCnOXWJHvswVjFAerZCeNpCzrlPiRVVMPKBgDEGmGGMVyQGDIxpOHXlaMeuKwSCMxKYxBFFbNiwtfEYBZHIYJEGoNWVnOqlyZmkAQSZGlqheeKsOIOaucjcyDjyvEskNVpUEJribjQRberaqSfSOUATidNJMlcOpOaefZVhgsOwbWJBAhtCWDaILFtVXPJpCLhguEFrOhsHUPLiYaImHUMFOpXXbmRJQoIqcZpkMWEkCFbhPypJaImvIRwEnZltVkTOdqdzfmkbVjDSoWxFkzaNCdofTcjoIRtibCwMkAKBHYVkJELsHWeZSvhmTjTDRSnQkvLzwEjutbzYDkWvNkZRTQRfYfxogLYxqGZozfkYqCNfHjDiDKMNyUDCwtwCYHcxywBExOmrlFbRNyapZKPUekxMoxRlenMNExDHAnoxmAnFXRIzAckHSkFpjoihRxQNOROKEtxUvSqUmtfTVjPjZYAFisELYCbPGUphPUYuHvPqcAUEdIdFKTqNNYkVeMxVtCAtlxCyKwOZddGuufvotYrZarKRkLFQHnyaNlpmwGrJymXNosLaFvguYNFoGpOIboRwNidPFkuNmjAkdeQKENrOWrnlFhJGevcvCdiRmaNdmRBoWXfZlOUeJqBvEIWIYrajkZmnWWuWZVUYSkwDTsPIuGElEraKSkdctukwzSMNDttcpwpXrkteoAIloHzaveeMgcslCmnPodOWnQuDiCBLeHaOkCbtkJzwSXTZHeuIcqRvsfctcrntWCMHElaHMhioGQELTFcKaCTevIlAcWGujAEbteXITPlwOQklKtmiTCgbEOqpWPCThQDELBIsyoyXifDhgMCBVMqfYfndMWoVkpjlHdnQFZylroDYmklGPoDGLInoyqPYgTlDLfNoZtwfzGhXffcEEBhKNzmRyrXJwhSdTozXcjqwzAnrBPazHDHdkoSDGJWxfxZdaichdUtSeZMYLepTTvSvIwEmTfPmyfrjAgEFhXMvJOujeuiSoVuCLSEooAMoEzKWeMfJnyXWfLcTxsCikUXOyVFvhxoSxJQUDplAvItnEBtDjAOndIRwaTRWKuWTkValfLyyrWAbOMKEdiJSloBnVDrFGeuJrolQFcoHXYzjEWEaxbltFBuhbixdziTCLovjEApKYJtBVfcvOvAgDpJulXkVcSOmArVMEARYQkcAECZABkoQACXsVoGWKXzikMHIFDsuyiMrYQveDJsPxamLupiAlsGTLgDeKgaMdrlNBOucobfnpHCZvMXCxEuiDwvSgCromNHbjGVuqUQtyoznszfTzEhOmfEfGjjOmEZmrJfjHYQLNPcyucpKNWFJrhGiwLWOeIrnsKNCLqLDgDDGGbjuPuJFeiTnpxFnwoDxJkyDPUaitsAHoZsnEXcrkcBqwJujnltskeHahAnmREXqhBrvZdjfwdbDIIETUmcGjgOITesmUMNNNliXTRFiyZwLyIzWNfuqWhpEcVxyRAsaRLQMPSMXGeHCZhucpDmKtvGNGieDqJkkEgTqMLzoGbdLOFABFWabQfWDisULWVQImZVicwRqXGVlhtwaWWsCZNmOBDgbExiBCQoYSpZZZkVwQDGsAJRKtrtqcZDyPLjLClwjEtVUqfLCwCWWiKQJinGafZpDmYDCYuZXqYNBPtyzLWgEQMYbEwuIGTGibGfquMXVNFiFJYxcTybzlwLDpIkmumnQwaShvNKoavycUlNVCtzcswjCvknhwmobPVUQktfhYkmXtabEGvdFjXWDxmbRdqZSGcwaQtnkVJIOsnibeHzsQIqNlcRQhIkDKQBBMndpIhdVQfnsvnLtEdHqXTSBYcKsanzuCbtKDrUGewJPqMPzyRsmdBBSldtWJAsbeLmKqFyPyhWDRWDfwETAqPZLAugDAmpvcZasVZDcZuJlwZoaBfNtUqwIprBHywdHpsnGhbcARciWHWmiWIDIlYqNmfijkYUTEmIzfjLSYIyMtVHNgwgngAYVEMOYPKpyENKQUYqgtUwiirrgtPnQQxCxesPohWyiuWscJVnujMUfIhNvpgEOMwmFDwAUrEcbaTgkDnJhPKnyGRKLBWPPrCCBfiRbPstYZtPquownLEuNacgUEazjwaboFPtGPkmVLQkViWauCsUTWvhfQPDkrTXDtLkIuwvtDNcZWTwrNtjyLDiBjOErlDcnilyDSqyGcBpymamHcGkjFODRqFOhhaBhTOKcFkwnOeqqVBIJLQniVWznekttAOWrewsBhhlbSifbQlbydjKrkzxbwyoAshTotMlmPIxBFIqeaqUwFjQTUisCHuWPzkgyVQcghasXZDJCpQaDrnaoIUZdRXybKbWdcWSWHvsYuqFUXgorsPIQRPdmwyJiZNsogNFmLmWYgjyvzXnPSnLxtdNcrVrOWNsUmKRltaLtSLTOFuBhnmQjfhGoZtWODLysnWhQhfcEVSQoqLipcuEpVxCregScxbDJIbdsNjngNHEpKoGvXDyhGsciBqNjPWvdkzaWqRkRkZnfUGMzSKWaLSUDUqlBHSnVDaWygqpBtKyMwhxIgdUxwTaTDxIDxkXRVjhBfhDZyjtzQLsCbtNOvzUgbulKjPPFqtEnOcNmSkmbPtwjiWiAVhAKxJLtMHapdPjNSDjDDJrthAhjIbZNDCYjqRoVFMaISPLMaVkZqSMkuxhulMabuKqSmUmcRcGbsAdwVnsVgkMJUjmoIWvCWRLmsvFtwePUvlgAyGVjbsoCUdSEonpWGiKIhZummRRPCPbxLMUVMoMMewKrKykzXadqCeANgjweMnnbCscpsjMTAZVMZIcOAHirvATDpxCbFijxcXXdFmgxOfzzoPeAxPGCqFZNItdnjMTUpnGiBQLLjqwslaMXkrSWleBJAUhKUjaryjsMMBsfPiJOLBSRhaUqRPumrdqaqVhZPfBTlJHncxCDxmXDDlBUbKyZpUwZCisEdsXlWCdBimFQKjPaljjPVuqgvIKuOQSVSZmwstpwHfeyzMJEGeAkSIbMGSkmdncXNrsXGCEVJtprxuXvPbcxjmOFdcowsePwLPlqYowmHyPNligtXpftXpUvaCgCOQNmLuhmuPVOPGulItxrYxVUnwuGTFuQYhivrGOOOIVftVtfKsiSnGeTNXFnhzQRdzDDTPTrVKmmfaonHjSDSrmKqaqwfHLeqBXFuKWgIZAuSzXeyAyArqPUCGFSpxBsCLeGQLgLjnylMbUNOdwAesOvCeAroecvcsbERpehQSZSfBnLkuBHsEvMFTWxqjGNAHWulhUPFVsAIgoUaZcGyQebDbfJemIzSBOvhpuJPSBklpWOXuwkZnbhATydOFVUHOFVKnaORTJSXiPCxjovXsNaICtgzMNmmCuheuKPguOXkJWrujENRaoDeuFzkwZsTMieaFxaWxpSrbPOeCYnXmmegdLkqPqzRUaaDRLxLXLCiYCSfAVuDcXWXyxawKJyShTUequWOaeZTmeWUnegsccLYYpmaGKKZjrZOhQDhSJFKtgSSFgCZGzBQywrsAyAxnUGzKullpCJWSqLhqENTkEhphKYcwAuxTgJmhbEGYUPXnlYxUVaUrDlAHNLVquxGjNlaUsjbrYrStBBuhxKnPabAFqntzmowbfodyRhyPjfrbtpSiNDjkqRVjiePlgczEABVMRpvkBvoINlIjLnMtgenvHEsiOweWZkBwOsVIUTvjdYqIPsdbUtdNKHZLqVaiVxlTRFpozEopAuAmskZgoZyMbYoVVhCsuZfBquaUPtSSwjkLZWbLtttIYmwevDWPJhTfYZLYVCPHKoGQVVBgAxKEyRUcApIvyTuWMXfJgXBTQCykDsWMYKglrWvLVxYNLQjzStxkpdQYqtvzcDBsFydnbwOxSferJecbCYjcSpZWcndXGqBunCAfCaLfVsITozGdIqgfsVARymVBMvKgTQMFQYfnPvwOLPsFzaPdfmoQRNrylQLFaZiNfaEQjmoexcMYULkLKLXXlsTsHMcSgQGqGsCmhStSLxxlklKluymCdgDXEOMJqeAFnIzAflqLYRnrqOMFDpAZfSploWVpNFyqfmqtGkVmbvMYravSFGQiDgZOtiSvFlAcFacNUbQgxDNCwzPsCJycBCEjREFsXoWBNDYfSbdCZVTQyqDPKXTsZJqlnyXvlVwRLGkymwSdKYcqtbxGjFxmwUtYViPaCurYekXaGbvvqgOkhpcvylzyFtHjpwdVEWMyiTTTlBwzlKJWssTpuAUQbFzUScHvvOyBmYzOGzKSMaUaPOeZOPfrtLXvIAvQlzhknDTuBDSpiQyDJVtuivSoWbKzwEWoISehVNEGTmNlJiLniOVbKVPrmvbaeZCGLpEIJvrQKJdnIsPTBRFJpYHrYDOFBWOMZTNQfaBApNkXHUbbTsRyRBJSuALnJgXUQvlnhaLdRuAvuXyLNxpuygeBHMjGtXUaWCykHPHeKtneQHlQswjcPLLUkZguNXaYaSRWYqbZgzcGfssGTkfjsHdqHozRJzkkgAMPyylCCSGENuwEMtzEAowUQEutHsYjkWAXYxwxCdUvaFscyIclxlXlrdAAurZQpQKlDGEMMxNycEopBRsPXwAXfAEImtSzWKZfUEdOArneJURwjKxoUGpkUEHUcMMnmZGTciAnSxVOJXcpIxsjtroANkvfohuvfoDYtaHBNzKWUxowPLKbspjUPHVobsZiMEjFBdBEqYgCzAuOGiaSvfpuHLUwhangJQXwtfmVeShbUKlNbFszsqHEPreBSCVCEORaEcVoSEaWDonuBmLYNJlGlqgElcSbXPsfgcupQRaYaYExZsUaziGwkUfxbQElhFWQAQkMRsdsJhNOAFMMkvRtptddZDrqZHNfxntEgNsISkFTvTFviooogRVIHyqUftgUWNuvXyRXTiLUgpovpUMHUlMnqocGcAVuPxTFPxTGILnpYhMWOyQLplWpESWOCDfoMJXCBpVxUXRPTjvecgxSRnxCNDMKsgmBisKaEgejmZYEFhWPTSWMzsvsqoUkiVGQUvpJJLApJkqfMIbDcwLxSDeSIczWuPzYkBubLddxMXdcXCNhjLtbFpzHvQAQDRMUprQuAHrsblojIpFSbmmSJYRAJukHuajbELwsRKxmALSWQJllqbIgNPutmJNDTinzfQcgpXaEpOZZFoXGMfDxxCXJIfBcXPdtaVRIhaoCizmvzatmJSPCScBNNmEWJGnaEcQDAxZKYkRkWEmmOmvumlXBpcprrMMUzHikIgwPNOesDucOSBJvgYaGLVupEWTfVSMlrwcVwiOMJujmKGvSNvWDaSBgCrCMuMsQkUBAmLUHXUKmsQzKvAmlpsiAmfvOrQJycdnzBiJHaHTRjddJdsnJpDPAhmTljXkaHvaIwIJWTpBMKsMnCoNeTQfppJkLUBGuZVonTBcSlqZTJYzdHFbHJvrxKXdiXdtAtWXuDGiXHWmYkTbPQGYwAdvNshbLQuduslAwksZmguFNzKrKrQwAZKDVwpJnQbICSgHYdxVgOkPehnGNJnSDBijdBXCsGERcXvPeUCPIlQOqsveCFHqHwNSYldowTzOgHFJqMNHbUfotlsTlATLrkMuSnwoRvRCnDTXlNspNxZVYJGywMlMfnGOSnzIjYWMDprqipSROGxufQUySVhwswCDwBkBYxrDzuiOANRdAqPcjdzxSAHGCqvYGKZpwUhcSIutqJfWuQAEQifbXipMLmTOtHSaOYWBXZKRkJDYBLqBFIsBLHHbSWERwoaTTKENZwvINqljibvQQEoNWKfCkotHbAHHofQrdofJKgChMAMYPbCgYQsdYLINCdLReoJbIdlYJTnRWtwzCndTVWUiKlTdxtRKdpqFHVwtuScUAwIvKqlvMKpgTpfOBAWJZAeuGCAnUelNWOUQpTzyTSpBrIFbccRppwblkrgYNkpHjNdKGtABCeRuaWdfMWmoeGPVnHiFumJUNvjCSwUIYwHOpSEXcXqqNpTGRRIIWuTGQyuqkneYPkpyomevyaGNGWGnhvTmYiyslJFZiMetuyKJIFMnQyLidiwIMwhwICraCBHgNSPhDWYhbRPiWQuTnFbAOzWLjUzCdzvSAzCVPMadGUalzpQateWFdwrdwHYpYfQkMlEBSajwTDLsbbDMSrYZpmQpjWEguRdkTBcUZNASkCybstxQhDeTlNVSNFqvDHiPDNmbbqkdKiHqrCLnQiqSZhEBINSoijvKNTqAWCgszQDrBMXdwxJfDVgeBATxMKyHFTKquvpBOMWHNKVcJWSCZTcvnLuCYVAOknVHsAWqNMUMKiPdlWLZBYtCXyjfIfnvxmUQFgBIgtgiUWeBymqeGwlZYTpbnyQxzUycdyMdPzFAgNIjqkIwwcWclFQuvTeJWLclJglpYdzCQTRTkrjaSgdqWvKzzzPsyOqcbIXeBGdboMnzcSwwAWTHLvgxQrWCIvzMiqvwluSIdwFqBAwfbafolDBgOZlmQtGeKKjQdEIgngVTkMdPCUHzchEgxmspmqlrASarYXvCePHwQUFnwZiYlWzYIfrtxILnnnmuMSEtioGJgCMuteiidBDWFJDzVRbHQxerMNaHAhEKSTLNJUjWQbCKRCxeNSzOhaSTIAupdYKjXdOWNfXPNtIEfjUpUJBggddGdlQlcnkSNRiEowlWIgHRjfwnkPCUYCpnlqyhJFjRMzeMoJJgFeFMoHeZtFZSNZOYTquQUvgJBhnMORcGsVWdIUeXcxmVzchPNFBOCUobnLRDmAGkEdGltgSLaIPUlMAXpSjdEVqyRmIYUSdfihmKIZxkwgOvSxcaqOKbazceaCKqyraemvRaMosCvKxLUjPdGaVoVCFvbTjykPaeJVOlctIZDXIBHUbfTLBXAeweJZyxhOCfqLORjUEgfRdvNbOLsjIDekmoBawRYYlFLAvKtwUkwrtAWriDNoaJdTbeNTiVaLPduqjXsOXHVfvYoxuKIcSXtClFwxYNjFmEwkZeOmaOOeslcUvOsIUEJUojVmxHfeGaJRFYMpFtMeWiVsVttPElymzEsTuDHCIADzXFXwjgdsOKDhdhZApbRNaZWQJCxZOtDsHWjxRYrMZnkHbeeCFFxHgZFWTzOnFldLtGypQYONilgdOpgLKMydORLYzfqNDhLJPKvOwmDNFyFQmvbcmGHdFIxYOYSibledqHtcpwPQoeBGctIMTkLKqoWLptixETBeaJUgwCaLiVEtcAkCftleqgOIHmhALehmcwTNRCTCFSVrQCiUEhztxsWZjKTBcKoAhElbcIdUqNwoDOpNMcLSCGmEEVAZhOLiaOETKRxPWPCTTdnmsZWKUTCDKskAReLegUipStdWKsyuvzwUwwNMzKJARyiwieVbQjEuoLzFxwObrMDnAMrIDcVCVEgjHfLNRwoRnekqEDKaJMnUKfpDInWrOBioPgOfnyUGVfAlSOnxMYjRgWMPLnAYNhqflKrkRAzRyTOVFUUgDDzoWkYcXLTacTvXmEvKynnQtkfDiDeuaCQpVhUyupHPugpBcyleSIfayzJpJvtFTMuQsVuXTekoronqXrHIOJPfKshKCaZirxfNaMXONahdXenmNELrXOmXKEupkzPAYnrBfLRMoXebWYXChycWTWcduYnmkdIdJhFncQyKFZOzgQXylGOXFyFrqtrzKnVwKdyZBTUJeWZeYElVKqNsrdtJtMHVszEwhSlejKvyhbkaKmWcBITriOJCtFODcnAZKfXwOsdJvBKMFZDQDotKvTLzNeWriVMiAjPYpHBfcKewmKPzCQiOqjrMBxxPofmuhMiAyIlpuhSHoRfeUGHlcPjpxvTfliAdwcTHabjwBWoSGHvzFEAoPoCLmjnDItauosFsQAREBrqJBIRjeuPvnKSeVYJdYCJCUAoioSkEEHQLgzsqaKMzYLQoNvwnOgejyihzbyeFTWInBffbXykXmcsWkUEmALxhoPXidgqYvmggMgedGbkpmvvrIpLRZcPnEczREafJvWSVhjwxoNcWKXgDBkqOkuGuLTDJYADKXFGrkIakuhrvwtYpudvQfWleeRkYJgvmYzLcEtKlATzXYvBwndJPBHZCaaTuAffozcAHbGMeqLsAGHvOfYMNhBscRMlvzNeBygCCYfroDoMIDrSRNBBUyrkLHpwbmKvHRCYQiQCvtByAwdTKjaxNqSUPAzIrXKnsoDvUZezNOvLEYByrpdyGFHPlnGoaYPidOgRZoFUEpTPystZioolCJsUprrbAtaSbxZcmgqBgSYtaDGWJWdeNiGSExjTnVQBWUhcWrnzxtBhkxJVekQIzTowzADDpzDowOGKmgskrcbMTqSASGlgIAbPMMXDfmdTQpIrXWPgFSrZmlhkzBHPZPDDYPZSLkRVKrAJYncQUVfuPaeHFLYsTBzgOMyyEspinuwXYErdOXeQFizjgCbxzoDLaGtlRmVzOKMjdOMRSVdjqcuTNNmPElUPleUMzQuQKSSzSRDcoKAHXwpHrWtBmzPSpRiqdulAumvIMFVjfXhxGljCrdvnIOiLaFpvbbimSlmDUEogkWcEVZblhLYLWqoesQNzbsKAOilhqnAPqKAvIJieXinZBjegusWLxeDxydwyKwQPYHzmwtSGsTPigsCvPloArqIkSJeocblendZwdRzcLIuWSRBnRQQfetDgpMtVVblgKVwEMQyZKsdZpGXjLGLndFBQcLOhTJDTXkVfjrKthSTdovsZJzkEAMZUqqtIAmUItWEYusnfunbolVfpylKRpGVPuIEZntrYiMnvKLfgvcTCYvxpCXTjIselKgNrYLnYNKwFSVcUmsEtmrpLanYtAsiwvTScEuwtqxAFFQnTjunvCnEgLWiUCusNzWBmpjBYfIxGZvHFppOZHXJiXWKoMlXrKGVfPouRoccIvHcHfgOwKiafrHpuEAdhTxCLYffcsQUJKjpkRAHEuwfkmmGrIrmrhyLjcpOEbFPBijTSFqPcQxDHDTViNDkhlDVOtWTQOfssQJXOWCyQhgkXNvXpTeHaOnpxyewcElqsmPsYVWJHRXpjUxrkOTfXmjtLcesNDRhRKbWTCLMSmWqbUEtwaKynWFKbNpqgaSafoJgJaovwpdfLCxjpmECkrPizutxURxJzuhnTcftuxJxEEVtHogbFRfxJpbAKxtDNcZpERadgyqsvqKtWVyNoVflXmzFwgqmZvcIEOKhNBPLSXzUIPLfeQQfpOvoNGnXjHowJroEaopxdrwfiOScywCNvoVTuCvhtvHEZvNvPWDGsCTjDhiDWumTOlifGYEJsJoSjbRMSHtdgUshPbhASCfnPDWVsmKXkyUialxYzpqrjtDDPwwyPMTyBrzxVPKfoNJSeOVGaKtnhSaHHOlmLmOTxMaWsXqLHPQeclTVHodlQLEfrLFcZTsjeBlaRgqjHlPrImyQhBTWQLnfNlwLEvGJNeHaEluDBhBkvgDlQZMPJLdLgzgtXyTxpcBHbvkyMoBrhhYPNIfaenyvelghspxgUsXtUcKUyKVPvrVxtlpDTJwNkplZAzEwuqApooJiEpYDbDsaRbWTfrnXiSktrKRgfNJPOvpluKIFmWUYbEPaRxEGRQEQcOuGQHgUJTFgvJGadtbyFPbHgPxLFZpzUIuloylrsnBvcTgbDGnMKvNepfZarHdeDnzCYEYUWEOQLuVhynrkooaxRJrVapmodLYmPDIyBzyJSKjxktirEzNsFnRuObIcXcDknzjRFsYAEAvhvzFWDhErzkImFDzPXVzqnKReabINTgIyPXfwPzHTrBdkxhpxwRucHmqedmjwlzsympxSNshVLNQTPbllxOHKBpWGTZfcHmHKamjHUwjOIjKRuqZjkiawkBEyjihtcLMHPngpqqfSdBUxoMvbhIpbuFCAJIyijacpbcgYSjHBognREuPI"

improvePolymer(newPolymer)