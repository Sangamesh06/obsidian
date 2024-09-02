
Steps for analytics integration


Has anyone done integration before for same site or similar sit just copy the same and change only when required

Is there any particular approach wen need to follow
Test for cart removal event no event(cart) should fire 
Test for search event on using sort by and page view should only fire(using fire search misc in search event)
Test if category page and order events are integrated 
Ask for how to do order and can we do It using cod
Whenever doing config do for mobile and also check for mobile also
Just for safety check for pid in feed sometime pid pattern is different
If in big query error is coming it s because of mobile version may be wrong or different selectors
Try to use url selectors along with Dom selectors
check if selector for product click grid are same for grid and list view and browse pages
Sometimes even though necessary add gitqtyfromcb since the qa team will raise the error


Don’t worry about these events for version2
Click firing after add to favourite on sup and crp
Page view after sort by in srp and crp
Issues related to order

The infö that must be I notepad for analytics integration

console link : "https://console-apac.unbxd.io/departments"


stagesite
site key : ss-unbxd-auk-dev-Fueltankshop53931716296619
api key : c11f28fa7f1d7790ef991b80e8e88d8a
searchapi : http://search.unbxd.io/c11f28fa7f1d7790ef991b80e8e88d8a/ss-unbxd-auk-dev-Fueltankshop53931716296619/search?q=*
secretkey : c733e14a19b192192ab0f3205ce79936


Prod site
site key : ss-unbxd-auk-Prod-Fueltankshop53931716296896
api key : 9424ab74e643c39485363486de8f5cb6
searchapi : http://search.unbxd.io/9424ab74e643c39485363486de8f5cb6/ss-unbxd-auk-Prod-Fueltankshop53931716296896/search?q=*
secretkey : 9301bc7b071052f043e096bf16484fe2

Order page url
Order credentials

Link for analytics documentation : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for analytics prerequisites : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for chatgpt : "https://chatgpt.com/"
Link for claude3 : "https://claude.ai/chats"

Link for bigquery report : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-auk-dev-Fueltankshop53931716296619?fromDate=2024-06-09&toDate=2024-06-09"
link for bigquery prod site : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-auk-Prod-Fueltankshop53931716296896?fromDate=2024-06-09&toDate=2024-06-09"





prodmetadata.json file
{
  "siteName": "ss-unbxd-auk-Prod-Fueltankshop53931716296896",
  "sdkVersion": "v6.2.5"
}

stagemetadata.json file
{
  "siteName": "ss-unbxd-auk-dev-Fueltankshop53931716296619",
  "sdkVersion": "v6.2.5"
}

one liner script for stage and prod site
stage site
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-auk-dev-Fueltankshop53931716296619/ua-staging/ua.js

prod site script
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-auk-Prod-Fueltankshop53931716296896/ua/ua.js

commands to replace sitekey apikey siteurl produrl 

%s/ss-unbxd-auk-dev-Fueltankshop53931716296619/stgsitk/g
%s/c11f28fa7f1d7790ef991b80e8e88d8a/stgapik/g
%s/siteurl/stgsiturl/g
%s/c733e14a19b192192ab0f3205ce79936/seckeyv1/g


%s/ss-unbxd-auk-Prod-Fueltankshop53931716296896/prodsitk/g
%s/9424ab74e643c39485363486de8f5cb6/prodapik/g
%s/siteurl/prodsiturl/g
%s/9301bc7b071052f043e096bf16484fe2/seckeyv2/g

```
const websitenamestage = {
  metadata: {
    siteName: "",
    sdkVersion: "v6.3.1"
  },
  autosuggest:[
  {
    // config to track Popular Products & POPULAR_PRODUCTS_FILTERED
    eventListener: "click",
    elemWrapper: ".unbxd-as-maincontent li.unbxd-as-popular-product",
    cartBtn: ".unbxd-as-wrapper li.unbxd-as-popular-product .cartBtn",
    type: {
      selector: "",
      attr: "data-type"
    },
    pid: {
      selector:""
      attr: "data-pid",
    },
    //for only   POPULAR_PRODUCTS_FILTERED
    srcQuery: {
      attr: "data-src_query",
    },
    titleAsQuery: {
      selector: ".unbxd-as-sidecontent li.unbxd-as-popular-product .unbxd-liqud-tit",
      attr:""
    },
    prank:{
      selector:"",
      attr: "data-index",
    },
  },
  {
    // single config to track All types of Suggestions. 
    // example: KEYWORD_SUGGESTION, PROMOTED_SUGGESTION, TOP_SEARCH_QUERIES etc
    eventListener: "click",
    elemWrapper: ".unbxd-as-maincontent li.unbxd-as-popular-product",
    type: {
      selector: "",
      attr: "data-type"
    },
    suggestion: {
      attr: "data-value"
    },
    prank:{
      attr: "data-index",
    },
    //for only in-feild suggeestion type
    fieldName: {
      selector:"",
      attr: "data-filtername"
    },
    fieldValue: {
      selector :"",
      attr: "data-filtervalue"
    },
    internalQuery: {
      selector: ".search-input.unbxdsearchbox",
      // if Default template present, list of AS docTypes used in the Default template
      starQuery: ["TRENDING_QUERIES", "KEYWORD_SUGGESTION"].
    }
  }
]
  search: {
    inputBox: "",
    queryBtn: "",
    urlParam: "",
  },
  productClickGrid: {
    productElemWrapper: "",
    pidSelector: "",
    productPidAttr: "",
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

#main-body .pagecontainer div[itemprop="itemOffered"] meta[itemprop="productID"]
