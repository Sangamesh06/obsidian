```

```

.products-grid .product-items .item

.minisearch  #searchbox


[/small-appliance>/small-appliance/petit-dejeuner>/small-appliance/petit-breakfast/grill-bread-toaster](https://search.unbxd.io/petit-electromenager%3E/petit-electromenager/petit-dejeuner%3E/petit-electromenager/petit-dejeuner/grill-pain-toaster)


HAIER HTO5A3011


APPLE MUQ93

20399

EF-XS926CTEGWW


MEDIA RANGE MRCS166

**Electroplate**

const websitenamestage = {

  search: {

    inputBox: ".sm-searchbox #search",

    queryBtn: ".sm-searchbox .searchbox-actions",

    urlParam: "q",

  },

  productClickGrid: {

    productElemWrapper: ".products-grid .product-items .product-item",

    pidSelector: ".products-grid .product-items .product-item .product-item-details .price-box",

    productPidAttr: "data-product-id",

    source: "PRODUCT_CLICK_GRID"

  },

  addToCartFromPDP: {

    addToCartBtnSelector: ".product-info-main .add-to-cart-container .purchase-action-wrapper  .purchase-action-link",

    pidSelector: ".product-info-main .product-info-price .price-box",

    productPidAttr: "data-product-id",

    qtySelector: "",

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

  autosuggest:[

  {   elemWrapper: ".mst-searchautocomplete__index li.mst-searchautocomplete__item",

      eventListener: "click",

      //cartBtn: ".unbxd-as-wrapper li.unbxd-as-popular-product .cartBtn",

      type: { 

            attr: "data-type" 

            },

      pid: {

           selector : ".meta  .store .price-box",

           attr: "data-product-id",

      },

      srcQuery: {

           selector: ".meta  .title a",

      },

      titleAsQuery: {

         selector: ".meta  .title a"

      },

        prank:{

      attr: "",

    },

  },

  {     

    elemWrapper: ".mst-searchautocomplete__index li.mst-searchautocomplete__item",  

    eventListener: "click",

    type: { 

            attr: "data-type" 

        },

    suggestion: {

      attr: ""

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

  }

]

