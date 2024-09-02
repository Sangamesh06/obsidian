
```
const websitestage = {
  search: {
    inputBox: ".primary-header #search #txtSearchNav",
    queryBtn: ".primary-header #search #btnSearchNav",
    urlParam: "search",
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
    productElemWrapper: ".prods-list .product-list-items-allviews .product-list-item",
    excludeSelectors: [".prods-list .product-list-items-allviews .product-list-item .btn-add-to-cart", "", "", ""],
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
