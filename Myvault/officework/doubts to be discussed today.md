

mapclub
	I am getting an error called sizelimit for feild


```
FieldSizeLimitError: CSV contains a field longer than the maximum length of 131072 characters on line 2079. 
```



my resolution
import sys  
csv.field_size_limit(sys.maxsize)

there is another  error of using incorrect escape character
	Skipping record: ['0510-DRMAC91700700B000', '0510-DRMAC917007', 'SP220427772053', 'SATCHELS 7', 'SATCHELS 7', 'SATCHELS 7\\";SATCHELS 7\\""', 'GENERAL', 'GENERAL,WOMEN>BAGS & WALLETS>Cross Body', 'https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/01-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/02-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/03-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/04-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/05-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg', 'IDR', 'DR. MARTENS', 'One Size', '16', '10', '30', 'Hitam', 'Black', '2299000.000', '1609300.000', '30.00', 'Active']. Reason: The number of header fields does not match the number of fields in the row data: ['0510-DRMAC91700700B000', '0510-DRMAC917007', 'SP220427772053', 'SATCHELS 7', 'SATCHELS 7', 'SATCHELS 7\\";SATCHELS 7\\""', 'GENERAL', 'GENERAL,WOMEN>BAGS & WALLETS>Cross Body', 'https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/01-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/02-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/03-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/04-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg, https://bb-scm-prod-pim.oss-ap-southeast-5.aliyuncs.com/products/61424cca3cb0081d0572c785ccdfefc6/titan/05-DR-MARTENS-BUSM2DRM0-SATCHELS-7-Black.jpg', 'IDR', 'DR. MARTENS', 'One Size', '16', '10', '30', 'Hitam', 'Black', '2299000.000', '1609300.000', '30.00', 'Active']

and i tried to resolve the same 
	through replaciing incorrect escape character with correct escape character
	 https://unbxddev.atlassian.net/browse/CS-6897?focusedCommentId=241344
```
      sed 's/\\"/""/g' raw_feed_file.csv > formatted_feed.csv	 
```

	
and there is some error called 
```
	"message": "failed time-taken: [ 56 minutes 21 seconds 716 milliseconds 658 microseconds ] errors: [ length=58, field=categoryPath, length=35, length=32, uniqueId=SP231117655175, uniqueId=SP200908010121,failed to execute task, uniqueId=SP220708833801, uniqueId=SP230125125717, length=36, length=37,category path depth exceeds threshold, length=50, uniqueId=SP200908012246, threshold=30, uniqueId=SP230704050376, uniqueId=SP231208574018, uniqueId=SP240215074742, length=46 ]",
```

and there is another error called
```
"message": "failed time-taken: [ 57 minutes 33 seconds 559 milliseconds 183 microseconds ] errors: [ unx.cause=Pod was active on the node longer than the specified deadline, failed.stage=source-of-truth-creation(1),internal server error ]",
```

and my resolution is
[https://unbxddev.atlassian.net/issues/CRI-6716?filter=-2](https://unbxddev.atlassian.net/issues/CRI-6716?filter=-2)

I have raised cri ticket with appropriate details

