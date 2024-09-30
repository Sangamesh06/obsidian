```
username : dmart  
password:y"rVXgKJ4}
Hostname: sftp.unbxdapi.com
Port: 22
```


feilds in search result page
image url
title
mrp
dmart mrp
change in price(discount)
qty(in title there is quantity)
vegetarian or not
storeid




Categories.CSV 
 Categories,,,,,,,
StoreId,CategoryId,Identifier,TopCategory,ParentCategoryId,Name,ShortDescription,Keyword
10151,93193,aesc-grocerycore,TRUE,,Grocery,Grocery,

 Inventory.csv 
Inventory,,,
SkuId,PartNumber,InventoryStatus,StoreId
10001,110000000,1,10151

Prices.csv
Prices,,,,
SkuId,PartNumber,Mrp,Sp,StoreId
10001,110000000,54,38,10151

Product & SKU List.csv
ProductAndSku
ProductId,PartNumber,ParentProductId,Type,SkuName,ShortDescription,Keyword,BrandName,MarketerManufacturerName,DefiningAttribute_Colour,DefiningAttribute_Weight,DefiningAttribute_Volume,DefiningAttribute_Quantity,DefiningAttribute_Size,VideoLink,DisclaimerText,ManufacturerInfo,Description,ProductShipMode,ProductCODPayMode,NutritionDetail,NutritionFact,FoodType,DmartTag,ProductImageTag,ProductSource,ProductDetailFact,Expiry,ProductTag,Offers,
,**1626145**,PCOOKIES12xx20924,,Product,Unibic Fruit & Nut Cookies,,Unibic, Cookies, Unibic Cookies, Fruit & Nut Cookies, Unibic Fruit & Nut Cookies, Biscuit,,Unibic,Unibic,,,,,,,,,,,,,,,,,,,,,,

ProductAvailability.csv
ProductAvailability,,,
ProductAndSkuId,PartNumber,Status,StoreId
14546,PMensDeosFOG749XX290216,0,10151

ProductCategoryRelationship.csv
ProductCategoryRelationship,,,
ProductId,CategoryId,StoreId,
10001,10134,10151,

productid
storeid
categorypath 
category
image url
title
price(mrp)
dmart price
change in price(discount)
qty(in title there is quantity)
vegetarian or not
storeid


### Pseudo Code to Construct the Combined File:

Here’s the overall flow to combine the data:

1. **Join `ProductAndSkuList.csv` with `ProductCategoryRelationship.csv`**:
    
    - Use `ProductId` as the key to get the related `CategoryId` and `StoreId`.
2. **Join with `Categories.csv`**:
    
    - Using `CategoryId`, fetch the category name and build the category path.
3. **Join with `Prices.csv`**:
    
    - Using `SkuId` or `PartNumber`, get the MRP, selling price (dmart price), and calculate the discount.
4. **Join with `Inventory.csv`**:
    
    - Fetch inventory status using `SkuId`.
5. **Join with `ProductAvailability.csv`**:
    
    - Using `ProductAndSkuId` or `PartNumber`, get the availability status.



pondiscussion with  kiran and arpit
ignore 



```
head -n 10 ProductAvailability.csv
ProductAvailability,,,
ProductAndSkuId,PartNumber,Status,StoreId
14546,PMensDeosFOG749XX290216,0,10151
13502,PCookware4597XX290216,0,10151
13505,PCookware4559XX290216,0,10151
13506,PCookware4561XX290216,0,10151
13507,PMuesliBGR122XX290216,0,10151
13510,PCookiesBTN212XX290216,0,10151
13512,PCookiesBTN215XX290216,0,10151
13513,PCookiesBTN217XX290216,0,10151
```



```
head -n 10 Inventory.csv
Inventory,,,
SkuId,PartNumber,InventoryStatus,StoreId
10001,110000000,1,10151
10001,110000000,1,10654
10001,110000000,1,10655
10001,110000000,1,10656
10001,110000000,1,10657
10001,110000000,1,10658
10001,110000000,1,10659
10001,110000000,1,10660
```

