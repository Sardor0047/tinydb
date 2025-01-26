from tinydb import TinyDB
import requests


db = TinyDB('texnomart.json')

notebooks = {
    'Lenovo':[
        {
            'model': 'ThinkPad X1 Carbon Gen 10',
            'characteristic' : {
                'Processor': 'Intel Core i7-1260P',
                'RAM': '16GB',
                'Storage': '512GB SSD',
                'Display': "14-inch WUXGA (1920x1200)",
                'Weight': '2.48 lbs',
                'Best For': 'Business professionals',
                'Cost': '1500-1800 $'
            }
        },
        {
            'model':'Yoga 9i',
            'characteristic':{
                'Processor': 'Intel Core i7-1360P',
                'RAM': '16 GB',
                'Storage' : '1 TB',
                'Display':"14' 4K UHD OLED",
                'Weight':'3.09 lbs',
                'Best For':'Creatives and multimedia',
                'Cost':'1600-2000 $'
            }
        }
    ]
}