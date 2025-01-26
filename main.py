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
    ],
    'Asus':[
        {
            'model': 'ZenBook 14',
            'specs': {
                'Processor': 'AMD Ryzen 7 5800H',
                'RAM': '16 GB',
                'Storage': '512 GB',
                'Display': "14-inch FHD (1920x1080)",
                'Weight': '2.65 lbs',
                'Best For': 'Everyday users and professionals',
                'Cost': '1200-1400 $'
            }
        },
        {
            'model': 'ROG Zephyrus G14',
            'specs': {
                'Processor': 'AMD Ryzen 9 6900HS',
                'RAM': '16 GB',
                'Storage': '1 TB',
                'Display': "14-inch QHD (2560x1440), 120Hz",
                'Weight': '3.64 lbs',
                'Best For': 'Gamers and creators',
                'Cost': '1600-2000 $'
            }
        },
        {
            'model': 'VivoBook 15',
            'specs': {
                'Processor': 'Intel Core i5-1235U',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': "15.6-inch FHD (1920x1080)",
                'Weight': '3.75 lbs',
                'Best For': 'Students and budget users',
                'Cost': '600-800 $'
            }
        },
        {
            'model': 'TUF Gaming A15',
            'specs': {
                'Processor': 'AMD Ryzen 7 6800H',
                'RAM': '16 GB',
                'Storage': '1 TB',
                'Display': "15.6-inch FHD (1920x1080), 144Hz",
                'Weight': '4.85 lbs',
                'Best For': 'Gamers and power users',
                'Cost': '1300-1600 $'
            }
        },
        {
            'model': 'ProArt Studiobook 16',
            'specs': {
                'Processor': 'Intel Core i9-13980HX',
                'RAM': '32 GB',
                'Storage': '2 TB',
                'Display': "16-inch 4K UHD (3840x2400), OLED",
                'Weight': '5.16 lbs',
                'Best For': 'Professionals and creators',
                'Cost': '3000-3500 $'
            }
        }
    ],
        'Apple': [
        {
            'model': 'MacBook Air M2',
            'specs': {
                'Processor': 'Apple M2',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': "13.6-inch Retina (2560x1664)",
                'Weight': '2.7 lbs',
                'Best For': 'Everyday users and students',
                'Cost': '1200-1500 $'
            }
        },
        {
            'model': 'MacBook Air M1',
            'specs': {
                'Processor': 'Apple M1',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': "13.3-inch Retina (2560x1600)",
                'Weight': '2.8 lbs',
                'Best For': 'Budget-conscious users',
                'Cost': '999-1200 $'
            }
        },
        {
            'model': 'MacBook Pro 14-inch',
            'specs': {
                'Processor': 'Apple M2 Pro',
                'RAM': '16 GB',
                'Storage': '512 GB',
                'Display': "14.2-inch Liquid Retina XDR (3024x1964)",
                'Weight': '3.5 lbs',
                'Best For': 'Professionals and creatives',
                'Cost': '2000-2500 $'
            }
        },
        {
            'model': 'MacBook Pro 16-inch',
            'specs': {
                'Processor': 'Apple M2 Max',
                'RAM': '32 GB',
                'Storage': '1 TB',
                'Display': "16.2-inch Liquid Retina XDR (3456x2234)",
                'Weight': '4.7 lbs',
                'Best For': 'Power users and creators',
                'Cost': '3000-3500 $'
            }
        },
        {
            'model': 'MacBook Pro 13-inch',
            'specs': {
                'Processor': 'Apple M2',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': "13.3-inch Retina (2560x1600)",
                'Weight': '3.0 lbs',
                'Best For': 'Students and professionals',
                'Cost': '1300-1600 $'
            }
        }
    ]
}