import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import os
import urllib, urllib2
from time import gmtime, strftime

class Pastebin(callbacks.Plugin):
    """This plugin contains a command to upload text to pastebin.com."""
    threaded = True

    def pastebin(self, irc, msg, args, optlist, text):
        """[--visibility public|unlisted|private] [--pastename name] <text>
        post <text> to pastebin.com. Default visibility is unlisted. Name the paste using --pastename name.
        """

        api_key = self.registryValue('pastebinAPIkey')

        if api_key == '':
            irc.reply('Pastebin API key must be set. See plugins.pastebinAPIkey value.')

        api_url = 'http://pastebin.com/api/api_post.php'

        # default args.
        visibility = self.registryValue('Visibility').lower()
        pastename = msg.nick + "@" + msg.args[0] + "@" + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        for (key, value) in optlist:
            if key == 'visibility':
                visibility = value
            if key == 'pastename':
                pastename = value
        
        visibility_map = {'public': '0', 'unlisted': '1', 'private': '2'}
        visibility = visibility_map[visibility]

        #expiredate_map = {'never': '
        #expiredate = expiredate_map[expiredate]
        #valid_paste_expire_dates = ('N', '10M', '1H', '1D', '1M')

        #Possible API responses:
        # Bad API request
        # invalid api_dev_key Bad API request
        # invalid login Bad API request
        # account not active Bad API request
        # invalid POST parameters

        values = {'api_paste_code': text,
                  'api_paste_name': pastename,
                  'api_paste_format':'text',
                  'api_paste_private': visibility,
                  'api_paste_expire_date': '1M',
                  'api_option': 'paste',
                  'api_dev_key': api_key
                  }

        data = urllib.urlencode(values)
        req = urllib2.Request(api_url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        irc.reply(the_page)

    pastebin = wrap(pastebin, [getopts({'visibility': ('literal',
                                                        ('public', 
                                                        'unlisted', 
                                                        'private')),
                                         'pastename': ('something')
                                                        }), ('text')])

Class = Pastebin


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
