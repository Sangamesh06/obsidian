https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration

https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2412052481/Analytics+V2+Config+Documentation#Pageview

check if there is pid and vid for all products in srp , pdp , category , cart , ccartpopup pages
and ensure it is in dev element rather than just in script or some other element

for autosuggest 
elemwrapper should hold the entire value like suggestion otherwise ask the customer to create an attribute that holds the entire suggestion 
type : check if in suggestion is ther attribute that tells the type of suggestion or products that is (popular product , keyword suggestion)
check if there are popular prodducts filtered that is used for src query
pid : for popular products and popular products filtered there should be pid
srcquery : 
titleasquery : to recieve 



for product impressions
for search result page : search query is required
for 

```run-json
const websitenamestage = {
  search: {
    inputBox: "",
    queryBtn: "",
    urlParam: "q",
  },
  productClickGrid: {
    productElemWrapper: "",
    // productElemWrapper: "[data-unxItem='product']", //for unbxd sdk customer
    pidSelector: "",
    productPidAttr: "",
    // productPidAttr: "data-unxId",  //for unbxd sdk customer
    qtySelector: "",
    qtyPlusSelector: "",
    qtyMinusSelector: "",
    qtyDelay: 2000, // for 2sec
    source: "PRODUCT_CLICK_GRID"
  },
  addToCartFromSRP: {
    addToCartBtnSelector: "",
    // addToCartBtnSelector: "[data-unxCartBtn='addToCart']", //for unbxd sdk customer
    source: "ADD_TO_CART_SRP",
  },
  addToCartFromPDP: {
    addToCartBtnSelector: "",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "",
    variant: false,
    vidSelector: "",
    productVidAttr: "",
    source: "ADD_TO_CART_PDP",
  },
  addToCartFromCartPage: {
    cartItemWrapper: "",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "[data-unxQty='qty']", // SDK integration customer
    // qtySelector: "", // SDK integration customer (original value removed)
    qtyPlusSelector: "",
    qtyPlusSelector: "[data-unxQtyPlus='qtyPlus']", // SDK customer
    qtyMinusSelector: "",
    qtyMinusSelector: "[data-unxQtyMinus='qtyMinus']", // SDK customer
    qtyDelay: "", // for 2sec
    variant: "",
    vidSelector: "",
    productVidAttr: "",
    source: "ADD_TO_CART_FROM_CART_PAGE",
  },
  orderFromCheckoutPage: {
    orderItemWrapper: "",
    buyButtonSelector: "",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "",
    qtyPlusSelector: "",
    qtyMinusSelector: "",
    qtyDelay: "2000", // for 2sec
    priceSelector: "",
    productPriceAttr: "",
    variant: "",
    vidSelector: "",
    productVidAttr: "",
    source: "ORDER_FROM_CHECKOUT",
  },
  pageView: {
    delay: "1500",
    events: {
      home: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      search: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      category: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      productDisplay: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      cart: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      order: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
    },
  },
};
```

hello
```run-json
const websitestage = {
  search: {
    inputBox: "",
    queryBtn: "",
    urlParam: "q",
  },
autosuggest:[
  {
    // config to track Popular Products & POPULAR_PRODUCTS_FILTERED
    eventListener: "click",
    elemWrapper: "",
    cartBtn: "",
    type: {
      attr: ""
    },
    pid: {
      attr: "",
    },
    srcQuery: {
      attr: "",
    },
    titleAsQuery: {
      selector: ""
    },
     prank:{
      attr: "",
    },
    internalQuery: {
      selector: "",
      // if Default template present, list of AS docTypes used in the Default template
      starQuery: ["", ""].
    }

  },
  {
    // single config to track All types of Suggestions. 
    // example: KEYWORD_SUGGESTION, PROMOTED_SUGGESTION, TOP_SEARCH_QUERIES etc
    eventListener: "click",
    elemWrapper: "",
    type: {
      attr: ""
    },
    suggestion: {
      attr: ""
    },
     prank:{
      attr: "",
    },
    fieldName: {
      attr: ""
    },
    fieldValue: {
      attr: ""
    },
    internalQuery: {
      selector: "",
      // if Default template present, list of AS docTypes used in the Default template
      starQuery: ["", ""].
    }

  }
]
  productClickGrid: {
    productElemWrapper: "",
    excludeSelectors: ["", "", "", ""],
    // productElemWrapper: "[data-unxItem='product']", //for unbxd sdk customer
    pidSelector: "",
    productPidAttr: "",
    // productPidAttr: "data-unxId",  //for unbxd sdk customer
    qtySelector: "",
    qtyPlusSelector: "",
    qtyMinusSelector: "",
    qtyDelay: 2000, // for 2sec
    source: "PRODUCT_CLICK_GRID"
  },
  addToCartFromSRP: {
    addToCartBtnSelector: "",
    // addToCartBtnSelector: "[data-unxCartBtn='addToCart']", //for unbxd sdk customer
    source: "ADD_TO_CART_SRP",
  },
  addToCartFromPDP: {
    addToCartBtnSelector: "",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "",
    variant: false,
    vidSelector: "",
    productVidAttr: "",
    source: "ADD_TO_CART_PDP",
  },
  addToCartFromCartPage: {
    cartItemWrapper: "",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "[data-unxQty='qty']", // SDK integration customer
    // qtySelector: "", // SDK integration customer (original value removed)
    qtyPlusSelector: "",
    qtyPlusSelector: "[data-unxQtyPlus='qtyPlus']", // SDK customer
    qtyMinusSelector: "",
    qtyMinusSelector: "[data-unxQtyMinus='qtyMinus']", // SDK customer
    qtyDelay: "", // for 2sec
    variant: "",
    vidSelector: "",
    productVidAttr: "",
    source: "ADD_TO_CART_FROM_CART_PAGE",
  },
  orderFromCheckoutPage: {
    orderItemWrapper: "",
    buyButtonSelector: "",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "",
    qtyPlusSelector: "",
    qtyMinusSelector: "",
    qtyDelay: "2000", // for 2sec
    priceSelector: "",
    productPriceAttr: "",
    variant: "",
    vidSelector: "",
    productVidAttr: "",
    source: "ORDER_FROM_CHECKOUT",
  },
  pageView: {
    delay: "1500",
    events: {
      home: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      search: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      category: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      productDisplay: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      cart: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
      order: {
        uniqueSelectors: {
          selectors: [],
        },
        urlIdentifiers: {
          urls: [],
          exactMatch: "",
        },
      },
    },
  },
};



```

some of the questions related to analytics integration
1) should product elementwrapper select recommendation products also
		no


autosuggest 
	doubt for src query in autosuggest what if whole title is nt present in one dev
	and element having title does not have class name for the same
	 