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

    def pastebin(self, irc, msg, args, text):
        """<text>
        post <text> to pastebin.com.  Expires in 1 month.
        """

        api_key = self.registryValue('pastebinAPIkey')

        if api_key == '':
            irc.reply('Pastebin API key must be set. See plugins.pastebinAPIkey value.')

        api_url = 'http://pastebin.com/api/api_post.php'
        
        #valid_paste_expire_dates = ('N', '10M', '1H', '1D', '1M')
        #valid_paste_private ('0', '1', '2') # 0=public, 1=unlisted, 2=private

        #Possible API responses:
        # Bad API request
        # invalid api_dev_key Bad API request
        # invalid login Bad API request
        # account not active Bad API request
        # invalid POST parameters

        pastename = irc.nick + "@" + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        
        values = {'api_paste_code': text,
                  'api_paste_name': pastename,
                  'api_paste_format':'text',
                  'api_paste_private': 1,
                  'api_paste_expire_date': '1M',
                  'api_option': 'paste',
                  'api_dev_key': api_key
                  }

        data = urllib.urlencode(values)
        req = urllib2.Request(api_url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        irc.reply(the_page)

    pastebin = wrap(pastebin, ['text'])

Class = Pastebin


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
