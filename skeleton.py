# -*- coding: utf-8 -*-

import requests


def main():
    '''
            There are 14625793 wikipedia articles
            numbers are generated between 0 and 65535 (this is the max provided by the api: https://qrng.anu.edu.au/API/api-demo.php)
            I generate 223 numbers and get a summation of their numbers
            Then I add 223 to that sum
            (because my index for the articles starts at 1)
    '''
    try:
        print('sending request to: https://qrng.anu.edu.au/API/jsonI.php?length=223&type=uint16')
        r = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=223&type=uint16").json()
        print('response: ')
        print(r)
        rsum = sum(r['data'])
        rsum = rsum + 223
        print('sum: %i' % rsum)
        print('There are 14625793 wikipedia articles')
        print('%i will be mapped to an article' % rsum)
    except Exception as e:

        print("oops unexpected error")

    return

main()
