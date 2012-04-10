import gettext

def getTranslation(lang):
    t = gettext.translation('guildpact','locale',languages=[lang])
    return t.ugettext

