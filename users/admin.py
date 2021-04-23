from django.contrib import admin
from .models import Profile, JProfile, Coin, Item, Certificate, UserKey, Ranker, Classification

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ("user", "image", "dream", "hobby", "nickname", "interest")

@admin.register(JProfile)
class JProfile(admin.ModelAdmin):
    list_display = ("user", "political_orientation", "levels", "position", "department")

@admin.register(Coin)
class Coin(admin.ModelAdmin):
    list_display = ("user", "blackcoin","bluecoin", "greencoin", "orangecoin", "pinkcoin", "purplecoin")

@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = (
        "user",
        "spear",
        "shield",
        "sword",
        "armor",
        "getsword",
        "star",
        "reference_letter",
        "recommended",
        "refutation",
        "impeachment",
        "impeached",
        "swordOfGod",
        "spearOfGod",
        "shieldOfGod",
        "impeachment_shield"
    )

@admin.register(Certificate)
class Certificate(admin.ModelAdmin):
    list_display = (
        "user",
        "OPCcertificate",
        "MPMcertificate",
        "MSITcertificate",
        "SPOcertificate",
        "BAIcertificate",
        "NPAcertificate"
    )

@admin.register(UserKey)
class UserKEY(admin.ModelAdmin):
    list_display = (
        "user",
        "MSITfirstkey",
        "MSITsecondkey",
        "MSITthirdkey",
        "MSITfourthkey",
        "MSITfifthkey",
        "MPMfirstkey",
        "MPMsecondkey",
        "MPMthirdkey",
        "MPMfourthkey",
        "MPMfifthkey",
        "BAIfirstkey",
        "BAIsecondkey",
        "BAIthirdkey",
        "BAIfourthkey",
        "SPOfirstkey",
        "SPOsecondkey",
        "SPOthirdkey",
        "SPOfourthkey",
        "SPOfifthkey",
        "NPAfirstkey",
        "NPAsecondkey",
        "NPAthirdkey",
        "NPAfourthkey",
        "NPAfifthkey",
        "OPCfirstkey",
        "OPCsecondkey",
        "OPCthirdkey",
        "OPCfourthkey",
        "OPCfifthkey",
        "OPCsixthkey",
        "OPCseventhkey",
        "SSkey"
    )

@admin.register(Ranker)
class Ranker(admin.ModelAdmin):
    list_display = ("user", 'nickname', "rankpoint")

@admin.register(Classification)
class Classification(admin.ModelAdmin):
    list_display= ("political_orientation", "numberOfUser", "date_changed")
