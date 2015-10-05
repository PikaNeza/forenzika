   import urllib2
response = urllib2.urlopen("https://dl.dropboxusercontent.com/u/29645703/SmartNinja/DNK/dna.txt")
dnk = response.read()
print dnk

spol_z = dnk.find("TGAAGGACCTTC")
spol_m = dnk.find("TGCAGGAACTTC")
if spol_z != -1:
    print("Osumljenka je!")
    spol = "Z"
else:
    print("Osumljenec je moski!")
    spol = "M"
belec = dnk.find("AAAACCTCA")
negro = dnk.find("CGACTACAG")
aziat = dnk.find("CGCGGGCCG")
if belec != -1:
    print("Je belec.")
    rasa = "belec"
elif negro != -1:
    print("Je afro-ameriskega rodu.")
    rasa = "crnc"
else:
    print("Je azijskega rodu.")
    rasa = "aziat"
crni_lasje = dnk.find("CCAGCAATCGC")
rjavi_lasje = dnk.find("GCCAGTGCCG")
korenckasti = dnk.find("TTAGCTATCGC")
if crni_lasje != -1:
    print("Ima crne lase")
    lasje = "crni"
elif rjavi_lasje != -1:
    print("Ima rjave lase")
    lasje = "rjavi"
else:
    print("Ima oranzne lase")
    lasje = "oranzni"
kvadraten = dnk.find("GCCACGG")
okrogel = dnk.find("ACCACAA")
ovalen = dnk.find("AGGCCTCA")
if kvadraten != -1:
    print("Ima kvadraten obraz")
    obraz = "kvadraten"
elif okrogel != -1:
    print("Ima okrogel obraz")
    obraz = "okrogel"
else:
    print("Ima ovalen obraz")
    obraz = "ovalen"
modre_oci = dnk.find("TTGTGGTGGC")
zelene_oci = dnk.find("GGGAGGTGGC")
rjave_oci = dnk.find("AAGTAGTGAC")
if modre_oci != -1:
    print("Oci ima modre.")
    oci = "modre"
elif zelene_oci != -1:
    print("Oci ima zelene.")
    oci = "zelene"
else:
    print("Oci ima rjave.")
    oci = "rjave"
print("Osumljenec ima sledece karakteristike: %s" % spol, rasa, lasje, obraz, oci)
if spol == "M" and rasa == belec and lasje == oranzni and obraz == okrogel and oci == rjave:
    print("Osumljenec je ZIGA")
elif spol == "M" and rasa == belec and lasje == crni and obraz == ovalen and oci == modre:
	print("Osumljenec je MATEJ")
else:
    print("Osumljenec je MIHA")


