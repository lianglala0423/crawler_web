import json
import requests
from urllib.parse import quote


query_name = 'DABL-jp009 金亮'

headers = {
    'origin': 'https://www.ruten.com.tw',
    'user-agent': 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
}


def get_prod_id(query_name):
    '''
    get prodID
    '''
    query_name = quote(query_name)
    url = f'https://rtapi.ruten.com.tw/api/search/v3/index.php/core/prod?q={query_name}&type=direct&sort=rnk%2Fdc&limit=99&offset=1'
    res = requests.get(url, headers=headers)
    res_json = json.loads(res.text)
    return [ item['Id'] for item in res_json.get('Rows') ]


def get_prod_info(prod_id_list):
    '''
    get prodinfo by prod_id_list as input
    '''
    prod_id_str = ','.join(prod_id_list)
    url = f'https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod?id={prod_id_str}'
    res = requests.get(url, headers=headers)
    res_json = json.loads(res.text)
    return [ {'ProdId': item['ProdId'], 'ProdName': item['ProdName'],
              'PriceRange': item['PriceRange'], 'Currency': item['Currency']} 
             for item in res_json ]


if __name__ == '__main__':
    prod_id_list = get_prod_id(query_name)
    info = get_prod_info(prod_id_list)
    print(info)
