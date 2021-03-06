# -*- coding: utf-8 -*-

import requests
from random import randint
from time import sleep

def main():
    session.links = []
    return dict(message="hello from qreddit.py")

def fetch():
    '''
            fetch random number from quantum random number generator

            There are 1082444 articles
			numbers are generated between 0 and 65535

			I generate 16 numbers and get a summation of their numbers
		    Then I add 16 to that sum

	'''
    try:
        # rsum = randint(1, 1082444)
        logger.debug('sent request to anu')

        r = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=16&type=uint16").json()
        rsum = sum(r['data'])
        rsum = rsum + 16

        # rsum = randint(1, 1082444)
        logger.debug(rsum)

        # sql query
        rsite = db(db.subreddits.id == rsum).select()[0].site
        rsite = 'https://www.reddit.com/r/' + rsite
        logger.debug(rsite)
        session.links = [rsite] + session.links

    except Exception as e:
        logger.error(traceback.format_exc())
        session.links = [rsite] + "oops unexpected error"

    logger.debug('test button end')
    html = make_html()
    return html

def make_html():
    table = TABLE([A(v, _href=v, _target="_blank") for v in session.links]).xml()
    html = '''
        <nav class="navbar navbar-expand-md navbar-light bg-light">
          <span class="navbar-brand mb-0 h1">RandReddit</span>
          <a class="nav-link github-link" href="#">github</a>
          <ul class="navbar-nav ml-auto">
            <button onclick="go()" id="go" class="btn btn-outline-warning" type="button">
                go
            </button>
          </ul>

        </nav>
        <div class="container-fluid flex-fill" id='siteloader'>
               '''
    html = html + table + '</div>'
    return html
