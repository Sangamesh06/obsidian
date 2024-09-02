

```
const peddersstage = {

  

search: {

inputBox: "#search_mini_form #search",

queryBtn: ".actions .search",

urlParam: "q",

},

productClickGrid: {

productElemWrapper: ".products.wrapper .products .product-item",

pidSelector: ".products.wrapper .products .product-item .product-item-info",

productPidAttr: "id",

getPidFromCB: function (pidString) {

let pid = pidString.split('_');

return pid[pid.length-1];

},

source: "PRODUCT_CLICK_GRID",

},

  
  

pageView: {

delay: "1500",

events: {

home: {

uniqueSelectors: {

selectors: [".block-static-block .home-slider"],

},

urlIdentifiers: {

urls: ["https://mcstaging.pedders.com.au/"],

exactMatch: true

}

},

search: {

uniqueSelectors: {

selectors: [".UNX-product-results #searchResultsWrapper"]

},

urlIdentifiers: {

urls: ["?q="],

exactMatch: false,

},

},

category: {

uniqueSelectors: {

selectors: ['#maincontent #amasty-shopby-product-list'],

}

},

productDisplay: {

uniqueSelectors: {

selectors: [".columns .product-info-main .page-title-wrapper"]

},

urlIdentifiers: {

urls: ["product/"],

exactMatch: false,

},

},

order: {

urlIdentifiers: {

urls: ["https://mcstaging.pedders.com.au/checkout/cart/"],

exactMatch: true,

},

},

}

}

};

  

export default peddersstage;
```


```
{

"siteName": "ss-unbxd-stage-pedders-magento45311690751591",

"sdkVersion": "v5.0.9"

}
```


http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-aapac-prod-lifestyle-LandMark48741706891693?fromDate=2024-06-09&toDate=2024-06-09


firepageveiwevent
processPageView
pushPageView
checkForPageView
 observer


https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-prod-pedders-magento45311690751706/ua/ua.js




Unbxd.trackMultiple('order', [{"pid":"test"},{"pid":"test2"},{"pid":"test3"},{"pid":"test4"}], misc = {"pageType": "PDP"})

 for order event misc data 
 Unbxd.trackMultiple("order", [{pid:"test", price: "0"}], {"form": "true", "page": "HOME"}) 
ask aditya

form submitting details
name :  sangamesh soma
no : +61-455-529-141
reg no:12876yjnbuyt56
email :somashettisangamesh@gmail.com
reg state: NSW
selected store :Maribyrnong, 155 Rosamond Road, VIC 3032

