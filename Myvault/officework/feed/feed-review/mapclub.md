todo
for diffrent size products with same spu it shoudl be one producs with size array wit two sizes
for diffrent products with same spu and diffrent color make it same product 



sftp credentials
```
Hostname: sftp.unbxdapi.com
Username: mapclub
Password: mapclub@#$123
Port: 22
```

sftp credentials link
https://unbxddev.atlassian.net/browse/CS-6897?focusedCommentId=241054

https://search.unbxd.io/864d1797bfd230ef72d5cfdde5868364/ss-unbxd-gcp-kits-com-stage16621684171061/search?q=*&filter=accept_high_rx:1 OR smart_glasses:1 OR accept_progressive:1 OR accept_light_transition:1&promotion=false&fields=accept*, smart*, features*

http://search.unbxd.io/09f89d543e20147b639edf5a9faf1467/ss-unbxd-aapac-dev-mapclub-en56931721299790/search?q=*&variants=false&filter=Details and Style:1 &promotion=false&fields=details*,features*

english
	search api : http://search.unbxd.io/09f89d543e20147b639edf5a9faf1467/ss-unbxd-aapac-dev-mapclub-en56931721299790/search?q=*&variants=false
status : https://feed-apac.unbxd.io/api/ss-unbxd-aapac-dev-mapclub-en56931721299790/catalog/status
sitekey : ss-unbxd-aapac-dev-mapclub-en56931721299790
apikey : 09f89d543e20147b639edf5a9faf1467
secret key : cc78518faceb363a8c9ab5a4e1735169

bahasa
search api  : http://search.unbxd.io/8a8dfca62d64c3456122c4180dd81cde/ss-unbxd-aapac-dev-mapclub-ba56931721299793/search?q=*&variants=false
status : https://feed-apac.unbxd.io/api/ss-unbxd-aapac-dev-mapclub-ba56931721299793/catalog/status
sitekey :ss-unbxd-aapac-dev-mapclub-ba56931721299793
apikey :8a8dfca62d64c3456122c4180dd81cde
secret key : 737440040890657e5f9184c7a648d2fa
console link for same : https://console-apac.unbxd.io/search/sites/1670/keys



feilds in plp
//image(change according to swatches)
//brand
title
//price
selling price
price
discount
//color swatches
//color
there are tags(buy 2 get 50% off)
//category
size
discount
//uniqueId
//availability
//currency



{"siteKey": "ss-unbxd-aapac-dev-mapclub-en56931721299790", "initialProductCount (mainFile)": 49272, "initialProductCount (variantFile)": 0, "initialProductCount (secondaryFiles)": 0, "finalProductCount": 49272, "totalFieldCount": 24, "totalVariantFieldCount": 0, "perf": {"timeTakenToFetchProducts": "1363 ms", "timeTakenForTransformation": "21969 ms", "timeTakenForUpload": "8 ms", "timeTakenForTransformationIncludingUpload": "21977 ms", "timeTakenForPrimaryInsertion": "1456 ms", "timeTakenForSecondaryInsertion": "0 ms", "timeTakenForVariantInsertion": "0 ms", "timeTakenForPrimaryConversion": "3840 ms", "timeTakenForSecondaryConversion": "0 ms", "timeTakenForVariantConversion": "0 ms", "totalTimeTaken": "37289 ms"}, "missingFields": {"titleMissingCount": 0, "imageUrlMissingCount": 0, "productUrlMissingCount": 49272, "priceMissingCount": 0}}



color
imageurl
price
sellingprice
discount
```

def process_category_path(self, category_path):  
    # Strip the input only of the outer brackets and any surrounding whitespace  
    category_path = category_path.strip().strip('[]').strip()  
  
    # Split by the delimiter '>'  
    categories = category_path.split('>')  
  
    # If there are more than 8 categories, keep only the first 8  
    if len(categories) > 8:  
        categories = categories[:8]  
  
    # Join the categories back using '>'  
    processed_category_path = '>'.join(categories)  
  
    # Return the correctly formatted string with a single newline before and after  
    return f'[\n{processed_category_path}\n]'
```

```
  
# if 'categoryPath' in product and product['categoryPath']:  
#     categoryPath = product.get('categoryPath')  
#     product['categoryPath'] = self.process_category_path(categoryPath)
```




filepath : 

/files/English/Dev/UNBXD_en_US.csv


schedule : 0 10,17 * * *

color grouping
```

            # # Generate color_string for products with the same productCode
            # product_code = product.get('productCode')
            # if product_code and product_code in product_groups:
            #     related_products = product_groups[product_code]
            #     # print(product_groups[product_code])
            #     color_string_entries = []
            #
            #     for related_product in related_products:
            #         color_string_entry = {
            #             "uniqueId": related_product.get("uniqueId"),
            #             "imageUrl": related_product.get("imageUrl"),
            #             "size": related_product.get("size"),
            #             "color": related_product.get("color"),
            #             "colorEn": related_product.get("colorEn"),
            #             "price": related_product.get("price"),
            #             "salePrice": related_product.get("salePrice"),
            #             "discount": related_product.get("discount"),
            #             "availability": related_product.get("availability"),
            #         }
            #         color_string_entries.append(color_string_entry)
            #
            #
            #     # Convert the list of entries into a JSON-like string and assign it to color_string
            #     product["color_string"] = json.dumps(color_string_entries)

```