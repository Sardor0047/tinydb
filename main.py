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
            'model':'Yoga 9i ',
            'characteristic':{
                'Processor': 'Intel Core i7-1360P',
                'RAM': '16 GB',
                'Storage' : '1 TB SSD',
                'Display': "14' 4K UHD OLED",
                'Weight':'3.09 lbs',
                'Best For':'Creatives and multimedia',
                'Cost':'1600-2000 $'
            }
        },
        {
            'model':'Legion 5 Pro (16-inch)',
            'characteristic':{
                'Processor' : 'AMD Ryzen 7 6800H',
                'RAM' : '16 GB',
                'Storage' : '1TB SSD',
                'Display' : "16' WQXGA (2560x1600), IPS, 165Hz, 500 nits",
                'Weight':'5.4 lbs',
                'Best For':'Gamers and content creators',
                'Cost':'1800-2300 $'
            }
        },
        {
            'model': 'IdeaPad Flex 5 (14-inch)',
            'characteristic':{
                'Processor': 'AMD Ryzen 5 5500U',
                'RAM': '8 GB',
                'Storage':'256GB SSD',
                'Display':'14" FHD (1920x1080), IPS, Touchscreen, 300 nits',
                'Weight':'3.64 lbs',
                'Best for':'Students and budget users',
                'Cost':'700-900 $'
            }
        },
        {
            'model':'ThinkBook 16p Gen 4',
            'characteristic':{
                'Processor':'AMD Ryzen 9 6900HX',
                'RAM':'32 GB',
                'Storage': '1TB SSD',
                'Display': '16" WQXGA (2560x1600), IPS, 165Hz, 500 nits',
                'Weight':'4.5 lbs',
                'Best for':'Professionals and creators',
                'Cost' :'2000-2500 $'
            }
        }
    ]
}