```
head -n 10 "Product & SKU List.csv"
ProductAndSku,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
ProductId, PartNumber,ParentProductId,Type, SkuName, ShortDescription, Keyword,BrandName,MarketerManufacturerName, DefiningAttribute_Colour, DefiningAttribute_Weight, DefiningAttribute_Volume,  DefiningAttribute_Quantity, DefiningAttribute_Size, VideoLink, DisclaimerText, ManufacturerInfo, Description, ProductShipMode, ProductCODPayMode, NutritionDetail, NutritionFact, FoodType, DmartTag, ProductImageTag, ProductSource, ProductDetailFact, Expiry,ProductTag,Offers
1626145,PCOOKIES12xx20924,,Product,Unibic Fruit & Nut Cookies,,"Unibic, Cookies, Unibic Cookies, Fruit & Nut Cookies, Unibic Fruit & Nut Cookies, Biscuit,",Unibic,Unibic,,,,,,,,,,,,,,,,,,,,,
1626156,PTRACKPANTS4xx40924,,Product,Urban Hug Women's Rayon Shorts (14) - Size XL,,"Urbun Hug's Shorts, Shorts,Women's Shorts,Printed Shorts, Multicolour Shorts",UrbanHug,UrbanHug,,,,,,,,,,,,,,,,,,,,,
1626166,PTRACKPANTS14xx40924,,Product,Urban Hug Women's Rayon Shorts (30) - Size XL,,"Urbun Hug's Shorts, Shorts,Women's Shorts,Printed Shorts, Multicolour Shorts",UrbanHug,UrbanHug,,,,,,,,,,,,,,,,,,,,,
1626171,PBLANKETS&QUILTS19xx40924,,Product,VAA Single Micro Comforter Floral - Blue,,"printed comforter, indian comforter,bed comferter, vaa, vaa comforter",VAA,VAA,,,,,,,,,,,,,,,,,,,,,
1626177,PHANDTOWEL25xx40924,,Product,VAA Kitchen Utility Set-Brown,,"Apron ,kitchen utility set , apron glove pot holder , vaa",VAA,VAA,,,,,,,,,,,,,,,,,,,,,
1626188,PUNIVERSALADAPTER36xx40924,,Product,Zebronics Mobile Adaptor With Micro Usb Cable (MA102B) - White,,"Zebronics , Zebronics , Cable , Type C Cable , C Type Cable , USB Cable , Adapter , Cabl , Wier , Mobaile Wier , Cord , USB , Type C , C to C Cable , USB To C , Cable ,",Zebronics,Zebronics,,,,,,,,,,,,,,,,,,,,,
1626198,PEARPHONES46xx40924,,Product,Zebronics Stereo Earphone With Mic (Star) - Black & Gold,,"Zebronics , Zebronics  Earphone , Zebronics Wired Earphone , Earphone Wired , Wier , Cord , Zebronics",Zebronics,Zebronics,,,,,,,,,,,,,,,,,,,,,
1626203,PFESTIVALITEMSDIWALI1xx50924,,Product,Se Clay Lamp Colourful Diya,,"Diwali , Diya Colorfull Diya , Pack Of 12 Diya , Lamp , Clay Lamp , Diya , Deepak",Shreeji Enterprises,Shreeji Enterprises,,,,,,,,,,,,,,,,,,,,,
```

```
head -n 10 "ProductCategoryRelationship.csv"
ProductCategoryRelationship,,,
ProductId,CategoryId,StoreId
10001,10134,10151
10001,93246,10151
10001,93250,10151
10001,93279,10151
10001,120501,10151
10001,10134,10654
10001,93246,10654
10001,93250,10654
```

```
head -n 10 Categories.CSV
Categories,,,,,,,
StoreId,CategoryId,Identifier,TopCategory,ParentCategoryId,Name,ShortDescription,Keyword
10151,93193,aesc-grocerycore,TRUE,,Grocery,Grocery,
10151,93194,aesc-dmartgrocerycore,TRUE,,,,
10151,93195,aesc-packagedfoodcore,TRUE,,Packaged Food,Packaged Food,
10151,93196,aesc-personalcarecore,TRUE,,Personal Care,Personal Care,
10151,93197,aesc-babyandkidscore,TRUE,,Baby & Kids,Baby & Kids,
10151,93198,aesc-specialscore,TRUE,,Seasonal & More,SpecialsSC2,
10151,93199,aesc-fruitsandvegetablescore,TRUE,,Fruits & Vegetables,Fruits & Vegetables,
10151,93200,aesc-homeandkitchencore,TRUE,,Home & Kitchen,Home & Kitchen,


```



```
head -n 10 Prices.csv
Prices,,,,
SkuId,PartNumber,Mrp,Sp,StoreId
10001,110000000,54,38,10151
10001,110000000,54,38,10654
10001,110000000,66,56,10655
10001,110000000,66,51,10656
10001,110000000,66,51,10657
10001,110000000,64,56,10658
10001,110000000,64,49,10659
10001,110000000,64,49,10660
```

