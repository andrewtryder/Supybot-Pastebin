import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Pastebin', True)

Pastebin = conf.registerPlugin('Pastebin')

conf.registerGlobalValue(Pastebin, 'pastebinAPIkey', registry.String('', ("""Your pastebin.com API key."""), private=True))
conf.registerGlobalValue(Pastebin, 'visibility', registry.String('Unlisted', ("""Paste visibility. Default unlisted. Must be one of the following: Public, Unlisted, Private""")))
conf.registerGlobalValue(Pastebin, 'expire', registry.String('1Month', ("""Paste expiration date. Default 1Month. Must be one of the following: Never, 10min, 1Hour, 1Day, 1Month""")))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=200:
