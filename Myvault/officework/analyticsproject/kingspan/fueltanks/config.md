

```
const websitestage = {
  search: {
    inputBox: ".search form[action="/search"] input[id*=search]",
    queryBtn: ".search form[action="/search"] input.submit",
    urlParam: "search",
  },
  productClickGrid: {
    productElemWrapper: "#main-body #prodlist .productframe",
    productPidAttr: "unbxdparam_sku",
    source: "PRODUCT_CLICK_GRID"
  },
  addToCartFromSRP: {
    addToCartBtnSelector: "",
    // addToCartBtnSelector: "[data-unxCartBtn='addToCart']", //for unbxd sdk customer
    source: "ADD_TO_CART_SRP",
  },
  addToCartFromPDP: {
    addToCartBtnSelector: "#main-body #productrightbox .addtobasket .actionbutton",
    pidSelector: "#main-body #productrightbox .addtobasket input[id="prodid"]",
    productPidAttr: "value",
    qtySelector: "#productrightbox .addtobasket .qtywrap  #quantity",
    variant: true,
    vidSelector: "#main-body #productrightbox #optionswrap input[id="optionvarid"]",
    productVidAttr: "value",
    source: "ADD_TO_CART_PDP",
  },
  addToCartFromCartPage: {
    cartItemWrapper: "#main-body  form[id="basket"]  .odd",
    pidSelector: "#main-body  form[id="basket"]  .odd .basketimage",
    productPidAttr: "src",  
    getPidFromCB: function (pidString) {
    	const pidlast = src.split("/").pop();
    	const pid = pidlast.split("_")[0]; 
    	return pid;
    },
    qtyPlusSelector: "#main-body  form[id="basket"]  .odd .qtywrap .qtyup",
    qtyMinusSelector: "#main-body  form[id="basket"]  .odd .qtywrap .qtydown",
    qtyDelay: "",
    variant: true,
    vidSelector: "",
    productVidAttr: "",
    source: "ADD_TO_CART_FROM_CART_PAGE",
  },
  pageView: {
    delay: "1500",
    events: {
      home: {
        uniqueSelectors: {
          selectors: ['#home .hometop  #imagechanger'],
        },
        urlIdentifiers: {
          urls: ["https://fueltank.iconography.co.uk/"],
          exactMatch: true,
        },
      },
      search: {
        uniqueSelectors: {
          selectors: ['body[id="search"] #main-body .pagecontainer'],
        },
        urlIdentifiers: {
          urls: ["https://fueltank.iconography.co.uk/search/"],
          exactMatch: false,
        },
      },
      category: {
        uniqueSelectors: {
          selectors: ['body[id="categories"] #main-body .pagecontainer'],
        },
      },
      productDisplay: {
        uniqueSelectors: {
          selectors: ['body[id="product"]'],
        },
      },
      cart: {
        uniqueSelectors: {
          selectors: [body[id="shoppingbasket"]],
        },
        urlIdentifiers: {
          urls: ["https://fueltank.iconography.co.uk/shopping-basket"],
          exactMatch: true,
        },
      },
   
    },
  },
};
```

final

```
const FuelTankShopStage = {  
  metaData: {  
        siteName: "ss-unbxd-auk-dev-Fueltankshop53931716296619",  
  },  
  search: {  
    inputBox: '.search form[action="/search"] input[id*="search"]',  
    queryBtn: '.search form[action="/search"] input.submit',  
    urlParam: "search",  
  },  
  productClickGrid: {  
    productElemWrapper: "#main-body #prodlist .productframe",  
    productPidAttr: "unbxdparam_sku",  
    source: "PRODUCT_CLICK_GRID"  
  },  
  addToCartFromPDP: {  
    addToCartBtnSelector: "#main-body #productrightbox .addtobasket .actionbutton",  
    pidSelector: '#main-body #productrightbox .addtobasket input[id="prodid"]',  
    productPidAttr: "value",  
    qtySelector: "#productrightbox .addtobasket .qtywrap  #quantity",  
    variant: true,  
    vidSelector: '#main-body #productrightbox #optionswrap input[id="optionvarid"]',  
    productVidAttr: "value",  
    source: "ADD_TO_CART_PDP",  
  },  
  addToCartFromCartPage: {  
    cartItemWrapper: '#main-body  form[id="basket"]  .odd',  
    pidSelector: '#main-body  form[id="basket"]  .odd .basketimage',  
    productPidAttr: "src",  
    getPidFromCB: function (pidString) {  
        const pidlast = src.split("/").pop();  
        const pid = pidlast.split("_")[0];  
        return pid;  
    },  
    qtyPlusSelector: '#main-body  form[id="basket"]  .odd .qtywrap .qtyup',  
    qtyMinusSelector: '#main-body  form[id="basket"]  .odd .qtywrap .qtydown',  
    qtyDelay: "",  
    variant: true,  
    vidSelector: "",  
    productVidAttr: "",  
    source: "ADD_TO_CART_FROM_CART_PAGE",  
  },  
  pageView: {  
    delay: "1500",  
    events: {  
      home: {  
        uniqueSelectors: {  
          selectors: ['#home .hometop  #imagechanger'],  
        },  
        urlIdentifiers: {  
          urls: ["https://fueltank.iconography.co.uk/"],  
          exactMatch: true,  
        },  
      },  
      search: {  
        uniqueSelectors: {  
          selectors: ['body[id="search"] #main-body .pagecontainer'],  
        },  
        urlIdentifiers: {  
          urls: ["https://fueltank.iconography.co.uk/search/"],  
          exactMatch: false,  
        },  
      },  
      category: {  
        uniqueSelectors: {  
          selectors: ['body[id="categories"] #main-body .pagecontainer'],  
        },  
      },  
      productDisplay: {  
        uniqueSelectors: {  
          selectors: ['body[id="product"]'],  
        },  
      },  
      cart: {  
        uniqueSelectors: {  
          selectors: [body[id="shoppingbasket"]],  
        },  
        urlIdentifiers: {  
          urls: ["https://fueltank.iconography.co.uk/shopping-basket"],  
          exactMatch: true,  
        },  
      },  
  
    },  
  },  
};
```


```
{
  "siteName": "ss-unbxd-auk-dev-Fueltankshop53931716296619",
  "sdkVersion": "v6.3.1"
}

```

