search api : 

https://console-apac.unbxd.io/search/sites/1625/keys

shyaway
i have used relative selectors

```
autosuggest:[
  {
    // config to track Popular Products & POPULAR_PRODUCTS_FILTERED
    eventListener: "click",
    elemWrapper: "#search_mini_form .unbxd-autocomplete .popular-products .popular-product-item",
    type: {
      attr: ""
    },
    pid: {
      selector: ".product-name"
      attr: "data-id",
    },
    srcQuery: {
      attr: "",
    },
    titleAsQuery: {
      selector: ".product-name"
    },
     prank:{
      attr: "",
    },
    internalQuery: {
      selector: ".block-search  .block-content  .search .control #search.input-text",
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
```
