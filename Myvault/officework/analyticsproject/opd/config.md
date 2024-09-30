const opdstage = {
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
    excludeSelectors: [".prods-list .product-list-items-allviews .product-list-item .btn-add-to-cart", ".prods-list .product-list-items-allviews .product-list-item  .qty", ".prods-list .product-list-items-allviews .product-list-item  .btn-qty-up", ".prods-list .product-list-items-allviews .product-list-item .btn-qty-down",".prods-list .product-list-items-allviews .product-list-item .prodcompare"],
    productPidAttr: "data-uniqueid",
    qtySelector: ".price-etc .add-to-ord .qty",
    qtyPlusSelector: ".price-etc .add-to-ord .btn-qty-up",
    qtyMinusSelector: ".price-etc .add-to-ord .btn-qty-down",
    qtyDelay: 2000, // for 2sec
    source: "PRODUCT_CLICK_GRID"
  },
  addToCartFromSRP: {
    addToCartBtnSelector: "#simplemodal-container #simplemodal-data .btn,.price-etc .add-to-ord .btn-add-to-cart",
    source: "ADD_TO_CART_SRP",
  },
  addToCartFromPDP: {
    addToCartBtnSelector: "#simplemodal-data .btn",
    pidSelector: ".product-top .codes-etc .code",
    productPidAttr: "data-uniqueid",
    qtySelector: ".product-top .product-pricing .add-to-ord .qty",
    source: "ADD_TO_CART_PDP",
  },
  addToCartFromCartPage: {
    cartItemWrapper: ".cart-table .products_tr",
    pidSelector: ".cart-table .products_tr .c_Code a",
    productPidAttr: "data-uniqueid",
    qtySelector: ".cart-table .products_tr .c_Qty .txtbox1",
    qtyDelay: 2000, // for 2sec
    source: "ADD_TO_CART_FROM_CART_PAGE",
  },
  pageView: {
    delay: "1500",
    events: {
      home: {
        uniqueSelectors: {
          selectors: ['#myBody.homepage .home-banner'],
        },
        urlIdentifiers: {
          urls: ["https://advance.opd.co.nz/"],
          exactMatch: true,
        },
      },
      category: {
        uniqueSelectors: {
          selectors: ['.container [class*="cat"] .prods-list'],
        },
        urlIdentifiers: {
          urls: ["https://advance.opd.co.nz/products/"],
          exactMatch: false,
        },
      },
      search: {
        uniqueSelectors: {
          selectors: ['.container .searchresults .prods-list'],
        },
        urlIdentifiers: {
          urls: ["https://advance.opd.co.nz/products?search"],
          exactMatch: false,
        },
      },
      productDisplay: {
        uniqueSelectors: {
          selectors: ['[class*="productdetail"]#myBody'],
        },
        urlIdentifiers: {
          urls: [".container .productdetail .product-top"],
          exactMatch: false,
        },
      },
      cart: {
        uniqueSelectors: {
          selectors: ['.shoppingcart .cart-table .cart-table'],
        },
        urlIdentifiers: {
          urls: ["https://advance.opd.co.nz/cart"],
          exactMatch: "",
        },
      },
    },
  },
};

