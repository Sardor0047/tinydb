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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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
            'characteristic': {
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

phones = {
    'Samsung': [
        {
            'model': 'Galaxy S24 Ultra',
            'category': 'Flagship',
            'characteristic': {
                'Processor': 'Snapdragon 8 Gen 3',
                'RAM': '12 GB',
                'Storage': '256 GB',
                'Display': '6.8-inch Dynamic AMOLED 2X (3088x1440)',
                'Battery': '5000 mAh',
                'Camera': '200 MP + 12 MP + 50 MP + 10 MP',
                'OS': 'Android 14 (One UI 6)',
                'Features': ['Built-in S Pen', 'Titanium frame', '100x Space Zoom'],
                'Cost': '$1,300-1,600'
            }
        },
        {
            'model': 'Galaxy Z Fold 6',
            'category': 'Foldable',
            'characteristic': {
                'Processor': 'Snapdragon 8 Gen 3',
                'RAM': '12 GB',
                'Storage': '512 GB',
                'Display': '7.6-inch Foldable AMOLED (2176x1812)',
                'Battery': '4800 mAh',
                'Camera': '50 MP + 12 MP + 10 MP',
                'OS': 'Android 14 (One UI 6)',
                'Features': ['IPX8 water resistance', 'Multi-window multitasking'],
                'Cost': '$1,800-2,000'
            }
        },
        {
            'model': 'Galaxy A35 5G',
            'category': 'Mid-Range',
            'characteristic': {
                'Processor': 'Exynos 1380',
                'RAM': '8 GB',
                'Storage': '128 GB',
                'Display': '6.5-inch Super AMOLED (1080x2340)',
                'Battery': '5000 mAh',
                'Camera': '50 MP + 8 MP + 5 MP',
                'OS': 'Android 14 (One UI 6)',
                'Features': ['120Hz refresh rate', '25W fast charging'],
                'Cost': '$350-450'
            }
        },
        {
            'model': 'Galaxy S23 FE',
            'category': 'Affordable Flagship',
            'characteristic': {
                'Processor': 'Exynos 2200',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': '6.4-inch Dynamic AMOLED (1080x2340)',
                'Battery': '4500 mAh',
                'Camera': '50 MP + 12 MP + 8 MP',
                'OS': 'Android 14 (One UI 6)',
                'Features': ['Wireless charging', 'Flagship-grade camera'],
                'Cost': '$600-750'
            }
        },
        {
            'model': 'Galaxy M54 5G',
            'category': 'Budget',
            'characteristic': {
                'Processor': 'Exynos 1380',
                'RAM': '6 GB',
                'Storage': '128 GB',
                'Display': '6.7-inch Super AMOLED (1080x2400)',
                'Battery': '6000 mAh',
                'Camera': '64 MP + 12 MP + 5 MP',
                'OS': 'Android 14 (One UI 6)',
                'Features': ['25W charging', '5G support'],
                'Cost': '$250-350'
            }
        }
    ],
    'Apple': [
        {
            'model': 'iPhone 15 Pro Max',
            'category': 'Flagship',
            'specs': {
                'Processor': 'A17 Bionic',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': '6.7-inch Super Retina XDR (2796x1290)',
                'Battery': '4352 mAh',
                'Camera': '48 MP + 12 MP + 12 MP',
                'OS': 'iOS 17',
                'Cost': '$1,200-1,400'
            }
        },
        {
            'model': 'iPhone 15',
            'category': 'Mainstream',
            'specs': {
                'Processor': 'A16 Bionic',
                'RAM': '6 GB',
                'Storage': '128 GB',
                'Display': '6.1-inch Super Retina XDR (2532x1170)',
                'Battery': '3349 mAh',
                'Camera': '48 MP + 12 MP',
                'OS': 'iOS 17',
                'Cost': '$800-1,000'
            }
        },
        {
            'model': 'iPhone SE (4th Gen)',
            'category': 'Budget',
            'specs': {
                'Processor': 'A16 Bionic',
                'RAM': '4 GB',
                'Storage': '64 GB',
                'Display': '6.1-inch LCD (1792x828)',
                'Battery': '2018 mAh',
                'Camera': '12 MP',
                'OS': 'iOS 17',
                'Cost': '$450-550'
            }
        },
        {
            'model': 'iPhone 14 Plus',
            'category': 'Large Display',
            'specs': {
                'Processor': 'A15 Bionic',
                'RAM': '6 GB',
                'Storage': '128 GB',
                'Display': '6.7-inch Super Retina XDR (2778x1284)',
                'Battery': '4325 mAh',
                'Camera': '12 MP + 12 MP',
                'OS': 'iOS 17',
                'Cost': '$900-1,100'
            }
        },
        {
            'model': 'iPhone 13 Mini',
            'category': 'Compact',
            'specs': {
                'Processor': 'A15 Bionic',
                'RAM': '4 GB',
                'Storage': '128 GB',
                'Display': '5.4-inch Super Retina XDR (2340x1080)',
                'Battery': '2406 mAh',
                'Camera': '12 MP + 12 MP',
                'OS': 'iOS 17',
                'Cost': '$600-700'
            }
        }
    ],
        'Xiaomi': [
        {
            'model': 'Xiaomi 14 Pro',
            'category': 'Flagship',
            'specs': {
                'Processor': 'Snapdragon 8 Gen 3',
                'RAM': '12 GB',
                'Storage': '256 GB',
                'Display': '6.73-inch AMOLED (3200x1440)',
                'Battery': '5000 mAh',
                'Camera': '50 MP + 50 MP + 50 MP',
                'OS': 'Android 14 (HyperOS)',
                'Features': ['Leica camera', '120W fast charging', 'IP68 rating'],
                'Cost': '$900-1,100'
            }
        },
        {
            'model': 'Xiaomi 13T Pro',
            'category': 'Mid-Range',
            'specs': {
                'Processor': 'Dimensity 9200+',
                'RAM': '12 GB',
                'Storage': '512 GB',
                'Display': '6.67-inch AMOLED (2712x1220)',
                'Battery': '5000 mAh',
                'Camera': '50 MP + 12 MP + 8 MP',
                'OS': 'Android 14 (HyperOS)',
                'Features': ['144Hz display', '120W fast charging'],
                'Cost': '$600-750'
            }
        },
        {
            'model': 'Redmi Note 13 Pro+',
            'category': 'Budget Flagship',
            'specs': {
                'Processor': 'Dimensity 7200 Ultra',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': '6.67-inch AMOLED (2712x1220)',
                'Battery': '5000 mAh',
                'Camera': '200 MP + 8 MP + 2 MP',
                'OS': 'Android 14 (HyperOS)',
                'Cost': '$400-500'
            }
        },
        {
            'model': 'Poco F5',
            'category': 'Gaming',
            'specs': {
                'Processor': 'Snapdragon 7+ Gen 2',
                'RAM': '8 GB',
                'Storage': '256 GB',
                'Display': '6.67-inch AMOLED (2400x1080)',
                'Battery': '5000 mAh',
                'Camera': '64 MP + 8 MP + 2 MP',
                'OS': 'Android 14 (HyperOS)',
                'Cost': '$350-450'
            }
        },
        {
            'model': 'Redmi 12',
            'category': 'Budget',
            'specs': {
                'Processor': 'Helio G88',
                'RAM': '4 GB',
                'Storage': '128 GB',
                'Display': '6.79-inch IPS (2460x1080)',
                'Battery': '5000 mAh',
                'Camera': '50 MP + 8 MP + 2 MP',
                'OS': 'Android 13 (MIUI 14)',
                'Cost': '$150-200'
            }
        }
    ]

}


db.insert_multiple([notebooks,phones])