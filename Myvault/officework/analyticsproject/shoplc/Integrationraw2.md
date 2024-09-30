const ShoplcProd = {
  search: {
    inputBox: ".menu-search-container .simple-search-form .search-field",
    queryBtn: ".menu-search-container .simple-search-form .search-button",
    urlParam: "&text",
  },
autosuggest:[
  {
    eventListener: "click",
    elemWrapper: ".menu-search-container .unbxd-as-wrapper .unbxd-as-popular-product",
    type: {
      attr: "data-type"
    },
    pid: {
      selector:".unbxd-as-popular-product-image-container",
      attr: "src",
      getPidFromCB: function (pidString) {
        pidString = pidString.split("?")[0];
        pidString = pidString.split("/"); 
        pidString = pidString[pidString.length - 2];
        return pidString;
      },
    },
    srcQuery: {
      selector:".menu-search-container .unbxd-as-maincontent  .unbxd-as-keysuggestion",
      attr: "data-value",
      attr:"data-src",
    },
    titleAsQuery: {
      selector: ".menu-search-container .unbxd-as-wrapper .unbxd-as-popular-product .unbxd-as-popular-product-info .unbxd-as-popular-product-name"
    },
     prank:{
      attr: "data-index",
    },
    internalQuery: {
      selector: ".menu-search-container .simple-search-form .search-field",
      starQuery: ["POPULAR_PRODUCTS"].
    }
  },
  {
    eventListener: "click",
    elemWrapper: ".menu-search-container .unbxd-as-wrapper .unbxd-as-keysuggestion,.menu-search-container .unbxd-as-wrapper .unbxd-as-insuggestion",
    type: {
      attr: "data-type"
    },
    suggestion: {
      attr: "data-value"
    },
     prank:{
      attr: "data-index",
    },
    fieldName: {
      attr: "data-filtername"
    },
    fieldValue: {
      attr: "data-filtervalue"
    },
    internalQuery: {
      selector: ".menu-search-container .simple-search-form .search-field",
      starQuery: ["TOP_SEARCH_QUERIES"]
    }

  }
]
  productClickGrid: {
    productElemWrapper: ".search-results .unbxd-results-container .unbxd-products-list .product",
    excludeSelectors: [".wishlist-air-container", ".tile-body","rate", ".bx-wrapper", ".prod-price-info",".saveextra-price",".unbxd-bp-container"],
    productPidAttr: "data-pid",
    source: "PRODUCT_CLICK_GRID"
  },
  addToCartFromSRP: {
    addToCartBtnSelector: ".product-tile .prod-actions .cart-wrapper",
    source: "ADD_TO_CART_SRP",
  },
  addToCartFromPDP: {
    addToCartBtnSelector: ".add-to-cart-sidebar .add-to-cart.trigger-add-to-cart",
    pidSelector: ".page[data-querystring]",
    productPidAttr: "data-querystring",
    getPidFromCB: function (pidString) {
        pid = pidString.split("=")[1] ? pidString.split("=")[1] : "";
        return pid;
    },
    qtySelector: ".add-to-cart-sidebar .quantity .quantity-select",
    variant: true,
    vidSelector: "#maincontent .product-detail",
    productVidAttr: "data-productdetails",
    getPidFromCB: function (pidString) {
        pidString = JSON.parse(pidString);
        pid = pidString["id"] ? pidString["id"] : "";
        return pid;
    },
    source: "ADD_TO_CART_PDP",
  },
  addToCartFromCartPage: {
    cartItemWrapper: ".cart-items .product-info",
    pidSelector: "",
    productPidAttr: "",
    qtySelector: "",
    qtyPlusSelector: "",
    qtyMinusSelector: "",
    qtyDelay: "", // for 2sec
    variant: true,
    vidSelector: ".cart-items .product-info",
    productVidAttr: "data-id",
    source: "ADD_TO_CART_FROM_CART_PAGE",
  },
  pageView: {
    delay: "1500",
    events: {
      home: {
        uniqueSelectors: {
          selectors: ['#maincontent #homepage-SHOP_LC .slick-slide'],
        },
        urlIdentifiers: {
          urls: ["https://www.shoplc.com/"],
          exactMatch: true,
        },
      },
      search: {
        uniqueSelectors: {
          selectors: ['.search-results .unbxd-products-list-container .unbxd-products-list'],
        },
        urlIdentifiers: {
          urls: ["https://www.shoplc.com/search?&text"],
          exactMatch: false,
        },
      },
      category: {
        urlIdentifiers: {
          urls: ["https://www.shoplc.com/c"],
          exactMatch: false,
        },
      },
      productDisplay: {
        uniqueSelectors: {
          selectors: ['#maincontent .pdp [class*=pdp] #productdescriptionpdp'],
        },
      },
      cart: {
        uniqueSelectors: {
          selectors: ['#maincontent .cart-page'],
        },
        urlIdentifiers: {
          urls: ["https://www.shoplc.com/cart?"],
          exactMatch: false,
        },
      },
    },
  },
};


