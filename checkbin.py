import requests 
from os import system as SYSS 
from sys import exit as EXT 

"""main checker brodi""" 
class main(object): 

    """startin it out""" 
    @classmethod 
    def check(cls, bins): 
        if bins == '':
            EXT('[!] Bin not Found!') 
        else: 
            cls.main(bins) 


    """requests data json""" 
    @classmethod 
    def main(cls, x): 
        x = { 
            'author': 'DR4G0N5', 
            'url': 'https://bins-su-api.now.sh/api/'+x,
            'version': '0.1.1' 
        }

        req = requests.get(x['url']) 
        requests_json = req.json() 

        """Send that shit to json brodi"""
        if requests_json['result'] == 'false': 
            EXT('[!] Bin Error.')
        else: 
            r = requests_json['data'] 
            cls.main_check(r, x) 

    @classmethod 
    def main_check(cls, r, xx): 
        full_data = r 

        """data shit""" 
        data = { 
            'Bin': full_data['bin'], 
            'Vendor': full_data['vendor'], 
            'Type': full_data['type'], 
            'Level': full_data['level'], 
            'Bank': full_data['bank'], 
            'Country': full_data['country'] 
        }

        print("""
    [+] Author: {}
    [+] Version: {}""".format(xx['author'],xx['version']))
        print("""
    [+] Bin: {} 
    [+] vendor: {} 
    [+] Type: {} 
    [+] Level: {}
    [+] Bank: {}
    [+] Country: {}""".format(data['Bin'],
    data['Vendor'],
    data['Type'],
    data['Level'],
    data['Bank'],
    data['Country']))


if __name__ == '__main__': 

    BINS = input('[+] Bin: ') 
    main.check(BINS) 
