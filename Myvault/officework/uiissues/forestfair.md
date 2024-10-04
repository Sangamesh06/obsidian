```
Furniture fair unbxd_autosuggest.js
/* helper variables and consts */
let hidePagesBorder = false;
const removeQueryParam = (paramName) => {
  const currentURL = new URL(window.location.href);

  // Check if the parameter exists in the URL
  if (currentURL.searchParams.has(paramName)) {
    currentURL.searchParams.delete(paramName);

    // Update the page's URL without a page reload
    window.history.replaceState(null, "", currentURL);
  }
};
let intialLeft = "";
const getUidCookie = document.cookie.match("\\bunbxd.userId=([^;]*)\\b");
const uidCookie = getUidCookie ? getUidCookie[1] : null;

const customRequestsCache = {
  search: {},
  autosuggest: {},
  blogs: {},
  pages: {},
};

const headerQuantityValues = {};
const defaultImageUrl =
  "https://libraries.unbxdapi.com/sdk-assets/defaultImage.svg";

/* * * ANALYTICS CONFIGURATION * * */
var UnbxdSiteName = getSiteName();
var UnbxdApiKey = getApiKey();

/* Analytics library is added in theme.liquid in shopify theme */

const unbxdAnalytics = (type, payload) => {
  // convert undefined to null
  for (const key in payload) {
    if (payload[key] === undefined) {
      payload[key] = null;
    }
  }
  // convert pid and qty to string
  if (payload.pid != undefined) {
    payload.pid = String(payload.pid);
  }
  if (payload.qty != undefined) {
    payload.qty = String(payload.qty);
  }
  if (type != undefined && Unbxd && typeof Unbxd.track === "function") {
    Unbxd.track(type, payload);
  } else {
    console.error("unbxdAnalytics.js is not loaded!");
  }
};
const experienceImpressionAnalytic = (templateData, widgetMapSelector) => {
  const pids = [];
  const widget = templateData.analyticsData.widgetNum.toUpperCase();
  if (widgetMapSelector[widget] == null) {
    return;
  }
  for (const product of templateData.recommendations) {
    pids.push(product.uniqueId);
  }

  const payload = {
    requestId: templateData.analyticsData.requestId,
    pids_list: pids,
    experience_pagetype: templateData.analyticsData.pageType,
    experience_widget: widget,
  };
  unbxdAnalytics("experience_impression", payload);
};

const addToCartAnalytics = (productMain) => {
  const addToCartAnalyticsPayload = getAddToCartAnalyticsPayload(productMain);
  unbxdAnalytics("addToCart", addToCartAnalyticsPayload);
};

const getAddToCartAnalyticsPayload = (productMain) => {
  const productId =
    productMain.querySelector(".gallery-cell").dataset.productId;

  const queryString = new URLSearchParams(location.search);
  const variantId = queryString.get("variant");

  const quantity = productMain.querySelector("#quantity").value;
  const price = productMain.querySelector(".money").innerHTML.replace("$", "");

  headerQuantityValues[productId] = quantity;

  return {
    pid: productId ?? null,
    variantId: variantId,
    qty: quantity,
    price: price,
  };
};

const addSearchAnalyticAttr = ({ input, button }) => {
  if (input != null) {
    input.setAttribute("unbxdattr", "sq");
  }
  if (button != null) {
    button.setAttribute("unbxdattr", "sq_bt");
  }
};

function unbxdRecsFnc(
  productType,
  productIds,
  widgetIdFirst,
  widgetIdSecond,
  widgetIdThird,
  uidCookie
) {
  let allWidgets = [
    {
      name: "widget1",
      selector: widgetIdFirst,
    },
    {
      name: "widget2",
      selector: widgetIdSecond,
    },
    {
      name: "widget3",
      selector: widgetIdThird,
    },
  ];

  const widgetMapSelector = {};
  for (const widget of allWidgets) {
    if (widget.selector == null) {
      continue;
    }
    widgetMapSelector[widget.name.toUpperCase()] = widget.selector;
  }

  window.getUnbxdRecommendations({
    widgets: allWidgets,
    userInfo: {
      userId: uidCookie,
      siteKey: getSiteName(),
      apiKey: getApiKey(),
    },
    pageInfo: {
      pageType: productType,
      productIds: productIds,
      boutiqueButton: true,
    },
    itemClickHandler: function (product) {},
    dataParser: function (templateData) {
      experienceImpressionAnalytic(templateData, widgetMapSelector);

      return templateData;
    },
  });
}

const [pageType] = location.href
  .substring(window.location.origin.length + 1)
  .split("/");
if (pageType != undefined && pageType.toLowerCase() == "products") {
  const shopifyRecsEl = document.querySelector(
    ".shopify-section--recommended-products"
  );
  const productId = document.querySelector(`[name="product-id"]`).value ?? "";

  shopifyRecsEl != null &&
    shopifyRecsEl.insertAdjacentHTML(
      "afterend",
      `<div id="UNX-pdp-recs" class="shopify-section unbxdRECSSplide"></div>
      <div id="UNX-pdp-recs-cross-sell" class="shopify-section unbxdRECSSplide"></div>`
    );
  unbxdRecsFnc(
    "PRODUCT",
    [productId],
    null,
    "UNX-pdp-recs",
    "UNX-pdp-recs-cross-sell",
    uidCookie
  );
}

if (pageType != undefined && document.querySelector("body.index") != null) {
  const UNXhomePage = document.querySelector(
    "body.index #s-a80db67a-0928-4ecf-80b9-310d37b52cc3"
  );
  if (UNXhomePage != null) {
    UNXhomePage.insertAdjacentHTML(
      "beforebegin",
      `<div id="UNX-homePage-RECS-1" class="unbxdRECSSplide"></div>`
    );
    unbxdRecsFnc("HOME", null, null, "UNX-homePage-RECS-1", null, uidCookie);
  }
}

let window_width = $(window).width();
let windowInnerWidth = window.innerWidth;
let changeWindowWidthMobileLayout = false;
if (windowInnerWidth <= 798) {
  changeWindowWidthMobileLayout = true;
}

let isMobile = {
  Android: function () {
    return navigator.userAgent.match(/Android/i);
  },
  BlackBerry: function () {
    return navigator.userAgent.match(/BlackBerry/i);
  },
  iOS: function () {
    return navigator.userAgent.match(/iPhone|iPad|iPod/i);
  },
  Opera: function () {
    return navigator.userAgent.match(/Opera Mini/i);
  },
  Windows: function () {
    return navigator.userAgent.match(/IEMobile/i);
  },
  any: function () {
    return (
      isMobile.Android() ||
      isMobile.BlackBerry() ||
      isMobile.iOS() ||
      isMobile.Opera() ||
      isMobile.Windows()
    );
  },
};
let searchInputSelector =
  ".header .main-nav > .search-container .unbxd-auto-suggest-input";
let autosuggest_input_element = $(
  ".header .main-nav > .search-container .unbxd-auto-suggest-input"
);
let changeASLayoutToMobile = false;
if (window_width < 799) {
  changeASLayoutToMobile = true;
}

if (changeASLayoutToMobile) {
  autosuggest_input_element = $(".mobile-search .unbxd-auto-suggest-input");
  searchInputSelector = ".mobile-search .unbxd-auto-suggest-input";
}

const currency = "$";
const getUnbxdASConfig = () => {
  let unbxd_as_config = {
    siteName: getSiteName(),
    APIKey: getApiKey(),
    resultsClass: "unbxd-as-wrapper unbxd-as-wrapper-default",
    minChars: 1,
    platform: "io",
    searchEndPoint: "//search.unbxd.io",
    delay: 100,
    loadingClass: "unbxd-as-loading",
    mainWidth: autosuggest_input_element.outerWidth() * 0.6,
    sideWidth: autosuggest_input_element.outerWidth() * 1.2,
    zIndex: 10000,
    position: "absolute",
    template: "2column",
    mainTpl: ["promotedSuggestions", "keywordSuggestions", "topQueries"],
    sideTpl: ["popularProducts"],
    sideContentOn: "right",
    suggestionsHeader: "Suggestions",
    topQueries: {
      count: 3,
    },
    keywordSuggestions: {
      count: 3,
      header: "",
      tpl: "",
    },
    inFields: {
      count: 0,
    },
    promotedSuggestions: {
      count: 3,
      header: "Promoted Suggestions",
      tpl: "",
    },
    hbsHelpers: function () {
      Handlebars.registerHelper("getSkuUI", function (product) {
        let SkuUI = "";
        if (
          product.variants[0] != undefined &&
          product.variants[0].v_sku != undefined
        ) {
          SkuUI = `<p class="unbxd-auto-suggest-sku">SKU: ${product.variants[0].v_sku}</p>`;
        }
        return SkuUI;
      });

      Handlebars.registerHelper("getImageUrl", function (product) {
        return product.imageUrl != undefined
          ? product.imageUrl
          : defaultImageUrl;
      });

      Handlebars.registerHelper("getPriceUI", function (product) {
        const { price, compareAtPrice, vendor } = product;
        let priceUI;

        if (["Smith Brothers", "L and J.G. Stickley Inc"].includes(vendor)) {
          return "";
        }

        const getNormalPriceHTML = (price) => {
          return `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;`;
        };

        if (
          (price == 0 || price == undefined) &&
          (compareAtPrice == 0 || compareAtPrice == undefined)
        ) {
          /* price & compareAtPrice both doesn't exists */
          priceUI = getNormalPriceHTML(0);
        } else if (
          (price == 0 || price == undefined) &&
          compareAtPrice != 0 &&
          compareAtPrice != undefined
        ) {
          /* price doesn't exists; compareAtPrice exists */
          priceUI = getNormalPriceHTML(compareAtPrice);
        } else if (
          (compareAtPrice == 0 || compareAtPrice == undefined) &&
          price != 0 &&
          price != undefined
        ) {
          /* compareAtPrice doesn't exists; price exists */
          priceUI = getNormalPriceHTML(price);
        } else if (price == compareAtPrice) {
          /* both prices exists and are equal */
          priceUI = getNormalPriceHTML(price);
        } else {
          /* both prices exists but not equal */
          priceUI = `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;
				<s>${currency}${compareAtPrice}</s>`;
        }
        const priceUIContainer = `
      <p class="unbxd-auto-suggest-price-p">
        ${priceUI}
      </p>`;
        return priceUIContainer;
      });
    },
    popularProducts: {
      fields: [
        "title",
        "uniqueId",
        "productUrl",
        "imageUrl",
        "vendor",
        "price",
        "compareAtPrice",
        "v_sku",
      ],
      price: true,
      priceFunctionOrKey: "price",
      image: true,
      imageUrlOrFunction: "imageUrl",
      name: true,
      nameFunctionOrKey: "title",
      currency: currency,
      header: "Popular Products",
      view: "grid",
      tpl: [
        `
          <a title="{{ _original.title }}" href="{{ _original.productUrl }}">
            <div class="unbxd-as-popular-product-info">
                <div class="unbxd-as-popular-product-image-container">
                  <img src="{{ getImageUrl _original }}" alt="{{ _original.title }}">
                </div>
                <div class="unbxd-as-popular-product-name">{{ _original.title }}</div>
                <p class="unbxd-auto-suggest-vendor">{{ _original.vendor }}</p>
                <div class="unbxd-as-popular-product-price">{{{ getPriceUI _original }}}</div>
            </div>
          </a>`,
      ].join(""),
    },
    onItemSelect: function (data, original) {
      window.location =
        window.location.origin + "/search?q=" + encodeURIComponent(data.value);
    },
    onSimpleEnter: function (e) {
      e.preventDefault();
      let data = jQuery(this.input).val();
      data = $.trim(data);
      if (data.length > 0) {
        const payload = {
          query: data,
        };
        if (Unbxd && typeof Unbxd.track === "function") {
          Unbxd.track("search", payload);
        } else {
          console.error("unbxdAnalytics.js is not loaded!");
        }
        window.location =
          window.location.origin + "/search?q=" + encodeURIComponent(data);
      }
      e.stopPropagation();
    },
    noResultTpl: function (query) {
      const decodedQuery = decodeURIComponent(query);
      if (query.trim() == "") {
        setTimeout(() => {
          const unbxdAsMainContent = document.querySelector(
            ".unbxd-as-wrapper-default .unbxd-as-maincontent"
          );
          unbxdAsMainContent &&
            unbxdAsMainContent.style.setProperty("display", "none");
        });
        return "";
      }
      setTimeout(() => {
        const noResultElem = document.querySelector(
          `.boost-pfs-search-suggestion-header-view-all`
        );
        if (noResultElem != null) {
          noResultElem.classList.add("hide");
        }
      });
      return `<div class="boost-pfs-search-suggestion-no-result" data-group="empty"
            data-label="No Results: ${decodedQuery}" data-value="${decodedQuery}" aria-label="No Results">
              <p>Sorry, nothing found for "<strong>${decodedQuery}</strong>".</p>
            </div>`;
    },
    extraParams: {
      filter: `-content_type:"PAGES"&filter=-content_type:"BLOGS"`,
    },
    removeDuplicates: true,
  };
  if (window.innerWidth <= 798 || isMobile.any()) {
    unbxd_as_config.filtered = false;
    unbxd_as_config.template = "1column";
    unbxd_as_config.zIndex = 999999;
    unbxd_as_config.mainTpl = [
      "promotedSuggestions",
      "keywordSuggestions",
      "topQueries",
      "popularProducts",
    ];
    unbxd_as_config.popularProducts.count = 4;
  } else {
    unbxd_as_config.filtered = true;
    unbxd_as_config.template = "2column";
    unbxd_as_config.mainTpl = [
      "promotedSuggestions",
      "keywordSuggestions",
      "topQueries",
    ];
    unbxd_as_config.sideTpl = ["popularProducts"];
    unbxd_as_config.popularProducts.count = 6;
  }
  return unbxd_as_config;
};
/* Update header cart helpers START */

const updateHeaderQuantityValues = () => {
  const cartItems = document.querySelectorAll(`.header .mini-cart__item`);
  for (const cartItem of cartItems) {
    headerQuantityValues[
      cartItem.querySelector(".mini-cart__product-id").innerText
    ] = cartItem.querySelector(`[data-cart-quantity-input]`).value;
  }
};

const headerCartQuantityChangeHandler = (e) => {
  const target = e.target;
  /* changed quantity */
  if (e.type == "change" && e.target.dataset.cartQuantityInput == "mini-cart") {
    const liCartItem = e.target.closest(".mini-cart__item");
    const productId = liCartItem.querySelector(
      ".mini-cart__product-id"
    ).innerText;

    const previousQuantity = headerQuantityValues[productId];
    const changedQuantity = e.target.value;

    const variantId = liCartItem.dataset.variantId;

    const moneyElem =
      liCartItem.querySelector(".money.sale") ??
      liCartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const quantityDiff = changedQuantity - previousQuantity;

    const cartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 0,
      price: price,
    };

    if (quantityDiff > 0) {
      cartAnalyticsPayload.qty = quantityDiff;
      unbxdAnalytics("addToCart", cartAnalyticsPayload);
    } else {
      cartAnalyticsPayload.qty = Math.abs(quantityDiff);
      unbxdAnalytics("cartRemoval", cartAnalyticsPayload);
    }
    updateHeaderQuantityValues();
  }

  /* clicked on plus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-plus") ||
      e.target.classList.contains("icon-plus"))
  ) {
    const liCartItem = e.target.closest(".mini-cart__item");

    const productId = liCartItem.querySelector(
      ".mini-cart__product-id"
    ).innerText;
    const variantId = liCartItem.dataset.variantId;

    const moneyElem =
      liCartItem.querySelector(".money.sale") ??
      liCartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const addToCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("addToCart", addToCartAnalyticsPayload);
    headerQuantityValues[productId]++;
  }

  /* clicked on minus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-minus") ||
      e.target.classList.contains("icon-minus"))
  ) {
    const liCartItem = e.target.closest(".mini-cart__item");

    const productId = liCartItem.querySelector(
      ".mini-cart__product-id"
    ).innerText;
    const variantId = liCartItem.dataset.variantId;

    const moneyElem =
      liCartItem.querySelector(".money.sale") ??
      liCartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const removeFromCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("cartRemoval", removeFromCartAnalyticsPayload);
    headerQuantityValues[productId]--;
  }
};

const cartPageCartQuantityChangeHandler = (e) => {
  /* clicked on plus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-plus") ||
      e.target.classList.contains("icon-plus"))
  ) {
    const cartItem = e.target.closest(".cart__item");

    const productId = cartItem.dataset.productId;
    const variantId = cartItem.dataset.variantId;

    const moneyElem =
      cartItem.querySelector(".money.sale") ?? cartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const addToCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("addToCart", addToCartAnalyticsPayload);
    headerQuantityValues[productId]++;
  }

  /* clicked on minus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-minus") ||
      e.target.classList.contains("icon-minus"))
  ) {
    const cartItem = e.target.closest(".cart__item");

    const productId = cartItem.dataset.productId;
    const variantId = cartItem.dataset.variantId;

    const moneyElem =
      cartItem.querySelector(".money.sale") ?? cartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const removeFromCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("cartRemoval", removeFromCartAnalyticsPayload);
    headerQuantityValues[productId]--;
  }

  /* clicked on remove */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    e.target.classList.contains("remove-text")
  ) {
    const cartItem = e.target.closest(".cart__item");

    const productId = cartItem.dataset.productId;
    const variantId = cartItem.dataset.variantId;

    const moneyElem =
      cartItem.querySelector(".money.sale") ?? cartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const quantity = cartItem.querySelector(".quantity").value;

    const removeFromCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: quantity,
      price: price,
    };
    unbxdAnalytics("cartRemoval", removeFromCartAnalyticsPayload);
    headerQuantityValues[productId]--;
  }
};
/* Update header cart helpers END */

async function unbxdAPI(type, query) {
  let response;
  if (query in customRequestsCache[type]) {
    return customRequestsCache[type][query];
  }
  switch (type) {
    case "search":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/${type}?q=${query}`
      );
      break;

    case "autosuggest":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/${type}?q=${query}`
      );
      break;

    case "blogs":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/autosuggest?q=${query}&filter=-content_type:"PRODUCT"&filter=-content_type:"PAGE"&fields=title,imageUrl,productUrl,doctype,autosuggest,content_type&keywordSuggestions.count=0&topQueries.count=0&promotedSuggestion.count=0&inFields.count=0&popularProducts.count=3&sourceFields=category_handle&sourceField.category_handle.count=3`
      );
      break;
    case "pages":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/autosuggest?q=${query}&filter=-content_type:"PRODUCT"&filter=-content_type:"BLOG"&fields=title,imageUrl,productUrl,doctype,autosuggest,content_type&keywordSuggestions.count=0&topQueries.count=0&promotedSuggestion.count=0&inFields.count=0&popularProducts.count=3&sourceFields=category_handle&sourceField.category_handle.count=0`
      );
      break;
  }
  const responseJson = await response.json();
  customRequestsCache[type][query] = responseJson;
  return responseJson;
}
async function getBlogsData(query) {
  let result = await unbxdAPI("blogs", query);
  return result.response;
}

async function getPagesData(query) {
  let result = await unbxdAPI("pages", query);
  return result.response;
}

async function getTotalNumberOfProducts(query) {
  let result = await unbxdAPI("search", query);
  return result.response.numberOfProducts;
}

const addHTMLToRightAs = (
  rightSectionContainer,
  pagesAr,
  containerClass,
  header
) => {
  let pagesHTMLStr = "";
  let pagesUl = "";
  let counter = 0;
  for (const pageHTML of pagesAr) {
    counter++;
    if (counter > 6) {
      break;
    }
    pagesHTMLStr += pageHTML;
  }
  pagesUl = `<ul class="${containerClass}">
                    <li class="boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header" aria-label="Pages">${header}</li>
                      ${pagesHTMLStr}
                  </ul>`;
  const unbxdRightAspages = rightSectionContainer.querySelector(
    `.${containerClass}`
  );
  if (unbxdRightAspages != null) {
    unbxdRightAspages.remove();
  }
  rightSectionContainer.insertAdjacentHTML("beforeend", pagesUl);
};

const addCollectionHTMLToRightAs = (
  rightSectionContainer,
  pagesAr,
  containerClass,
  header
) => {
  let pagesHTMLStr = "";
  let pagesUl = "";
  for (const pageHTML of pagesAr) {
    pagesHTMLStr += pageHTML;
  }
  pagesUl = `<ul class="${containerClass}">
                    <li class="boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header" aria-label="collection">${header}</li>
                      ${pagesHTMLStr}
                  </ul>`;
  const unbxdRightAspages = document.querySelector(`.${containerClass}`);
  if (unbxdRightAspages != null) {
    unbxdRightAspages.remove();
  }
  rightSectionContainer.insertAdjacentHTML("beforeend", pagesUl);
};

function getAsRightSectionData(blogsData) {
  let rightSection = {};
  let titleCss = "";
  rightSection.blogs = [];
  rightSection.pages = [];
  rightSection.category = [];
  for (const blog of blogsData.products) {
    let blogHTML = "";
    let blogTitle = blog.title != undefined ? blog.title : blog.autosuggest;
    let productUrl = blog.productUrl != undefined ? blog.productUrl : "#";

    if (blog.doctype == "category_handle") {
      let collectionTitle = blog.autosuggest;
      blogTitle = collectionTitle.replace(/-/g, " ");
      productUrl = `${window.location.origin}/collections/${collectionTitle}`;
      titleCss = `style=text-transform:capitalize;`;
    }

    blogHTML = `<li ${titleCss} class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
                    aria-label="pages: ${blogTitle}" role="option"
                    data-title="${blogTitle}">
                    <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${blogTitle}</a>
                </li>`;

    if (blog.content_type == "BLOG") {
      rightSection.blogs.push(blogHTML);
    } else if (blog.content_type == "PAGE") {
      rightSection.pages.push(blogHTML);
    } else if (blog.doctype == "category_handle") {
      rightSection.category.push(blogHTML);
    }
  }
  return rightSection;
}

const appendResultsCountHTML = async (inputSelector) => {
  try {
    const query = getSearchQuery(inputSelector);
    const viewMoreContainer = document.querySelector(
      ".boost-pfs-search-suggestion-header-view-all"
    );
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
      `.unbxd-as-maincontent`
    );
    const unbxdAsSideContent = unbxd_as_wrapper.querySelector(
      `.unbxd-as-sidecontent`
    );
    if (viewMoreContainer == null) {
      let viewMoreHTML = `<div class="boost-pfs-search-suggestion-header-view-all boost-pfs-search-suggestion-header" data-group="view-all" aria-label="View All">
      <a class="view-more-query" href="">
      <span>View all&nbsp;<span class="unbxd-as-number-of-products UNX-as-result-count">...</span>&nbsp;products<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.1657 7.43443L10.1657 3.43443C9.8529 3.12163 9.3473 3.12163 9.0345 3.43443C8.7217 3.74723 8.7217 4.25283 9.0345 4.56563L11.6689 7.20003H2.4001C1.9577 7.20003 1.6001 7.55843 1.6001 8.00003C1.6001 8.44163 1.9577 8.80003 2.4001 8.80003H11.6689L9.0345 11.4344C8.7217 11.7472 8.7217 12.2528 9.0345 12.5656C9.1905 12.7216 9.3953 12.8 9.6001 12.8C9.8049 12.8 10.0097 12.7216 10.1657 12.5656L14.1657 8.56563C14.4785 8.25283 14.4785 7.74723 14.1657 7.43443" fill="#5C5F62"></path></svg></span></a>
    </div>`;

      const viewMoreQueryElem =
        unbxd_as_wrapper.querySelector(`.view-more-query`);
      if (viewMoreQueryElem != null) {
        viewMoreQueryElem.setAttribute("href", `/search?q=${query}`);
      }
      if (changeWindowWidthMobileLayout) {
        unbxdAsMainContent &&
          unbxdAsMainContent.insertAdjacentHTML("beforeend", viewMoreHTML);
      } else {
        unbxdAsSideContent &&
          unbxdAsSideContent.insertAdjacentHTML("beforeend", viewMoreHTML);
      }
    }
  } catch (error) {
    console.error(
      `Could not add "view more button" in auto suggestion.\n`,
      error
    );
  }
};
const updateResultCount = async (inputSelector) => {
  try {
    const query = getSearchQuery(inputSelector);
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    if (query == "") {
      return false;
    }
    let totalNumberOfProducts = await getTotalNumberOfProducts(query);
    if (totalNumberOfProducts > 0) {
      const resultCountEl = document.querySelector(`.UNX-as-result-count`);
      resultCountEl != null &&
        (resultCountEl.textContent = totalNumberOfProducts);
    }
  } catch (error) {
    console.error(
      `Could not update results count in "view more button".\n`,
      error
    );
  }
};
const getSearchQuery = (inputSelector) => {
  const elem = document.querySelector(inputSelector);
  let query = "";
  if (elem != null) {
    query = elem.value.trim();
  }
  return query;
};
async function getOtherAutoSuggHTML() {
  const query = getSearchQuery(searchInputSelector)
  // param `query` should be string with minimum 1 character
  if (query == "") {
    return;
  }
  var padingCss = 'style="padding: 10px 10px 12px;"';
  let blogsAutoSuggHTML = `<li ${padingCss} class="UNX-blogs-heading boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header" aria-label="Pages">Learning Center</li>`;
  let pageAutoSuggHTML = `<li ${padingCss} class="UNX-blogs-heading boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header unbxd-ac-selected" aria-label="Pages">Pages</li>`;
  let collectionAutoSuggHTML = `<li ${padingCss} class="UNX-blogs-heading boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header unbxd-ac-selected" aria-label="Pages">Collections</li>`;

  const blogsData = await getBlogsData(query);
  const pagesData = await getPagesData(query);

  let blogsAutoSuggData = blogsData.products;
  let pagesAutoSuggData = pagesData.products;

  let blogsExists = false;
  let collectionsExists = false;
  let pagesExists = false;
  var padingliCss = 'style="padding:6px 10px;"';
  for (const pageData of pagesAutoSuggData) {
    pagesExists = true;
    const productUrl = pageData.productUrl;
    const pageTitle = pageData.title;

    pageAutoSuggHTML += `<li ${padingliCss} class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
        aria-label="pages: ${pageTitle}" role="option"
        data-title="${pageTitle}">
        <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${pageTitle}</a>
    </li>`;
  }
  for (const blogData of blogsAutoSuggData) {
    const productUrl = blogData.productUrl;
    const blogTitle = blogData.title;
    const titleCss = "";

    if (blogData.doctype == "category_handle") {
      collectionsExists = true;
      const collectionTitle = blogData.autosuggest;
      const blogTitle = collectionTitle.replace(/[_-]/g, " ");
      const productUrl = `${window.location.origin}/collections/${collectionTitle}`;
      const titleCss = 'style="text-transform: capitalize; padding: 6px 10px;"';

      collectionAutoSuggHTML += `<li ${titleCss} class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
              aria-label="pages: ${blogTitle}" role="option"
              data-title="${blogTitle}">
              <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${blogTitle}</a>
          </li>`;
    } else {
      blogsExists = true;
      blogsAutoSuggHTML += `<li ${titleCss} ${padingliCss}class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
          aria-label="pages: ${blogTitle}" role="option"
          data-title="${blogTitle}">
          <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${blogTitle}</a>
      </li>`;
    }
  }
  if (!collectionsExists) {
    collectionAutoSuggHTML = "";
  }
  if (!blogsExists) {
    blogsAutoSuggHTML = "";
  }
  if (!pagesExists) {
    pageAutoSuggHTML = "";
  }

  return {
    collections: collectionAutoSuggHTML,
    pages: pageAutoSuggHTML,
    blogs: blogsAutoSuggHTML,
  };
}

function addBlogsInAs(blogsAutoSuggHTML) {
  try {
    if (blogsAutoSuggHTML == undefined || blogsAutoSuggHTML == "") {
      return;
    }
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    if (
      unbxd_as_wrapper.querySelector(
        `.boost-pfs-search-suggestion-group-collection`
      ) == null
    ) {
      const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
        `.unbxd-as-maincontent`
      );
      const collectionContainerHTML = `<div class="UNX-collection-blogs boost-pfs-search-suggestion-group-collection" data-group="collections" aria-label="collections">
      </div>`;
      const blogsContainerHTML = `<div class="boost-pfs-search-suggestion-group ${
        hidePagesBorder ? "hide-border" : ""
      }" data-group="pages" aria-label="Pages">
        </div>`;
      if (changeWindowWidthMobileLayout) {
        const unbxdAsPopularProductHeading = unbxdAsMainContent.querySelector(
          ".unbxd-as-popular-product-header"
        );
        unbxdAsPopularProductHeading &&
          unbxdAsPopularProductHeading.insertAdjacentHTML(
            "beforebegin",
            collectionContainerHTML
          );
      } else {
        unbxdAsMainContent &&
          unbxdAsMainContent.insertAdjacentHTML(
            "beforeend",
            collectionContainerHTML
          );
      }
    }
    if (
      changeASLayoutToMobile &&
      document.querySelector(".UNX-mobile-as-lower") == null
    ) {
      const unbxdMainContentMobile = document.querySelector(
        `.unbxd-as-wrapper-default.unbxd-as-wrapper-mobile .unbxd-as-maincontent`
      );
      unbxdMainContentMobile.insertAdjacentHTML(
        "beforeend",
        `<div class="UNX-mobile-as-lower boost-pfs-search-suggestion-group-collection" data-group="collections" aria-label="collections">
        </div>`
      );
      const unbxdAsMobileLower = document.querySelector(`.UNX-mobile-as-lower`);
      unbxdAsMobileLower.innerHTML = "";
    }

    const unbxdBlogsWrapper = document.querySelector(
      `.UNX-collection-blogs.boost-pfs-search-suggestion-group-collection`
    );
    unbxdBlogsWrapper.innerHTML = "";

    for (let [key, value] of Object.entries(blogsAutoSuggHTML)) {
      if (changeASLayoutToMobile && ["pages", "blogs"].includes(key)) {
        const unbxdAsMobileLower =
          document.querySelector(`.UNX-mobile-as-lower`);
        unbxdAsMobileLower.innerHTML += value;
      } else {
        unbxdBlogsWrapper.innerHTML += value;
      }
    }
  } catch (error) {
    console.error(`Error in adding blogs in autosuggestion\n${error}`);
  }
}

/* driver code */

/* param type conflicts with SEO friendly URL in search sdk */
removeQueryParam("type");

/* Analytics  */

/* update header cart */
updateHeaderQuantityValues();

document
  .querySelector(".header")
  .addEventListener("change", headerCartQuantityChangeHandler);
document
  .querySelector(".header")
  .addEventListener("click", headerCartQuantityChangeHandler);

if (document.querySelector(".cart__wrapper > div:first-child") != null) {
  document
    .querySelector(".cart__wrapper > div:first-child")
    .addEventListener("click", cartPageCartQuantityChangeHandler);
}

/* Add to cart for PDP page START */
const addToCartButton = document.querySelector(`[data-label="Add to Cart"]`);
if (addToCartButton != null) {
  addToCartButton.addEventListener("click", () => {
    const productMain = document.querySelector(".product-main");
    addToCartAnalytics(productMain);
  });
}
const setupMtObToCenterAs = () => {
  const unbxdAsMtObConfig = {
    childList: true,
    subtree: true,
  };

  const unbxd_as_wrapper = document.querySelector(
    ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
  );
  const observer = new MutationObserver(async function (
    mutationsList,
    observer
  ) {
    /* disconnect observer before making any changes in DOM to avoid infinite loop */
    observer.disconnect();
    for (const mutation of mutationsList) {
      if (mutation.type === "childList") {
        centerAlignUnxdWrapper();
      }
    }
    observer.observe(unbxd_as_wrapper, unbxdAsMtObConfig);
  });
  observer.observe(unbxd_as_wrapper, unbxdAsMtObConfig);
};
/* Add to cart for PDP page END */
jQuery(document).ready(function () {
  unbxdAutoSuggestFunction(jQuery, Handlebars);
  const unbxd_as_config = getUnbxdASConfig();
  autosuggest_input_element.unbxdautocomplete(unbxd_as_config);
  setupMtObToCenterAs();
  const unbxd_as_wrapperOuter = document.querySelector(
    ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
  );

  const unbxdAsMtObConfig = {
    childList: true,
    subtree: true,
  };
  const observer = new MutationObserver(async function (
    mutationsList,
    observer
  ) {
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    /* disconnect observer before making any changes in DOM to avoid infinite loop */
    observer.disconnect();
    for (const mutation of mutationsList) {
      if (mutation.type === "childList") {
        if (changeASLayoutToMobile) {
          unbxd_as_wrapper.classList.add("unbxd-as-wrapper-mobile");
          if (isMobile.iOS()) {
            unbxd_as_wrapper.classList.add("mobile-ios");
          }
        }
        const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
          `.unbxd-as-maincontent`
        );
        const mainAsNoResultElem = unbxd_as_wrapper.querySelector(
          ".boost-pfs-search-suggestion-no-result"
        );

        /* no result found in main autosuggestion */
        if (changeASLayoutToMobile) {
          if (mainAsNoResultElem != null) {
            mainAsNoResultElem.parentNode.classList.add("hide");
            hidePagesBorder = true;
          }
        } else {
          if (unbxdAsMainContent != null) {
            if (mainAsNoResultElem != null) {
              unbxdAsMainContent.classList.add("hide");
            } else {
              unbxdAsMainContent.classList.remove("hide");
            }
          }
        }
        appendResultsCountHTML(searchInputSelector);
        updateResultCount(searchInputSelector);
        
        const othersAutoSuggHTML = await getOtherAutoSuggHTML();
        addBlogsInAs(othersAutoSuggHTML);
      }
    }
    observer.observe(unbxd_as_wrapper, unbxdAsMtObConfig);
  });

  // mutations types to observe
  if (unbxd_as_wrapperOuter != null) {
    observer.observe(unbxd_as_wrapperOuter, unbxdAsMtObConfig);
  }
});

setTimeout(() => {
  if (changeASLayoutToMobile) {
    document
      .querySelector(".icon-cross.close-search")
      .addEventListener("touchstart", (e) => {
        const unbxdAsWrapperMobile = document.querySelector(
          ".unbxd-as-wrapper-mobile"
        );
        if (unbxdAsWrapperMobile != null) {
          unbxdAsWrapperMobile.style.setProperty("display", "none");
        }
      });
  }
}, 500);

/* header > search */
headerSearchElems = {
  input: document.querySelector(".header .unbxd-auto-suggest-input"),
  button: document.querySelector(".header .search-container .search-submit"),
};
// addSearchAnalyticAttr(headerSearchElems);

/* main content > search */
mainContentSearchElems = {
  input: document.querySelector(".search__wrapper .boost-pfs-search-box"),
  button: document.querySelector(".search__wrapper .search__button"),
};
// addSearchAnalyticAttr(mainContentSearchElems);

/* prevent search on empty query */
headerSearchElems.input.addEventListener("keydown", (e) => {
  if (e.key == "Enter" && headerSearchElems.input.value.trim() == "") {
    e.preventDefault();
  }
});

/* prevent empty query search Desktop */
headerSearchElems.button.addEventListener("click", (e) => {
  let input = headerSearchElems.input;
  if (input.value.trim() == "") {
    e.target.disabled = true;
  } else {
    e.target.disabled = false;
    let input = $(".header .unbxd-auto-suggest-input");
    let inputValue = input.val();

    const data = $.trim(inputValue);
    if (data.length > 0) {
      const payload = {
        query: data,
      };
      if (Unbxd && typeof Unbxd.track === "function") {
        Unbxd.track("search", payload);
      } else {
        console.error("unbxdAnalytics.js is not loaded!");
      }
      window.location =
        window.location.origin + "/search?q=" + encodeURIComponent(data);
    }
  }
});

// Function to initialize Yotpo widget
function initializeYotpoWidget() {
  // Check if the Yotpo widget is available
  if (typeof yotpo !== "undefined" && typeof yotpo.initWidgets === "function") {
    yotpo.initWidgets();
  } else {
    // Yotpo script hasn't fully loaded, wait and retry
    setTimeout(initializeYotpoWidget, 100); // Adjust the delay as needed
  }
}

// Re-initialize Yotpo widget on page change
window.onpopstate = function () {
  // You might want to add a slight delay to allow the DOM to update before re-initializing
  setTimeout(function () {
    initializeYotpoWidget();
  }, 1000); // Adjust the delay as needed
};

let PDPSplideSlider;
const revertSplideConfig = (splide) => {
  const splideList = splide.Components.Elements.list;
  splideList.style.removeProperty("justify-content");
  splide.Components.Arrows.arrows.next.style.setProperty("display", "flex");
  splide.Components.Arrows.arrows.prev.style.setProperty("display", "flex");
  splide.Components.Drag.disable(false);
};
const updateSplideConfig = (splide) => {
  const slidesLength = splide.Components.Slides.getLength();
  const splideList = splide.Components.Elements.list;
  splideList.style.setProperty("justify-content", "center");
  splide.Components.Arrows.arrows.next.style.setProperty("display", "none");
  splide.Components.Arrows.arrows.prev.style.setProperty("display", "none");
  splide.Components.Move.jump(slidesLength);
  splide.Components.Drag.disable(true);
};
const makeSplideResponsive = (splide) => {
  if (splide == undefined || splide == null) {
    return;
  }
  const windowWidth = window.innerWidth;
  const slidesLength = splide.Components.Slides.getLength();
  let updateConfig = 0;
  if (windowWidth <= 480 && slidesLength == 1) {
    updateSplideConfig(splide);
    updateConfig = 1;
  }
  if (windowWidth <= 798 && slidesLength <= 2) {
    updateSplideConfig(splide);
    updateConfig = 1;
  }
  if (windowWidth > 798 && slidesLength <= 6) {
    updateSplideConfig(splide);
    updateConfig = 1;
  }
  if (!updateConfig) {
    revertSplideConfig(splide);
  }
};

$(window).resize(function () {
  intialLeft = "";
  calculation();
  centerAlignUnxdWrapper();
});

function addScriptDynamically(src) {
  var script = document.createElement("script");
  script.src = src;
  document.head.insertAdjacentElement("afterbegin", script);
}

document.addEventListener("DOMContentLoaded", () => {
  addScriptDynamically(
    "https://cdnjs.cloudflare.com/ajax/libs/splidejs/4.1.4/js/splide.min.js"
  );

  if (pageType != undefined && pageType.toLowerCase() == "products") {
    const findPDPRecsInterval = setInterval(() => {
      if (
        document.querySelector(`#UNX-pdp-recs`) != null &&
        document.querySelector("#UNX-pdp-recs .splide") != null
      ) {
        clearInterval(findPDPRecsInterval);
        const PDPSplideSlider = new Splide("#UNX-pdp-recs .splide", {
          type: "slide",
          trimSpace: "move",
          perPage: 3,
          focus: "center",
        });

        PDPSplideSlider.mount();

        PDPSplideSlider.on("mounted refresh move resize", () => {
          makeSplideResponsive(PDPSplideSlider);
        });

        initializeYotpoWidget();
      }
    }, 200);

    const findPDPRecsCrossSellInterval = setInterval(() => {
      if (
        document.querySelector(`#UNX-pdp-recs-cross-sell`) != null &&
        document.querySelector("#UNX-pdp-recs-cross-sell .splide") != null
      ) {
        clearInterval(findPDPRecsCrossSellInterval);
        const PDPSplideSlider = new Splide("#UNX-pdp-recs-cross-sell .splide", {
          type: "slide",
          trimSpace: "move",
          perPage: 3,
          focus: "center",
        });

        PDPSplideSlider.mount();

        PDPSplideSlider.on("mounted refresh move resize", () => {
          makeSplideResponsive(PDPSplideSlider);
        });

        initializeYotpoWidget();
      }
    }, 200);
  }
  if (document.querySelector("body.index") != null) {
    const findHomeRecsCrossSellInterval = setInterval(() => {
      if (
        document.querySelector(`#UNX-homePage-RECS-1`) != null &&
        document.querySelector("#UNX-homePage-RECS-1 .splide") != null
      ) {
        clearInterval(findHomeRecsCrossSellInterval);
        const PDPSplideSlider = new Splide("#UNX-homePage-RECS-1 .splide", {
          type: "slide",
          trimSpace: "move",
          perPage: 3,
          focus: "center",
        });

        PDPSplideSlider.mount();

        PDPSplideSlider.on("mounted refresh move resize", () => {
          makeSplideResponsive(PDPSplideSlider);
        });

        initializeYotpoWidget();
      }
    }, 200);
  }
});

function centerAlignUnxdWrapper() {
  const unbxdAsWrapper = document.querySelector(
    ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
  );
  if (
    autosuggest_input_element != null &&
    unbxdAsWrapper != null &&
    unbxdAsWrapper.offsetWidth > autosuggest_input_element.width()
  ) {
    // Calculate offset based on input width and autosuggest container width
    const autosuggestOffset =
      (unbxdAsWrapper.offsetWidth - autosuggest_input_element.width()) / 2;
    const getAutoElLeft = parseInt(unbxdAsWrapper.style.left);

    if (intialLeft == "") {
      intialLeft = getAutoElLeft;
    }
    const calculateLeft = intialLeft - autosuggestOffset;
    // Set the left position of the autosuggest container
    unbxdAsWrapper.style.left = `${calculateLeft}px`;
  }
}

function calculation() {
  const location = autosuggest_input_element.offset();
  const left = location.left;
  $(".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest").css({
    position: "absolute",
    left: left + "px",
  });
}

// fix redirection to blank search page when clicked on search icon of stick header
const findStickHeaderSearch = setInterval(() => {
  if (
    document.querySelector(
      ".sticky_nav .nav--combined .icon-search.dropdown_link"
    ) != null
  ) {
    clearInterval(findStickHeaderSearch);
    const stickyHeaderSearch = document.querySelector(
      ".sticky_nav .nav--combined .icon-search.dropdown_link"
    );
    stickyHeaderSearch != null &&
      stickyHeaderSearch.addEventListener("click", (e) => {
        e.preventDefault();
        $("html, body").animate(
          {
            scrollTop: 0,
          },
          100
        );
        $(".unbxd-auto-suggest-input") != null &&
          $(".unbxd-auto-suggest-input").focus();
      });
  }
}, 100);


async function addAsStaticOtherContent() {
  let blogsData = await getBlogsData("*");
  let pagesData = await getPagesData("*");
  let combinedProducts = [...blogsData.products, ...pagesData.products];

  const rightSection = getAsRightSectionData({
    products: combinedProducts,
  });
  const unbxd_as_wrapper = document.querySelector(".unbxd-custom-as");
  if (
    unbxd_as_wrapper.querySelector(".boost-pfs-search-suggestion-group") ==
    null
  ) {
    const blogsContainerHTML = `<div class="boost-pfs-search-suggestion-group" data-group="pages" aria-label="Pages">
                                </div>`;
    const collectionContainerHTML = `<div class="boost-pfs-search-suggestion-group-collection" data-group="collections" aria-label="collections">
                                </div>`;
    const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
      ".unbxd-as-maincontent"
    );
    if (changeWindowWidthMobileLayout) {
      const unbxdAsPopularProductHeading = unbxdAsMainContent.querySelector(
        ".unbxd-as-popular-product-header"
      );
      unbxdAsPopularProductHeading &&
        unbxdAsPopularProductHeading.insertAdjacentHTML(
          "beforebegin",
          collectionContainerHTML
        );
      unbxdAsMainContent &&
        unbxdAsMainContent.insertAdjacentHTML(
          "beforeend",
          blogsContainerHTML
        );
    } else {
      unbxdAsMainContent &&
        unbxdAsMainContent.insertAdjacentHTML(
          "beforeend",
          blogsContainerHTML
        );
    }
  }
  const blogsContainer = unbxd_as_wrapper.querySelector(
    ".boost-pfs-search-suggestion-group"
  );
  const collectionContainer = unbxd_as_wrapper.querySelector(
    ".boost-pfs-search-suggestion-group-collection"
  );
  if (changeWindowWidthMobileLayout) {
    addHTMLToRightAs(
      collectionContainer,
      rightSection.category,
      "UNX-right-as-category",
      "Collections"
    );
  } else {
    addHTMLToRightAs(
      blogsContainer,
      rightSection.category,
      "UNX-right-as-category",
      "Collections"
    );
  }

  addHTMLToRightAs(
    blogsContainer,
    rightSection.pages,
    "UNX-right-as-pages",
    "Pages"
  );
  addHTMLToRightAs(
    blogsContainer,
    rightSection.blogs,
    "UNX-right-as-blogs",
    "Learning Center"
  );
}

/* Autosuggestion results on click of search box without typing query */

$(document).ready(function () {
  let productsHtml = "",
    suggestionHtml = "",
    headerHtml = "",
    productHeaderHtml = "",
    parentHtml = "";
  let popularProductCount = 6;
  if (screen.width <= 798) {
    popularProductCount = 4;
  }

  $.ajax({
    url: `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/autosuggest?q=*&topQueries.count=5&promotedSuggestion.count=5&keywordSuggestions.count=0&inFields.count=0&popularProducts.count=${popularProductCount}&filter=-content_type:"PAGES"&filter=-content_type:"BLOGS"`,
    type: "GET",
  })
    .done(function (res) {
      const searchedQuery = res.searchMetaData.queryParams.q;
      const products = res.response.products;
      $.each(products, function (key, value) {
        const UNXautosuggest = value.autosuggest;
        if (value.content_type == "PRODUCT") {
          const unxProductUrl = value.productUrl;
          const unxImageUrl =
            value.imageUrl ||
            "https://libraries.unbxdapi.com/sdk-assets/defaultImage.svg";
          const title = value.title || "";
          const vendor = value.vendor || "";
          const doctype = value.doctype;
          const uniqueId = value.uniqueId;
          let price = value.price;
          const compareAtPrice = value.compareAtPrice;
          let priceUI;

          if (["Smith Brothers", "L and J.G. Stickley Inc"].includes(vendor)) {
            price = "";
          }

          const getNormalPriceHTML = (price) => {
            return `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;`;
          };

          if (
            (price == 0 || price == undefined) &&
            (compareAtPrice == 0 || compareAtPrice == undefined)
          ) {
            /* price & compareAtPrice both doesn't exists */
            priceUI = getNormalPriceHTML(0);
          } else if (
            (price == 0 || price == undefined) &&
            compareAtPrice != 0 &&
            compareAtPrice != undefined
          ) {
            /* price doesn't exists; compareAtPrice exists */
            priceUI = getNormalPriceHTML(compareAtPrice);
          } else if (
            (compareAtPrice == 0 || compareAtPrice == undefined) &&
            price != 0 &&
            price != undefined
          ) {
            /* compareAtPrice doesn't exists; price exists */
            priceUI = getNormalPriceHTML(price);
          } else if (price == compareAtPrice) {
            /* both prices exists and are equal */
            priceUI = getNormalPriceHTML(price);
          } else {
            /* both prices exists but not equal */
            priceUI = `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;
				                <s>${currency}${compareAtPrice}</s>`;
          }

          const priceUIContainer = `<p class="unbxd-auto-suggest-price-p"> ${priceUI} </p>`;

          productsHtml += `<li class="unbxd-as-popular-product unbxd-as-popular-product-grid UNX-product-click-event" data-value="${title}"
          data-type="${doctype}" data-pid="${uniqueId}" data-prank="${
            key + 1
          }" data-query="${searchedQuery}">
          <a title="${title}" href="${unxProductUrl}">
            <div class="unbxd-as-popular-product-info">
              <div class="unbxd-as-popular-product-image-container">
                <img src="${unxImageUrl}" alt="${title}">
              </div>
              <div class="unbxd-as-popular-product-name">${title}</div>
              <p class="unbxd-auto-suggest-vendor">${vendor}</p>
              <div class="unbxd-as-popular-product-price">
              ${
                vendor == "Smith Brothers" ||
                vendor == "L and J.G. Stickley Inc"
                  ? ""
                  : priceUIContainer
              }
              </div>
            </div>
          </a>
        </li>`;
        } else {
          suggestionHtml += `<a href="/search?q=${value.autosuggest}">
            <li class="unbxd-as-sorted-suggestion UNX-static-as-suggestion" data-value="${value.autosuggest}" data-type="${value.doctype}"
            data-source="" data-query="${searchedQuery}" data-field-name="autosuggest" data-sorted="true">${UNXautosuggest}</li>
          </a>`;
        }
      });

      // -----Trending Headers div-----
      headerHtml += `<li class="unbxd-as-header unbxd-as-suggestions-header">Suggestions</li>`;

      // // Trending Product Header
      productHeaderHtml += `<li class="unbxd-as-header unbxd-as-popular-product-header">Popular Products</li>`;

      let desktopSearchContainer = $(
        ".header .main-nav > .search-container .search__form"
      );
      let mobileSearchContainer = $(
        ".mobile-search .search-form.search-popup__form"
      );

      // merged div's
      if (window.innerWidth <= 798 || isMobile.any()) {
        parentHtml += `<div id="unbxd-custom-mobile-autosuggestion" class="unbxd-custom-as unbxd-as-wrapper unbxd-as-overall-autosuggest unbxd-as-wrapper-mobile mobile-ios" style="position: absolute; z-index: 999999; top: 54px; left: 20px;">
        <ul class="unbxd-as-maincontent unbxd-as-suggestions-overall unbxd-as-mobile-view" style="width: 234px; box-sizing: border-box;">
        ${headerHtml}
        ${suggestionHtml}
        ${productHeaderHtml}
        ${productsHtml}
        </ul></div>`;
        mobileSearchContainer.append(parentHtml);
      } else {
        parentHtml += `<div id="unbxd-custom-autosuggestion" class="unbxd-as-wrapper unbxd-as-overall-autosuggest unbxd-as-extra-right unbxd-custom-as" style="position: absolute;z-index: 10000;top: 100% !important; display:none; left: 50%; transform: translate(-50%);">
        <ul class="unbxd-as-maincontent unbxd-as-suggestions-overall" style="width: 300px; box-sizing: border-box;">
        ${headerHtml}
        ${suggestionHtml}
        </ul>
        <ul class="unbxd-as-sidecontent-custom" style="width: 600px; box-sizing: border-box;">
        ${productHeaderHtml}
        ${productsHtml}
        </ul>
      </div>`;
        desktopSearchContainer.append(parentHtml);
      }
      addAsStaticOtherContent();

      if (changeASLayoutToMobile) {
        document
          .querySelector(".mobile-search .search-form .close-search")
          .addEventListener("touchstart", (e) => {
            const unbxdAsWrapperMobile = document.querySelector(
              ".unbxd-as-wrapper-default"
            );
            if (unbxdAsWrapperMobile != null) {
              unbxdAsWrapperMobile.style.setProperty("display", "none");
            }
          });
      }
      document.addEventListener("click", (e) => {
        if (
          e.target.closest(
            ".header .main-nav > .search-container .search__form"
          ) == null
        ) {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
        }
      });

      $(document).on("focus click", autosuggest_input_element, function () {
        let inputValue = autosuggest_input_element.val();
        if (inputValue == "") {
          if (window.innerWidth <= 1024) {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "block");
          } else {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "flex");
          }
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "block");
        } else {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        }
      });
      $(document).on("focus click", "input#filterZip", function () {
        let inputValue = autosuggest_input_element.val();
        if (inputValue == "") {
          if (window.innerWidth <= 1024) {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "none");
          } else {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "none");
          }
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        } else {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        }
      });
      $(document).on("input", autosuggest_input_element, function () {
        let inputValue = autosuggest_input_element.val();
        if (inputValue == "") {
          if (window.innerWidth <= 1024) {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "block");
          } else {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "none");
          }
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "block");
        } else {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        }
      });
      // analytics events
      // product click
      const staticAsProducts = document.querySelectorAll(
        ".unbxd-custom-as .UNX-product-click-event"
      );
      for (const staticAsProduct of staticAsProducts) {
        const { pid, prank, query, type, value } = staticAsProduct.dataset;

        staticAsProduct.addEventListener("click", () => {
          const payload = {
            query: value,
            autosuggestParams: {
              autosuggest_type: type,
              pid: String(pid),
              unbxdprank: Number(prank),
              internal_query: query,
            },
          };
          unbxdAnalytics("search", payload);
        });
      }

      // suggestion click
      const staticAsSuggestions = document.querySelectorAll(
        ".UNX-static-as-suggestion"
      );
      for (const staticAsSuggestion of staticAsSuggestions) {
        const { type, fieldName, value, query } = staticAsSuggestion.dataset;

        staticAsSuggestion.addEventListener("click", () => {
          const autosuggestParams = {
            autosuggest_type: type,
            autosuggest_suggestion: value,
            field_name: fieldName,
            field_value: value,
            src_field: "",
            internal_query: query,
          };
          const payload = {
            query: value,
          };
          payload.autosuggestParams = autosuggestParams;
          unbxdAnalytics("search", payload);
        });
      }
    })
    .fail(function (res) {
      console.log("error occurs");
    });
});


```

```
Furniture fair ss-unbxd_funriture_fair_sitekey_autosuggest.js
/**!

 @license
 handlebars v4.7.8

Copyright (C) 2011-2019 by Yehuda Katz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

*/
!function(a,b){"object"==typeof exports&&"object"==typeof module?module.exports=b():"function"==typeof define&&define.amd?define([],b):"object"==typeof exports?exports.Handlebars=b():a.Handlebars=b()}(this,function(){return function(a){function b(d){if(c[d])return c[d].exports;var e=c[d]={exports:{},id:d,loaded:!1};return a[d].call(e.exports,e,e.exports,b),e.loaded=!0,e.exports}var c={};return b.m=a,b.c=c,b.p="",b(0)}([function(a,b,c){"use strict";function d(){var a=r();return a.compile=function(b,c){return k.compile(b,c,a)},a.precompile=function(b,c){return k.precompile(b,c,a)},a.AST=i["default"],a.Compiler=k.Compiler,a.JavaScriptCompiler=m["default"],a.Parser=j.parser,a.parse=j.parse,a.parseWithoutProcessing=j.parseWithoutProcessing,a}var e=c(1)["default"];b.__esModule=!0;var f=c(2),g=e(f),h=c(84),i=e(h),j=c(85),k=c(90),l=c(91),m=e(l),n=c(88),o=e(n),p=c(83),q=e(p),r=g["default"].create,s=d();s.create=d,q["default"](s),s.Visitor=o["default"],s["default"]=s,b["default"]=s,a.exports=b["default"]},function(a,b){"use strict";b["default"]=function(a){return a&&a.__esModule?a:{"default":a}},b.__esModule=!0},function(a,b,c){"use strict";function d(){var a=new h.HandlebarsEnvironment;return n.extend(a,h),a.SafeString=j["default"],a.Exception=l["default"],a.Utils=n,a.escapeExpression=n.escapeExpression,a.VM=p,a.template=function(b){return p.template(b,a)},a}var e=c(3)["default"],f=c(1)["default"];b.__esModule=!0;var g=c(4),h=e(g),i=c(77),j=f(i),k=c(6),l=f(k),m=c(5),n=e(m),o=c(78),p=e(o),q=c(83),r=f(q),s=d();s.create=d,r["default"](s),s["default"]=s,b["default"]=s,a.exports=b["default"]},function(a,b){"use strict";b["default"]=function(a){if(a&&a.__esModule)return a;var b={};if(null!=a)for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&(b[c]=a[c]);return b["default"]=a,b},b.__esModule=!0},function(a,b,c){"use strict";function d(a,b,c){this.helpers=a||{},this.partials=b||{},this.decorators=c||{},i.registerDefaultHelpers(this),j.registerDefaultDecorators(this)}var e=c(1)["default"];b.__esModule=!0,b.HandlebarsEnvironment=d;var f=c(5),g=c(6),h=e(g),i=c(10),j=c(70),k=c(72),l=e(k),m=c(73),n="4.7.8";b.VERSION=n;var o=8;b.COMPILER_REVISION=o;var p=7;b.LAST_COMPATIBLE_COMPILER_REVISION=p;var q={1:"<= 1.0.rc.2",2:"== 1.0.0-rc.3",3:"== 1.0.0-rc.4",4:"== 1.x.x",5:"== 2.0.0-alpha.x",6:">= 2.0.0-beta.1",7:">= 4.0.0 <4.3.0",8:">= 4.3.0"};b.REVISION_CHANGES=q;var r="[object Object]";d.prototype={constructor:d,logger:l["default"],log:l["default"].log,registerHelper:function(a,b){if(f.toString.call(a)===r){if(b)throw new h["default"]("Arg not supported with multiple helpers");f.extend(this.helpers,a)}else this.helpers[a]=b},unregisterHelper:function(a){delete this.helpers[a]},registerPartial:function(a,b){if(f.toString.call(a)===r)f.extend(this.partials,a);else{if("undefined"==typeof b)throw new h["default"]('Attempting to register a partial called "'+a+'" as undefined');this.partials[a]=b}},unregisterPartial:function(a){delete this.partials[a]},registerDecorator:function(a,b){if(f.toString.call(a)===r){if(b)throw new h["default"]("Arg not supported with multiple decorators");f.extend(this.decorators,a)}else this.decorators[a]=b},unregisterDecorator:function(a){delete this.decorators[a]},resetLoggedPropertyAccesses:function(){m.resetLoggedProperties()}};var s=l["default"].log;b.log=s,b.createFrame=f.createFrame,b.logger=l["default"]},function(a,b){"use strict";function c(a){return k[a]}function d(a){for(var b=1;b<arguments.length;b++)for(var c in arguments[b])Object.prototype.hasOwnProperty.call(arguments[b],c)&&(a[c]=arguments[b][c]);return a}function e(a,b){for(var c=0,d=a.length;c<d;c++)if(a[c]===b)return c;return-1}function f(a){if("string"!=typeof a){if(a&&a.toHTML)return a.toHTML();if(null==a)return"";if(!a)return a+"";a=""+a}return m.test(a)?a.replace(l,c):a}function g(a){return!a&&0!==a||!(!p(a)||0!==a.length)}function h(a){var b=d({},a);return b._parent=a,b}function i(a,b){return a.path=b,a}function j(a,b){return(a?a+".":"")+b}b.__esModule=!0,b.extend=d,b.indexOf=e,b.escapeExpression=f,b.isEmpty=g,b.createFrame=h,b.blockParams=i,b.appendContextPath=j;var k={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#x27;","`":"&#x60;","=":"&#x3D;"},l=/[&<>"'`=]/g,m=/[&<>"'`=]/,n=Object.prototype.toString;b.toString=n;var o=function(a){return"function"==typeof a};o(/x/)&&(b.isFunction=o=function(a){return"function"==typeof a&&"[object Function]"===n.call(a)}),b.isFunction=o;var p=Array.isArray||function(a){return!(!a||"object"!=typeof a)&&"[object Array]"===n.call(a)};b.isArray=p},function(a,b,c){"use strict";function d(a,b){var c=b&&b.loc,g=void 0,h=void 0,i=void 0,j=void 0;c&&(g=c.start.line,h=c.end.line,i=c.start.column,j=c.end.column,a+=" - "+g+":"+i);for(var k=Error.prototype.constructor.call(this,a),l=0;l<f.length;l++)this[f[l]]=k[f[l]];Error.captureStackTrace&&Error.captureStackTrace(this,d);try{c&&(this.lineNumber=g,this.endLineNumber=h,e?(Object.defineProperty(this,"column",{value:i,enumerable:!0}),Object.defineProperty(this,"endColumn",{value:j,enumerable:!0})):(this.column=i,this.endColumn=j))}catch(m){}}var e=c(7)["default"];b.__esModule=!0;var f=["description","fileName","lineNumber","endLineNumber","message","name","number","stack"];d.prototype=new Error,b["default"]=d,a.exports=b["default"]},function(a,b,c){a.exports={"default":c(8),__esModule:!0}},function(a,b,c){var d=c(9);a.exports=function(a,b,c){return d.setDesc(a,b,c)}},function(a,b){var c=Object;a.exports={create:c.create,getProto:c.getPrototypeOf,isEnum:{}.propertyIsEnumerable,getDesc:c.getOwnPropertyDescriptor,setDesc:c.defineProperty,setDescs:c.defineProperties,getKeys:c.keys,getNames:c.getOwnPropertyNames,getSymbols:c.getOwnPropertySymbols,each:[].forEach}},function(a,b,c){"use strict";function d(a){h["default"](a),j["default"](a),l["default"](a),n["default"](a),p["default"](a),r["default"](a),t["default"](a)}function e(a,b,c){a.helpers[b]&&(a.hooks[b]=a.helpers[b],c||delete a.helpers[b])}var f=c(1)["default"];b.__esModule=!0,b.registerDefaultHelpers=d,b.moveHelperToHooks=e;var g=c(11),h=f(g),i=c(12),j=f(i),k=c(65),l=f(k),m=c(66),n=f(m),o=c(67),p=f(o),q=c(68),r=f(q),s=c(69),t=f(s)},function(a,b,c){"use strict";b.__esModule=!0;var d=c(5);b["default"]=function(a){a.registerHelper("blockHelperMissing",function(b,c){var e=c.inverse,f=c.fn;if(b===!0)return f(this);if(b===!1||null==b)return e(this);if(d.isArray(b))return b.length>0?(c.ids&&(c.ids=[c.name]),a.helpers.each(b,c)):e(this);if(c.data&&c.ids){var g=d.createFrame(c.data);g.contextPath=d.appendContextPath(c.data.contextPath,c.name),c={data:g}}return f(b,c)})},a.exports=b["default"]},function(a,b,c){"use strict";var d=c(13)["default"],e=c(43)["default"],f=c(55)["default"],g=c(60)["default"],h=c(1)["default"];b.__esModule=!0;var i=c(5),j=c(6),k=h(j);b["default"]=function(a){a.registerHelper("each",function(a,b){function c(b,c,d){n&&(n.key=b,n.index=c,n.first=0===c,n.last=!!d,o&&(n.contextPath=o+b)),m+=h(a[b],{data:n,blockParams:i.blockParams([a[b],b],[o+b,null])})}if(!b)throw new k["default"]("Must pass iterator to #each");var h=b.fn,j=b.inverse,l=0,m="",n=void 0,o=void 0;if(b.data&&b.ids&&(o=i.appendContextPath(b.data.contextPath,b.ids[0])+"."),i.isFunction(a)&&(a=a.call(this)),b.data&&(n=i.createFrame(b.data)),a&&"object"==typeof a)if(i.isArray(a))for(var p=a.length;l<p;l++)l in a&&c(l,l,l===a.length-1);else if("function"==typeof d&&a[e]){for(var q=[],r=f(a),s=r.next();!s.done;s=r.next())q.push(s.value);a=q;for(var p=a.length;l<p;l++)c(l,l,l===a.length-1)}else!function(){var b=void 0;g(a).forEach(function(a){void 0!==b&&c(b,l-1),b=a,l++}),void 0!==b&&c(b,l-1,!0)}();return 0===l&&(m=j(this)),m})},a.exports=b["default"]},function(a,b,c){a.exports={"default":c(14),__esModule:!0}},function(a,b,c){c(15),c(42),a.exports=c(21).Symbol},function(a,b,c){"use strict";var d=c(9),e=c(16),f=c(17),g=c(18),h=c(20),i=c(24),j=c(19),k=c(27),l=c(28),m=c(30),n=c(29),o=c(31),p=c(36),q=c(37),r=c(38),s=c(39),t=c(32),u=c(26),v=d.getDesc,w=d.setDesc,x=d.create,y=p.get,z=e.Symbol,A=e.JSON,B=A&&A.stringify,C=!1,D=n("_hidden"),E=d.isEnum,F=k("symbol-registry"),G=k("symbols"),H="function"==typeof z,I=Object.prototype,J=g&&j(function(){return 7!=x(w({},"a",{get:function(){return w(this,"a",{value:7}).a}})).a})?function(a,b,c){var d=v(I,b);d&&delete I[b],w(a,b,c),d&&a!==I&&w(I,b,d)}:w,K=function(a){var b=G[a]=x(z.prototype);return b._k=a,g&&C&&J(I,a,{configurable:!0,set:function(b){f(this,D)&&f(this[D],a)&&(this[D][a]=!1),J(this,a,u(1,b))}}),b},L=function(a){return"symbol"==typeof a},M=function(a,b,c){return c&&f(G,b)?(c.enumerable?(f(a,D)&&a[D][b]&&(a[D][b]=!1),c=x(c,{enumerable:u(0,!1)})):(f(a,D)||w(a,D,u(1,{})),a[D][b]=!0),J(a,b,c)):w(a,b,c)},N=function(a,b){s(a);for(var c,d=q(b=t(b)),e=0,f=d.length;f>e;)M(a,c=d[e++],b[c]);return a},O=function(a,b){return void 0===b?x(a):N(x(a),b)},P=function(a){var b=E.call(this,a);return!(b||!f(this,a)||!f(G,a)||f(this,D)&&this[D][a])||b},Q=function(a,b){var c=v(a=t(a),b);return!c||!f(G,b)||f(a,D)&&a[D][b]||(c.enumerable=!0),c},R=function(a){for(var b,c=y(t(a)),d=[],e=0;c.length>e;)f(G,b=c[e++])||b==D||d.push(b);return d},S=function(a){for(var b,c=y(t(a)),d=[],e=0;c.length>e;)f(G,b=c[e++])&&d.push(G[b]);return d},T=function(a){if(void 0!==a&&!L(a)){for(var b,c,d=[a],e=1,f=arguments;f.length>e;)d.push(f[e++]);return b=d[1],"function"==typeof b&&(c=b),!c&&r(b)||(b=function(a,b){if(c&&(b=c.call(this,a,b)),!L(b))return b}),d[1]=b,B.apply(A,d)}},U=j(function(){var a=z();return"[null]"!=B([a])||"{}"!=B({a:a})||"{}"!=B(Object(a))});H||(z=function(){if(L(this))throw TypeError("Symbol is not a constructor");return K(m(arguments.length>0?arguments[0]:void 0))},i(z.prototype,"toString",function(){return this._k}),L=function(a){return a instanceof z},d.create=O,d.isEnum=P,d.getDesc=Q,d.setDesc=M,d.setDescs=N,d.getNames=p.get=R,d.getSymbols=S,g&&!c(41)&&i(I,"propertyIsEnumerable",P,!0));var V={"for":function(a){return f(F,a+="")?F[a]:F[a]=z(a)},keyFor:function(a){return o(F,a)},useSetter:function(){C=!0},useSimple:function(){C=!1}};d.each.call("hasInstance,isConcatSpreadable,iterator,match,replace,search,species,split,toPrimitive,toStringTag,unscopables".split(","),function(a){var b=n(a);V[a]=H?b:K(b)}),C=!0,h(h.G+h.W,{Symbol:z}),h(h.S,"Symbol",V),h(h.S+h.F*!H,"Object",{create:O,defineProperty:M,defineProperties:N,getOwnPropertyDescriptor:Q,getOwnPropertyNames:R,getOwnPropertySymbols:S}),A&&h(h.S+h.F*(!H||U),"JSON",{stringify:T}),l(z,"Symbol"),l(Math,"Math",!0),l(e.JSON,"JSON",!0)},function(a,b){var c=a.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=c)},function(a,b){var c={}.hasOwnProperty;a.exports=function(a,b){return c.call(a,b)}},function(a,b,c){a.exports=!c(19)(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},function(a,b){a.exports=function(a){try{return!!a()}catch(b){return!0}}},function(a,b,c){var d=c(16),e=c(21),f=c(22),g="prototype",h=function(a,b,c){var i,j,k,l=a&h.F,m=a&h.G,n=a&h.S,o=a&h.P,p=a&h.B,q=a&h.W,r=m?e:e[b]||(e[b]={}),s=m?d:n?d[b]:(d[b]||{})[g];m&&(c=b);for(i in c)j=!l&&s&&i in s,j&&i in r||(k=j?s[i]:c[i],r[i]=m&&"function"!=typeof s[i]?c[i]:p&&j?f(k,d):q&&s[i]==k?function(a){var b=function(b){return this instanceof a?new a(b):a(b)};return b[g]=a[g],b}(k):o&&"function"==typeof k?f(Function.call,k):k,o&&((r[g]||(r[g]={}))[i]=k))};h.F=1,h.G=2,h.S=4,h.P=8,h.B=16,h.W=32,a.exports=h},function(a,b){var c=a.exports={version:"1.2.6"};"number"==typeof __e&&(__e=c)},function(a,b,c){var d=c(23);a.exports=function(a,b,c){if(d(a),void 0===b)return a;switch(c){case 1:return function(c){return a.call(b,c)};case 2:return function(c,d){return a.call(b,c,d)};case 3:return function(c,d,e){return a.call(b,c,d,e)}}return function(){return a.apply(b,arguments)}}},function(a,b){a.exports=function(a){if("function"!=typeof a)throw TypeError(a+" is not a function!");return a}},function(a,b,c){a.exports=c(25)},function(a,b,c){var d=c(9),e=c(26);a.exports=c(18)?function(a,b,c){return d.setDesc(a,b,e(1,c))}:function(a,b,c){return a[b]=c,a}},function(a,b){a.exports=function(a,b){return{enumerable:!(1&a),configurable:!(2&a),writable:!(4&a),value:b}}},function(a,b,c){var d=c(16),e="__core-js_shared__",f=d[e]||(d[e]={});a.exports=function(a){return f[a]||(f[a]={})}},function(a,b,c){var d=c(9).setDesc,e=c(17),f=c(29)("toStringTag");a.exports=function(a,b,c){a&&!e(a=c?a:a.prototype,f)&&d(a,f,{configurable:!0,value:b})}},function(a,b,c){var d=c(27)("wks"),e=c(30),f=c(16).Symbol;a.exports=function(a){return d[a]||(d[a]=f&&f[a]||(f||e)("Symbol."+a))}},function(a,b){var c=0,d=Math.random();a.exports=function(a){return"Symbol(".concat(void 0===a?"":a,")_",(++c+d).toString(36))}},function(a,b,c){var d=c(9),e=c(32);a.exports=function(a,b){for(var c,f=e(a),g=d.getKeys(f),h=g.length,i=0;h>i;)if(f[c=g[i++]]===b)return c}},function(a,b,c){var d=c(33),e=c(35);a.exports=function(a){return d(e(a))}},function(a,b,c){var d=c(34);a.exports=Object("z").propertyIsEnumerable(0)?Object:function(a){return"String"==d(a)?a.split(""):Object(a)}},function(a,b){var c={}.toString;a.exports=function(a){return c.call(a).slice(8,-1)}},function(a,b){a.exports=function(a){if(void 0==a)throw TypeError("Can't call method on  "+a);return a}},function(a,b,c){var d=c(32),e=c(9).getNames,f={}.toString,g="object"==typeof window&&Object.getOwnPropertyNames?Object.getOwnPropertyNames(window):[],h=function(a){try{return e(a)}catch(b){return g.slice()}};a.exports.get=function(a){return g&&"[object Window]"==f.call(a)?h(a):e(d(a))}},function(a,b,c){var d=c(9);a.exports=function(a){var b=d.getKeys(a),c=d.getSymbols;if(c)for(var e,f=c(a),g=d.isEnum,h=0;f.length>h;)g.call(a,e=f[h++])&&b.push(e);return b}},function(a,b,c){var d=c(34);a.exports=Array.isArray||function(a){return"Array"==d(a)}},function(a,b,c){var d=c(40);a.exports=function(a){if(!d(a))throw TypeError(a+" is not an object!");return a}},function(a,b){a.exports=function(a){return"object"==typeof a?null!==a:"function"==typeof a}},function(a,b){a.exports=!0},function(a,b){},function(a,b,c){a.exports={"default":c(44),__esModule:!0}},function(a,b,c){c(45),c(51),a.exports=c(29)("iterator")},function(a,b,c){"use strict";var d=c(46)(!0);c(48)(String,"String",function(a){this._t=String(a),this._i=0},function(){var a,b=this._t,c=this._i;return c>=b.length?{value:void 0,done:!0}:(a=d(b,c),this._i+=a.length,{value:a,done:!1})})},function(a,b,c){var d=c(47),e=c(35);a.exports=function(a){return function(b,c){var f,g,h=String(e(b)),i=d(c),j=h.length;return i<0||i>=j?a?"":void 0:(f=h.charCodeAt(i),f<55296||f>56319||i+1===j||(g=h.charCodeAt(i+1))<56320||g>57343?a?h.charAt(i):f:a?h.slice(i,i+2):(f-55296<<10)+(g-56320)+65536)}}},function(a,b){var c=Math.ceil,d=Math.floor;a.exports=function(a){return isNaN(a=+a)?0:(a>0?d:c)(a)}},function(a,b,c){"use strict";var d=c(41),e=c(20),f=c(24),g=c(25),h=c(17),i=c(49),j=c(50),k=c(28),l=c(9).getProto,m=c(29)("iterator"),n=!([].keys&&"next"in[].keys()),o="@@iterator",p="keys",q="values",r=function(){return this};a.exports=function(a,b,c,s,t,u,v){j(c,b,s);var w,x,y=function(a){if(!n&&a in C)return C[a];switch(a){case p:return function(){return new c(this,a)};case q:return function(){return new c(this,a)}}return function(){return new c(this,a)}},z=b+" Iterator",A=t==q,B=!1,C=a.prototype,D=C[m]||C[o]||t&&C[t],E=D||y(t);if(D){var F=l(E.call(new a));k(F,z,!0),!d&&h(C,o)&&g(F,m,r),A&&D.name!==q&&(B=!0,E=function(){return D.call(this)})}if(d&&!v||!n&&!B&&C[m]||g(C,m,E),i[b]=E,i[z]=r,t)if(w={values:A?E:y(q),keys:u?E:y(p),entries:A?y("entries"):E},v)for(x in w)x in C||f(C,x,w[x]);else e(e.P+e.F*(n||B),b,w);return w}},function(a,b){a.exports={}},function(a,b,c){"use strict";var d=c(9),e=c(26),f=c(28),g={};c(25)(g,c(29)("iterator"),function(){return this}),a.exports=function(a,b,c){a.prototype=d.create(g,{next:e(1,c)}),f(a,b+" Iterator")}},function(a,b,c){c(52);var d=c(49);d.NodeList=d.HTMLCollection=d.Array},function(a,b,c){"use strict";var d=c(53),e=c(54),f=c(49),g=c(32);a.exports=c(48)(Array,"Array",function(a,b){this._t=g(a),this._i=0,this._k=b},function(){var a=this._t,b=this._k,c=this._i++;return!a||c>=a.length?(this._t=void 0,e(1)):"keys"==b?e(0,c):"values"==b?e(0,a[c]):e(0,[c,a[c]])},"values"),f.Arguments=f.Array,d("keys"),d("values"),d("entries")},function(a,b){a.exports=function(){}},function(a,b){a.exports=function(a,b){return{value:b,done:!!a}}},function(a,b,c){a.exports={"default":c(56),__esModule:!0}},function(a,b,c){c(51),c(45),a.exports=c(57)},function(a,b,c){var d=c(39),e=c(58);a.exports=c(21).getIterator=function(a){var b=e(a);if("function"!=typeof b)throw TypeError(a+" is not iterable!");return d(b.call(a))}},function(a,b,c){var d=c(59),e=c(29)("iterator"),f=c(49);a.exports=c(21).getIteratorMethod=function(a){if(void 0!=a)return a[e]||a["@@iterator"]||f[d(a)]}},function(a,b,c){var d=c(34),e=c(29)("toStringTag"),f="Arguments"==d(function(){return arguments}());a.exports=function(a){var b,c,g;return void 0===a?"Undefined":null===a?"Null":"string"==typeof(c=(b=Object(a))[e])?c:f?d(b):"Object"==(g=d(b))&&"function"==typeof b.callee?"Arguments":g}},function(a,b,c){a.exports={"default":c(61),__esModule:!0}},function(a,b,c){c(62),a.exports=c(21).Object.keys},function(a,b,c){var d=c(63);c(64)("keys",function(a){return function(b){return a(d(b))}})},function(a,b,c){var d=c(35);a.exports=function(a){return Object(d(a))}},function(a,b,c){var d=c(20),e=c(21),f=c(19);a.exports=function(a,b){var c=(e.Object||{})[a]||Object[a],g={};g[a]=b(c),d(d.S+d.F*f(function(){c(1)}),"Object",g)}},function(a,b,c){"use strict";var d=c(1)["default"];b.__esModule=!0;var e=c(6),f=d(e);b["default"]=function(a){a.registerHelper("helperMissing",function(){if(1!==arguments.length)throw new f["default"]('Missing helper: "'+arguments[arguments.length-1].name+'"')})},a.exports=b["default"]},function(a,b,c){"use strict";var d=c(1)["default"];b.__esModule=!0;var e=c(5),f=c(6),g=d(f);b["default"]=function(a){a.registerHelper("if",function(a,b){if(2!=arguments.length)throw new g["default"]("#if requires exactly one argument");return e.isFunction(a)&&(a=a.call(this)),!b.hash.includeZero&&!a||e.isEmpty(a)?b.inverse(this):b.fn(this)}),a.registerHelper("unless",function(b,c){if(2!=arguments.length)throw new g["default"]("#unless requires exactly one argument");return a.helpers["if"].call(this,b,{fn:c.inverse,inverse:c.fn,hash:c.hash})})},a.exports=b["default"]},function(a,b){"use strict";b.__esModule=!0,b["default"]=function(a){a.registerHelper("log",function(){for(var b=[void 0],c=arguments[arguments.length-1],d=0;d<arguments.length-1;d++)b.push(arguments[d]);var e=1;null!=c.hash.level?e=c.hash.level:c.data&&null!=c.data.level&&(e=c.data.level),b[0]=e,a.log.apply(a,b)})},a.exports=b["default"]},function(a,b){"use strict";b.__esModule=!0,b["default"]=function(a){a.registerHelper("lookup",function(a,b,c){return a?c.lookupProperty(a,b):a})},a.exports=b["default"]},function(a,b,c){"use strict";var d=c(1)["default"];b.__esModule=!0;var e=c(5),f=c(6),g=d(f);b["default"]=function(a){a.registerHelper("with",function(a,b){if(2!=arguments.length)throw new g["default"]("#with requires exactly one argument");e.isFunction(a)&&(a=a.call(this));var c=b.fn;if(e.isEmpty(a))return b.inverse(this);var d=b.data;return b.data&&b.ids&&(d=e.createFrame(b.data),d.contextPath=e.appendContextPath(b.data.contextPath,b.ids[0])),c(a,{data:d,blockParams:e.blockParams([a],[d&&d.contextPath])})})},a.exports=b["default"]},function(a,b,c){"use strict";function d(a){g["default"](a)}var e=c(1)["default"];b.__esModule=!0,b.registerDefaultDecorators=d;var f=c(71),g=e(f)},function(a,b,c){"use strict";b.__esModule=!0;var d=c(5);b["default"]=function(a){a.registerDecorator("inline",function(a,b,c,e){var f=a;return b.partials||(b.partials={},f=function(e,f){var g=c.partials;c.partials=d.extend({},g,b.partials);var h=a(e,f);return c.partials=g,h}),b.partials[e.args[0]]=e.fn,f})},a.exports=b["default"]},function(a,b,c){"use strict";b.__esModule=!0;var d=c(5),e={methodMap:["debug","info","warn","error"],level:"info",lookupLevel:function(a){if("string"==typeof a){var b=d.indexOf(e.methodMap,a.toLowerCase());a=b>=0?b:parseInt(a,10)}return a},log:function(a){if(a=e.lookupLevel(a),"undefined"!=typeof console&&e.lookupLevel(e.level)<=a){var b=e.methodMap[a];console[b]||(b="log");for(var c=arguments.length,d=Array(c>1?c-1:0),f=1;f<c;f++)d[f-1]=arguments[f];console[b].apply(console,d)}}};b["default"]=e,a.exports=b["default"]},function(a,b,c){"use strict";function d(a){var b=i(null);b.constructor=!1,b.__defineGetter__=!1,b.__defineSetter__=!1,b.__lookupGetter__=!1;var c=i(null);return c.__proto__=!1,{properties:{whitelist:l.createNewLookupObject(c,a.allowedProtoProperties),defaultValue:a.allowProtoPropertiesByDefault},methods:{whitelist:l.createNewLookupObject(b,a.allowedProtoMethods),defaultValue:a.allowProtoMethodsByDefault}}}function e(a,b,c){return"function"==typeof a?f(b.methods,c):f(b.properties,c)}function f(a,b){return void 0!==a.whitelist[b]?a.whitelist[b]===!0:void 0!==a.defaultValue?a.defaultValue:(g(b),!1)}function g(a){o[a]!==!0&&(o[a]=!0,n["default"].log("error",'Handlebars: Access has been denied to resolve the property "'+a+'" because it is not an "own property" of its parent.\nYou can add a runtime option to disable the check or this warning:\nSee https://handlebarsjs.com/api-reference/runtime-options.html#options-to-control-prototype-access for details'))}function h(){j(o).forEach(function(a){delete o[a]})}var i=c(74)["default"],j=c(60)["default"],k=c(1)["default"];b.__esModule=!0,b.createProtoAccessControl=d,b.resultIsAllowed=e,b.resetLoggedProperties=h;var l=c(76),m=c(72),n=k(m),o=i(null)},function(a,b,c){a.exports={"default":c(75),__esModule:!0}},function(a,b,c){var d=c(9);a.exports=function(a,b){return d.create(a,b)}},function(a,b,c){"use strict";function d(){for(var a=arguments.length,b=Array(a),c=0;c<a;c++)b[c]=arguments[c];return f.extend.apply(void 0,[e(null)].concat(b))}var e=c(74)["default"];b.__esModule=!0,b.createNewLookupObject=d;var f=c(5)},function(a,b){"use strict";function c(a){this.string=a}b.__esModule=!0,c.prototype.toString=c.prototype.toHTML=function(){return""+this.string},b["default"]=c,a.exports=b["default"]},function(a,b,c){"use strict";function d(a){var b=a&&a[0]||1,c=v.COMPILER_REVISION;if(!(b>=v.LAST_COMPATIBLE_COMPILER_REVISION&&b<=v.COMPILER_REVISION)){if(b<v.LAST_COMPATIBLE_COMPILER_REVISION){var d=v.REVISION_CHANGES[c],e=v.REVISION_CHANGES[b];throw new u["default"]("Template was precompiled with an older version of Handlebars than the current runtime. Please update your precompiler to a newer version ("+d+") or downgrade your runtime to an older version ("+e+").")}throw new u["default"]("Template was precompiled with a newer version of Handlebars than the current runtime. Please update your runtime to a newer version ("+a[1]+").")}}function e(a,b){function c(c,d,e){e.hash&&(d=s.extend({},d,e.hash),e.ids&&(e.ids[0]=!0)),c=b.VM.resolvePartial.call(this,c,d,e);var f=s.extend({},e,{hooks:this.hooks,protoAccessControl:this.protoAccessControl}),g=b.VM.invokePartial.call(this,c,d,f);if(null==g&&b.compile&&(e.partials[e.name]=b.compile(c,a.compilerOptions,b),g=e.partials[e.name](d,f)),null!=g){if(e.indent){for(var h=g.split("\n"),i=0,j=h.length;i<j&&(h[i]||i+1!==j);i++)h[i]=e.indent+h[i];g=h.join("\n")}return g}throw new u["default"]("The partial "+e.name+" could not be compiled when running in runtime-only mode")}function d(b){function c(b){return""+a.main(g,b,g.helpers,g.partials,f,i,h)}var e=arguments.length<=1||void 0===arguments[1]?{}:arguments[1],f=e.data;d._setup(e),!e.partial&&a.useData&&(f=j(b,f));var h=void 0,i=a.useBlockParams?[]:void 0;return a.useDepths&&(h=e.depths?b!=e.depths[0]?[b].concat(e.depths):e.depths:[b]),(c=k(a.main,c,g,e.depths||[],f,i))(b,e)}if(!b)throw new u["default"]("No environment passed to template");if(!a||!a.main)throw new u["default"]("Unknown template object: "+typeof a);a.main.decorator=a.main_d,b.VM.checkRevision(a.compiler);var e=a.compiler&&7===a.compiler[0],g={strict:function(a,b,c){if(!(a&&b in a))throw new u["default"]('"'+b+'" not defined in '+a,{loc:c});return g.lookupProperty(a,b)},lookupProperty:function(a,b){var c=a[b];return null==c?c:Object.prototype.hasOwnProperty.call(a,b)?c:y.resultIsAllowed(c,g.protoAccessControl,b)?c:void 0},lookup:function(a,b){for(var c=a.length,d=0;d<c;d++){var e=a[d]&&g.lookupProperty(a[d],b);if(null!=e)return a[d][b]}},lambda:function(a,b){return"function"==typeof a?a.call(b):a},escapeExpression:s.escapeExpression,invokePartial:c,fn:function(b){var c=a[b];return c.decorator=a[b+"_d"],c},programs:[],program:function(a,b,c,d,e){var g=this.programs[a],h=this.fn(a);return b||e||d||c?g=f(this,a,h,b,c,d,e):g||(g=this.programs[a]=f(this,a,h)),g},data:function(a,b){for(;a&&b--;)a=a._parent;return a},mergeIfNeeded:function(a,b){var c=a||b;return a&&b&&a!==b&&(c=s.extend({},b,a)),c},nullContext:n({}),noop:b.VM.noop,compilerInfo:a.compiler};return d.isTop=!0,d._setup=function(c){if(c.partial)g.protoAccessControl=c.protoAccessControl,g.helpers=c.helpers,g.partials=c.partials,g.decorators=c.decorators,g.hooks=c.hooks;else{var d=s.extend({},b.helpers,c.helpers);l(d,g),g.helpers=d,a.usePartial&&(g.partials=g.mergeIfNeeded(c.partials,b.partials)),(a.usePartial||a.useDecorators)&&(g.decorators=s.extend({},b.decorators,c.decorators)),g.hooks={},g.protoAccessControl=y.createProtoAccessControl(c);var f=c.allowCallsToHelperMissing||e;w.moveHelperToHooks(g,"helperMissing",f),w.moveHelperToHooks(g,"blockHelperMissing",f)}},d._child=function(b,c,d,e){if(a.useBlockParams&&!d)throw new u["default"]("must pass block params");if(a.useDepths&&!e)throw new u["default"]("must pass parent depths");return f(g,b,a[b],c,0,d,e)},d}function f(a,b,c,d,e,f,g){function h(b){var e=arguments.length<=1||void 0===arguments[1]?{}:arguments[1],h=g;return!g||b==g[0]||b===a.nullContext&&null===g[0]||(h=[b].concat(g)),c(a,b,a.helpers,a.partials,e.data||d,f&&[e.blockParams].concat(f),h)}return h=k(c,h,a,g,d,f),h.program=b,h.depth=g?g.length:0,h.blockParams=e||0,h}function g(a,b,c){return a?a.call||c.name||(c.name=a,a=c.partials[a]):a="@partial-block"===c.name?c.data["partial-block"]:c.partials[c.name],a}function h(a,b,c){var d=c.data&&c.data["partial-block"];c.partial=!0,c.ids&&(c.data.contextPath=c.ids[0]||c.data.contextPath);var e=void 0;if(c.fn&&c.fn!==i&&!function(){c.data=v.createFrame(c.data);var a=c.fn;e=c.data["partial-block"]=function(b){var c=arguments.length<=1||void 0===arguments[1]?{}:arguments[1];return c.data=v.createFrame(c.data),c.data["partial-block"]=d,a(b,c)},a.partials&&(c.partials=s.extend({},c.partials,a.partials))}(),void 0===a&&e&&(a=e),void 0===a)throw new u["default"]("The partial "+c.name+" could not be found");if(a instanceof Function)return a(b,c)}function i(){return""}function j(a,b){return b&&"root"in b||(b=b?v.createFrame(b):{},b.root=a),b}function k(a,b,c,d,e,f){if(a.decorator){var g={};b=a.decorator(b,g,c,d&&d[0],e,f,d),s.extend(b,g)}return b}function l(a,b){o(a).forEach(function(c){var d=a[c];a[c]=m(d,b)})}function m(a,b){var c=b.lookupProperty;return x.wrapHelper(a,function(a){return s.extend({lookupProperty:c},a)})}var n=c(79)["default"],o=c(60)["default"],p=c(3)["default"],q=c(1)["default"];b.__esModule=!0,b.checkRevision=d,b.template=e,b.wrapProgram=f,b.resolvePartial=g,b.invokePartial=h,b.noop=i;var r=c(5),s=p(r),t=c(6),u=q(t),v=c(4),w=c(10),x=c(82),y=c(73)},function(a,b,c){a.exports={"default":c(80),__esModule:!0}},function(a,b,c){c(81),a.exports=c(21).Object.seal},function(a,b,c){var d=c(40);c(64)("seal",function(a){return function(b){return a&&d(b)?a(b):b}})},function(a,b){"use strict";function c(a,b){if("function"!=typeof a)return a;var c=function(){var c=arguments[arguments.length-1];return arguments[arguments.length-1]=b(c),a.apply(this,arguments)};return c}b.__esModule=!0,b.wrapHelper=c},function(a,b){"use strict";b.__esModule=!0,b["default"]=function(a){!function(){"object"!=typeof globalThis&&(Object.prototype.__defineGetter__("__magic__",function(){return this}),__magic__.globalThis=__magic__,delete Object.prototype.__magic__)}();var b=globalThis.Handlebars;a.noConflict=function(){return globalThis.Handlebars===a&&(globalThis.Handlebars=b),a}},a.exports=b["default"]},function(a,b){"use strict";b.__esModule=!0;var c={helpers:{helperExpression:function(a){return"SubExpression"===a.type||("MustacheStatement"===a.type||"BlockStatement"===a.type)&&!!(a.params&&a.params.length||a.hash)},scopedId:function(a){return/^\.|this\b/.test(a.original)},simpleId:function(a){return 1===a.parts.length&&!c.helpers.scopedId(a)&&!a.depth}}};b["default"]=c,a.exports=b["default"]},function(a,b,c){"use strict";function d(a,b){if("Program"===a.type)return a;i["default"].yy=o,o.locInfo=function(a){return new o.SourceLocation(b&&b.srcName,a)};var c=i["default"].parse(a);return c}function e(a,b){var c=d(a,b),e=new k["default"](b);return e.accept(c)}var f=c(1)["default"],g=c(3)["default"];b.__esModule=!0,b.parseWithoutProcessing=d,b.parse=e;var h=c(86),i=f(h),j=c(87),k=f(j),l=c(89),m=g(l),n=c(5);b.parser=i["default"];var o={};n.extend(o,m)},function(a,b){"use strict";b.__esModule=!0;var c=function(){function a(){this.yy={}}var b={trace:function(){},yy:{},symbols_:{error:2,root:3,program:4,EOF:5,program_repetition0:6,statement:7,mustache:8,block:9,rawBlock:10,partial:11,partialBlock:12,content:13,COMMENT:14,CONTENT:15,openRawBlock:16,rawBlock_repetition0:17,END_RAW_BLOCK:18,OPEN_RAW_BLOCK:19,helperName:20,openRawBlock_repetition0:21,openRawBlock_option0:22,CLOSE_RAW_BLOCK:23,openBlock:24,block_option0:25,closeBlock:26,openInverse:27,block_option1:28,OPEN_BLOCK:29,openBlock_repetition0:30,openBlock_option0:31,openBlock_option1:32,CLOSE:33,OPEN_INVERSE:34,openInverse_repetition0:35,openInverse_option0:36,openInverse_option1:37,openInverseChain:38,OPEN_INVERSE_CHAIN:39,openInverseChain_repetition0:40,openInverseChain_option0:41,openInverseChain_option1:42,inverseAndProgram:43,INVERSE:44,inverseChain:45,inverseChain_option0:46,OPEN_ENDBLOCK:47,OPEN:48,mustache_repetition0:49,mustache_option0:50,OPEN_UNESCAPED:51,mustache_repetition1:52,mustache_option1:53,CLOSE_UNESCAPED:54,OPEN_PARTIAL:55,partialName:56,partial_repetition0:57,partial_option0:58,openPartialBlock:59,OPEN_PARTIAL_BLOCK:60,openPartialBlock_repetition0:61,openPartialBlock_option0:62,param:63,sexpr:64,OPEN_SEXPR:65,sexpr_repetition0:66,sexpr_option0:67,CLOSE_SEXPR:68,hash:69,hash_repetition_plus0:70,hashSegment:71,ID:72,EQUALS:73,blockParams:74,OPEN_BLOCK_PARAMS:75,blockParams_repetition_plus0:76,CLOSE_BLOCK_PARAMS:77,path:78,dataName:79,STRING:80,NUMBER:81,BOOLEAN:82,UNDEFINED:83,NULL:84,DATA:85,pathSegments:86,SEP:87,$accept:0,$end:1},terminals_:{2:"error",5:"EOF",14:"COMMENT",15:"CONTENT",18:"END_RAW_BLOCK",19:"OPEN_RAW_BLOCK",23:"CLOSE_RAW_BLOCK",29:"OPEN_BLOCK",33:"CLOSE",34:"OPEN_INVERSE",39:"OPEN_INVERSE_CHAIN",44:"INVERSE",47:"OPEN_ENDBLOCK",48:"OPEN",51:"OPEN_UNESCAPED",54:"CLOSE_UNESCAPED",55:"OPEN_PARTIAL",60:"OPEN_PARTIAL_BLOCK",65:"OPEN_SEXPR",68:"CLOSE_SEXPR",72:"ID",73:"EQUALS",75:"OPEN_BLOCK_PARAMS",77:"CLOSE_BLOCK_PARAMS",80:"STRING",81:"NUMBER",82:"BOOLEAN",83:"UNDEFINED",84:"NULL",85:"DATA",87:"SEP"},productions_:[0,[3,2],[4,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[13,1],[10,3],[16,5],[9,4],[9,4],[24,6],[27,6],[38,6],[43,2],[45,3],[45,1],[26,3],[8,5],[8,5],[11,5],[12,3],[59,5],[63,1],[63,1],[64,5],[69,1],[71,3],[74,3],[20,1],[20,1],[20,1],[20,1],[20,1],[20,1],[20,1],[56,1],[56,1],[79,2],[78,1],[86,3],[86,1],[6,0],[6,2],[17,0],[17,2],[21,0],[21,2],[22,0],[22,1],[25,0],[25,1],[28,0],[28,1],[30,0],[30,2],[31,0],[31,1],[32,0],[32,1],[35,0],[35,2],[36,0],[36,1],[37,0],[37,1],[40,0],[40,2],[41,0],[41,1],[42,0],[42,1],[46,0],[46,1],[49,0],[49,2],[50,0],[50,1],[52,0],[52,2],[53,0],[53,1],[57,0],[57,2],[58,0],[58,1],[61,0],[61,2],[62,0],[62,1],[66,0],[66,2],[67,0],[67,1],[70,1],[70,2],[76,1],[76,2]],performAction:function(a,b,c,d,e,f,g){
var h=f.length-1;switch(e){case 1:return f[h-1];case 2:this.$=d.prepareProgram(f[h]);break;case 3:this.$=f[h];break;case 4:this.$=f[h];break;case 5:this.$=f[h];break;case 6:this.$=f[h];break;case 7:this.$=f[h];break;case 8:this.$=f[h];break;case 9:this.$={type:"CommentStatement",value:d.stripComment(f[h]),strip:d.stripFlags(f[h],f[h]),loc:d.locInfo(this._$)};break;case 10:this.$={type:"ContentStatement",original:f[h],value:f[h],loc:d.locInfo(this._$)};break;case 11:this.$=d.prepareRawBlock(f[h-2],f[h-1],f[h],this._$);break;case 12:this.$={path:f[h-3],params:f[h-2],hash:f[h-1]};break;case 13:this.$=d.prepareBlock(f[h-3],f[h-2],f[h-1],f[h],!1,this._$);break;case 14:this.$=d.prepareBlock(f[h-3],f[h-2],f[h-1],f[h],!0,this._$);break;case 15:this.$={open:f[h-5],path:f[h-4],params:f[h-3],hash:f[h-2],blockParams:f[h-1],strip:d.stripFlags(f[h-5],f[h])};break;case 16:this.$={path:f[h-4],params:f[h-3],hash:f[h-2],blockParams:f[h-1],strip:d.stripFlags(f[h-5],f[h])};break;case 17:this.$={path:f[h-4],params:f[h-3],hash:f[h-2],blockParams:f[h-1],strip:d.stripFlags(f[h-5],f[h])};break;case 18:this.$={strip:d.stripFlags(f[h-1],f[h-1]),program:f[h]};break;case 19:var i=d.prepareBlock(f[h-2],f[h-1],f[h],f[h],!1,this._$),j=d.prepareProgram([i],f[h-1].loc);j.chained=!0,this.$={strip:f[h-2].strip,program:j,chain:!0};break;case 20:this.$=f[h];break;case 21:this.$={path:f[h-1],strip:d.stripFlags(f[h-2],f[h])};break;case 22:this.$=d.prepareMustache(f[h-3],f[h-2],f[h-1],f[h-4],d.stripFlags(f[h-4],f[h]),this._$);break;case 23:this.$=d.prepareMustache(f[h-3],f[h-2],f[h-1],f[h-4],d.stripFlags(f[h-4],f[h]),this._$);break;case 24:this.$={type:"PartialStatement",name:f[h-3],params:f[h-2],hash:f[h-1],indent:"",strip:d.stripFlags(f[h-4],f[h]),loc:d.locInfo(this._$)};break;case 25:this.$=d.preparePartialBlock(f[h-2],f[h-1],f[h],this._$);break;case 26:this.$={path:f[h-3],params:f[h-2],hash:f[h-1],strip:d.stripFlags(f[h-4],f[h])};break;case 27:this.$=f[h];break;case 28:this.$=f[h];break;case 29:this.$={type:"SubExpression",path:f[h-3],params:f[h-2],hash:f[h-1],loc:d.locInfo(this._$)};break;case 30:this.$={type:"Hash",pairs:f[h],loc:d.locInfo(this._$)};break;case 31:this.$={type:"HashPair",key:d.id(f[h-2]),value:f[h],loc:d.locInfo(this._$)};break;case 32:this.$=d.id(f[h-1]);break;case 33:this.$=f[h];break;case 34:this.$=f[h];break;case 35:this.$={type:"StringLiteral",value:f[h],original:f[h],loc:d.locInfo(this._$)};break;case 36:this.$={type:"NumberLiteral",value:Number(f[h]),original:Number(f[h]),loc:d.locInfo(this._$)};break;case 37:this.$={type:"BooleanLiteral",value:"true"===f[h],original:"true"===f[h],loc:d.locInfo(this._$)};break;case 38:this.$={type:"UndefinedLiteral",original:void 0,value:void 0,loc:d.locInfo(this._$)};break;case 39:this.$={type:"NullLiteral",original:null,value:null,loc:d.locInfo(this._$)};break;case 40:this.$=f[h];break;case 41:this.$=f[h];break;case 42:this.$=d.preparePath(!0,f[h],this._$);break;case 43:this.$=d.preparePath(!1,f[h],this._$);break;case 44:f[h-2].push({part:d.id(f[h]),original:f[h],separator:f[h-1]}),this.$=f[h-2];break;case 45:this.$=[{part:d.id(f[h]),original:f[h]}];break;case 46:this.$=[];break;case 47:f[h-1].push(f[h]);break;case 48:this.$=[];break;case 49:f[h-1].push(f[h]);break;case 50:this.$=[];break;case 51:f[h-1].push(f[h]);break;case 58:this.$=[];break;case 59:f[h-1].push(f[h]);break;case 64:this.$=[];break;case 65:f[h-1].push(f[h]);break;case 70:this.$=[];break;case 71:f[h-1].push(f[h]);break;case 78:this.$=[];break;case 79:f[h-1].push(f[h]);break;case 82:this.$=[];break;case 83:f[h-1].push(f[h]);break;case 86:this.$=[];break;case 87:f[h-1].push(f[h]);break;case 90:this.$=[];break;case 91:f[h-1].push(f[h]);break;case 94:this.$=[];break;case 95:f[h-1].push(f[h]);break;case 98:this.$=[f[h]];break;case 99:f[h-1].push(f[h]);break;case 100:this.$=[f[h]];break;case 101:f[h-1].push(f[h])}},table:[{3:1,4:2,5:[2,46],6:3,14:[2,46],15:[2,46],19:[2,46],29:[2,46],34:[2,46],48:[2,46],51:[2,46],55:[2,46],60:[2,46]},{1:[3]},{5:[1,4]},{5:[2,2],7:5,8:6,9:7,10:8,11:9,12:10,13:11,14:[1,12],15:[1,20],16:17,19:[1,23],24:15,27:16,29:[1,21],34:[1,22],39:[2,2],44:[2,2],47:[2,2],48:[1,13],51:[1,14],55:[1,18],59:19,60:[1,24]},{1:[2,1]},{5:[2,47],14:[2,47],15:[2,47],19:[2,47],29:[2,47],34:[2,47],39:[2,47],44:[2,47],47:[2,47],48:[2,47],51:[2,47],55:[2,47],60:[2,47]},{5:[2,3],14:[2,3],15:[2,3],19:[2,3],29:[2,3],34:[2,3],39:[2,3],44:[2,3],47:[2,3],48:[2,3],51:[2,3],55:[2,3],60:[2,3]},{5:[2,4],14:[2,4],15:[2,4],19:[2,4],29:[2,4],34:[2,4],39:[2,4],44:[2,4],47:[2,4],48:[2,4],51:[2,4],55:[2,4],60:[2,4]},{5:[2,5],14:[2,5],15:[2,5],19:[2,5],29:[2,5],34:[2,5],39:[2,5],44:[2,5],47:[2,5],48:[2,5],51:[2,5],55:[2,5],60:[2,5]},{5:[2,6],14:[2,6],15:[2,6],19:[2,6],29:[2,6],34:[2,6],39:[2,6],44:[2,6],47:[2,6],48:[2,6],51:[2,6],55:[2,6],60:[2,6]},{5:[2,7],14:[2,7],15:[2,7],19:[2,7],29:[2,7],34:[2,7],39:[2,7],44:[2,7],47:[2,7],48:[2,7],51:[2,7],55:[2,7],60:[2,7]},{5:[2,8],14:[2,8],15:[2,8],19:[2,8],29:[2,8],34:[2,8],39:[2,8],44:[2,8],47:[2,8],48:[2,8],51:[2,8],55:[2,8],60:[2,8]},{5:[2,9],14:[2,9],15:[2,9],19:[2,9],29:[2,9],34:[2,9],39:[2,9],44:[2,9],47:[2,9],48:[2,9],51:[2,9],55:[2,9],60:[2,9]},{20:25,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:36,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{4:37,6:3,14:[2,46],15:[2,46],19:[2,46],29:[2,46],34:[2,46],39:[2,46],44:[2,46],47:[2,46],48:[2,46],51:[2,46],55:[2,46],60:[2,46]},{4:38,6:3,14:[2,46],15:[2,46],19:[2,46],29:[2,46],34:[2,46],44:[2,46],47:[2,46],48:[2,46],51:[2,46],55:[2,46],60:[2,46]},{15:[2,48],17:39,18:[2,48]},{20:41,56:40,64:42,65:[1,43],72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{4:44,6:3,14:[2,46],15:[2,46],19:[2,46],29:[2,46],34:[2,46],47:[2,46],48:[2,46],51:[2,46],55:[2,46],60:[2,46]},{5:[2,10],14:[2,10],15:[2,10],18:[2,10],19:[2,10],29:[2,10],34:[2,10],39:[2,10],44:[2,10],47:[2,10],48:[2,10],51:[2,10],55:[2,10],60:[2,10]},{20:45,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:46,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:47,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:41,56:48,64:42,65:[1,43],72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{33:[2,78],49:49,65:[2,78],72:[2,78],80:[2,78],81:[2,78],82:[2,78],83:[2,78],84:[2,78],85:[2,78]},{23:[2,33],33:[2,33],54:[2,33],65:[2,33],68:[2,33],72:[2,33],75:[2,33],80:[2,33],81:[2,33],82:[2,33],83:[2,33],84:[2,33],85:[2,33]},{23:[2,34],33:[2,34],54:[2,34],65:[2,34],68:[2,34],72:[2,34],75:[2,34],80:[2,34],81:[2,34],82:[2,34],83:[2,34],84:[2,34],85:[2,34]},{23:[2,35],33:[2,35],54:[2,35],65:[2,35],68:[2,35],72:[2,35],75:[2,35],80:[2,35],81:[2,35],82:[2,35],83:[2,35],84:[2,35],85:[2,35]},{23:[2,36],33:[2,36],54:[2,36],65:[2,36],68:[2,36],72:[2,36],75:[2,36],80:[2,36],81:[2,36],82:[2,36],83:[2,36],84:[2,36],85:[2,36]},{23:[2,37],33:[2,37],54:[2,37],65:[2,37],68:[2,37],72:[2,37],75:[2,37],80:[2,37],81:[2,37],82:[2,37],83:[2,37],84:[2,37],85:[2,37]},{23:[2,38],33:[2,38],54:[2,38],65:[2,38],68:[2,38],72:[2,38],75:[2,38],80:[2,38],81:[2,38],82:[2,38],83:[2,38],84:[2,38],85:[2,38]},{23:[2,39],33:[2,39],54:[2,39],65:[2,39],68:[2,39],72:[2,39],75:[2,39],80:[2,39],81:[2,39],82:[2,39],83:[2,39],84:[2,39],85:[2,39]},{23:[2,43],33:[2,43],54:[2,43],65:[2,43],68:[2,43],72:[2,43],75:[2,43],80:[2,43],81:[2,43],82:[2,43],83:[2,43],84:[2,43],85:[2,43],87:[1,50]},{72:[1,35],86:51},{23:[2,45],33:[2,45],54:[2,45],65:[2,45],68:[2,45],72:[2,45],75:[2,45],80:[2,45],81:[2,45],82:[2,45],83:[2,45],84:[2,45],85:[2,45],87:[2,45]},{52:52,54:[2,82],65:[2,82],72:[2,82],80:[2,82],81:[2,82],82:[2,82],83:[2,82],84:[2,82],85:[2,82]},{25:53,38:55,39:[1,57],43:56,44:[1,58],45:54,47:[2,54]},{28:59,43:60,44:[1,58],47:[2,56]},{13:62,15:[1,20],18:[1,61]},{33:[2,86],57:63,65:[2,86],72:[2,86],80:[2,86],81:[2,86],82:[2,86],83:[2,86],84:[2,86],85:[2,86]},{33:[2,40],65:[2,40],72:[2,40],80:[2,40],81:[2,40],82:[2,40],83:[2,40],84:[2,40],85:[2,40]},{33:[2,41],65:[2,41],72:[2,41],80:[2,41],81:[2,41],82:[2,41],83:[2,41],84:[2,41],85:[2,41]},{20:64,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{26:65,47:[1,66]},{30:67,33:[2,58],65:[2,58],72:[2,58],75:[2,58],80:[2,58],81:[2,58],82:[2,58],83:[2,58],84:[2,58],85:[2,58]},{33:[2,64],35:68,65:[2,64],72:[2,64],75:[2,64],80:[2,64],81:[2,64],82:[2,64],83:[2,64],84:[2,64],85:[2,64]},{21:69,23:[2,50],65:[2,50],72:[2,50],80:[2,50],81:[2,50],82:[2,50],83:[2,50],84:[2,50],85:[2,50]},{33:[2,90],61:70,65:[2,90],72:[2,90],80:[2,90],81:[2,90],82:[2,90],83:[2,90],84:[2,90],85:[2,90]},{20:74,33:[2,80],50:71,63:72,64:75,65:[1,43],69:73,70:76,71:77,72:[1,78],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{72:[1,79]},{23:[2,42],33:[2,42],54:[2,42],65:[2,42],68:[2,42],72:[2,42],75:[2,42],80:[2,42],81:[2,42],82:[2,42],83:[2,42],84:[2,42],85:[2,42],87:[1,50]},{20:74,53:80,54:[2,84],63:81,64:75,65:[1,43],69:82,70:76,71:77,72:[1,78],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{26:83,47:[1,66]},{47:[2,55]},{4:84,6:3,14:[2,46],15:[2,46],19:[2,46],29:[2,46],34:[2,46],39:[2,46],44:[2,46],47:[2,46],48:[2,46],51:[2,46],55:[2,46],60:[2,46]},{47:[2,20]},{20:85,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{4:86,6:3,14:[2,46],15:[2,46],19:[2,46],29:[2,46],34:[2,46],47:[2,46],48:[2,46],51:[2,46],55:[2,46],60:[2,46]},{26:87,47:[1,66]},{47:[2,57]},{5:[2,11],14:[2,11],15:[2,11],19:[2,11],29:[2,11],34:[2,11],39:[2,11],44:[2,11],47:[2,11],48:[2,11],51:[2,11],55:[2,11],60:[2,11]},{15:[2,49],18:[2,49]},{20:74,33:[2,88],58:88,63:89,64:75,65:[1,43],69:90,70:76,71:77,72:[1,78],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{65:[2,94],66:91,68:[2,94],72:[2,94],80:[2,94],81:[2,94],82:[2,94],83:[2,94],84:[2,94],85:[2,94]},{5:[2,25],14:[2,25],15:[2,25],19:[2,25],29:[2,25],34:[2,25],39:[2,25],44:[2,25],47:[2,25],48:[2,25],51:[2,25],55:[2,25],60:[2,25]},{20:92,72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:74,31:93,33:[2,60],63:94,64:75,65:[1,43],69:95,70:76,71:77,72:[1,78],75:[2,60],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:74,33:[2,66],36:96,63:97,64:75,65:[1,43],69:98,70:76,71:77,72:[1,78],75:[2,66],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:74,22:99,23:[2,52],63:100,64:75,65:[1,43],69:101,70:76,71:77,72:[1,78],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{20:74,33:[2,92],62:102,63:103,64:75,65:[1,43],69:104,70:76,71:77,72:[1,78],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{33:[1,105]},{33:[2,79],65:[2,79],72:[2,79],80:[2,79],81:[2,79],82:[2,79],83:[2,79],84:[2,79],85:[2,79]},{33:[2,81]},{23:[2,27],33:[2,27],54:[2,27],65:[2,27],68:[2,27],72:[2,27],75:[2,27],80:[2,27],81:[2,27],82:[2,27],83:[2,27],84:[2,27],85:[2,27]},{23:[2,28],33:[2,28],54:[2,28],65:[2,28],68:[2,28],72:[2,28],75:[2,28],80:[2,28],81:[2,28],82:[2,28],83:[2,28],84:[2,28],85:[2,28]},{23:[2,30],33:[2,30],54:[2,30],68:[2,30],71:106,72:[1,107],75:[2,30]},{23:[2,98],33:[2,98],54:[2,98],68:[2,98],72:[2,98],75:[2,98]},{23:[2,45],33:[2,45],54:[2,45],65:[2,45],68:[2,45],72:[2,45],73:[1,108],75:[2,45],80:[2,45],81:[2,45],82:[2,45],83:[2,45],84:[2,45],85:[2,45],87:[2,45]},{23:[2,44],33:[2,44],54:[2,44],65:[2,44],68:[2,44],72:[2,44],75:[2,44],80:[2,44],81:[2,44],82:[2,44],83:[2,44],84:[2,44],85:[2,44],87:[2,44]},{54:[1,109]},{54:[2,83],65:[2,83],72:[2,83],80:[2,83],81:[2,83],82:[2,83],83:[2,83],84:[2,83],85:[2,83]},{54:[2,85]},{5:[2,13],14:[2,13],15:[2,13],19:[2,13],29:[2,13],34:[2,13],39:[2,13],44:[2,13],47:[2,13],48:[2,13],51:[2,13],55:[2,13],60:[2,13]},{38:55,39:[1,57],43:56,44:[1,58],45:111,46:110,47:[2,76]},{33:[2,70],40:112,65:[2,70],72:[2,70],75:[2,70],80:[2,70],81:[2,70],82:[2,70],83:[2,70],84:[2,70],85:[2,70]},{47:[2,18]},{5:[2,14],14:[2,14],15:[2,14],19:[2,14],29:[2,14],34:[2,14],39:[2,14],44:[2,14],47:[2,14],48:[2,14],51:[2,14],55:[2,14],60:[2,14]},{33:[1,113]},{33:[2,87],65:[2,87],72:[2,87],80:[2,87],81:[2,87],82:[2,87],83:[2,87],84:[2,87],85:[2,87]},{33:[2,89]},{20:74,63:115,64:75,65:[1,43],67:114,68:[2,96],69:116,70:76,71:77,72:[1,78],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{33:[1,117]},{32:118,33:[2,62],74:119,75:[1,120]},{33:[2,59],65:[2,59],72:[2,59],75:[2,59],80:[2,59],81:[2,59],82:[2,59],83:[2,59],84:[2,59],85:[2,59]},{33:[2,61],75:[2,61]},{33:[2,68],37:121,74:122,75:[1,120]},{33:[2,65],65:[2,65],72:[2,65],75:[2,65],80:[2,65],81:[2,65],82:[2,65],83:[2,65],84:[2,65],85:[2,65]},{33:[2,67],75:[2,67]},{23:[1,123]},{23:[2,51],65:[2,51],72:[2,51],80:[2,51],81:[2,51],82:[2,51],83:[2,51],84:[2,51],85:[2,51]},{23:[2,53]},{33:[1,124]},{33:[2,91],65:[2,91],72:[2,91],80:[2,91],81:[2,91],82:[2,91],83:[2,91],84:[2,91],85:[2,91]},{33:[2,93]},{5:[2,22],14:[2,22],15:[2,22],19:[2,22],29:[2,22],34:[2,22],39:[2,22],44:[2,22],47:[2,22],48:[2,22],51:[2,22],55:[2,22],60:[2,22]},{23:[2,99],33:[2,99],54:[2,99],68:[2,99],72:[2,99],75:[2,99]},{73:[1,108]},{20:74,63:125,64:75,65:[1,43],72:[1,35],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{5:[2,23],14:[2,23],15:[2,23],19:[2,23],29:[2,23],34:[2,23],39:[2,23],44:[2,23],47:[2,23],48:[2,23],51:[2,23],55:[2,23],60:[2,23]},{47:[2,19]},{47:[2,77]},{20:74,33:[2,72],41:126,63:127,64:75,65:[1,43],69:128,70:76,71:77,72:[1,78],75:[2,72],78:26,79:27,80:[1,28],81:[1,29],82:[1,30],83:[1,31],84:[1,32],85:[1,34],86:33},{5:[2,24],14:[2,24],15:[2,24],19:[2,24],29:[2,24],34:[2,24],39:[2,24],44:[2,24],47:[2,24],48:[2,24],51:[2,24],55:[2,24],60:[2,24]},{68:[1,129]},{65:[2,95],68:[2,95],72:[2,95],80:[2,95],81:[2,95],82:[2,95],83:[2,95],84:[2,95],85:[2,95]},{68:[2,97]},{5:[2,21],14:[2,21],15:[2,21],19:[2,21],29:[2,21],34:[2,21],39:[2,21],44:[2,21],47:[2,21],48:[2,21],51:[2,21],55:[2,21],60:[2,21]},{33:[1,130]},{33:[2,63]},{72:[1,132],76:131},{33:[1,133]},{33:[2,69]},{15:[2,12],18:[2,12]},{14:[2,26],15:[2,26],19:[2,26],29:[2,26],34:[2,26],47:[2,26],48:[2,26],51:[2,26],55:[2,26],60:[2,26]},{23:[2,31],33:[2,31],54:[2,31],68:[2,31],72:[2,31],75:[2,31]},{33:[2,74],42:134,74:135,75:[1,120]},{33:[2,71],65:[2,71],72:[2,71],75:[2,71],80:[2,71],81:[2,71],82:[2,71],83:[2,71],84:[2,71],85:[2,71]},{33:[2,73],75:[2,73]},{23:[2,29],33:[2,29],54:[2,29],65:[2,29],68:[2,29],72:[2,29],75:[2,29],80:[2,29],81:[2,29],82:[2,29],83:[2,29],84:[2,29],85:[2,29]},{14:[2,15],15:[2,15],19:[2,15],29:[2,15],34:[2,15],39:[2,15],44:[2,15],47:[2,15],48:[2,15],51:[2,15],55:[2,15],60:[2,15]},{72:[1,137],77:[1,136]},{72:[2,100],77:[2,100]},{14:[2,16],15:[2,16],19:[2,16],29:[2,16],34:[2,16],44:[2,16],47:[2,16],48:[2,16],51:[2,16],55:[2,16],60:[2,16]},{33:[1,138]},{33:[2,75]},{33:[2,32]},{72:[2,101],77:[2,101]},{14:[2,17],15:[2,17],19:[2,17],29:[2,17],34:[2,17],39:[2,17],44:[2,17],47:[2,17],48:[2,17],51:[2,17],55:[2,17],60:[2,17]}],defaultActions:{4:[2,1],54:[2,55],56:[2,20],60:[2,57],73:[2,81],82:[2,85],86:[2,18],90:[2,89],101:[2,53],104:[2,93],110:[2,19],111:[2,77],116:[2,97],119:[2,63],122:[2,69],135:[2,75],136:[2,32]},parseError:function(a,b){throw new Error(a)},parse:function(a){function b(){var a;return a=c.lexer.lex()||1,"number"!=typeof a&&(a=c.symbols_[a]||a),a}var c=this,d=[0],e=[null],f=[],g=this.table,h="",i=0,j=0,k=0;this.lexer.setInput(a),this.lexer.yy=this.yy,this.yy.lexer=this.lexer,this.yy.parser=this,"undefined"==typeof this.lexer.yylloc&&(this.lexer.yylloc={});var l=this.lexer.yylloc;f.push(l);var m=this.lexer.options&&this.lexer.options.ranges;"function"==typeof this.yy.parseError&&(this.parseError=this.yy.parseError);for(var n,o,p,q,r,s,t,u,v,w={};;){if(p=d[d.length-1],this.defaultActions[p]?q=this.defaultActions[p]:(null!==n&&"undefined"!=typeof n||(n=b()),q=g[p]&&g[p][n]),"undefined"==typeof q||!q.length||!q[0]){var x="";if(!k){v=[];for(s in g[p])this.terminals_[s]&&s>2&&v.push("'"+this.terminals_[s]+"'");x=this.lexer.showPosition?"Parse error on line "+(i+1)+":\n"+this.lexer.showPosition()+"\nExpecting "+v.join(", ")+", got '"+(this.terminals_[n]||n)+"'":"Parse error on line "+(i+1)+": Unexpected "+(1==n?"end of input":"'"+(this.terminals_[n]||n)+"'"),this.parseError(x,{text:this.lexer.match,token:this.terminals_[n]||n,line:this.lexer.yylineno,loc:l,expected:v})}}if(q[0]instanceof Array&&q.length>1)throw new Error("Parse Error: multiple actions possible at state: "+p+", token: "+n);switch(q[0]){case 1:d.push(n),e.push(this.lexer.yytext),f.push(this.lexer.yylloc),d.push(q[1]),n=null,o?(n=o,o=null):(j=this.lexer.yyleng,h=this.lexer.yytext,i=this.lexer.yylineno,l=this.lexer.yylloc,k>0&&k--);break;case 2:if(t=this.productions_[q[1]][1],w.$=e[e.length-t],w._$={first_line:f[f.length-(t||1)].first_line,last_line:f[f.length-1].last_line,first_column:f[f.length-(t||1)].first_column,last_column:f[f.length-1].last_column},m&&(w._$.range=[f[f.length-(t||1)].range[0],f[f.length-1].range[1]]),r=this.performAction.call(w,h,j,i,this.yy,q[1],e,f),"undefined"!=typeof r)return r;t&&(d=d.slice(0,-1*t*2),e=e.slice(0,-1*t),f=f.slice(0,-1*t)),d.push(this.productions_[q[1]][0]),e.push(w.$),f.push(w._$),u=g[d[d.length-2]][d[d.length-1]],d.push(u);break;case 3:return!0}}return!0}},c=function(){var a={EOF:1,parseError:function(a,b){if(!this.yy.parser)throw new Error(a);this.yy.parser.parseError(a,b)},setInput:function(a){return this._input=a,this._more=this._less=this.done=!1,this.yylineno=this.yyleng=0,this.yytext=this.matched=this.match="",this.conditionStack=["INITIAL"],this.yylloc={first_line:1,first_column:0,last_line:1,last_column:0},this.options.ranges&&(this.yylloc.range=[0,0]),this.offset=0,this},input:function(){var a=this._input[0];this.yytext+=a,this.yyleng++,this.offset++,this.match+=a,this.matched+=a;var b=a.match(/(?:\r\n?|\n).*/g);return b?(this.yylineno++,this.yylloc.last_line++):this.yylloc.last_column++,this.options.ranges&&this.yylloc.range[1]++,this._input=this._input.slice(1),a},unput:function(a){var b=a.length,c=a.split(/(?:\r\n?|\n)/g);this._input=a+this._input,this.yytext=this.yytext.substr(0,this.yytext.length-b-1),this.offset-=b;var d=this.match.split(/(?:\r\n?|\n)/g);this.match=this.match.substr(0,this.match.length-1),this.matched=this.matched.substr(0,this.matched.length-1),c.length-1&&(this.yylineno-=c.length-1);var e=this.yylloc.range;return this.yylloc={first_line:this.yylloc.first_line,last_line:this.yylineno+1,first_column:this.yylloc.first_column,last_column:c?(c.length===d.length?this.yylloc.first_column:0)+d[d.length-c.length].length-c[0].length:this.yylloc.first_column-b},this.options.ranges&&(this.yylloc.range=[e[0],e[0]+this.yyleng-b]),this},more:function(){return this._more=!0,this},less:function(a){this.unput(this.match.slice(a))},pastInput:function(){var a=this.matched.substr(0,this.matched.length-this.match.length);return(a.length>20?"...":"")+a.substr(-20).replace(/\n/g,"")},upcomingInput:function(){var a=this.match;return a.length<20&&(a+=this._input.substr(0,20-a.length)),(a.substr(0,20)+(a.length>20?"...":"")).replace(/\n/g,"")},showPosition:function(){var a=this.pastInput(),b=new Array(a.length+1).join("-");return a+this.upcomingInput()+"\n"+b+"^"},next:function(){if(this.done)return this.EOF;this._input||(this.done=!0);var a,b,c,d,e;this._more||(this.yytext="",this.match="");for(var f=this._currentRules(),g=0;g<f.length&&(c=this._input.match(this.rules[f[g]]),!c||b&&!(c[0].length>b[0].length)||(b=c,d=g,this.options.flex));g++);return b?(e=b[0].match(/(?:\r\n?|\n).*/g),e&&(this.yylineno+=e.length),this.yylloc={first_line:this.yylloc.last_line,last_line:this.yylineno+1,first_column:this.yylloc.last_column,last_column:e?e[e.length-1].length-e[e.length-1].match(/\r?\n?/)[0].length:this.yylloc.last_column+b[0].length},this.yytext+=b[0],this.match+=b[0],this.matches=b,this.yyleng=this.yytext.length,this.options.ranges&&(this.yylloc.range=[this.offset,this.offset+=this.yyleng]),this._more=!1,this._input=this._input.slice(b[0].length),this.matched+=b[0],a=this.performAction.call(this,this.yy,this,f[d],this.conditionStack[this.conditionStack.length-1]),this.done&&this._input&&(this.done=!1),a?a:void 0):""===this._input?this.EOF:this.parseError("Lexical error on line "+(this.yylineno+1)+". Unrecognized text.\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})},lex:function(){var a=this.next();return"undefined"!=typeof a?a:this.lex()},begin:function(a){this.conditionStack.push(a)},popState:function(){return this.conditionStack.pop()},_currentRules:function(){return this.conditions[this.conditionStack[this.conditionStack.length-1]].rules},topState:function(){return this.conditionStack[this.conditionStack.length-2]},pushState:function(a){this.begin(a)}};return a.options={},a.performAction=function(a,b,c,d){function e(a,c){return b.yytext=b.yytext.substring(a,b.yyleng-c+a)}switch(c){case 0:if("\\\\"===b.yytext.slice(-2)?(e(0,1),this.begin("mu")):"\\"===b.yytext.slice(-1)?(e(0,1),this.begin("emu")):this.begin("mu"),b.yytext)return 15;break;case 1:return 15;case 2:return this.popState(),15;case 3:return this.begin("raw"),15;case 4:return this.popState(),"raw"===this.conditionStack[this.conditionStack.length-1]?15:(e(5,9),"END_RAW_BLOCK");case 5:return 15;case 6:return this.popState(),14;case 7:return 65;case 8:return 68;case 9:return 19;case 10:return this.popState(),this.begin("raw"),23;case 11:return 55;case 12:return 60;case 13:return 29;case 14:return 47;case 15:return this.popState(),44;case 16:return this.popState(),44;case 17:return 34;case 18:return 39;case 19:return 51;case 20:return 48;case 21:this.unput(b.yytext),this.popState(),this.begin("com");break;case 22:return this.popState(),14;case 23:return 48;case 24:return 73;case 25:return 72;case 26:return 72;case 27:return 87;case 28:break;case 29:return this.popState(),54;case 30:return this.popState(),33;case 31:return b.yytext=e(1,2).replace(/\\"/g,'"'),80;case 32:return b.yytext=e(1,2).replace(/\\'/g,"'"),80;case 33:return 85;case 34:return 82;case 35:return 82;case 36:return 83;case 37:return 84;case 38:return 81;case 39:return 75;case 40:return 77;case 41:return 72;case 42:return b.yytext=b.yytext.replace(/\\([\\\]])/g,"$1"),72;case 43:return"INVALID";case 44:return 5}},a.rules=[/^(?:[^\x00]*?(?=(\{\{)))/,/^(?:[^\x00]+)/,/^(?:[^\x00]{2,}?(?=(\{\{|\\\{\{|\\\\\{\{|$)))/,/^(?:\{\{\{\{(?=[^/]))/,/^(?:\{\{\{\{\/[^\s!"#%-,\.\/;->@\[-\^`\{-~]+(?=[=}\s\/.])\}\}\}\})/,/^(?:[^\x00]+?(?=(\{\{\{\{)))/,/^(?:[\s\S]*?--(~)?\}\})/,/^(?:\()/,/^(?:\))/,/^(?:\{\{\{\{)/,/^(?:\}\}\}\})/,/^(?:\{\{(~)?>)/,/^(?:\{\{(~)?#>)/,/^(?:\{\{(~)?#\*?)/,/^(?:\{\{(~)?\/)/,/^(?:\{\{(~)?\^\s*(~)?\}\})/,/^(?:\{\{(~)?\s*else\s*(~)?\}\})/,/^(?:\{\{(~)?\^)/,/^(?:\{\{(~)?\s*else\b)/,/^(?:\{\{(~)?\{)/,/^(?:\{\{(~)?&)/,/^(?:\{\{(~)?!--)/,/^(?:\{\{(~)?![\s\S]*?\}\})/,/^(?:\{\{(~)?\*?)/,/^(?:=)/,/^(?:\.\.)/,/^(?:\.(?=([=~}\s\/.)|])))/,/^(?:[\/.])/,/^(?:\s+)/,/^(?:\}(~)?\}\})/,/^(?:(~)?\}\})/,/^(?:"(\\["]|[^"])*")/,/^(?:'(\\[']|[^'])*')/,/^(?:@)/,/^(?:true(?=([~}\s)])))/,/^(?:false(?=([~}\s)])))/,/^(?:undefined(?=([~}\s)])))/,/^(?:null(?=([~}\s)])))/,/^(?:-?[0-9]+(?:\.[0-9]+)?(?=([~}\s)])))/,/^(?:as\s+\|)/,/^(?:\|)/,/^(?:([^\s!"#%-,\.\/;->@\[-\^`\{-~]+(?=([=~}\s\/.)|]))))/,/^(?:\[(\\\]|[^\]])*\])/,/^(?:.)/,/^(?:$)/],a.conditions={mu:{rules:[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44],inclusive:!1},emu:{rules:[2],inclusive:!1},com:{rules:[6],inclusive:!1},raw:{rules:[3,4,5],inclusive:!1},INITIAL:{rules:[0,1,44],inclusive:!0}},a}();return b.lexer=c,a.prototype=b,b.Parser=a,new a}();b["default"]=c,a.exports=b["default"]},function(a,b,c){"use strict";function d(){var a=arguments.length<=0||void 0===arguments[0]?{}:arguments[0];this.options=a}function e(a,b,c){void 0===b&&(b=a.length);var d=a[b-1],e=a[b-2];return d?"ContentStatement"===d.type?(e||!c?/\r?\n\s*?$/:/(^|\r?\n)\s*?$/).test(d.original):void 0:c}function f(a,b,c){void 0===b&&(b=-1);var d=a[b+1],e=a[b+2];return d?"ContentStatement"===d.type?(e||!c?/^\s*?\r?\n/:/^\s*?(\r?\n|$)/).test(d.original):void 0:c}function g(a,b,c){var d=a[null==b?0:b+1];if(d&&"ContentStatement"===d.type&&(c||!d.rightStripped)){var e=d.value;d.value=d.value.replace(c?/^\s+/:/^[ \t]*\r?\n?/,""),d.rightStripped=d.value!==e}}function h(a,b,c){var d=a[null==b?a.length-1:b-1];if(d&&"ContentStatement"===d.type&&(c||!d.leftStripped)){var e=d.value;return d.value=d.value.replace(c?/\s+$/:/[ \t]+$/,""),d.leftStripped=d.value!==e,d.leftStripped}}var i=c(1)["default"];b.__esModule=!0;var j=c(88),k=i(j);d.prototype=new k["default"],d.prototype.Program=function(a){var b=!this.options.ignoreStandalone,c=!this.isRootSeen;this.isRootSeen=!0;for(var d=a.body,i=0,j=d.length;i<j;i++){var k=d[i],l=this.accept(k);if(l){var m=e(d,i,c),n=f(d,i,c),o=l.openStandalone&&m,p=l.closeStandalone&&n,q=l.inlineStandalone&&m&&n;l.close&&g(d,i,!0),l.open&&h(d,i,!0),b&&q&&(g(d,i),h(d,i)&&"PartialStatement"===k.type&&(k.indent=/([ \t]+$)/.exec(d[i-1].original)[1])),b&&o&&(g((k.program||k.inverse).body),h(d,i)),b&&p&&(g(d,i),h((k.inverse||k.program).body))}}return a},d.prototype.BlockStatement=d.prototype.DecoratorBlock=d.prototype.PartialBlockStatement=function(a){this.accept(a.program),this.accept(a.inverse);var b=a.program||a.inverse,c=a.program&&a.inverse,d=c,i=c;if(c&&c.chained)for(d=c.body[0].program;i.chained;)i=i.body[i.body.length-1].program;var j={open:a.openStrip.open,close:a.closeStrip.close,openStandalone:f(b.body),closeStandalone:e((d||b).body)};if(a.openStrip.close&&g(b.body,null,!0),c){var k=a.inverseStrip;k.open&&h(b.body,null,!0),k.close&&g(d.body,null,!0),a.closeStrip.open&&h(i.body,null,!0),!this.options.ignoreStandalone&&e(b.body)&&f(d.body)&&(h(b.body),g(d.body))}else a.closeStrip.open&&h(b.body,null,!0);return j},d.prototype.Decorator=d.prototype.MustacheStatement=function(a){return a.strip},d.prototype.PartialStatement=d.prototype.CommentStatement=function(a){var b=a.strip||{};return{inlineStandalone:!0,open:b.open,close:b.close}},b["default"]=d,a.exports=b["default"]},function(a,b,c){"use strict";function d(){this.parents=[]}function e(a){this.acceptRequired(a,"path"),this.acceptArray(a.params),this.acceptKey(a,"hash")}function f(a){e.call(this,a),this.acceptKey(a,"program"),this.acceptKey(a,"inverse")}function g(a){this.acceptRequired(a,"name"),this.acceptArray(a.params),this.acceptKey(a,"hash")}var h=c(1)["default"];b.__esModule=!0;var i=c(6),j=h(i);d.prototype={constructor:d,mutating:!1,acceptKey:function(a,b){var c=this.accept(a[b]);if(this.mutating){if(c&&!d.prototype[c.type])throw new j["default"]('Unexpected node type "'+c.type+'" found when accepting '+b+" on "+a.type);a[b]=c}},acceptRequired:function(a,b){if(this.acceptKey(a,b),!a[b])throw new j["default"](a.type+" requires "+b)},acceptArray:function(a){for(var b=0,c=a.length;b<c;b++)this.acceptKey(a,b),a[b]||(a.splice(b,1),b--,c--)},accept:function(a){if(a){if(!this[a.type])throw new j["default"]("Unknown type: "+a.type,a);this.current&&this.parents.unshift(this.current),this.current=a;var b=this[a.type](a);return this.current=this.parents.shift(),!this.mutating||b?b:b!==!1?a:void 0}},Program:function(a){this.acceptArray(a.body)},MustacheStatement:e,Decorator:e,BlockStatement:f,DecoratorBlock:f,PartialStatement:g,PartialBlockStatement:function(a){g.call(this,a),this.acceptKey(a,"program")},ContentStatement:function(){},CommentStatement:function(){},SubExpression:e,PathExpression:function(){},StringLiteral:function(){},NumberLiteral:function(){},BooleanLiteral:function(){},UndefinedLiteral:function(){},NullLiteral:function(){},Hash:function(a){this.acceptArray(a.pairs)},HashPair:function(a){this.acceptRequired(a,"value")}},b["default"]=d,a.exports=b["default"]},function(a,b,c){"use strict";function d(a,b){if(b=b.path?b.path.original:b,a.path.original!==b){var c={loc:a.path.loc};throw new q["default"](a.path.original+" doesn't match "+b,c)}}function e(a,b){this.source=a,this.start={line:b.first_line,column:b.first_column},this.end={line:b.last_line,column:b.last_column}}function f(a){return/^\[.*\]$/.test(a)?a.substring(1,a.length-1):a}function g(a,b){return{open:"~"===a.charAt(2),close:"~"===b.charAt(b.length-3)}}function h(a){return a.replace(/^\{\{~?!-?-?/,"").replace(/-?-?~?\}\}$/,"")}function i(a,b,c){c=this.locInfo(c);for(var d=a?"@":"",e=[],f=0,g=0,h=b.length;g<h;g++){var i=b[g].part,j=b[g].original!==i;if(d+=(b[g].separator||"")+i,j||".."!==i&&"."!==i&&"this"!==i)e.push(i);else{if(e.length>0)throw new q["default"]("Invalid path: "+d,{loc:c});".."===i&&f++}}return{type:"PathExpression",data:a,depth:f,parts:e,original:d,loc:c}}function j(a,b,c,d,e,f){var g=d.charAt(3)||d.charAt(2),h="{"!==g&&"&"!==g,i=/\*/.test(d);return{type:i?"Decorator":"MustacheStatement",path:a,params:b,hash:c,escaped:h,strip:e,loc:this.locInfo(f)}}function k(a,b,c,e){d(a,c),e=this.locInfo(e);var f={type:"Program",body:b,strip:{},loc:e};return{type:"BlockStatement",path:a.path,params:a.params,hash:a.hash,program:f,openStrip:{},inverseStrip:{},closeStrip:{},loc:e}}function l(a,b,c,e,f,g){e&&e.path&&d(a,e);var h=/\*/.test(a.open);b.blockParams=a.blockParams;var i=void 0,j=void 0;if(c){if(h)throw new q["default"]("Unexpected inverse block on decorator",c);c.chain&&(c.program.body[0].closeStrip=e.strip),j=c.strip,i=c.program}return f&&(f=i,i=b,b=f),{type:h?"DecoratorBlock":"BlockStatement",path:a.path,params:a.params,hash:a.hash,program:b,inverse:i,openStrip:a.strip,inverseStrip:j,closeStrip:e&&e.strip,loc:this.locInfo(g)}}function m(a,b){if(!b&&a.length){var c=a[0].loc,d=a[a.length-1].loc;c&&d&&(b={source:c.source,start:{line:c.start.line,column:c.start.column},end:{line:d.end.line,column:d.end.column}})}return{type:"Program",body:a,strip:{},loc:b}}function n(a,b,c,e){return d(a,c),{type:"PartialBlockStatement",name:a.path,params:a.params,hash:a.hash,program:b,openStrip:a.strip,closeStrip:c&&c.strip,loc:this.locInfo(e)}}var o=c(1)["default"];b.__esModule=!0,b.SourceLocation=e,b.id=f,b.stripFlags=g,b.stripComment=h,b.preparePath=i,b.prepareMustache=j,b.prepareRawBlock=k,b.prepareBlock=l,b.prepareProgram=m,b.preparePartialBlock=n;var p=c(6),q=o(p)},function(a,b,c){"use strict";function d(){}function e(a,b,c){if(null==a||"string"!=typeof a&&"Program"!==a.type)throw new l["default"]("You must pass a string or Handlebars AST to Handlebars.precompile. You passed "+a);b=b||{},"data"in b||(b.data=!0),b.compat&&(b.useDepths=!0);var d=c.parse(a,b),e=(new c.Compiler).compile(d,b);return(new c.JavaScriptCompiler).compile(e,b)}function f(a,b,c){function d(){var d=c.parse(a,b),e=(new c.Compiler).compile(d,b),f=(new c.JavaScriptCompiler).compile(e,b,void 0,!0);return c.template(f)}function e(a,b){return f||(f=d()),f.call(this,a,b)}if(void 0===b&&(b={}),null==a||"string"!=typeof a&&"Program"!==a.type)throw new l["default"]("You must pass a string or Handlebars AST to Handlebars.compile. You passed "+a);b=m.extend({},b),"data"in b||(b.data=!0),b.compat&&(b.useDepths=!0);var f=void 0;return e._setup=function(a){return f||(f=d()),f._setup(a)},e._child=function(a,b,c,e){return f||(f=d()),f._child(a,b,c,e)},e}function g(a,b){if(a===b)return!0;if(m.isArray(a)&&m.isArray(b)&&a.length===b.length){for(var c=0;c<a.length;c++)if(!g(a[c],b[c]))return!1;return!0}}function h(a){if(!a.path.parts){var b=a.path;a.path={type:"PathExpression",data:!1,depth:0,parts:[b.original+""],original:b.original+"",loc:b.loc}}}var i=c(74)["default"],j=c(1)["default"];b.__esModule=!0,b.Compiler=d,b.precompile=e,b.compile=f;var k=c(6),l=j(k),m=c(5),n=c(84),o=j(n),p=[].slice;d.prototype={compiler:d,equals:function(a){var b=this.opcodes.length;if(a.opcodes.length!==b)return!1;for(var c=0;c<b;c++){var d=this.opcodes[c],e=a.opcodes[c];if(d.opcode!==e.opcode||!g(d.args,e.args))return!1}b=this.children.length;for(var c=0;c<b;c++)if(!this.children[c].equals(a.children[c]))return!1;
return!0},guid:0,compile:function(a,b){return this.sourceNode=[],this.opcodes=[],this.children=[],this.options=b,this.stringParams=b.stringParams,this.trackIds=b.trackIds,b.blockParams=b.blockParams||[],b.knownHelpers=m.extend(i(null),{helperMissing:!0,blockHelperMissing:!0,each:!0,"if":!0,unless:!0,"with":!0,log:!0,lookup:!0},b.knownHelpers),this.accept(a)},compileProgram:function(a){var b=new this.compiler,c=b.compile(a,this.options),d=this.guid++;return this.usePartial=this.usePartial||c.usePartial,this.children[d]=c,this.useDepths=this.useDepths||c.useDepths,d},accept:function(a){if(!this[a.type])throw new l["default"]("Unknown type: "+a.type,a);this.sourceNode.unshift(a);var b=this[a.type](a);return this.sourceNode.shift(),b},Program:function(a){this.options.blockParams.unshift(a.blockParams);for(var b=a.body,c=b.length,d=0;d<c;d++)this.accept(b[d]);return this.options.blockParams.shift(),this.isSimple=1===c,this.blockParams=a.blockParams?a.blockParams.length:0,this},BlockStatement:function(a){h(a);var b=a.program,c=a.inverse;b=b&&this.compileProgram(b),c=c&&this.compileProgram(c);var d=this.classifySexpr(a);"helper"===d?this.helperSexpr(a,b,c):"simple"===d?(this.simpleSexpr(a),this.opcode("pushProgram",b),this.opcode("pushProgram",c),this.opcode("emptyHash"),this.opcode("blockValue",a.path.original)):(this.ambiguousSexpr(a,b,c),this.opcode("pushProgram",b),this.opcode("pushProgram",c),this.opcode("emptyHash"),this.opcode("ambiguousBlockValue")),this.opcode("append")},DecoratorBlock:function(a){var b=a.program&&this.compileProgram(a.program),c=this.setupFullMustacheParams(a,b,void 0),d=a.path;this.useDecorators=!0,this.opcode("registerDecorator",c.length,d.original)},PartialStatement:function(a){this.usePartial=!0;var b=a.program;b&&(b=this.compileProgram(a.program));var c=a.params;if(c.length>1)throw new l["default"]("Unsupported number of partial arguments: "+c.length,a);c.length||(this.options.explicitPartialContext?this.opcode("pushLiteral","undefined"):c.push({type:"PathExpression",parts:[],depth:0}));var d=a.name.original,e="SubExpression"===a.name.type;e&&this.accept(a.name),this.setupFullMustacheParams(a,b,void 0,!0);var f=a.indent||"";this.options.preventIndent&&f&&(this.opcode("appendContent",f),f=""),this.opcode("invokePartial",e,d,f),this.opcode("append")},PartialBlockStatement:function(a){this.PartialStatement(a)},MustacheStatement:function(a){this.SubExpression(a),a.escaped&&!this.options.noEscape?this.opcode("appendEscaped"):this.opcode("append")},Decorator:function(a){this.DecoratorBlock(a)},ContentStatement:function(a){a.value&&this.opcode("appendContent",a.value)},CommentStatement:function(){},SubExpression:function(a){h(a);var b=this.classifySexpr(a);"simple"===b?this.simpleSexpr(a):"helper"===b?this.helperSexpr(a):this.ambiguousSexpr(a)},ambiguousSexpr:function(a,b,c){var d=a.path,e=d.parts[0],f=null!=b||null!=c;this.opcode("getContext",d.depth),this.opcode("pushProgram",b),this.opcode("pushProgram",c),d.strict=!0,this.accept(d),this.opcode("invokeAmbiguous",e,f)},simpleSexpr:function(a){var b=a.path;b.strict=!0,this.accept(b),this.opcode("resolvePossibleLambda")},helperSexpr:function(a,b,c){var d=this.setupFullMustacheParams(a,b,c),e=a.path,f=e.parts[0];if(this.options.knownHelpers[f])this.opcode("invokeKnownHelper",d.length,f);else{if(this.options.knownHelpersOnly)throw new l["default"]("You specified knownHelpersOnly, but used the unknown helper "+f,a);e.strict=!0,e.falsy=!0,this.accept(e),this.opcode("invokeHelper",d.length,e.original,o["default"].helpers.simpleId(e))}},PathExpression:function(a){this.addDepth(a.depth),this.opcode("getContext",a.depth);var b=a.parts[0],c=o["default"].helpers.scopedId(a),d=!a.depth&&!c&&this.blockParamIndex(b);d?this.opcode("lookupBlockParam",d,a.parts):b?a.data?(this.options.data=!0,this.opcode("lookupData",a.depth,a.parts,a.strict)):this.opcode("lookupOnContext",a.parts,a.falsy,a.strict,c):this.opcode("pushContext")},StringLiteral:function(a){this.opcode("pushString",a.value)},NumberLiteral:function(a){this.opcode("pushLiteral",a.value)},BooleanLiteral:function(a){this.opcode("pushLiteral",a.value)},UndefinedLiteral:function(){this.opcode("pushLiteral","undefined")},NullLiteral:function(){this.opcode("pushLiteral","null")},Hash:function(a){var b=a.pairs,c=0,d=b.length;for(this.opcode("pushHash");c<d;c++)this.pushParam(b[c].value);for(;c--;)this.opcode("assignToHash",b[c].key);this.opcode("popHash")},opcode:function(a){this.opcodes.push({opcode:a,args:p.call(arguments,1),loc:this.sourceNode[0].loc})},addDepth:function(a){a&&(this.useDepths=!0)},classifySexpr:function(a){var b=o["default"].helpers.simpleId(a.path),c=b&&!!this.blockParamIndex(a.path.parts[0]),d=!c&&o["default"].helpers.helperExpression(a),e=!c&&(d||b);if(e&&!d){var f=a.path.parts[0],g=this.options;g.knownHelpers[f]?d=!0:g.knownHelpersOnly&&(e=!1)}return d?"helper":e?"ambiguous":"simple"},pushParams:function(a){for(var b=0,c=a.length;b<c;b++)this.pushParam(a[b])},pushParam:function(a){var b=null!=a.value?a.value:a.original||"";if(this.stringParams)b.replace&&(b=b.replace(/^(\.?\.\/)*/g,"").replace(/\//g,".")),a.depth&&this.addDepth(a.depth),this.opcode("getContext",a.depth||0),this.opcode("pushStringParam",b,a.type),"SubExpression"===a.type&&this.accept(a);else{if(this.trackIds){var c=void 0;if(!a.parts||o["default"].helpers.scopedId(a)||a.depth||(c=this.blockParamIndex(a.parts[0])),c){var d=a.parts.slice(1).join(".");this.opcode("pushId","BlockParam",c,d)}else b=a.original||b,b.replace&&(b=b.replace(/^this(?:\.|$)/,"").replace(/^\.\//,"").replace(/^\.$/,"")),this.opcode("pushId",a.type,b)}this.accept(a)}},setupFullMustacheParams:function(a,b,c,d){var e=a.params;return this.pushParams(e),this.opcode("pushProgram",b),this.opcode("pushProgram",c),a.hash?this.accept(a.hash):this.opcode("emptyHash",d),e},blockParamIndex:function(a){for(var b=0,c=this.options.blockParams.length;b<c;b++){var d=this.options.blockParams[b],e=d&&m.indexOf(d,a);if(d&&e>=0)return[b,e]}}}},function(a,b,c){"use strict";function d(a){this.value=a}function e(){}function f(a,b,c,d,e){var f=b.popStack(),g=c.length;for(a&&g--;d<g;d++)f=b.nameLookup(f,c[d],e);return a?[b.aliasable("container.strict"),"(",f,", ",b.quotedString(c[d]),", ",JSON.stringify(b.source.currentLocation)," )"]:f}var g=c(60)["default"],h=c(1)["default"];b.__esModule=!0;var i=c(4),j=c(6),k=h(j),l=c(5),m=c(92),n=h(m);e.prototype={nameLookup:function(a,b){return this.internalNameLookup(a,b)},depthedLookup:function(a){return[this.aliasable("container.lookup"),"(depths, ",JSON.stringify(a),")"]},compilerInfo:function(){var a=i.COMPILER_REVISION,b=i.REVISION_CHANGES[a];return[a,b]},appendToBuffer:function(a,b,c){return l.isArray(a)||(a=[a]),a=this.source.wrap(a,b),this.environment.isSimple?["return ",a,";"]:c?["buffer += ",a,";"]:(a.appendToBuffer=!0,a)},initializeBuffer:function(){return this.quotedString("")},internalNameLookup:function(a,b){return this.lookupPropertyFunctionIsUsed=!0,["lookupProperty(",a,",",JSON.stringify(b),")"]},lookupPropertyFunctionIsUsed:!1,compile:function(a,b,c,d){this.environment=a,this.options=b,this.stringParams=this.options.stringParams,this.trackIds=this.options.trackIds,this.precompile=!d,this.name=this.environment.name,this.isChild=!!c,this.context=c||{decorators:[],programs:[],environments:[]},this.preamble(),this.stackSlot=0,this.stackVars=[],this.aliases={},this.registers={list:[]},this.hashes=[],this.compileStack=[],this.inlineStack=[],this.blockParams=[],this.compileChildren(a,b),this.useDepths=this.useDepths||a.useDepths||a.useDecorators||this.options.compat,this.useBlockParams=this.useBlockParams||a.useBlockParams;var e=a.opcodes,f=void 0,g=void 0,h=void 0,i=void 0;for(h=0,i=e.length;h<i;h++)f=e[h],this.source.currentLocation=f.loc,g=g||f.loc,this[f.opcode].apply(this,f.args);if(this.source.currentLocation=g,this.pushSource(""),this.stackSlot||this.inlineStack.length||this.compileStack.length)throw new k["default"]("Compile completed with content left on stack");this.decorators.isEmpty()?this.decorators=void 0:(this.useDecorators=!0,this.decorators.prepend(["var decorators = container.decorators, ",this.lookupPropertyFunctionVarDeclaration(),";\n"]),this.decorators.push("return fn;"),d?this.decorators=Function.apply(this,["fn","props","container","depth0","data","blockParams","depths",this.decorators.merge()]):(this.decorators.prepend("function(fn, props, container, depth0, data, blockParams, depths) {\n"),this.decorators.push("}\n"),this.decorators=this.decorators.merge()));var j=this.createFunctionContext(d);if(this.isChild)return j;var l={compiler:this.compilerInfo(),main:j};this.decorators&&(l.main_d=this.decorators,l.useDecorators=!0);var m=this.context,n=m.programs,o=m.decorators;for(h=0,i=n.length;h<i;h++)n[h]&&(l[h]=n[h],o[h]&&(l[h+"_d"]=o[h],l.useDecorators=!0));return this.environment.usePartial&&(l.usePartial=!0),this.options.data&&(l.useData=!0),this.useDepths&&(l.useDepths=!0),this.useBlockParams&&(l.useBlockParams=!0),this.options.compat&&(l.compat=!0),d?l.compilerOptions=this.options:(l.compiler=JSON.stringify(l.compiler),this.source.currentLocation={start:{line:1,column:0}},l=this.objectLiteral(l),b.srcName?(l=l.toStringWithSourceMap({file:b.destName}),l.map=l.map&&l.map.toString()):l=l.toString()),l},preamble:function(){this.lastContext=0,this.source=new n["default"](this.options.srcName),this.decorators=new n["default"](this.options.srcName)},createFunctionContext:function(a){var b=this,c="",d=this.stackVars.concat(this.registers.list);d.length>0&&(c+=", "+d.join(", "));var e=0;g(this.aliases).forEach(function(a){var d=b.aliases[a];d.children&&d.referenceCount>1&&(c+=", alias"+ ++e+"="+a,d.children[0]="alias"+e)}),this.lookupPropertyFunctionIsUsed&&(c+=", "+this.lookupPropertyFunctionVarDeclaration());var f=["container","depth0","helpers","partials","data"];(this.useBlockParams||this.useDepths)&&f.push("blockParams"),this.useDepths&&f.push("depths");var h=this.mergeSource(c);return a?(f.push(h),Function.apply(this,f)):this.source.wrap(["function(",f.join(","),") {\n  ",h,"}"])},mergeSource:function(a){var b=this.environment.isSimple,c=!this.forceBuffer,d=void 0,e=void 0,f=void 0,g=void 0;return this.source.each(function(a){a.appendToBuffer?(f?a.prepend("  + "):f=a,g=a):(f&&(e?f.prepend("buffer += "):d=!0,g.add(";"),f=g=void 0),e=!0,b||(c=!1))}),c?f?(f.prepend("return "),g.add(";")):e||this.source.push('return "";'):(a+=", buffer = "+(d?"":this.initializeBuffer()),f?(f.prepend("return buffer + "),g.add(";")):this.source.push("return buffer;")),a&&this.source.prepend("var "+a.substring(2)+(d?"":";\n")),this.source.merge()},lookupPropertyFunctionVarDeclaration:function(){return"\n      lookupProperty = container.lookupProperty || function(parent, propertyName) {\n        if (Object.prototype.hasOwnProperty.call(parent, propertyName)) {\n          return parent[propertyName];\n        }\n        return undefined\n    }\n    ".trim()},blockValue:function(a){var b=this.aliasable("container.hooks.blockHelperMissing"),c=[this.contextName(0)];this.setupHelperArgs(a,0,c);var d=this.popStack();c.splice(1,0,d),this.push(this.source.functionCall(b,"call",c))},ambiguousBlockValue:function(){var a=this.aliasable("container.hooks.blockHelperMissing"),b=[this.contextName(0)];this.setupHelperArgs("",0,b,!0),this.flushInline();var c=this.topStack();b.splice(1,0,c),this.pushSource(["if (!",this.lastHelper,") { ",c," = ",this.source.functionCall(a,"call",b),"}"])},appendContent:function(a){this.pendingContent?a=this.pendingContent+a:this.pendingLocation=this.source.currentLocation,this.pendingContent=a},append:function(){if(this.isInline())this.replaceStack(function(a){return[" != null ? ",a,' : ""']}),this.pushSource(this.appendToBuffer(this.popStack()));else{var a=this.popStack();this.pushSource(["if (",a," != null) { ",this.appendToBuffer(a,void 0,!0)," }"]),this.environment.isSimple&&this.pushSource(["else { ",this.appendToBuffer("''",void 0,!0)," }"])}},appendEscaped:function(){this.pushSource(this.appendToBuffer([this.aliasable("container.escapeExpression"),"(",this.popStack(),")"]))},getContext:function(a){this.lastContext=a},pushContext:function(){this.pushStackLiteral(this.contextName(this.lastContext))},lookupOnContext:function(a,b,c,d){var e=0;d||!this.options.compat||this.lastContext?this.pushContext():this.push(this.depthedLookup(a[e++])),this.resolvePath("context",a,e,b,c)},lookupBlockParam:function(a,b){this.useBlockParams=!0,this.push(["blockParams[",a[0],"][",a[1],"]"]),this.resolvePath("context",b,1)},lookupData:function(a,b,c){a?this.pushStackLiteral("container.data(data, "+a+")"):this.pushStackLiteral("data"),this.resolvePath("data",b,0,!0,c)},resolvePath:function(a,b,c,d,e){var g=this;if(this.options.strict||this.options.assumeObjects)return void this.push(f(this.options.strict&&e,this,b,c,a));for(var h=b.length;c<h;c++)this.replaceStack(function(e){var f=g.nameLookup(e,b[c],a);return d?[" && ",f]:[" != null ? ",f," : ",e]})},resolvePossibleLambda:function(){this.push([this.aliasable("container.lambda"),"(",this.popStack(),", ",this.contextName(0),")"])},pushStringParam:function(a,b){this.pushContext(),this.pushString(b),"SubExpression"!==b&&("string"==typeof a?this.pushString(a):this.pushStackLiteral(a))},emptyHash:function(a){this.trackIds&&this.push("{}"),this.stringParams&&(this.push("{}"),this.push("{}")),this.pushStackLiteral(a?"undefined":"{}")},pushHash:function(){this.hash&&this.hashes.push(this.hash),this.hash={values:{},types:[],contexts:[],ids:[]}},popHash:function(){var a=this.hash;this.hash=this.hashes.pop(),this.trackIds&&this.push(this.objectLiteral(a.ids)),this.stringParams&&(this.push(this.objectLiteral(a.contexts)),this.push(this.objectLiteral(a.types))),this.push(this.objectLiteral(a.values))},pushString:function(a){this.pushStackLiteral(this.quotedString(a))},pushLiteral:function(a){this.pushStackLiteral(a)},pushProgram:function(a){null!=a?this.pushStackLiteral(this.programExpression(a)):this.pushStackLiteral(null)},registerDecorator:function(a,b){var c=this.nameLookup("decorators",b,"decorator"),d=this.setupHelperArgs(b,a);this.decorators.push(["fn = ",this.decorators.functionCall(c,"",["fn","props","container",d])," || fn;"])},invokeHelper:function(a,b,c){var d=this.popStack(),e=this.setupHelper(a,b),f=[];c&&f.push(e.name),f.push(d),this.options.strict||f.push(this.aliasable("container.hooks.helperMissing"));var g=["(",this.itemsSeparatedBy(f,"||"),")"],h=this.source.functionCall(g,"call",e.callParams);this.push(h)},itemsSeparatedBy:function(a,b){var c=[];c.push(a[0]);for(var d=1;d<a.length;d++)c.push(b,a[d]);return c},invokeKnownHelper:function(a,b){var c=this.setupHelper(a,b);this.push(this.source.functionCall(c.name,"call",c.callParams))},invokeAmbiguous:function(a,b){this.useRegister("helper");var c=this.popStack();this.emptyHash();var d=this.setupHelper(0,a,b),e=this.lastHelper=this.nameLookup("helpers",a,"helper"),f=["(","(helper = ",e," || ",c,")"];this.options.strict||(f[0]="(helper = ",f.push(" != null ? helper : ",this.aliasable("container.hooks.helperMissing"))),this.push(["(",f,d.paramsInit?["),(",d.paramsInit]:[],"),","(typeof helper === ",this.aliasable('"function"')," ? ",this.source.functionCall("helper","call",d.callParams)," : helper))"])},invokePartial:function(a,b,c){var d=[],e=this.setupParams(b,1,d);a&&(b=this.popStack(),delete e.name),c&&(e.indent=JSON.stringify(c)),e.helpers="helpers",e.partials="partials",e.decorators="container.decorators",a?d.unshift(b):d.unshift(this.nameLookup("partials",b,"partial")),this.options.compat&&(e.depths="depths"),e=this.objectLiteral(e),d.push(e),this.push(this.source.functionCall("container.invokePartial","",d))},assignToHash:function(a){var b=this.popStack(),c=void 0,d=void 0,e=void 0;this.trackIds&&(e=this.popStack()),this.stringParams&&(d=this.popStack(),c=this.popStack());var f=this.hash;c&&(f.contexts[a]=c),d&&(f.types[a]=d),e&&(f.ids[a]=e),f.values[a]=b},pushId:function(a,b,c){"BlockParam"===a?this.pushStackLiteral("blockParams["+b[0]+"].path["+b[1]+"]"+(c?" + "+JSON.stringify("."+c):"")):"PathExpression"===a?this.pushString(b):"SubExpression"===a?this.pushStackLiteral("true"):this.pushStackLiteral("null")},compiler:e,compileChildren:function(a,b){for(var c=a.children,d=void 0,e=void 0,f=0,g=c.length;f<g;f++){d=c[f],e=new this.compiler;var h=this.matchExistingProgram(d);if(null==h){this.context.programs.push("");var i=this.context.programs.length;d.index=i,d.name="program"+i,this.context.programs[i]=e.compile(d,b,this.context,!this.precompile),this.context.decorators[i]=e.decorators,this.context.environments[i]=d,this.useDepths=this.useDepths||e.useDepths,this.useBlockParams=this.useBlockParams||e.useBlockParams,d.useDepths=this.useDepths,d.useBlockParams=this.useBlockParams}else d.index=h.index,d.name="program"+h.index,this.useDepths=this.useDepths||h.useDepths,this.useBlockParams=this.useBlockParams||h.useBlockParams}},matchExistingProgram:function(a){for(var b=0,c=this.context.environments.length;b<c;b++){var d=this.context.environments[b];if(d&&d.equals(a))return d}},programExpression:function(a){var b=this.environment.children[a],c=[b.index,"data",b.blockParams];return(this.useBlockParams||this.useDepths)&&c.push("blockParams"),this.useDepths&&c.push("depths"),"container.program("+c.join(", ")+")"},useRegister:function(a){this.registers[a]||(this.registers[a]=!0,this.registers.list.push(a))},push:function(a){return a instanceof d||(a=this.source.wrap(a)),this.inlineStack.push(a),a},pushStackLiteral:function(a){this.push(new d(a))},pushSource:function(a){this.pendingContent&&(this.source.push(this.appendToBuffer(this.source.quotedString(this.pendingContent),this.pendingLocation)),this.pendingContent=void 0),a&&this.source.push(a)},replaceStack:function(a){var b=["("],c=void 0,e=void 0,f=void 0;if(!this.isInline())throw new k["default"]("replaceStack on non-inline");var g=this.popStack(!0);if(g instanceof d)c=[g.value],b=["(",c],f=!0;else{e=!0;var h=this.incrStack();b=["((",this.push(h)," = ",g,")"],c=this.topStack()}var i=a.call(this,c);f||this.popStack(),e&&this.stackSlot--,this.push(b.concat(i,")"))},incrStack:function(){return this.stackSlot++,this.stackSlot>this.stackVars.length&&this.stackVars.push("stack"+this.stackSlot),this.topStackName()},topStackName:function(){return"stack"+this.stackSlot},flushInline:function(){var a=this.inlineStack;this.inlineStack=[];for(var b=0,c=a.length;b<c;b++){var e=a[b];if(e instanceof d)this.compileStack.push(e);else{var f=this.incrStack();this.pushSource([f," = ",e,";"]),this.compileStack.push(f)}}},isInline:function(){return this.inlineStack.length},popStack:function(a){var b=this.isInline(),c=(b?this.inlineStack:this.compileStack).pop();if(!a&&c instanceof d)return c.value;if(!b){if(!this.stackSlot)throw new k["default"]("Invalid stack pop");this.stackSlot--}return c},topStack:function(){var a=this.isInline()?this.inlineStack:this.compileStack,b=a[a.length-1];return b instanceof d?b.value:b},contextName:function(a){return this.useDepths&&a?"depths["+a+"]":"depth"+a},quotedString:function(a){return this.source.quotedString(a)},objectLiteral:function(a){return this.source.objectLiteral(a)},aliasable:function(a){var b=this.aliases[a];return b?(b.referenceCount++,b):(b=this.aliases[a]=this.source.wrap(a),b.aliasable=!0,b.referenceCount=1,b)},setupHelper:function(a,b,c){var d=[],e=this.setupHelperArgs(b,a,d,c),f=this.nameLookup("helpers",b,"helper"),g=this.aliasable(this.contextName(0)+" != null ? "+this.contextName(0)+" : (container.nullContext || {})");return{params:d,paramsInit:e,name:f,callParams:[g].concat(d)}},setupParams:function(a,b,c){var d={},e=[],f=[],g=[],h=!c,i=void 0;h&&(c=[]),d.name=this.quotedString(a),d.hash=this.popStack(),this.trackIds&&(d.hashIds=this.popStack()),this.stringParams&&(d.hashTypes=this.popStack(),d.hashContexts=this.popStack());var j=this.popStack(),k=this.popStack();(k||j)&&(d.fn=k||"container.noop",d.inverse=j||"container.noop");for(var l=b;l--;)i=this.popStack(),c[l]=i,this.trackIds&&(g[l]=this.popStack()),this.stringParams&&(f[l]=this.popStack(),e[l]=this.popStack());return h&&(d.args=this.source.generateArray(c)),this.trackIds&&(d.ids=this.source.generateArray(g)),this.stringParams&&(d.types=this.source.generateArray(f),d.contexts=this.source.generateArray(e)),this.options.data&&(d.data="data"),this.useBlockParams&&(d.blockParams="blockParams"),d},setupHelperArgs:function(a,b,c,d){var e=this.setupParams(a,b,c);return e.loc=JSON.stringify(this.source.currentLocation),e=this.objectLiteral(e),d?(this.useRegister("options"),c.push("options"),["options=",e]):c?(c.push(e),""):e}},function(){for(var a="break else new var case finally return void catch for switch while continue function this with default if throw delete in try do instanceof typeof abstract enum int short boolean export interface static byte extends long super char final native synchronized class float package throws const goto private transient debugger implements protected volatile double import public let yield await null true false".split(" "),b=e.RESERVED_WORDS={},c=0,d=a.length;c<d;c++)b[a[c]]=!0}(),e.isValidJavaScriptVariableName=function(a){return!e.RESERVED_WORDS[a]&&/^[a-zA-Z_$][0-9a-zA-Z_$]*$/.test(a)},b["default"]=e,a.exports=b["default"]},function(a,b,c){"use strict";function d(a,b,c){if(g.isArray(a)){for(var d=[],e=0,f=a.length;e<f;e++)d.push(b.wrap(a[e],c));return d}return"boolean"==typeof a||"number"==typeof a?a+"":a}function e(a){this.srcFile=a,this.source=[]}var f=c(60)["default"];b.__esModule=!0;var g=c(5),h=void 0;try{}catch(i){}h||(h=function(a,b,c,d){this.src="",d&&this.add(d)},h.prototype={add:function(a){g.isArray(a)&&(a=a.join("")),this.src+=a},prepend:function(a){g.isArray(a)&&(a=a.join("")),this.src=a+this.src},toStringWithSourceMap:function(){return{code:this.toString()}},toString:function(){return this.src}}),e.prototype={isEmpty:function(){return!this.source.length},prepend:function(a,b){this.source.unshift(this.wrap(a,b))},push:function(a,b){this.source.push(this.wrap(a,b))},merge:function(){var a=this.empty();return this.each(function(b){a.add(["  ",b,"\n"])}),a},each:function(a){for(var b=0,c=this.source.length;b<c;b++)a(this.source[b])},empty:function(){var a=this.currentLocation||{start:{}};return new h(a.start.line,a.start.column,this.srcFile)},wrap:function(a){var b=arguments.length<=1||void 0===arguments[1]?this.currentLocation||{start:{}}:arguments[1];return a instanceof h?a:(a=d(a,this,b),new h(b.start.line,b.start.column,this.srcFile,a))},functionCall:function(a,b,c){return c=this.generateList(c),this.wrap([a,b?"."+b+"(":"(",c,")"])},quotedString:function(a){return'"'+(a+"").replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n").replace(/\r/g,"\\r").replace(/\u2028/g,"\\u2028").replace(/\u2029/g,"\\u2029")+'"'},objectLiteral:function(a){var b=this,c=[];f(a).forEach(function(e){var f=d(a[e],b);"undefined"!==f&&c.push([b.quotedString(e),":",f])});var e=this.generateList(c);return e.prepend("{"),e.add("}"),e},generateList:function(a){for(var b=this.empty(),c=0,e=a.length;c<e;c++)c&&b.add(","),b.add(d(a[c],this));return b},generateArray:function(a){var b=this.generateList(a);return b.prepend("["),b.add("]"),b}},b["default"]=e,a.exports=b["default"]}])});
!function(e){var t={};function n(r){if(t[r])return t[r].exports;var i=t[r]={i:r,l:!1,exports:{}};return e[r].call(i.exports,i,i.exports,n),i.l=!0,i.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var i in e)n.d(r,i,function(t){return e[t]}.bind(null,i));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="build/",n(n.s=14)}([function(e,t,n){"use strict";n.d(t,"a",(function(){return r})),n.d(t,"b",(function(){return i})),n.d(t,"e",(function(){return o})),n.d(t,"d",(function(){return s})),n.d(t,"c",(function(){return a})),n.d(t,"f",(function(){return d})),n.d(t,"g",(function(){return l})),n.d(t,"h",(function(){return c}));const r="mobile",i="small",o=()=>window.matchMedia("(orientation: portrait)").matches?window.screen.width<=667?r:"desktop":window.screen.height<=667?r:"desktop",s=()=>window.innerWidth<=667?i:"large",a=(e,t,n)=>{var r=new XMLHttpRequest;r.onreadystatechange=function(){var i;4!=this.readyState||200!=this.status&&204!=this.status?4!=this.readyState||200==this.status&&204==this.status||n("Invalid network request: "+e):(t&&(i=this.getResponseHeader("x-request-id")),n(null,r.responseText,i))},r.onerror=function(){n("Failed network request: "+e)},r.open("GET",e,!0),t&&r.setRequestHeader("unbxd-device-type",window.unbxdDeviceType),r.send()},d=function(e){const t=document.createElement("style");t.type="text/css",t.appendChild(document.createTextNode(e)),document.head.appendChild(t)},l=function(e,t){const n=document.createElement("script");e&&"//"!==e&&"/**/"!==e?(n.type="text/javascript",n.text="try{"+e+"}catch(e){console.log(e)}"):t&&(n.src=t),document.body.appendChild(n)},c={horizontal:{containerId:" #_unbxd_recs-slider-container",sliderItemClassSelector:"_unbxd_recs-slider__item",dimension:"width",offsetDimension:"offsetWidth",buttonClassSelector:"._unbxd_recs-slider-btn",prevButtonClass:"_unbxd_rex-slider--prev",nextButtonClass:"_unbxd_rex-slider--next",headingContainerId:" #_unbxd_recs-slider-heading",sliderContentClass:"_unbxd_recs-slider__content",RegexExp:/hz-item/,container:".unbxd-recs-slider",customNavClass:"_unbxd_rex_custom_nav"},vertical:{containerId:" #_unbxd_recs-vertical-slider-container",sliderItemClassSelector:"_unbxd_recs-vertical-slider__item",dimension:"height",offsetDimension:"offsetHeight",buttonClassSelector:"._unbxd_recs-vertical-slider-btn",prevButtonClass:"_unbxd_rex-vertical-slider--top",nextButtonClass:"_unbxd_rex-vertical-slider--bottom",headingContainerId:" #_unbxd_recs-vertical-slider-heading",sliderContentClass:"_unbxd_recs-vertical-slider__content",RegexExp:/[0-9]-vt-level2-/,container:"._unbxd_vertical-recs-slider",customNavClass:"_unbxd_rex_custom_nav"},boutique:{containerId:".unbxd-recs-boutique-wrapper",sliderItemClassSelector:"_unbxd_recs-boutique__item",headingContainerId:" #_unbxd_boutique-heading",dimension:"width",sliderContentClass:"_unbxd_recs-boutique-item__content",RegexExp:/boutique-item/,container:".unbxd-recs-boutique-wrapper",customNavClass:"_unbxd_rex_custom_nav"},boutique_standard:{containerId:".unbxd-recs-boutique-wrapper",sliderItemClassSelector:"_unbxd_recs-boutique__item",headingContainerId:" #_unbxd_boutique-heading",dimension:"width",sliderContentClass:"_unbxd_recs-boutique-item__content",RegexExp:/boutique-item/,container:".unbxd-recs-boutique-wrapper",customNavClass:"_unbxd_rex_custom_nav"},boutique_tinder:{containerId:".recs-boutique-tinder-widget-wrapper",sliderItemClassSelector:"_unbxd_recs-boutique-tinder__item",headingContainerId:" #_unbxd_recs-boutique-tinder-heading",dimension:"width",sliderContentClass:"_unbxd_recs-boutique-item__content",RegexExp:/boutique-item/,container:".recs-boutique-tinder-widget-wrapper",customNavClass:"_unbxd_rex_custom_nav"},boutique_instagram:{containerId:".unbxd-recs-boutique-insta-widget-wrapper",sliderItemClassSelector:"_unbxd_recs-boutique__item",headingContainerId:" #_unbxd_recs-boutique-insta-heading",dimension:"width",sliderContentClass:"_unbxd_recs-boutique-item__content",RegexExp:/boutique-item/,container:".unbxd-recs-boutique-insta-widget-wrapper",customNavClass:"_unbxd_rex_custom_nav"}}},function(e,t,n){"use strict";n.d(t,"a",(function(){return r})),n.d(t,"c",(function(){return a})),n.d(t,"d",(function(){return d})),n.d(t,"b",(function(){return i}));var r={_unbxd_recsSliderSideScroll:function(e,t){var n=0,r="#"+e+" #_unbxd_recs-slider-container",i=document.querySelector(r);if(!i)return console.warn("slider container id is missing. Execution can not continue");var o="#"+e+" ._unbxd_recs-slider__item",s=document.querySelector(o);if(!s)return console.warn("slider item tile class is missing. Execution can not continue");var a=document.querySelector("#_unbxd_recs-slider"),d=window._unbxd_recsItemToScrollHz,l=30+5*d,c=s.clientWidth*d+10*d,u=setInterval((function(){if("left"==t){let e=n+l;e>c&&(l-=e-c),i.scrollLeft-=l}else{let e=n+l;e>c&&(l-=e-c),i.scrollLeft+=l}if((n+=l)>=c&&window.clearInterval(u),0===i.scrollLeft){var e=document.querySelector(r+" ._unbxd_rex-slider--prev");if(!e)return console.warn("_unbxd_rex-slider--prev class missing");e.disabled=!0}if(i.scrollLeft+i.clientWidth===a.clientWidth){var o=document.querySelector(r+" ._unbxd_rex-slider--next");if(!o)return console.warn("_unbxd_rex-slider--next class missing");o.disabled=!0}}),25)},_unbxd_recsSliderScrollNext:function(e){var t;try{t=e.currentTarget.parentElement.parentElement.parentElement}catch(e){console.warn(e)}if(t){var n=t.id,r="#"+n+" ._unbxd_rex-slider--prev",i=document.querySelector(r);if(!i)return console.warn("_unbxd_rex-slider--prev class missing");i.disabled&&(i.disabled=!1),_unbxd_recsSliderSideScroll(n,"right")}else console.warn("target element not found. HTML was changed")},_unbxd_recsSliderScrollPrev:function(){var e;try{e=event.currentTarget.parentElement.parentElement.parentElement}catch(e){console.warn(e)}if(e){var t=e.id,n="#"+t+" ._unbxd_rex-slider--next",r=document.querySelector(n);if(!r)return console.warn("_unbxd_rex-slider--next class missing");r.disabled&&(r.disabled=!1),_unbxd_recsSliderSideScroll(t,"left")}else console.warn("target element not found. HTML was changed")},_unbxd_recsSliderVerticalScroll:function(e,t){var n=0,r="#"+e+" #_unbxd_recs-vertical-slider-container",i=document.querySelector(r);if(!i)return console.warn("slider container id is missing. Execution can not continue");var o="#"+e+" ._unbxd_recs-vertical-slider__item",s=document.querySelector(o);if(!s)return console.warn("vertical slider item tile class is missing. Execution can not continue");var a=55,d=1*(s.clientWidth+20),l=setInterval((function(){if("top"==t){let e=n+a;e>d&&(a-=e-d),i.scrollLeft-=a}else{let e=n+a;e>d&&(a-=e-d),i.scrollLeft+=a}if((n+=a)>=d&&window.clearInterval(l),0===i.scrollLeft){var r=document.querySelector("#"+e+" ._unbxd_rex-vertical-slider--top");if(!r)return console.warn("#"+e+" _unbxd_rex-vertical-slider--top class missing");r.disabled=!0}if(i.clientWidth+i.scrollLeft>=i.scrollWidth){var o=document.querySelector("#"+e+" ._unbxd_rex-vertical-slider--bottom");if(!o)return console.warn("#"+e+" _unbxd_rex-vertical-slider--bottom class missing");o.disabled=!0}}),40)},_unbxd_recsSliderScrollBottom:function(){var e;try{e=event.currentTarget.parentElement.parentElement.parentElement}catch(e){console.warn(e)}if(e){var t=e.id,n="#"+t+" ._unbxd_rex-vertical-slider--top",r=document.querySelector(n);if(!r)return console.warn("_unbxd_rex-vertical-slider--top class missing");r.disabled&&(r.disabled=!1),_unbxd_recsSliderVerticalScroll(t,"bottom")}else console.warn("target element not found. HTML was changed")},_unbxd_recsSliderScrollTop:function(){var e;try{e=event.currentTarget.parentElement.parentElement.parentElement}catch(e){console.warn(e)}if(e){var t=e.id,n="#"+t+" ._unbxd_rex-vertical-slider--bottom",r=document.querySelector(n);if(!r)return console.warn("_unbxd_rex-vertical-slider--bottom class missing");r.disabled&&(r.disabled=!1),_unbxd_recsSliderVerticalScroll(t,"top")}else console.warn("target element not found. HTML was changed")}},i=function(e){return console.warn(e)},o=function(e,t,n,r){for(var i=document.querySelectorAll("#"+r+" ."+e),o=0;o<i.length;o++){var s=document.createElement("img");s.src=t,s.alt=n,i[o].appendChild(s)}},s=function(e,t){for(var n=document.querySelectorAll("#"+t+" ."+e),r=0;r<n.length;r++){var i;if("_unbxd_rex-slider--next"===e)(i=document.createElement("span")).classList.add("next-arrow"),n[r].appendChild(i);if("_unbxd_rex-slider--prev"===e)(i=document.createElement("span")).classList.add("prev-arrow"),n[r].appendChild(i)}},a=function(e,t,n){let r=[];r=n?e.filter(e=>"Next Arrow"!==e.altText&&"Previous Arrow"!==e.altText):e;for(var i=0;i<r.length;i++)o(r[i].classname,r[i].url,r[i].altText,t)},d=function(e,t,n){if(n)for(var r=0;r<e.length;r++)s(e[r].classname,t)}},function(e,t){e.exports={development:{url:"http://34.86.42.94/v3.0/"},production:{url:"https://g-recommendations.unbxd.io/v3.0/"}}},function(e,t,n){"use strict";n.d(t,"a",(function(){return s}));var r=function(e){if(isNaN(e))return console.warn("Invalid rating value provided"),"";var t,n,r=e/.5,i=0,o="";r%2!=0&&(i=1),n=5-((t=Math.floor(r/2))+i);for(var s=0;s<t;s++)o+='<span class="_unbxd_rex-full-star recs-star _unbxd_rating-item"></span>';for(s=0;s<i;s++)o+='<span class="_unbxd_rex-half-star recs-star _unbxd_rating-item"></span>';for(s=0;s<n;s++)o+='<span class="_unbxd_rex-empty-star recs-star _unbxd_rating-item"></span>';return o};function i(e,t,n){return"<span class='_unbxd-rating-value-container'><span class='_unbxd-rating-value-prefix _unbxd_rating-item'>"+t.prefix.text+"</span><span class='_unbxd-rating-value'>"+e[n]+"</span></span>"}function o(e,t){setTimeout((function(){for(var n=document.querySelectorAll(e+" ._unbxd-rating-value-prefix"),r=document.querySelectorAll(e+" ._unbxd-rating-value"),i=0;i<n.length;i++)!function(e){for(var r=Object.keys(t.prefix.styles),i=0;i<r.length;i++)n[e].style[r[i]]=t.prefix.styles[r[i]]}(i),function(e){for(var n=Object.keys(t.value.styles),i=0;i<n.length;i++)r[e].style[n[i]]=t.value.styles[n[i]]}(i)}),0)}var s=function(e,t,n,s){if(e[s]){var a="";return"value"===t.type?(a=i(e,t,s),o(n,t)):"image"===t.type?a=r(e[s]):(a="image"===t.sequence[0]?r(e[s])+"<br>"+i(e,t,s):i(e,t,s)+"<br>"+r(e[s]),o(n,t)),a}}},function(e,t,n){"use strict";n.d(t,"a",(function(){return r}));var r=function(e,t,n){var r=t.products.strike_price_feature,i=r.new,o=r.old,s=r.discount,a=e[o.field],d=o.prefix,l=e[i.field],c="";return a&&a>l?(c="<p class='_unbxd_strike_through_container'><span class='_unbxd_strike_through_prefix'>"+d.text+"</span><span class='_unbxd_strike_through_text'>"+t.products.currency+a+"</span></p>",c+="<p class='_unbxd_original_price_container'>"+function(e){if(e.prefix.text)return"<span class='_unbxd_item_display_text'>"+e.prefix.text+"</span>";return""}(i)+function(e,t){return"<span class='_unbxd_original_price_value'>"+e.products.currency+t+"</span>"}(t,l)+"</p>"+function(e,t,n,r,i){var o="";if(e.enabled){var s=e.mode,a=0;if("percentage"==s){var d=(t-n)/t*100;a=d%1==0?d:parseFloat(d).toFixed(2),a+="%"}else{var l=t-n;l=l%1==0?l:parseFloat(l).toFixed(2),a=r.products.currency+l}e.prefix.text?(o="<p class='_unbxd_item_discount_text'><span class='_unbxd_discount_text_label'>"+e.prefix.text+"</span><span class='_unbxd_discount_text_val'>"+a+"</span></p>",function(e,t){setTimeout((function(){var n=document.querySelectorAll(t+" ._unbxd_discount_text_val"),r=e.products.strike_price_feature.discount.value.styles,i=document.querySelectorAll(t+" ._unbxd_discount_text_label"),o=e.products.strike_price_feature.discount.prefix.styles;for(let e=0;e<n.length;e++)!function(e){for(var t=Object.keys(r),i=0;i<t.length;i++)n[e].style[t[i]]=r[t[i]]}(e);for(let e=0;e<i.length;e++)!function(e){for(var t=Object.keys(o),n=0;n<t.length;n++)i[e].style[t[n]]=o[t[n]]}(e)}),0)}(r,i)):o="<p class='_unbxd_discount_text_val'>"+a+"</p>"}return o}(s,a,l,t,n),function(e,t){setTimeout((function(){var n=document.querySelectorAll(t+" ._unbxd_strike_through_text"),r=document.querySelectorAll(t+" ._unbxd_strike_through_prefix"),i=e.products.strike_price_feature.old.value.styles,o=e.products.strike_price_feature.old.prefix.styles;for(let e=0;e<n.length;e++)!function(e){for(var t=Object.keys(i),r=0;r<t.length;r++)n[e].style[t[r]]=i[t[r]]}(e);for(let e=0;e<r.length;e++)!function(e){for(var t=Object.keys(o),n=0;n<t.length;n++)r[e].style[t[n]]=o[t[n]]}(e)}),0),setTimeout((function(){var n=document.querySelectorAll(t+" ._unbxd_original_price_value"),r=e.products.strike_price_feature.new.value.styles,i=document.querySelectorAll(t+" ._unbxd_item_display_text"),o=e.products.strike_price_feature.new.prefix.styles;for(let e=0;e<n.length;e++)!function(e){for(var t=Object.keys(r),i=0;i<t.length;i++)n[e].style[t[i]]=r[t[i]]}(e);for(let e=0;e<i.length;e++)!function(e){for(var t=Object.keys(o),n=0;n<t.length;n++)i[e].style[t[n]]=o[t[n]]}(e)}),0)}(t,n)):c="<p class='_unbxd_original_price_container'>"+t.products.currency+l+"</p>",c}},function(e,t,n){"use strict";n.d(t,"a",(function(){return i}));var r=n(1);function i(e,t,n,i,o,s){try{"width"==e.dimension?setTimeout((function(){var a=document.querySelector("#"+t.selector+" "+e.container),d=a.parentElement;a.style.width=t.widgetWidth||"initial",d.clientWidth<a.clientWidth&&(a.style.width=d.clientWidth+"px"),n.style.width=n[e.offsetDimension]+"px";var l=(n[e.offsetDimension]-10*t.itemsToShow)/t.itemsToShow,c="#"+t.selector+" ."+o,u=document.querySelector(c);if(!u)return Object(r.b)("Slider Parent id was not found in the DOM");if(t.itemWidth)if("%"===t.itemWidthUnit){var p=.01*t.widgetWidthData*n[e.offsetDimension];for(let e=0;e<i.length;e++)i[e].style.width=p+"px",u.style.width=s*p+10*s+"px"}else for(let e=0;e<i.length;e++)i[e].style.width=t.widgetWidth,u.style.width=s*t.itemWidth+10*s+t.itemWidth;else for(var m=0;m<i.length;m++)i[m].style.width=l+"px",u.style.width=s*l+10*s+"px";document.querySelector("#"+t.selector+" ._unxbd_slider_hide").classList.remove("_unxbd_slider_hide")}),0):setTimeout((function(){var e=document.querySelector("#"+t.selector+" ._unbxd_vertical-recs-slider");var n=e.parentElement;if(e.style.width=t.widgetWidth||"initial",n.clientWidth<e.clientWidth&&(e.style.width=n.clientWidth+"px"),t.itemWidth)for(let e=0;e<i.length;e++)i[e].style.width=t.itemWidth;else for(let t=0;t<i.length;t++)i[t].style.width=e.clientWidth-20+"px";var s="#"+t.selector+" ."+o,a=document.querySelector(s);if(!a)return Object(r.b)("Slider Parent id was not found in the DOM");a.style.width=e.clientWidth*t.recommendationsModified.length+"px",document.querySelector("#"+t.selector+" ._unxbd_slider_hide").classList.remove("_unxbd_slider_hide")}),0)}catch(e){}}},function(e,t){var n;n=function(){return this}();try{n=n||new Function("return this")()}catch(e){"object"==typeof window&&(n=window)}e.exports=n},function(e,t,n){var r;!function(i){"use strict";var o,s={name:"doT",version:"1.1.1",templateSettings:{evaluate:/\{\{([\s\S]+?(\}?)+)\}\}/g,interpolate:/\{\{=([\s\S]+?)\}\}/g,encode:/\{\{!([\s\S]+?)\}\}/g,use:/\{\{#([\s\S]+?)\}\}/g,useParams:/(^|[^\w$])def(?:\.|\[[\'\"])([\w$\.]+)(?:[\'\"]\])?\s*\:\s*([\w$\.]+|\"[^\"]+\"|\'[^\']+\'|\{[^\}]+\})/g,define:/\{\{##\s*([\w\.$]+)\s*(\:|=)([\s\S]+?)#\}\}/g,defineParams:/^\s*([\w$]+):([\s\S]+)/,conditional:/\{\{\?(\?)?\s*([\s\S]*?)\s*\}\}/g,iterate:/\{\{~\s*(?:\}\}|([\s\S]+?)\s*\:\s*([\w$]+)\s*(?:\:\s*([\w$]+))?\s*\}\})/g,varname:"it",strip:!0,append:!0,selfcontained:!1,doNotSkipEncoded:!1},template:void 0,compile:void 0,log:!0};s.encodeHTMLSource=function(e){var t={"&":"&#38;","<":"&#60;",">":"&#62;",'"':"&#34;","'":"&#39;","/":"&#47;"},n=e?/[&<>"'\/]/g:/&(?!#?\w+;)|<|>|"|'|\//g;return function(e){return e?e.toString().replace(n,(function(e){return t[e]||e})):""}},o=function(){return this||(0,eval)("this")}(),e.exports?e.exports=s:void 0===(r=function(){return s}.call(t,n,t,e))||(e.exports=r);var a={append:{start:"'+(",end:")+'",startencode:"'+encodeHTML("},split:{start:"';out+=(",end:");out+='",startencode:"';out+=encodeHTML("}},d=/$^/;function l(e){return e.replace(/\\('|\\)/g,"$1").replace(/[\r\t\n]/g," ")}s.template=function(e,t,n){var r,i,c=(t=t||s.templateSettings).append?a.append:a.split,u=0,p=t.use||t.define?function e(t,n,r){return("string"==typeof n?n:n.toString()).replace(t.define||d,(function(e,n,i,o){return 0===n.indexOf("def.")&&(n=n.substring(4)),n in r||(":"===i?(t.defineParams&&o.replace(t.defineParams,(function(e,t,i){r[n]={arg:t,text:i}})),n in r||(r[n]=o)):new Function("def","def['"+n+"']="+o)(r)),""})).replace(t.use||d,(function(n,i){t.useParams&&(i=i.replace(t.useParams,(function(e,t,n,i){if(r[n]&&r[n].arg&&i){var o=(n+":"+i).replace(/'|\\/g,"_");return r.__exp=r.__exp||{},r.__exp[o]=r[n].text.replace(new RegExp("(^|[^\\w$])"+r[n].arg+"([^\\w$])","g"),"$1"+i+"$2"),t+"def.__exp['"+o+"']"}})));var o=new Function("def","return "+i)(r);return o?e(t,o,r):o}))}(t,e,n||{}):e;p=("var out='"+(t.strip?p.replace(/(^|\r|\n)\t* +| +\t*(\r|\n|$)/g," ").replace(/\r|\n|\t|\/\*[\s\S]*?\*\//g,""):p).replace(/'|\\/g,"\\$&").replace(t.interpolate||d,(function(e,t){return c.start+l(t)+c.end})).replace(t.encode||d,(function(e,t){return r=!0,c.startencode+l(t)+c.end})).replace(t.conditional||d,(function(e,t,n){return t?n?"';}else if("+l(n)+"){out+='":"';}else{out+='":n?"';if("+l(n)+"){out+='":"';}out+='"})).replace(t.iterate||d,(function(e,t,n,r){return t?(u+=1,i=r||"i"+u,t=l(t),"';var arr"+u+"="+t+";if(arr"+u+"){var "+n+","+i+"=-1,l"+u+"=arr"+u+".length-1;while("+i+"<l"+u+"){"+n+"=arr"+u+"["+i+"+=1];out+='"):"';} } out+='"})).replace(t.evaluate||d,(function(e,t){return"';"+l(t)+"out+='"}))+"';return out;").replace(/\n/g,"\\n").replace(/\t/g,"\\t").replace(/\r/g,"\\r").replace(/(\s|;|\}|^|\{)out\+='';/g,"$1").replace(/\+''/g,""),r&&(t.selfcontained||!o||o._encodeHTML||(o._encodeHTML=s.encodeHTMLSource(t.doNotSkipEncoded)),p="var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : ("+s.encodeHTMLSource.toString()+"("+(t.doNotSkipEncoded||"")+"));"+p);try{return new Function(t.varname,p)}catch(e){throw e}},s.compile=function(e,t){return s.template(e,null,t)},i.doT=s}(window)},function(e,t,n){"use strict";n.d(t,"b",(function(){return a})),n.d(t,"a",(function(){return d}));var r=n(0),i=n(10),o=n(3),s=n(4);n(7);const a=async e=>{try{let o={};if(e&&Object.keys(e).length>0){if(e.message)return void console.error("Error in widget response ",e.widgetId,e.templateId,e.message);if(e.widgetId){let s=e.widgetId,a=window.widgetsConfig.find(t=>t.name==e.widgetPlacementId);if(o[s]=new Object,o[s].widgetId=e.widgetId,o[s].widgetPlacementId=e.widgetPlacementId,o[s].widgetTitle=e.widgetTitle,!a)return console.error("No Element found for widgetID");if(e=Object.assign(a,e),o[s].selector=e.selector,e.recommendations&&e.templateData&&e.templateData.uuid){let a=e.templateData;o[s].orientation=a.conf&&a.conf.orientation?a.conf.orientation:"";var t=a.conf.products.max||a.conf.products.max_products||a.conf.max_recs;if(o[s].maxProducts=t,t&&e.recommendations.length&&t<e.recommendations.length&&(e.recommendations=e.recommendations.splice(0,t)),o[s].recommendations=e.recommendations,e.templateData.scriptUrl){o[s].url=e.templateData.scriptUrl;let t=await function(e){try{return new Promise((t,n)=>{Object(r.c)(e,!1,(function(e,n,r){t(n)}))})}catch(e){console.error(e)}}(e.templateData.scriptUrl);t?o[s].templateStructure=t:console.error("error in fetching template data",o[s].templateId)}if(e&&e.templateData&&e.templateData.conf){let t=e.templateData.conf.width||missingValueError("products.widget.width",e.templateData.conf);var n="";t.value&&0!=t.value&&(n=t.value+t.unit),o[s].conf=e.templateData.conf,o[s].styling=e.templateData.conf.css?e.templateData.conf.css:"",o[s].script=e.templateData.conf.js?e.templateData.conf.js:"",o[s].custom_properties=e.templateData.conf.custom_properties?e.templateData.conf.custom_properties:"",e.widgetWidth=n,o[s].widgetWidthData=t.value,o[s].widgetWidthUnit=t.unit,o[s].widgetWidth=n,e.device=Object(r.e)(),e.browserSize=Object(r.d)(),o[s].device=e.device,o[s].browserSize=e.browserSize;let a=function(e){
//!--! check this done
let t=e.templateData.conf.products&&e.templateData.conf.products.visible?e.templateData.conf.products.visible:e.templateData.conf&&e.templateData.conf.num_recs?e.templateData.conf.num_recs:2;var n,i,o;"mobile-browser"===window.unbxdDeviceType||"mobile-browser"===e.unbxdDeviceType||e.unbxdDeviceType===r.a||e.browserSize===r.b?(i=e.templateData.conf&&e.templateData.conf.width&&e.templateData.conf.width.value||0,o=e.templateData.conf&&e.templateData.conf.width&&e.templateData.conf.width.unit||"px",n=e.templateData.conf&&e.templateData.conf.products&&e.templateData.conf.products.visible?e.templateData.conf.products.visible:e.templateData.conf.products.visibleOn.mobile,t=n||"2"):(t=e.templateData.conf&&e.templateData.conf.products&&e.templateData.conf.products.visible?e.templateData.conf.products.visible:e.templateData.conf.products.visibleOn?e.templateData.conf.products.visibleOn.desktop:e.templateData.conf.numRecs,t=t||2);return{itemsToShow:t,itemWidthUnit:o,itemWidth:i}}(e);e={...e,...a},o[s]={...o[s],...a},o[s].itemsToShow=e.itemsToShow,"vertical"==e.orientation&&"boutique"!==e.templateType?window._unbxd_recsItemToScrollVt=e.itemsToShow:(window.unbxdDeviceType,window._unbxd_recsItemToScrollHz=e.itemsToShow);let d=function(e,t,n){
//!--! check this
let r={selector:e[n].selector,templateType:t.customProperties&&t.customProperties.widgetType?t.customProperties.widgetType:"",renderTemplate:1};t.widget_addon&&Object.keys(t.addonDetails).length>0&&(r.globalAssets=1,r.templateAddonData={...t.addonDetails});return r}(o,e.templateData.conf,e.widgetId);return o[s]={...o[s],...d},window.tc={...window.tc,...o},//!--! when doing exit intent
(2==o[s].templateType||o[s].isPopup)&&Object(i.a)(o[s]),3==o[s].templateType&&l.init(),function(e){if(e){let l=[];if("vertical"==e.orientation&&"boutique"!==e.conf.templateType)for(var t=0;t<e.recommendations.length;t++)if(t%e.itemsToShow==0){e.itemsToShow;var n=e.recommendations.slice(t,t+e.itemsToShow);l.push(n)}l&&(window.tc[e.widgetId].recommendationsModified=l);var i={recommendations:l.length>0?l:e.recommendations,heading:e.widgetTitle,analyticsData:{widgetNum:e.widgetPlacementId.toUpperCase(),pageType:window.unbxdPageType,requestId:window.reqId},isGlobalAddonEnabled:e.conf.widgetAddon,addOnData:{like:e.conf.addonDetails.likeable,dislike:e.conf.addonDetails.dislikeable,share:e.conf.addonDetails.shareable,fave:e.conf.addonDetails.wishlist}};if(window.dataParser&&"function"==typeof window.dataParser&&(i=window.dataParser(i)),window.eventQueue&&"function"==typeof window.eventQueue.beforeTemplateRender){var o=window.eventQueue.beforeTemplateRender;i=o(i)}var s=doT.template(e.templateStructure),a=document.getElementById(e.selector);a&&(a.innerHTML=s(i));var d=document.createElement("style");d.type="text/css",d.innerHTML=e.styling,document.head.appendChild(d),e.script&&Object(r.g)(e.script),e.conf.widgetAddon&&function(e){let t=e.conf.addonDetails,n="";window.globalAddonsAssets?(t.likeable&&Object.keys(window.globalAddonsAssets.likeButton).length>0&&(n+=`.liked-img{content : url(${window.globalAddonsAssets.likeButton.selectedIconSrc})}.like-img{content:url(${window.globalAddonsAssets.likeButton.unselectedIconSrc})}`),t.dislikeable&&Object.keys(window.globalAddonsAssets.dislikeButton).length>0&&(n+=`.disliked-img{content : url(${window.globalAddonsAssets.dislikeButton.selectedIconSrc})}.dislike-img{content:url(${window.globalAddonsAssets.dislikeButton.unselectedIconSrc})}`),t.wishlist&&Object.keys(window.globalAddonsAssets.wishlistButton).length>0&&(n+=`.wishlist-img{content : url(${window.globalAddonsAssets.wishlistButton.unselectedIconSrc})}.wishlisted-img{content:url(${window.globalAddonsAssets.wishlistButton.selectedIconSrc})}`),t.shareable&&Object.keys(window.globalAddonsAssets.shareButton).length>0&&(n+=`.share-img{content : url(${window.globalAddonsAssets.shareButton.unselectedIconSrc})}.shared-img{content:url(${window.globalAddonsAssets.shareButton.selectedIconSrc})}`),Object(r.f)(n)):console.error("global addons assest is not defined")}(e)}}(o[s]),Promise.resolve(!0)}}}}}catch(t){console.error("Error in parsing template Data",e,t)}};function d(e,t,n,r,i,a){for(var d=0;d<t.length;d++){for(var l=document.createDocumentFragment(),c=0;c<n.length;c++){var u=n[c].styles||missingValueError("styles",n[c]),p=n[c].unbxdDimensionKey||n[c].catalogKey||n[c].unbxd_dimension_key||missingValueError("unbxdDimensionKey or catalogKey",n[c]),m=Object.keys(u);if(r[d]&&!r[d][p]&&(p=n[c].catalogKey),"imageUrl"!=p&&r[d]){var g=document.createElement("p"),f=r[d][p];if(g.className=i.sliderContentClass,g.tabIndex=0,g.setAttribute("role","button"),e&&e.conf&&e.conf.products.strikePriceFeature&&p==e.conf.products.strikePriceFeature.new.field)e&&e.conf&&e.conf.products.strikePriceFeature.enabled?g.innerHTML=Object(s.a)(r[d],e.conf,a):g.innerHTML=e.conf.products.currency+f;else if(e&&e.conf&&e.conf.products.ratingsFeature&&e.conf.products.ratingsFeature.enabled&&n[c].unbxdDimensionKey&&"rating"==n[c].unbxdDimensionKey.toLowerCase()){var b=Object(o.a)(r[d],e.conf.products.ratingsFeature,a,p);b&&(g.innerHTML=b)}else g.innerHTML=f?f instanceof Array?f.join(", "):f:"";if(g.innerHTML){for(var w=0;w<m.length;w++)g.style[m[w]]=u[m[w]];l.appendChild(g)}}}t[d].querySelector("._unbxd_recs_product_details").appendChild(l)}}const l={animating:!1,swipeDelta:120,dragDx:0,startX:0,deg:0,pcd:void 0,pcdReject:void 0,pcdLike:void 0,bod:document.querySelector("body"),startEve:["touchstart"],moveEve:["touchmove"],endEve:["touchend"],init:()=>{window.bxTinderConf&&!objIsEmpty(window.bxTinderConf)&&Object.assign(l,bxTinderConf),l.startEve.forEach(e=>{l.bod.addEventListener(e,(function(e){!l.animating&&e.target.closest(".unbxdtin")&&(l.pcd=e.target.closest(".unbxdtin"),l.pcdReject=l.pcd.querySelector(".unbxddislikeablebtn"),l.pcdLike=l.pcd.querySelector(".unbxdlikeablebtn"),l.startX=e.pageX||e.targetTouches[0].pageX||e.originalEvent.touches[0].pageX,l.moveEve.forEach(e=>{l.bod.addEventListener(e,l.tinMv)}),l.endEve.forEach(e=>{l.bod.addEventListener(e,(function t(n){l.moveEve.forEach(e=>{l.bod.removeEventListener(e,l.tinMv)}),l.bod.removeEventListener(e,t),l.dragDx&&l.release()}))}))}))})},pullChange:()=>{l.animating=!0,l.deg=l.dragDx/10,l.pcd.style.transform="translateX("+l.dragDx+"px) rotate("+l.deg+"deg)";const e=l.dragDx/100,t=e>=0?0:Math.abs(e),n=e<=0?0:e;l.pcdReject.style.opacity=t,l.pcdLike.style.opacity=n},release:()=>{let e="liked";l.dragDx>=l.swipeDelta?l.pcd.classList.add("to-right"):l.dragDx<=-l.swipeDelta&&(l.pcd.classList.add("to-left"),e="disliked"),Math.abs(l.dragDx)>=l.swipeDelta&&(l.pcd.classList.add("inactive"),l.pcd.remove()),Math.abs(l.dragDx)<l.swipeDelta&&(l.pcd.classList.add("reset"),setTimeout(()=>{l.pcd.classList.remove("reset"),l.pcd.setAttribute("style",""),l.pcdLike.setAttribute("style",""),l.pcdReject.setAttribute("style","")},300)),l.dragDx=0,l.animating=!1},tinMv:e=>{const t=e.pageX||e.targetTouches[0].pageX||e.originalEvent.touches[0].pageX;l.dragDx=t-l.startX,l.dragDx&&l.pullChange()}}},function(e,t,n){"use strict";n.d(t,"a",(function(){return r}));const r={getDomain:function(e){var t=e.split(".").reverse();return t.length>=3&&t[1].match(/^(com|edu|gov|net|org|co|name|info|biz|myshopify)$/i)?t[2]+"."+t[1]+"."+t[0]:t[1]+"."+t[0]},setCookie:function(e,t,n){var i=new Date;let o=n?1e3*n:864e5;i.setTime(i.getTime()+o);var s="expires="+i.toUTCString(),a=e+"="+encodeURIComponent(btoa(t))+";path=/;domain=."+r.getDomain(window.location.origin);document.cookie=o?a+";"+s:a},getCookie:function(e){var t=e+"=",n=document.cookie;try{n=decodeURIComponent(n)}catch(e){}for(var r=n.split(";"),i=0;i<r.length;i++){for(var o=r[i];" "==o.charAt(0);)o=o.substring(1);if(0==o.indexOf(t)){var s=o.substring(t.length,o.length);try{return s=decodeURIComponent(s),atob(s)}catch(e){}return s}}return""}}},function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",(function(){return exitIntentInitator}));var _utils__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(0),_handlers_cookie__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(9);const exitIntentInitator=function(e){if(e&&e.conf&&e.conf.customProperties&&e.conf.customProperties.widgetCondition){let t=e.conf;const n=t.customProperties.widgetCondition.Listenon+"-"+t.customProperties.widgetCondition.event+"-modal";injectExitIntentModalStyles();const r=document.createElement("div");r.id=n+"-parent",r.classList.add("unbxd-intent-modal-parent"),document.body.appendChild(r),r.innerHTML='<div class="modalContainer" id="'+n+'"></div>',e.selector=n,e.inject="inner",attachIntentListener(e,t);let i=e.widgetId;window.tc[i].selector=e.selector,window.tc[i].inject=e.inject,2==window.tc[i].templateType&&(window.tc[i].canPopUp=1)}else console.warn("Widget inject selector found None or duplicates")},attachIntentListener=function(popup,widgetConfig){const evTarget=widgetConfig.customProperties.widgetCondition&&"window"===widgetConfig.customProperties.widgetCondition.Listenon?window:document.querySelector(widgetConfig.customProperties.widgetCondition.Listenon),modalId=widgetConfig.customProperties.widgetCondition.Listenon+"-"+widgetConfig.customProperties.widgetCondition.event+"-modal-parent";evTarget.addEventListener(widgetConfig.customProperties.widgetCondition.event,(function intentListenr(e){const modalId=widgetConfig.customProperties.widgetCondition.Listenon+"-"+widgetConfig.customProperties.widgetCondition.event+"-modal";if(document.getElementById(modalId))if(console.info("Popup intent detected "+modalId,window.tc[popup.widgetId]),!window.tc[popup.widgetId].canPopUp&&2!=window.tc[popup.widgetId].templateType||!eval(widgetConfig.customProperties.widgetCondition.callback)||_handlers_cookie__WEBPACK_IMPORTED_MODULE_1__.a.getCookie(modalId))console.info("Popup checks failed "+modalId);else{document.getElementById(modalId+"-parent").style.display="table",document.getElementById(modalId+"-parent").style.opacity=1,document.getElementById(modalId+"-parent").style.zIndex=99;let e=!!widgetConfig.customProperties.widgetCondition.expireTime&&widgetConfig.customProperties.widgetCondition.expireTime;_handlers_cookie__WEBPACK_IMPORTED_MODULE_1__.a.setCookie(modalId,"true",e),console.info("Popup triggered successfully "+modalId),document.querySelector(widgetConfig.customProperties.widgetCondition.Listenon).removeEventListener(widgetConfig.customProperties.widgetCondition.event,intentListenr)}else document.querySelector(widgetConfig.customProperties.widgetCondition.Listenon).removeEventListener(widgetConfig.customProperties.widgetCondition.event,intentListenr)}))},injectExitIntentModalStyles=function(){let e=".unbxd-intent-modal-parent{display:table;opacity:0;position:fixed;top:0;left:0;z-index:-1;width:100%;height:100%;background:#777777b8;text-align:center}";e+=".modalContainer{display:table-cell;vertical-align:middle}",Object(_utils__WEBPACK_IMPORTED_MODULE_0__.f)(".unbxd-intent-modal-parent{display:table;opacity:0;position:fixed;top:0;left:0;z-index:-1;width:100%;height:100%;background:#777777b8;text-align:center}.modalContainer{display:table-cell;vertical-align:middle}")}},function(e,t,n){"use strict";(function(e){n.d(t,"a",(function(){return s}));var r=n(0),i=n(2),o=n.n(i);class s{constructor(t){this.horizontalTemplateHandler=(e,t)=>{if(e)throw new Error("Failed to fetch templates");this.horizontalTemplate=t,this.handleWidgetRendering()},this.verticalTemplateHandler=(e,t)=>{if(e)throw new Error("Failed to fetch templates");this.verticalTemplate=t,this.handleWidgetRenderingVertical()},this._unbxd_generateRexContent=t=>{var n=t.template||missingValueError("template",t),i=t.targetDOMElementId||missingValueError("targetDOMElementId",t),o=t.recommendations||missingValueError("recommendations",t),s=t.heading||missingValueError("heading",t),a=t.rexConsoleConfigs||missingValueError("rexConsoleConfigs",t),d=a.products.visible||missingValueError("products.visible",a),l=a.products.max||missingValueError("products.max",a.products),c=t.clickHandler,u=t.dataParser,p=t.eventQueue,m=t.isVertical||!1;this.compressedStyle=a.css||missingValueError("css",a);var g=null,f=a.widget.width||missingValueError("products.widget.width",a.widget),b="";f.value&&0!=f.value&&(b=f.value+f.unit);var w,_,h=doT.template(n),x=document.getElementById(i),v=Object(r.e)(),y=Object(r.d)();if("mobile-browser"===window.unbxdDeviceType||"mobile-browser"===t.unbxdDeviceType||v===r.a||y===r.b?(w=a.products&&a.products.width&&a.products.width.value||0,_=a.products&&a.products.width&&a.products.width.unit||"px",d=(a&&a.products&&a.products.visibleOn?a.products.visibleOn.mobile:a.products.visible)||2):d=(d=a&&a.products&&a.products.visibleOn?a.products.visibleOn.desktop:a.products.visible)||2,!x)return sendWarning("The target element id <"+i+"> is not present in DOM. Execution can not continue");if(l<o.length&&(o=o.splice(0,l)),m){g=[];for(var T=0;T<o.length;T++)if(T%d==0){var S=o.slice(T,T+d);g.push(S)}}var C={recommendations:g||o,heading:s,analyticsData:{widgetNum:"WIDGET"+t.widgetNum,pageType:t.pageType,requestId:t.reqId}};(u&&"function"==typeof u&&(C=u(C)),p&&"function"==typeof p.beforeTemplateRender)&&(C=(0,p.beforeTemplateRender)(C));document.getElementById(i).innerHTML=h(C);var E={rexConsoleConfigs:a,recommendations:o,recommendationsModified:g,clickHandler:c,itemsToShow:d,itemWidth:w,itemWidthUnit:_,maxProducts:l,assets:t.assets,sliderType:m||"mobile-browser"===!window.unbxdDeviceType?"vertical":"horizontal",sliderClass:m||"mobile-browser"===!window.unbxdDeviceType?"_unbxd_recs-vertical-slider":"_unbxd_recs-slider",widgetWidth:b};m?e._unbxd_recsItemToScrollVt=d:(window.unbxdDeviceType,e._unbxd_recsItemToScrollHz=d);var D=document.createElement("style");(D.type="text/css",D.innerHTML=this.compressedStyle,document.head.appendChild(D),handleSizeCalculations(i,E),p&&"function"==typeof p.afterTemplateRender)&&(C=(0,p.afterTemplateRender)(m))},this.HOME_PAGE="home",this.PRODUCT_PAGE="product",this.CATEGORY_PAGE="category",this.CART_PAGE="cart",this.allowedPageTypes=[this.HOME_PAGE,this.PRODUCT_PAGE,this.CATEGORY_PAGE,this.CART_PAGE],this.pageType=this.getPageDetails(t.pageInfo);var n=o.a.production.url;window.unbxdDeviceType=this.getTemplateDetails(t);var i=t.widgets;if(this.widget1=this.getWidgetId(this.pageType,"widget1",i),this.widget2=this.getWidgetId(this.pageType,"widget2",i),this.widget3=this.getWidgetId(this.pageType,"widget3",i),!this.widget1&&!this.widget2&&!this.widget3)throw new Error("No widget id provided");this.itemClickHandler=this.getClickHandler(t),this.dataParser=this.getDataParserHandler(t),this.eventQueue=window.eventQueue;var s=t.userInfo,a=s&&s.userId||this.getCookie("unbxd.userId"),d=s&&s.siteKey||window.UnbxdSiteName,l=s&&s.apiKey||window.UnbxdApiKey,c=n+l+"/"+d+"/items?&template=true&pageType=";if(!a)throw new Error("user id is missing");if(!d)throw new Error("site Key is missing");if(!l)throw new Error("api key is missing");c+=encodeURIComponent(this.pageType);var u=t.pageInfo;switch(this.pageType.toLowerCase()){case this.PRODUCT_PAGE:case this.CART_PAGE:u.productIds&&(c+=this.getProductIdsAsUrlParams(u.productIds));break;case this.CATEGORY_PAGE:var p="",m=u.catlevel1Name,g=u.catlevel2Name,f=u.catlevel3Name,b=u.catlevel4Name;m&&(p="&"+this.getUrlEncodedParam("catlevel1Name",m),g&&(p+="&"+this.getUrlEncodedParam("catlevel2Name",g),f&&(p+="&"+this.getUrlEncodedParam("catlevel3Name",f),b&&(p+="&"+this.getUrlEncodedParam("catlevel4Name",b))))),c+=p;break;case this.HOME_PAGE:break;default:throw new Error("Invalid page type: "+this.pageType)}c+="&uid="+a;const w=t.extraParams;if(w&&"object"==typeof w&&Object.keys(w).length>0){let e="";Object.keys(w).forEach((t,n)=>{n>0&&(e+="&"),e+=`${t}=${encodeURIComponent(w[t])}`}),c+="&"+e}this.compressedStyleVertical="";var _=this;Object(r.c)(c,!0,(function(e,t,n){if(e)throw new Error("Failed to fetch recommendations");if(_.recommendationsResponse=JSON.parse(t),_.horizontalTemplate=_.recommendationsResponse.template.horizontal,_.reqId=n,_.horizontalTemplate){_.horizontalConfig=_.horizontalTemplate.conf,_.horizontalAssets=_.horizontalConfig.assets;var i=_.horizontalTemplate.scriptUrl;i?Object(r.c)(i,!1,_.horizontalTemplateHandler):console.warn("script url not found for horizontal template")}if(_.verticalTemplate=_.recommendationsResponse.template.vertical,_.verticalTemplate){_.verticalConfig=_.verticalTemplate.conf,_.verticalAssets=_.verticalConfig.assets;var o=_.verticalTemplate.scriptUrl;o?Object(r.c)(o,!1,_.verticalTemplateHandler):console.warn("script url not found for vertical template")}}))}getWidgetId(e,t,n){var r;return n?n[t]?n[t].name:null:(r=widgetIdMap[e.toLowerCase()][t],document.getElementById(r)?r:null)}getPageDetails(e){if(!e||!e.pageType)throw new Error("Page type info missing");var t=e.pageType;if(-1==this.allowedPageTypes.indexOf(t.toLowerCase()))throw new Error("Invalid value for page type");return t}getTemplateDetails(e){var t=Object(r.e)(),n=Object(r.d)();return e.unbxdDeviceType&&e.unbxdDeviceType.mobileBrowser?"mobile-browser":e.unbxdDeviceType&&e.unbxdDeviceType.desktopBrowser?"desktop-browser":t===r.a||n===r.b?"mobile-browser":"desktop-browser"}getClickHandler(e){return e.itemClickHandler}getDataParserHandler(e){return e.dataParser}getUrlEncodedParam(e,t){return e+"="+encodeURIComponent(t)}getProductIdsAsUrlParams(e){var t="";const n=this;return e instanceof Array?e.forEach((function(e){t+="&"+n.getUrlEncodedParam("id",e)})):t+="&"+n.getUrlEncodedParam("id",e),t}getCookie(e){for(var t,n,r=document.cookie.split(";"),i=0;i<r.length;i++)if(t=r[i].split("=")[0],n=r[i].split("=")[1],t.trim()===e)return n}renderWidgetDataHorizontal(e,t,n,r){var i=this.horizontalConfig.products.max||this.horizontalConfig.products.max_products,o=e,s=this.itemClickHandler;i<n.length&&(n=n.splice(0,i));var a={template:this.horizontalTemplate,targetDOMElementId:o,recommendations:n,heading:r,rexConsoleConfigs:this.horizontalConfig,assets:this.horizontalAssets,maxProducts:i,clickHandler:s,dataParser:this.dataParser,eventQueue:this.eventQueue,widgetNum:t,pageType:this.pageType,reqId:this.reqId,sliderClass:"_unbxd_recs-slider",compressedStyle:this.compressedStyle};_unbxd_generateRexContent(a)}renderWidgetDataVertical(e,t,n,r){var i=this.verticalConfig.products.max||this.verticalConfig.products.max_products,o=e,s=this.itemClickHandler;i<n.length&&(n=n.splice(0,i));var a={template:this.verticalTemplate,targetDOMElementId:o,recommendations:n,heading:r,rexConsoleConfigs:this.verticalConfig,assets:this.verticalAssets,maxProducts:i,clickHandler:s,eventQueue:this.eventQueue,dataParser:this.dataParser,widgetNum:t,pageType:this.pageType,reqId:this.reqId,isVertical:!0,sliderClass:"_unbxd_recs-vertical-slider",compressedStyle:this.compressedStyleVertical};_unbxd_generateRexContent(a)}handleWidgetRenderingVertical(){if(this.widget3){var e=this.recommendationsResponse.widget3,t=e.widgetTitle,n=e.recommendations;this.renderWidgetDataVertical(this.widget3,3,n,t)}}handleWidgetRendering(){if(this.widget1){var e=this.recommendationsResponse.widget1,t=e.widgetTitle,n=e.recommendations;this.renderWidgetDataHorizontal(this.widget1,1,n,t)}if(this.widget2){var r=this.recommendationsResponse.widget2,i=r.widgetTitle,o=r.recommendations;this.renderWidgetDataHorizontal(this.widget2,2,o,i)}}}}).call(this,n(6))},function(e,t,n){"use strict";function r(){try{let a=window.context.pageInfo,d="";switch(window.unbxdPageType.toLowerCase()){case"product":case"cart":a.productIds&&(d+=i(a.productIds));break;case"category":var e="",t=a.catlevel1Name,n=a.catlevel2Name,r=a.catlevel3Name,s=a.catlevel4Name;t&&(e="&"+o("catlevel1Name",t),n&&(e+="&"+o("catlevel2Name",n),r&&(e+="&"+o("catlevel3Name",r),s&&(e+="&"+o("catlevel4Name",s))))),d+=e;break;case"home":case"boutique":break;default:throw new Error("Invalid page type: "+window.unbxdPageType)}return d}catch(e){console.error("error at adding params for recommendation request pageType",e)}}function i(e){var t="";return e instanceof Array?e.forEach((function(e){t+="&"+o("id",e)})):t+="&"+o("id",e),t}function o(e,t){return e+"="+encodeURIComponent(t)}n.d(t,"a",(function(){return r}))},function(e,t,n){"use strict";(function(e){n.d(t,"a",(function(){return d}));var r=n(0),i=n(1),o=n(5),s=n(3),a=n(4);n(7);e._unbxd_recsSliderScrollNext=i.a._unbxd_recsSliderScrollNext,e._unbxd_recsSliderScrollPrev=i.a._unbxd_recsSliderScrollPrev,e._unbxd_recsSliderSideScroll=i.a._unbxd_recsSliderSideScroll;const d=e=>{try{var t=e.template||l("template",e);let w=e.recommendations||l("recommendations",e),_=e.targetDOMElementId||l("targetDOMElementId",e),h=e.heading;const x=e.showHeading;let v=e.rexConsoleConfigs||l("rexConsoleConfigs",e),y=v.products.visible||l("products.visible",v),T=v.products.max||l("products.max",v.products),S=e.orientation||l("orientation",e.orientation);window.globalAddonsAssets=e.globalAddonsAssets,window.assets=e.assets;v.css||l("css",v);let C=e.unbxdDeviceType||l("orientation",e),E=v.width?v.width:null;E||(E=v.widget.width||l("products.widget.width",v.widget));let D="";E.value&&0!=E.value&&(D=E.value+E.unit);let I=Object(r.e)(),k=Object(r.d)();T&&w.length&&T<w.length&&(w=w.splice(0,T));let O=function(e,t,n,i){let o=e.products&&e.products.visible?e.products.visible:2;var s,a,d;"mobile-browser"===t||"mobile-browser"===t||i===r.a||n===r.b?(a=e.products.widget&&e.products.widget.width&&e.products.widget.width.value||0,d=e.products.widget&&e.products.widget.width&&e.products.widget.width.unit||"px",s=e&&e.products&&e.products.visibleOn?e.products.visibleOnMobile:e.products.visible,o=s||2):e&&e.products?(e&&e.products&&e.products.visibleOn&&(o=e.products.visibleOn.desktop),e.products.visible&&(o=e.products.visible)):o=o||2;return{itemsToShow:o,itemWidthUnit:d,itemWidth:a}}(v,C,k,I);"vertical"==S?window._unbxd_recsItemToScrollVt=O.itemsToShow:window._unbxd_recsItemToScrollHz=O.itemsToShow;let P={orientation:S,recommendations:w,itemsToShow:y,itemsDetail:O,config:v,template:t,selector:_,heading:h,showHeading:x};if(w)var n=function(e){if(e){let l=[];if("vertical"==e.orientation&&"boutique"!==e.config.template_type)for(var t=0;t<e.recommendations.length;t++)if(t%e.itemsToShow==0){e.itemsToShow;var n=e.recommendations.slice(t,t+e.itemsToShow);l.push(n)}var i={recommendations:l.length>0?l:e.recommendations,analyticsData:{widgetNum:e.widgetPlacementId,pageType:window.unbxdPageType,requestId:window.reqId},heading:e.showHeading?e.heading:null,isGlobalAddonEnabled:e.config.widget_addon,addOnData:{like:e.config.addon_details.likeable,dislike:e.config.addon_details.dislikeable,share:e.config.addon_details.shareable,fave:e.config.addon_details.wishlist}};if(window.dataParser&&"function"==typeof window.dataParser&&(i=window.dataParser(i)),window.eventQueue&&"function"==typeof window.eventQueue.beforeTemplateRender){var o=window.eventQueue.beforeTemplateRender;i=o(i)}var s=doT.template(e.template),a=document.getElementById(e.selector);a&&(a.innerHTML=s(i));var d=document.createElement("style");d.type="text/css",d.innerHTML=e.config.css,document.head.appendChild(d),e.config.widget_addon&&function(e){let t=e.config.addon_details,n="vertical"!==e.orientation&&"boutique"!==e.config.template_type?".unbxd--action--buttons>a{padding:4%;width:20%;}":"boutique"===e.config.template_type&&e.config.custom_properties&&"instagram"===e.config.custom_properties.basedOn?".unbxd--wishlist{left:75px}":"";window.globalAddonsAssets&&(t.likeable&&window.globalAddonsAssets.likebutton&&Object.keys(window.globalAddonsAssets.likebutton).length>0&&(n+=`.liked-img{content : url(${window.globalAddonsAssets.likebutton.selected_icon_src})}.like-img{content:url(${window.globalAddonsAssets.likebutton.unselected_icon_src})}`),t.dislikeable&&Object.keys(window.globalAddonsAssets.dislikebutton).length>0&&(n+=`.disliked-img{content : url(${window.globalAddonsAssets.dislikebutton.selected_icon_src})}.dislike-img{content:url(${window.globalAddonsAssets.dislikebutton.unselected_icon_src})}`),t.wishlist&&Object.keys(window.globalAddonsAssets.wishlistbutton).length>0&&(n+=`.wishlist-img{content : url(${window.globalAddonsAssets.wishlistbutton.unselected_icon_src})}.wishlisted-img{content:url(${window.globalAddonsAssets.wishlistbutton.selected_icon_src})}`),t.shareable&&Object.keys(window.globalAddonsAssets.sharebutton).length>0&&(n+=`.share-img{content : url(${window.globalAddonsAssets.sharebutton.unselected_icon_src})}.shared-img{content:url(${window.globalAddonsAssets.sharebutton.selected_icon_src})}`),Object(r.f)(n))}(e)}return!0}(P);if(n){let e=3===v.custom_properties.widgetType?v.custom_properties.basedOn?`${v.template_type}_${v.custom_properties.basedOn}`:v.template_type:S;3===v.custom_properties.widgetType&&"boutique_tinder"===e&&(c.init(),Object(r.f)(".unbxd_recs-boutique-tinder-container{height:480px}"));let t=r.h[e];var d="#"+_+" "+t.containerId,u=document.querySelector(d);let n="vertical"==S||"mobile-browser"===!window.unbxdDeviceType?"_unbxd_recs-vertical-slider":"_unbxd_recs-slider",h="#"+_+" ."+t.sliderItemClassSelector,x=document.querySelectorAll(h);x.length||Object(i.b)("Found 0 nodes with class : "+t.sliderItemClassSelector);var p=P.config.products.fields;(function(e,t,n,r,i,o){for(var d=0;d<t.length;d++){for(var c=document.createDocumentFragment(),u=0;u<n.length;u++){var p=n[u].styles||l("styles",n[u]),m=n[u].unbxdDimensionKey||n[u].catalogKey||l("unbxdDimensionKey or catalogKey",n[u]),g=Object.keys(p);if(r[d][m]||(m=n[u].catalogKey),"imageUrl"!=m){var f=document.createElement("p"),b=r[d][m];if(f.className=i.sliderContentClass,f.tabIndex=0,f.setAttribute("role","button"),e&&e.products.strike_price_feature&&m==e.products.strike_price_feature.new.field)e&&e.products.strike_price_feature.enabled?f.innerHTML=Object(a.a)(r[d],e,o):f.innerHTML=e.products.currency+b;else if(e&&e.products.ratings_feature&&e.products.ratings_feature.enabled&&n[u].unbxdDimensionKey&&"rating"==n[u].unbxdDimensionKey.toLowerCase()){var w=Object(s.a)(r[d],e.products.ratings_feature,o,m);w&&(f.innerHTML=w)}else f.innerHTML=b?b instanceof Array?b.join(", "):b:"";if(f.innerHTML){for(var _=0;_<g.length;_++)f.style[g[_]]=p[g[_]];c.appendChild(f)}}}t[d].querySelector("._unbxd_recs_product_details").appendChild(c)}})(v,x,p=p.sort((function(e,t){return t.sequence=t.sequence||t.sequence_number,e.sequence=e.sequence||e.sequence_number,t.sequence<e.sequence?1:-1})),w,t,d);var m=T,g="#"+_+" ."+n;document.querySelector(g)||Object(i.b)("Slider Parent id was not found in the DOM"),w.length<T&&(m=w.length);let C=[];if("vertical"==S&&"boutique"!==v.template_type)for(var f=0;f<w.length;f++)if(f%y==0){var b=w.slice(f,f+y);C.push(b)}let E={selector:_,widgetWidth:D,itemsToShow:y,itemWidth:O.itemWidth,config:v,recommendationsModified:C};Object(o.a)(t,E,u,x,n,m),function(e,t,n){if(n.length<=e.itemsToShow){var r="#"+e.selector+" "+t.buttonClassSelector,o=document.querySelectorAll(r);o&&o.length||Object(i.b)(t.buttonClassSelector+"class not found on navigation buttons");for(var s=0;s<o.length;s++)o[s].style.display="none"}var a="#"+e.selector+" ."+t.prevButtonClass,d="#"+e.selector+" ."+t.customNavClass,l=document.querySelector(a),c=document.querySelector(d),u=!1;u=!!c;l||Object(i.b)(t.prevButtonClass+" class was not found on the navigation buttons");l&&(l.disabled=!0);var p="#"+e.selector+t.headingContainerId,m=e.config.header,g=document.querySelector(p);"null"==g.innerHTML||"undefined"==g.innerHTML?g.style.display="none":(g.style.textAlign=m.alignment,g.style.fontSize=m.text.size.value+m.text.size.unit,g.style.fontWeight=m.text.style,g.style.color=m.text.colour);var f=[],b={next_arrow:t.nextButtonClass,prev_arrow:t.prevButtonClass,empty_rating:"_unbxd_rex-empty-star",half_rating:"_unbxd_rex-half-star",full_rating:"_unbxd_rex-full-star"},w={next_arrow:"Next Arrow",prev_arrow:"Previous Arrow",empty_rating:"Empty star",half_rating:"half star",full_rating:"full star"};for(let e=0;e<window.assets.length;e++){var _=window.assets[e];f.push({classname:b[_.tag],altText:w[_.tag],url:_.src})}Object(i.d)(f,e.selector,u),Object(i.c)(f,e.selector,u)}(E,t,w)}}catch(e){console.error("error in rendering template",e)}};function l(e,t){throw new Error("Error: "+e+" not found in "+JSON.stringify(t))}const c={animating:!1,swipeDelta:120,dragDx:0,startX:0,deg:0,pcd:void 0,pcdReject:void 0,pcdLike:void 0,bod:document.querySelector("#widget-horizontal1"),startEve:["mousedown"],moveEve:["mousemove"],endEve:["mouseup"],init:()=>{window.bxTinderConf&&!objIsEmpty(window.bxTinderConf)&&Object.assign(c,bxTinderConf),c.startEve.forEach(e=>{c.bod.addEventListener(e,(function(e){!c.animating&&e.target.closest(".unbxdtin")&&(c.pcd=e.target.closest(".unbxdtin"),c.pcdReject=c.pcd.querySelector(".unbxddislikeablebtn"),c.pcdLike=c.pcd.querySelector(".unbxdlikeablebtn"),c.startX=e.pageX||e.targetTouches[0].pageX||e.originalEvent.touches[0].pageX,c.moveEve.forEach(e=>{c.bod.addEventListener(e,c.tinMv)}),c.endEve.forEach(e=>{c.bod.addEventListener(e,(function t(n){c.moveEve.forEach(e=>{c.bod.removeEventListener(e,c.tinMv)}),c.bod.removeEventListener(e,t),c.dragDx&&c.release()}))}))}))})},pullChange:()=>{c.animating=!0,c.deg=c.dragDx/10,c.pcd.style.transform="translateX("+c.dragDx+"px) rotate("+c.deg+"deg)";const e=c.dragDx/100,t=e>=0?0:Math.abs(e),n=e<=0?0:e;c.pcdReject.style.opacity=t,c.pcdLike.style.opacity=n},release:()=>{let e="liked";c.dragDx>=c.swipeDelta?c.pcd.classList.add("to-right"):c.dragDx<=-c.swipeDelta&&(c.pcd.classList.add("to-left"),e="disliked"),Math.abs(c.dragDx)>=c.swipeDelta&&(c.pcd.classList.add("inactive"),c.pcd.remove()),Math.abs(c.dragDx)<c.swipeDelta&&(c.pcd.classList.add("reset"),setTimeout(()=>{c.pcd.classList.remove("reset"),c.pcd.setAttribute("style",""),c.pcdLike.setAttribute("style",""),c.pcdReject.setAttribute("style","")},300)),c.dragDx=0,c.animating=!1},tinMv:e=>{const t=e.pageX||e.originalEvent.touches[0].pageX||e.targetTouches[0].pageX;c.dragDx=t-c.startX,c.dragDx&&c.pullChange()}}}).call(this,n(6))},function(e,t,n){"use strict";n.r(t),function(e){var t=n(1),r=n(2),i=n.n(r),o=n(0),s=n(8),a=(n(15),n(12)),d=n(5),l=n(13);window.generateRexContent=l.a,e._unbxd_recsSliderScrollNext=t.a._unbxd_recsSliderScrollNext,e._unbxd_recsSliderScrollPrev=t.a._unbxd_recsSliderScrollPrev,e._unbxd_recsSliderSideScroll=t.a._unbxd_recsSliderSideScroll,e.eventQueue={},e._unbxd_registerHook=function(t,n){e.eventQueue[t]=n},e._unbxd_recsSliderScrollBottom=t.a._unbxd_recsSliderScrollBottom,e._unbxd_recsSliderScrollTop=t.a._unbxd_recsSliderScrollTop,e._unbxd_recsSliderVerticalScroll=t.a._unbxd_recsSliderVerticalScroll,window.objIsEmpty=function(e){for(const t in e)if(e.hasOwnProperty(t))return!1;return!0},window.getUnbxdRecommendations=t=>{try{window.unbxdDeviceType=function(e){var t=Object(o.e)(),n=Object(o.d)();return e.unbxdDeviceType&&e.unbxdDeviceType.mobileBrowser?"mobile-browser":e.unbxdDeviceType&&e.unbxdDeviceType.desktopBrowser?"desktop-browser":t===o.a||n===o.b?"mobile-browser":"desktop-browser"}(t);var n=t.widgets;if(!(n&&n.length>0))throw new Error("No widget id provided");window.context=t,window.widgetsConfig=t.widgets;let r=["home","product","category","cart","boutique"];window.allowedPageTypes=r;let i=function(e){if(!e||!e.pageType)throw new Error("Page type info missing");var t=e.pageType;if(-1==window.allowedPageTypes.indexOf(t.toLowerCase()))throw new Error("Invalid value for page type");return t}(t.pageInfo);window.unbxdPageType=i,window.itemClickHandler=function(e){return e.itemClickHandler}(t),window.dataParser=function(e){return e.dataParser}(t),window.eventQueue=e.eventQueue,c(t)}catch(e){}};const c=e=>{try{let t=e.userInfo&&e.userInfo.userId||(void 0).getCookie("unbxd.userId"),n=e.userInfo&&e.userInfo.siteKey||window.UnbxdSiteName,r=e.userInfo&&e.userInfo.apiKey||window.UnbxdApiKey,s=i.a.production.url+r+"/"+n+"/recommendation?&template=true&pageType=";if(!t)throw new Error("user id is missing");if(!n)throw new Error("site Key is missing");if(!r)throw new Error("api key is missing");s+=encodeURIComponent(window.unbxdPageType);let d=Object(a.a)(s);if(d&&(s+=d),s+="&uid="+t,e&&e.extraParams&&"object"==typeof e.extraParams&&Object.keys(e.extraParams).length>0){let t="";Object.keys(e.extraParams).forEach((n,r)=>{r>0&&(t+="&"),t+=`${n}=${encodeURIComponent(e.extraParams[n])}`}),s+="&"+t}Object(o.c)(s,!0,u)}catch(e){}};function u(e,n,r){try{if(e)throw console.error(e,"error in widget data"),new Error("Failed to fetch recommendations",e);let i=JSON.parse(n),a=r;if(window.reqId=a,i&&i.response&&i.response.globalTemplateData&&(i.response.globalTemplateData.addOnAssets&&(window.globalAddonsAssets=i.response.globalTemplateData.addOnAssets),i.response.globalTemplateData&&i.response.globalTemplateData.boutique&&i.response.globalTemplateData.boutique[0]&&Object.keys(i.response.globalTemplateData.boutique[0]).length>0&&function(e){if(e.content&&e.position&&e.name){const t=document.createElement("a"),n=document.querySelector("body");!function(e="left",t){const n=w[e];for(var r=Object.keys(n),i=0;i<r.length;i++)t.style[r[i]]=n[r[i]]}(e.position,t),t.href="/personal-boutique",t.className="boutique",n.appendChild(t),t.innerHTML=e.content,t.firstChild.innerHTML=e.name}}(i.response.globalTemplateData.boutique[0])),i&&i.response&&i.response.widgets&&i.response.widgets.length>0){window.tc={};let e=i.response.widgets;Promise.all(e.map((function(e){if(e.count)return Object(s.b)(e)}))).then((function(){for(const l in window.tc){let c=window.tc[l],u=3===c.conf.customProperties.widgetType?c.conf.customProperties.basedOn?`${c.conf.templateType}_${c.conf.customProperties.basedOn}`:c.conf.templateType:c.orientation,g=o.h[u];var e="#"+c.selector+" "+g.containerId,n=document.querySelector(e);let f="vertical"==c.orientation||"mobile-browser"===!window.unbxdDeviceType?"_unbxd_recs-vertical-slider":"_unbxd_recs-slider",b="#"+c.selector+" ."+g.sliderItemClassSelector,w=document.querySelectorAll(b);w.length||Object(t.b)("Found 0 nodes with class : "+g.sliderItemClassSelector);var r=c.conf.products.fields;r=r.sort((function(e,t){return t.sequence=t.sequence||t.sequence_number,e.sequence=e.sequence||e.sequence_number,t.sequence<e.sequence?1:-1})),Object(s.a)(c,w,r,c.recommendations,g,e,f,c.maxProducts,e);var i=c.maxProducts,a="#"+c.selector+" ."+f;document.querySelector(a)||Object(t.b)("Slider Parent id was not found in the DOM"),c.recommendations.length<c.maxProducts&&(i=c.recommendations.length),n&&(m(g,n,c.recommendationsModified&&c.recommendationsModified.length?c.recommendationsModified:c.recommendations,c),Object(d.a)(g,c,n,w,f,i),p(c,g))}}))}}catch(e){}}function p(e,n){if(e.recommendations.length<=e.itemsToShow){var r="#"+e.selector+" "+n.buttonClassSelector,i=document.querySelectorAll(r);i&&i.length||Object(t.b)(n.buttonClassSelector+"class not found on navigation buttons");for(var o=0;o<i.length;o++)i[o].style.display="none"}var s="#"+e.selector+" ."+n.prevButtonClass,a="#"+e.selector+" ."+n.customNavClass,d=document.querySelector(s),l=!1;l=!!document.querySelector(a),d||Object(t.b)(n.prevButtonClass+" class was not found on the navigation buttons"),d&&(d.disabled=!0);var c=[],u={next_arrow:n.nextButtonClass,prev_arrow:n.prevButtonClass,empty_rating:"_unbxd_rex-empty-star",half_rating:"_unbxd_rex-half-star",full_rating:"_unbxd_rex-full-star"},p={next_arrow:"Next Arrow",prev_arrow:"Previous Arrow",empty_rating:"Empty star",half_rating:"half star",full_rating:"full star"};for(let t=0;t<e.conf.assets.length;t++){var m=e.conf.assets[t];c.push({classname:u[m.tag],altText:p[m.tag],url:m.src})}Object(t.d)(c,e.selector,l),Object(t.c)(c,e.selector,l);var g="#"+e.selector+n.headingContainerId,f=e.conf.header,b=document.querySelector(g);"null"==b.innerHTML||"undefined"==b.innerHTML?b.style.display="none":(b.style.textAlign=f.alignment,b.style.fontSize=f.text.size.value+f.text.size.unit,b.style.fontWeight=f.text.style,b.style.color=f.text.colour)}function m(e,t,n,r){window.itemClickHandler&&("width"==e.dimension?t.addEventListener("click",(function(t){const r=t.target.closest(".unbxd--like"),i=t.target.closest(".unbxd--dislike"),o=t.target.closest(".unbxd--wishlist"),s=t.target.closest(".unbxd--share");(t.target.closest(".unbxd--action--buttons")&&(r&&(r.classList.toggle("like-img"),r.classList.toggle("liked-img"),_(r,"like","unlike")),i&&(i.classList.toggle("dislike-img"),i.classList.toggle("disliked-img"),_(i,"dislike","undislike")),o&&(o.classList.toggle("wishlisted-img"),o.classList.toggle("wishlist-img"),_(o,"favourite","unfavourite")),s&&(s.classList.toggle("shared-img"),s.classList.toggle("share-img"))),"unbxd--action--buttons"!==t.target.parentElement.className)&&(t.target.className==e.sliderItemClassSelector?g(t.target.id,window.itemClickHandler,n,e.RegexExp):g(b(t.target,"."+e.sliderItemClassSelector).id,window.itemClickHandler,n,e.RegexExp))})):t.addEventListener("click",(function(t){let i="";r&&r.conf&&"vertical"===r.conf.orientation&&r.conf.customProperties&&2===r.conf.customProperties.widgetType&&(i="-eivertical");const o=t.target.closest(".unbxd--like"+i),s=t.target.closest(".unbxd--dislike"+i),a=t.target.closest(".unbxd--wishlist"+i),d=t.target.closest(".unbxd--share"+i);if(t.target.closest(".unbxd--action--buttons")&&(o&&(o.classList.toggle("like-img"),o.classList.toggle("liked-img"),_(o,"like","unlike")),s&&(s.classList.toggle("dislike-img"),s.classList.toggle("disliked-img"),_(s,"dislike","undislike")),a&&(a.classList.toggle("wishlisted-img"),a.classList.toggle("wishlist-img"),_(a,"favourite","unfavourite")),d&&(d.classList.toggle("shared-img"),d.classList.toggle("share-img"))),"unbxd--action--buttons"!==e.sliderItemClassSelector)if(t.target.className==e.sliderItemClassSelector){let r=t.target.parentElement.parentElement.id;f(t.target.id,r,window.itemClickHandler,n,e.RegexExp)}else{var l=b(t.target,"."+e.sliderItemClassSelector);let r=l.parentElement.id;f(l.id,r,window.itemClickHandler,n,e.RegexExp)}})))}function g(e,t,n,r){r.test(e)&&t(n[e.split("-")[2]])}function f(e,t,n,r,i){if(i.test(e)){var o=e.split("-")[3];n(r[t.split("-")[3]][o])}}function b(e,t){for(var n=t.charAt(0);e&&e!==document;e=e.parentNode){if("."===n&&e.classList.contains(t.substr(1)))return e;if("#"===n&&e.id===t.substr(1))return e;if("["===n&&e.hasAttribute(t.substr(1,t.length-2)))return e;if(e.tagName.toLowerCase()===t)return e}return!1}const w={right:{position:"fixed","z-index":999,right:"-70px",top:"50%",transform:"rotate(270deg) translateX(-50%)",display:"flex","text-decoration":"none"},left:{position:"fixed","z-index":999,left:"-70px",top:"50%",transform:"rotate(90deg) translateX(-50%)",display:"flex","text-decoration":"none"},bottom:{position:"fixed","z-index":999,bottom:"-1%",left:"42%",display:"flex","text-decoration":"none"}};function _(e,t,n){e.getAttribute("data-unbxdparam_globaladdons_type")===t?e.setAttribute("data-unbxdparam_globaladdons_type",n):e.setAttribute("data-unbxdparam_globaladdons_type",t)}}.call(this,n(6))},function(e,t,n){"use strict";n(7);var r=n(1),i=n(3),o=n(4),s=n(2),a=n.n(s),d=n(11),l=n(0);!function(e){function t(e,t){for(var n=t.charAt(0);e&&e!==document;e=e.parentNode){if("."===n&&e.classList.contains(t.substr(1)))return e;if("#"===n&&e.id===t.substr(1))return e;if("["===n&&e.hasAttribute(t.substr(1,t.length-2)))return e;if(e.tagName.toLowerCase()===t)return e}return!1}var n,s,c,u,p,m,g,f=a.a.production.url,b=["home","product","category","cart"],w={};w.home={widget1:"unbxd_rex_home_w1",widget2:"unbxd_rex_home_w2",widget3:"unbxd_rex_home_w3"},w.product={widget1:"unbxd_rex_product_w1",widget2:"unbxd_rex_product_w2",widget3:"unbxd_rex_product_w3"},w.category={widget1:"unbxd_rex_category_w1",widget2:"unbxd_rex_category_w2",widget3:"unbxd_rex_category_w3"},w.cart={widget1:"unbxd_rex_cart_w1",widget2:"unbxd_rex_cart_w2",widget3:"unbxd_rex_cart_w3"};e._unbxd_recsSliderScrollNext=r.a._unbxd_recsSliderScrollNext,e._unbxd_recsSliderScrollPrev=r.a._unbxd_recsSliderScrollPrev,e._unbxd_recsSliderSideScroll=r.a._unbxd_recsSliderSideScroll,e._unbxd_recsSliderScrollBottom=r.a._unbxd_recsSliderScrollBottom,e._unbxd_recsSliderScrollTop=r.a._unbxd_recsSliderScrollTop,e._unbxd_recsSliderVerticalScroll=r.a._unbxd_recsSliderVerticalScroll;var _={horizontal:{containerId:" #_unbxd_recs-slider-container",sliderItemClassSelector:" ._unbxd_recs-slider__item",dimension:"width",offsetDimension:"offsetWidth",buttonClassSelector:"._unbxd_recs-slider-btn",prevButtonClass:"_unbxd_rex-slider--prev",nextButtonClass:"_unbxd_rex-slider--next",headingContainerId:" #_unbxd_recs-slider-heading",sliderContentClass:"_unbxd_recs-slider__content"},vertical:{containerId:" #_unbxd_recs-vertical-slider-container",sliderItemClassSelector:" ._unbxd_recs-vertical-slider__item",dimension:"height",offsetDimension:"offsetHeight",buttonClassSelector:"._unbxd_recs-vertical-slider-btn",prevButtonClass:"_unbxd_rex-vertical-slider--top",nextButtonClass:"_unbxd_rex-vertical-slider--bottom",headingContainerId:" #_unbxd_recs-vertical-slider-heading",sliderContentClass:"_unbxd_recs-vertical-slider__content"}};function h(e,t){throw new Error("Error: "+e+" not found in "+JSON.stringify(t))}function x(e,t,n){/hz-item/.test(e)&&t(n[e.split("-")[2]])}function v(e,t,n,r){if(/[0-9]-vt-level2-/.test(e)){var i=e.split("-")[3];n(r[t.split("-")[3]][i])}}e.eventQueue={},e._unbxd_registerHook=function(t,n){e.eventQueue[t]=n},e._unbxd_generateRexContent=function(n){var s=n.template||h("template",n),a=n.targetDOMElementId||h("targetDOMElementId",n),d=n.recommendations||h("recommendations",n),c=n.heading||h("heading",n),u=n.rexConsoleConfigs||h("rexConsoleConfigs",n),p=u.products.visible||h("products.visible",u),m=u.products.max||h("products.max",u.products),g=n.clickHandler,f=n.dataParser,b=n.eventQueue,w=n.isVertical||!1,y=u.css||h("css",u),T=null,S=u&&u.widget&&u.widget.width?u.widget.width:null,C="";S||(S=u.width||h("products.widget.width",u.widget)),S.value&&0!=S.value&&(C=S.value+S.unit);var E,D,I=doT.template(s),k=document.getElementById(a),O=Object(l.e)(),P=Object(l.d)();if("mobile-browser"===window.unbxdDeviceType||"mobile-browser"===n.unbxdDeviceType||O===l.a||P===l.b?(E=u.products&&u.products.width&&u.products.width.value||0,D=u.products&&u.products.width&&u.products.width.unit||"px",p=(u&&u.products&&u.products.visibleOn?u.products.visibleOn.mobile:u.products.visible)||2):p=u&&u.products&&u.products.visible_products?u.products.visible_products:(p=u&&u.products&&u.products.visibleOn?u.products.visibleOn.desktop:u.products.visible_products)||2,!k)return Object(r.b)("The target element id <"+a+"> is not present in DOM. Execution can not continue");if(m<d.length&&(d=d.splice(0,m)),w){T=[];for(var q=0;q<d.length;q++)if(q%p==0){var A=d.slice(q,q+p);T.push(A)}}var L={recommendations:T||d,heading:c,analyticsData:{widgetNum:"WIDGET"+n.widgetNum,pageType:n.pageType,requestId:n.reqId}};(f&&"function"==typeof f&&(L=f(L)),b&&"function"==typeof b.beforeTemplateRender)&&(L=(0,b.beforeTemplateRender)(L));document.getElementById(a).innerHTML=I(L);var j={rexConsoleConfigs:u,recommendations:d,recommendationsModified:T,clickHandler:g,itemsToShow:p,itemWidth:E,itemWidthUnit:D,maxProducts:m,assets:n.assets,sliderType:w||"mobile-browser"===!window.unbxdDeviceType?"vertical":"horizontal",sliderClass:w||"mobile-browser"===!window.unbxdDeviceType?"_unbxd_recs-vertical-slider":"_unbxd_recs-slider",widgetWidth:C};w?e._unbxd_recsItemToScrollVt=p:(window.unbxdDeviceType,e._unbxd_recsItemToScrollHz=p);var M=document.createElement("style");(M.type="text/css",M.innerHTML=y,document.head.appendChild(M),function(e,n){var s=n.rexConsoleConfigs,a=n.recommendations,d=n.clickHandler,l=n.itemsToShow,c=n.itemWidth,u=n.itemWidthUnit,p=n.maxProducts,m=n.assets,g=n.sliderType,f=n.sliderClass,b=n.recommendationsModified,w=_[g],y="#"+e+w.containerId,T=document.querySelector(y),S=n.widgetWidth,C=s.products.ratings_feature||s.products.ratingsFeature;if(!T)return Object(r.b)("The slider container id was not found. Script can not continue");var E="#"+e+w.sliderItemClassSelector,D=document.querySelectorAll(E);if(!D.length)return Object(r.b)("Found 0 nodes with class : "+w.sliderItemClassSelector);var I=s.products.fields||h("products.fields",s);I=I.sort((function(e,t){return t.sequence=t.sequence||t.sequence_number,e.sequence=e.sequence||e.sequence_number,t.sequence<e.sequence?1:-1}));var k=w.dimension;d&&("width"==w.dimension?T.addEventListener("click",(function(e){"_unbxd_recs-slider__item"==e.target.className?x(e.target.id,d,a):x(t(e.target,"._unbxd_recs-slider__item").id,d,a)})):T.addEventListener("click",(function(e){if("_unbxd_recs-vertical-slider__item"==e.target.className){var n=e.target.parentElement.id;v(e.target.id,n,d,b)}else{var r=t(e.target,"._unbxd_recs-vertical-slider__item");n=r.parentElement.id;v(r.id,n,d,b)}})));for(var O=0;O<D.length;O++){for(var P=document.createDocumentFragment(),q=0;q<I.length;q++){var A=I[q].styles||h("styles",I[q]),L=I[q].unbxdDimensionKey||I[q].catalogKey||h("unbxdDimensionKey or catalogKey",I[q]),j=Object.keys(A);if(a[O][L]||(L=I[q].catalogKey),"imageUrl"!=L){var M=document.createElement("p");k=a[O][L];if(M.className=w.sliderContentClass,M.tabIndex=0,M.setAttribute("role","button"),s.products.strike_price_feature&&L==s.products.strike_price_feature.new.field)s.products.strike_price_feature.enabled?M.innerHTML=Object(o.a)(a[O],s,y):M.innerHTML=s.products.currency+k;else if(C&&C.enabled&&I[q].unbxdDimensionKey&&"rating"==I[q].unbxdDimensionKey.toLowerCase()){var H=Object(i.a)(a[O],C,y,L);H&&(M.innerHTML=H)}else M.innerHTML=k?k instanceof Array?k.join(", "):k:"";if(M.innerHTML){for(var N=0;N<j.length;N++)M.style[j[N]]=A[j[N]];P.appendChild(M)}}}D[O].appendChild(P)}var R="#"+e+" ."+f,W=document.querySelector(R);if(!W)return Object(r.b)("Slider Parent id was not found in the DOM");var B=p;if(a.length<p&&(B=a.length),"width"==w.dimension?setTimeout((function(){var t=document.querySelector("#"+e+" .unbxd-recs-slider"),n=t.parentElement;t.style.width=S||"initial",n.clientWidth<t.clientWidth&&(t.style.width=n.clientWidth+"px"),T.style.width=T[w.offsetDimension]+"px";var r=(T[w.offsetDimension]-10*l)/l;if(c)if("%"===u)for(var i=.01*c*T[w.offsetDimension],o=0;o<D.length;o++)D[o].style.width=i+"px",W.style.width=B*i+10*B+"px";else for(o=0;o<D.length;o++)D[o].style.width=c+u,W.style.width=B*c+10*B+u;else for(o=0;o<D.length;o++)D[o].style.width=r+"px",W.style.width=B*r+10*B+"px";document.querySelector("#"+e+" ._unxbd_slider_hide").classList.remove("_unxbd_slider_hide")}),0):setTimeout((function(){var t=document.querySelector("#"+e+" ._unbxd_vertical-recs-slider"),n=t.parentElement;if(t.style.width=S||"initial",n.clientWidth<t.clientWidth&&(t.style.width=n.clientWidth+"px"),c)for(var r=0;r<D.length;r++)D[r].style.width=c+u;else for(r=0;r<D.length;r++)D[r].style.width=t.clientWidth-20+"px";W.style.width=t.clientWidth*b.length+"px",document.querySelector("#"+e+" ._unxbd_slider_hide").classList.remove("_unxbd_slider_hide")}),0),a.length<=l){var U="#"+e+" "+w.buttonClassSelector,z=document.querySelectorAll(U);if(!z||!z.length)return Object(r.b)(w.buttonClassSelector+"class not found on navigation buttons");for(O=0;O<z.length;O++)z[O].style.display="none"}var $="#"+e+" ."+w.prevButtonClass,K=document.querySelector($);if(!K)return Object(r.b)(w.prevButtonClass+" class was not found on the navigation buttons");K.disabled=!0;var V=[],F={next_arrow:w.nextButtonClass,prev_arrow:w.prevButtonClass,empty_rating:"_unbxd_rex-empty-star",half_rating:"_unbxd_rex-half-star",full_rating:"_unbxd_rex-full-star"},Q={next_arrow:"Next Arrow",prev_arrow:"Previous Arrow",empty_rating:"Empty star",half_rating:"half star",full_rating:"full star"};for(O=0;O<m.length;O++){var X=m[O];V.push({classname:F[X.tag],altText:Q[X.tag],url:X.src})}Object(r.c)(V,e);var G="#"+e+w.headingContainerId,J=s.header,Y=document.querySelector(G);"null"==Y.innerHTML||"undefined"==Y.innerHTML?Y.style.display="none":(Y.style.textAlign=J.alignment,Y.style.fontSize=J.text.size.value+J.text.size.unit,Y.style.fontWeight=J.text.style,Y.style.color=J.text.colour)}(a,j),b&&"function"==typeof b.afterTemplateRender)&&(L=(0,b.afterTemplateRender)(w))},e.getUnbxdRecommendations=d.a,e._unbxd_getRecommendations=function(t){function r(e,t,n){var r;return n?n[t]?n[t].name:null:(r=w[e.toLowerCase()][t],document.getElementById(r)?r:null)}function i(e,t){return e+"="+encodeURIComponent(t)}var o=function(e){if(!e||!e.pageType)throw new Error("Page type info missing");var t=e.pageType;if(-1==b.indexOf(t.toLowerCase()))throw new Error("Invalid value for page type");return t}(t.pageInfo);window.unbxdDeviceType=function(e){var t=Object(l.e)(),n=Object(l.d)();return e.unbxdDeviceType&&e.unbxdDeviceType.mobileBrowser?"mobile-browser":e.unbxdDeviceType&&e.unbxdDeviceType.desktopBrowser?"desktop-browser":t===l.a||n===l.b?"mobile-browser":"desktop-browser"}(t);var a=t.widgets;if(n=r(o,"widget1",a),s=r(o,"widget2",a),c=r(o,"widget3",a),!n&&!s&&!c)throw new Error("No widget id provided");var d=function(e){return e.itemClickHandler}(t),_=function(e){return e.dataParser}(t),h=e.eventQueue,x=t.userInfo,v=x&&x.userId||function(e){for(var t,n,r=document.cookie.split(";"),i=0;i<r.length;i++)if(t=r[i].split("=")[0],n=r[i].split("=")[1],t.trim()===e)return n}("unbxd.userId"),y=x&&x.siteKey||e.UnbxdSiteName,T=x&&x.apiKey||e.UnbxdApiKey,S=f+T+"/"+y+"/items?&template=true&pageType=";if(!v)throw new Error("user id is missing");if(!y)throw new Error("site Key is missing");if(!T)throw new Error("api key is missing");S+=encodeURIComponent(o);var C,E,D,I,k,O,P=t.pageInfo;switch(o.toLowerCase()){case"product":case"cart":P.productIds&&(S+=(C=P.productIds,E="",C instanceof Array?C.forEach((function(e){E+="&"+i("id",e)})):E+="&"+i("id",C),E));break;case"category":var q="",A=P.catlevel1Name,L=P.catlevel2Name,j=P.catlevel3Name,M=P.catlevel4Name;A&&(q="&"+i("catlevel1Name",A),L&&(q+="&"+i("catlevel2Name",L),j&&(q+="&"+i("catlevel3Name",j),M&&(q+="&"+i("catlevel4Name",M))))),S+=q;break;case"home":break;default:throw new Error("Invalid page type: "+o)}function H(e,t,n,r){var i=u.products.max||u.products.max_products,s=e,a=d;n.length&&(i<n.length&&(n=n.splice(0,i)),_unbxd_generateRexContent({template:I,targetDOMElementId:s,recommendations:n,heading:r,rexConsoleConfigs:u,assets:p,maxProducts:i,clickHandler:a,dataParser:_,eventQueue:h,widgetNum:t,pageType:o,reqId:O,sliderClass:"_unbxd_recs-slider",compressedStyle:void 0}))}function N(){if(c){var e=D.widget3,t=e.widgetTitle,n=e.recommendations;r=c,i=3,s=n,a=t,l=m.products.max||m.products.max_products,u=r,p=d,s.length&&(l<s.length&&(s=s.splice(0,l)),_unbxd_generateRexContent({template:k,targetDOMElementId:u,recommendations:s,heading:a,rexConsoleConfigs:m,assets:g,maxProducts:l,clickHandler:p,eventQueue:h,dataParser:_,widgetNum:i,pageType:o,reqId:O,isVertical:!0,sliderClass:"_unbxd_recs-vertical-slider",compressedStyle:void 0}))}var r,i,s,a,l,u,p}function R(e,t){if(e)throw new Error("Failed to fetch templates");I=t,function(){if(n){var e=D.widget1,t=e.widgetTitle,r=e.recommendations;H(n,1,r,t)}if(s){var i=D.widget2,o=i.widgetTitle,a=i.recommendations;H(s,2,a,o)}}()}function W(e,t){if(e)throw new Error("Failed to fetch templates");k=t,N()}S+="&uid="+v,Object(l.c)(S,!0,(function(e,t,n){if(e)throw new Error("Failed to fetch recommendations");if(D=JSON.parse(t),I=D.template.horizontal,O=n,I){u=I.conf,p=u.assets;var r=I.scriptUrl;r?Object(l.c)(r,!1,R):console.warn("script url not found for horizontal template")}if(k=D.template.vertical){m=k.conf,g=m.assets;var i=k.scriptUrl;i?Object(l.c)(i,!1,W):console.warn("script url not found for vertical template")}}))}}(window)}]);
//# sourceMappingURL=unbxd_recs_template_sdk_gcp.js.map
var unbxdAutoSuggestFunction=function($,Handlebars,params){window.Unbxd=window.Unbxd||{};Unbxd.autosuggestVersion="1.0.1";if(!window.location.origin){window.location.origin=window.location.protocol+"//"+window.location.hostname+(window.location.port?":"+window.location.port:"")}if(!Array.prototype.forEach){Array.prototype.forEach=function(callback,thisArg){var T,k;if(this==null){throw new TypeError(" this is null or not defined")}var O=Object(this);var len=O.length>>>0;if(typeof callback!=="function"){throw new TypeError(callback+" is not a function")}if(arguments.length>1){T=thisArg}var k=0;while(k<len){var kValue;if(k in O){kValue=O[k];callback.call(T,kValue,k,O)}k++}}}if(!Array.prototype.indexOf){Array.prototype.indexOf=function(searchElement,fromIndex){var k;if(this==null){throw new TypeError('"this" is null or not defined')}var O=Object(this);var len=O.length>>>0;if(len===0){return-1}var n=+fromIndex||0;if(Math.abs(n)===Infinity){n=0}if(n>=len){return-1}k=Math.max(n>=0?n:len-Math.abs(n),0);while(k<len){if(k in O&&O[k]===searchElement){return k}k++}return-1}}var topQuery="";var isMobile={Android:function(){return navigator.userAgent.match(/Android/i)},BlackBerry:function(){return navigator.userAgent.match(/BlackBerry/i)},iOS:function(){return navigator.userAgent.match(/iPhone|iPad|iPod/i)},Opera:function(){return navigator.userAgent.match(/Opera Mini/i)},Windows:function(){return navigator.userAgent.match(/IEMobile/i)},any:function(){return isMobile.Android()||isMobile.BlackBerry()||isMobile.iOS()||isMobile.Opera()||isMobile.Windows()}};var isDesktop=function(){return!(typeof this.options.isMobile==="function"?this.options.isMobile():isMobile.any())};var customSort=function(a,b){if(a.length-b.length===0){return a.localeCompare(b)}else{return a.length-b.length}};Handlebars.registerHelper("unbxdIf",function(v1,v2,options){return v1===v2?options.fn(this):options.inverse(this)});Handlebars.registerHelper("safestring",function(value){return new Handlebars.SafeString(value)});function autocomplete(input,options){this.input=input;this.init(input,options)}function debounce(func,wait,immediate){var timeout;return function(){var context=this,args=arguments;var later=function(){timeout=null;if(!immediate)func.apply(context,args)};var callNow=immediate&&!timeout;clearTimeout(timeout);timeout=setTimeout(later,wait);if(callNow)func.apply(context,args)}}window.autoSuggestObj=$.extend(autocomplete.prototype,{default_options:{siteName:"demosite-u1407617955968",APIKey:"64a4a2592a648ac8415e13c561e44991",integrations:{},resultsClass:"unbxd-as-wrapper",minChars:3,delay:100,loadingClass:"unbxd-as-loading",mainWidth:0,sideWidth:180,zIndex:1e4,position:"absolute",sideContentOn:"right",template:"1column",theme:"#ff8400",hideOnResize:false,mainTpl:["inFields","keywordSuggestions","topQueries","popularProducts","promotedSuggestions"],sideTpl:[],showCarts:true,cartType:"inline",onCartClick:function(obj){},hbsHelpers:null,onSimpleEnter:null,onItemSelect:null,noResultTpl:null,mobile:{template:"1column",mainTpl:["inFields","keywordSuggestions","topQueries","promotedSuggestions","popularProducts"],popularProducts:{count:2}},trendingSearches:{enabled:true,tpl:"{{{safestring highlighted}}}",maxCount:6,preferInputWidthTrending:true},inFields:{count:2,fields:{brand:3,category:3,color:3},header:"",tpl:"{{{safestring highlighted}}}"},topQueries:{count:2,hidden:false,header:"",tpl:"{{{safestring highlighted}}}"},keywordSuggestions:{count:2,header:"",tpl:"{{{safestring highlighted}}}"},promotedSuggestions:{count:3,tpl:"{{{safestring highlighted}}}"},suggestionsHeader:"",popularProducts:{count:2,price:true,priceFunctionOrKey:"price",name:true,nameFunctionOrKey:"title",salePrice:false,salePriceKey:"",image:true,imageUrlOrFunction:"imageUrl",currency:"Rs.",header:"",view:"list",tpl:["{{#if ../showCarts}}",'{{#unbxdIf ../../cartType "inline"}}','<div class="unbxd-as-popular-product-inlinecart">','<div class="unbxd-as-popular-product-image-container">',"{{#if image}}",'<img src="{{image}}" alt="{{autosuggest}}"/>',"{{/if}}","</div>",'<div  class="unbxd-as-popular-product-name popular-title">','<div style="table-layout:fixed;width:100%;display:table;">','<div style="display:table-row">','<div style="display:table-cell;text-overflow:ellipsis;overflow: hidden;white-space: nowrap;">',"{{{safestring highlighted}}}","</div>","</div>","</div>","</div>","{{#if price}}",'<div class="unbxd-as-popular-product-price">',"{{#if salePrice}}",'<span class="regular-price">',"{{currency}}{{price}}","</span>",'<span class="unbxd-as-discount">',"{{currency}}{{salePrice}}","</span>","{{else}}","{{currency}}{{price}}","{{/if}}","</div>","{{/if}}",'<div class="unbxd-as-popular-product-quantity">','<div class="unbxd-as-popular-product-quantity-container">',"<span>Qty</span>",'<input class="unbxd-popular-product-qty-input" value="1"/>',"</div>","</div>",'<div class="unbxd-as-popular-product-cart-action">','<button class="unbxd-as-popular-product-cart-button">Add to cart</button>',"</div>","</div>","{{else}}",'<div class="unbxd-as-popular-product-info">','<div class="unbxd-as-popular-product-image-container">',"{{#if image}}",'<img src="{{image}}" alt="{{autosuggest}}"/>',"{{/if}}","</div>","<div>",'<div  class="unbxd-as-popular-product-name popular-title">',"{{{safestring highlighted}}}","</div>",'<div class="unbxd-as-popular-product-cart">','<div class="unbxd-as-popular-product-cart-action">','<button class="unbxd-as-popular-product-cart-button">Add to cart</button>',"</div>",'<div class="unbxd-as-popular-product-quantity">','<div class="unbxd-as-popular-product-quantity-container">',"<span>Qty</span>",'<input class="unbxd-popular-product-qty-input" value="1"/>',"</div>","</div>","{{#if price}}",'<div class="unbxd-as-popular-product-price">',"{{#if salePrice}}",'<span class="regular-price">',"{{currency}}{{price}}","</span>",'<span class="unbxd-as-discount">',"{{currency}}{{salePrice}}","</span>","{{else}}","{{currency}}{{price}}","{{/if}}","</div>","{{/if}}","</div>","</div>","</div>","{{/unbxdIf}}","{{else}}",'<div class="unbxd-as-popular-product-info">','<div class="unbxd-as-popular-product-image-container">',"{{#if image}}",'<img src="{{image}}" alt="{{autosuggest}}"/>',"{{/if}}","</div>",'<div  class="unbxd-as-popular-product-name popular-title">',"{{{safestring highlighted}}}","</div>","{{#if price}}",'<div class="unbxd-as-popular-product-price">',"{{#if salePrice}}",'<span class="regular-price">',"{{currency}}{{price}}","</span>",'<span class="unbxd-as-discount">',"{{currency}}{{salePrice}}","</span>","{{else}}","{{currency}}{{price}}","{{/if}}","</div>","{{/if}}","</div>","{{/if}}"].join(""),viewMore:{enabled:false,tpl:"",redirect:function(){}}},removeDuplicates:false,filtered:false,preferInputWidthTotalContent:false,platform:"com",sortedSuggestions:{tpl:"{{{safestring highlighted}}}"},removeOnBackButton:false,resultsContainerSelector:null,processResultsStyles:null,inputContainerSelector:"",getProductsInfo:function(that){return that.productInfo},searchEndPoint:"//search.unbxd.io"},productInfo:{},$input:null,$results:null,timeout:null,previous:"",activeRow:-1,activeColumn:0,keyb:false,compiledPopularProductHeader:"",hasFocus:false,lastKeyPressCode:null,ajaxCall:null,currentResults:[],currentTopResults:[],cache:{},params:{query:"*",filters:{}},preferOneColumnFullWidth:false,selectedClass:"unbxd-ac-selected",scrollbarWidth:null,getPopularProductsHeader:function(ctxt){var popularProductsHeader=ctxt.options.popularProducts.header;var ppHeader="";if(typeof popularProductsHeader==="string"){ppHeader=popularProductsHeader}else if(typeof popularProductsHeader==="function"){ppHeader=popularProductsHeader(ctxt)}return ppHeader},init:function(input,options){this.options=$.extend({},this.default_options,options);this.setDefaultPopularProductsOptions();this.setDefaultOptions();this.getPopularProductFields();this.$input=$(input).attr("autocomplete","off");this.$results=$("<div/>",{class:this.options.resultsClass+" "+"unbxd-as-overall-autosuggest"}).css("position",this.options.position==="relative"?"absolute":this.options.position).hide();if(this.options.zIndex>0)this.$results.css("zIndex",this.options.zIndex);if(typeof this.options.resultsContainerSelector=="string"&&this.options.resultsContainerSelector.length)$(this.options.resultsContainerSelector).append(this.$results);else $("body").append(this.$results);if(typeof this.options.hbsHelpers==="function")this.options.hbsHelpers.call(this);if(this.options.trendingSearches.enabled){this.trendingQueries=[];var trendingUrl=(this.options.searchEndPoint?this.options.searchEndPoint+"/":"https://search.unbxd.io/")+this.options.APIKey+"/"+this.options.siteName+"/autosuggest?trending-queries=true&q=*";var that=this;$.ajax({url:trendingUrl,method:"GET"}).done(function(data){if(data&&data.response.products&&data.response.products.length>0){var products=data.response.products.splice(0,that.options.trendingSearches.maxCount);that.clickResults.TRENDING_QUERIES=products;for(var i=0;i<products.length;i++){var doc=products[i];that.processTrendingQueries(doc)}that.$results.html("");var cmpld=Handlebars.compile(that.prepareTrendingQueriesHTML());that.$results.html(cmpld({data1:that.trendingQueries}))}}).fail(function(xhr){console.log("error",xhr)})}this.wire()},wire:function(){var self=this;this.$input.bind("keydown.auto",this.keyevents());this.$input.bind("select.auto",function(){self.log("select : setting focus");self.hasFocus=true});$(".unbxd-as-wrapper").on("mouseover","ul.unbxd-as-maincontent",function(e){if($.contains(self.$results[0],e.target)&&self.options.filtered){$("."+self.selectedClass).removeClass(self.selectedClass);$(e.target).addClass(self.selectedClass);var $et=$(e.target),p=$et;self.hasFocus=false;if(e.target.tagName!=="LI"){p=$et.parents("li")}var dataValue=$(p).attr("data-value")?$(p).attr("data-value"):"";var dataFiltername=$(p).attr("data-filtername")?$(p).attr("data-filtername"):"";var dataFiltervalue=$(p).attr("data-filtervalue")?$(p).attr("data-filtervalue"):"";if(!p||p.hasClass("unbxd-as-header")||p.hasClass("unbxd-as-popular-product")||p.hasClass("topproducts")||e.target.tagName==="INPUT")return;if(dataValue){var query=dataValue+(dataFiltername!=""?":"+dataFiltername+":"+dataFiltervalue:"");if(self.options.filtered){var ppHeader=self.getPopularProductsHeader(self);var cmpldHeader=Handlebars.compile(ppHeader);self.compiledPopularProductHeader=cmpldHeader({hoverSuggestion:dataValue})}var cmpld="";if(self.options.popularProducts.viewMore&&self.options.popularProducts.viewMore.enabled){if(self.options.template==="1column"){$(".unbxd-as-maincontent").addClass("unbxd-as-view-more")}else{$(".unbxd-as-sidecontent").addClass("unbxd-as-view-more")}cmpld=Handlebars.compile(self.preparefilteredPopularProducts()+self.options.popularProducts.viewMore.tpl)}else{cmpld=Handlebars.compile(self.preparefilteredPopularProducts())}if(self.currentTopResults[query]&&self.currentTopResults[query].length>0){$(".unbxd-as-sidecontent").html(cmpld({data:self.currentTopResults[query],showCarts:self.options.showCarts,cartType:self.options.cartType}))}else{$(".unbxd-as-sidecontent").html(cmpld({data:self.currentResults.POPULAR_PRODUCTS,showCarts:self.options.showCarts,cartType:self.options.cartType}))}self.hoveredQuery=dataValue}if(self.options.popularProducts.view==="grid"&&self.options.popularProducts.rowCount){$(".unbxd-as-sidecontent").find("li.unbxd-as-popular-product-grid").css("width",100/self.options.popularProducts.rowCount+"%")}}});$(window).bind("resize",function(){if(self.options.hideOnResize){self.hideResults()}});window.addEventListener("popstate",function(event){if(self.options.removeOnBackButton){$(".unbxd-as-wrapper").hide()}});$(document).bind("click.auto",function(e){if(e.target==self.input){self.log("clicked on input : focused");self.hasFocus=true;if(self.previous===self.$input.val())if(self.$results.find(".unbxd-as-trending").length){self.showResults()}else if(self.$results.find(".unbxd-as-maincontent").length||self.$results.find(".unbxd-as-sidecontent").length){self.$results.html(self.prepareHTML());self.showResults()}else{self.showResults()}}else if(e.target==self.$results[0]){self.log("clicked on results block : selecting");self.hasFocus=false}else if($(e.target).hasClass("unbxd-as-view-more")){self.options.popularProducts.viewMore.redirect(self.hoveredQuery||self.$input.val())}else if($.contains(self.$results[0],e.target)){self.log("clicked on element for selection",e.target.tagName);var $et=$(e.target),p=$et;self.hasFocus=false;if(e.target.tagName!=="LI"){p=$et.parents("li")}if(!p||p.hasClass(".unbxd-as-header")||e.target.tagName=="INPUT")return;if(e.target.tagName=="BUTTON"&&$et.hasClass("unbxd-as-popular-product-cart-button")&&typeof self.options.onCartClick=="function"){self.log("BUTTON click");var data=p.data();data.quantity=parseFloat(p.find("input.unbxd-popular-product-qty-input").val());self.addToAnalytics("click",{pr:parseInt(data.index)+1,pid:data.pid||null,url:window.location.href});self.options.onCartClick.call(self,data,self.currentResults.POPULAR_PRODUCTS[parseInt(data["index"])]._original)&&self.hideResults();self.addToAnalytics("addToCart",{pid:data.pid||null,url:window.location.href});return}self.selectItem(p.data(),e)}else{self.hasFocus=false;self.hideResults()}});if(self.options.trendingSearches.enabled&&self.clickResults.TRENDING_QUERIES.length){$(document).bind("keyup.auto",function(e){if(e.target.value===""){self.$results.html("");var cmpld=Handlebars.compile(self.prepareTrendingQueriesHTML());self.$results.html(cmpld({data1:self.trendingQueries}));self.showResults()}})}},keyevents:function(){var self=this;if(params&&params.selfServe){self.onChange()}else{return function(e){self.lastKeyPressCode=e.keyCode;self.lastKeyEvent=e;switch(e.keyCode){case 38:e.preventDefault();self.moveSelect(-1);break;case 40:e.preventDefault();self.moveSelect(1);break;case 39:if(self.activeRow>-1){e.preventDefault();self.moveSide(1)}break;case 37:if(self.activeRow>-1){e.preventDefault();self.moveSide(-1)}break;case 9:case 13:if(self.selectCurrent(e)){e.preventDefault()}else{self.hideResultsNow()}break;default:self.activeRow=-1;self.hasFocus=true;if(self.timeout)clearTimeout(self.timeout);self.timeout=setTimeout(debounce(function(){self.onChange()},250),self.options.delay);break}}}},moveSide:function(step){var newcolumn=this.activeColumn;if(this.options.template=="2column"){if(this.options.sideContentOn=="left"){this.activeColumn==0&&step==-1&&(newcolumn=1);this.activeColumn==1&&step==1&&(newcolumn=0)}else{this.activeColumn==0&&step==1&&(newcolumn=1);this.activeColumn==1&&step==-1&&(newcolumn=0)}if(newcolumn!=this.activeColumn){this.activeColumn=newcolumn;this.activeRow=-1;this.moveSelect(1)}}},moveSelect:function(step){var lis=this.$results.find("ul."+(this.activeColumn?"unbxd-as-sidecontent":"unbxd-as-maincontent")).find("li:not(.unbxd-as-header)");if(!lis)return;this.activeRow+=step;if(this.activeRow<-1)this.activeRow=(typeof lis.size==="function"?lis.size():lis.length)-1;else if(this.activeRow==-1)this.$input.focus();else if(this.activeRow>=(typeof lis.size==="function"?lis.size():lis.length)){this.activeRow=-1;this.$input.focus()}$("."+this.selectedClass).removeClass(this.selectedClass);$(lis[this.activeRow]).addClass(this.selectedClass);if(this.activeRow>=0&&this.activeRow<(typeof lis.size==="function"?lis.size():lis.length)){this.$input.val($(lis[this.activeRow]).data("value"));if(this.options.filtered&&this.activeColumn===0){var dataValue=$(lis[this.activeRow]).attr("data-value")?$(lis[this.activeRow]).attr("data-value"):"";var dataFiltername=$(lis[this.activeRow]).attr("data-filtername")?$(lis[this.activeRow]).attr("data-filtername"):"";var dataFiltervalue=$(lis[this.activeRow]).attr("data-filtervalue")?$(lis[this.activeRow]).attr("data-filtervalue"):"";var query=dataValue+(dataFiltername!=""?":"+dataFiltername+":"+dataFiltervalue:"");if(this.options.filtered){var ppHeader=this.getPopularProductsHeader(this);var cmpldHeader=Handlebars.compile(ppHeader);this.compiledPopularProductHeader=cmpldHeader({hoverSuggestion:dataValue})}var cmpld="";if(this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){$(".unbxd-as-sidecontent").addClass("unbxd-as-view-more");cmpld=Handlebars.compile(this.preparefilteredPopularProducts()+this.options.popularProducts.viewMore.tpl)}else{cmpld=Handlebars.compile(this.preparefilteredPopularProducts())}if(this.currentTopResults[query]&&this.currentTopResults[query].length>0){$(".unbxd-as-sidecontent").html(cmpld({data:this.currentTopResults[query],showCarts:this.options.showCarts,cartType:this.options.cartType}))}else{$(".unbxd-as-sidecontent").html(cmpld({data:this.currentResults.POPULAR_PRODUCTS,showCarts:this.options.showCarts,cartType:this.options.cartType}))}if(this.options.popularProducts.view==="grid"&&this.options.popularProducts.rowCount){this.$results.find("ul li.unbxd-as-popular-product-grid").css("width",100/this.options.popularProducts.rowCount+"%")}}}else if(this.activeRow==-1){this.$input.val(this.previous);if(this.options.filtered){var cmpld="";if(this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){$(".unbxd-as-sidecontent").addClass("unbxd-as-view-more");cmpld=Handlebars.compile(this.preparefilteredPopularProducts()+this.options.popularProducts.viewMore.tpl)}else{cmpld=Handlebars.compile(this.preparefilteredPopularProducts())}if(this.currentTopResults[this.previous]&&this.currentTopResults[this.previous].length>0)$(".unbxd-as-sidecontent").html(cmpld({data:this.currentTopResults[this.previous],showCarts:this.options.showCarts,cartType:this.options.cartType}));else $(".unbxd-as-sidecontent").html(cmpld({data:this.currentResults.POPULAR_PRODUCTS,showCarts:this.options.showCarts,cartType:this.options.cartType}));if(this.options.popularProducts.view==="grid"&&this.options.popularProducts.rowCount){this.$results.find("ul li.unbxd-as-popular-product-grid").css("width",100/this.options.popularProducts.rowCount+"%")}}}},selectCurrent:function(e){var li=this.$results.find("li."+this.selectedClass),self=this;if(li.length){this.selectItem(li.data(),e);return true}else{if(typeof this.options.onSimpleEnter=="function"&&(this.lastKeyPressCode==10||this.lastKeyPressCode==13)){this.lastKeyEvent.preventDefault();self.options.onSimpleEnter.call(self,e)}return false}},selectItem:function(data,e){if(!("value"in data))return;this.log("selected Item : ",data);var v=$.trim(data["value"]),prev=this.previous;this.previous=v;this.input.lastSelected=data;this.$results.html("");this.$input.val(v);this.hideResultsNow(this);this.addToAnalytics("search",{query:data.value,autosuggestParams:{autosuggest_type:data.type,autosuggest_suggestion:data.value,field_value:data.filtervalue||null,field_name:data.filtername||null,src_field:data.source||null,pid:data.pid||null,unbxdprank:parseInt(data.index,10)+1||0,internal_query:prev}});if(typeof this.options.onItemSelect=="function"&&data.type!=="POPULAR_PRODUCTS_FILTERED"){if(data.sorted){this.options.onItemSelect.call(this,data,this.currentResults["SORTED_SUGGESTIONS"][parseInt(data["index"])]._original,e)}else{this.options.onItemSelect.call(this,data,this.currentResults[data.type][parseInt(data["index"])]._original,e)}}else if(data.type==="POPULAR_PRODUCTS_FILTERED"){this.options.onItemSelect.call(this,data,this.currentTopResults[data.src][parseInt(data["index"])]._original,e)}},addToAnalytics:function(type,obj){if("Unbxd"in window&&"track"in window.Unbxd&&typeof window.Unbxd.track=="function"){this.log("Pushing data to analytics",type,obj);Unbxd.track(type,obj)}if(type!=="search")return;if("classical"in this.options.integrations){this.trackclassical(type,obj)}if("universal"in this.options.integrations){this.trackuniversal(type,obj)}},getEventAction:function(autosuggestType){var types={IN_FIELD:"Scope_Click",POPULAR_PRODUCTS:"Pop_Click",KEYWORD_SUGGESTION:"TQ_Click",TOP_SEARCH_QUERIES:"TQ_Click",POPULAR_PRODUCTS_FILTERED:"Filtered_Pop_Click",PROMOTED_SUGGESTION:"TQ_Click"};return types[autosuggestType]},getEventLabel:function(autosuggest){var params=autosuggest.autosuggestParams;var value=params.autosuggest_suggestion;var index=params.unbxdprank;var filter=params.field_name&&params.field_value?params.field_name+":"+params.field_value:undefined;var types={IN_FIELD:value+(filter?"&filter="+filter:"")+"-"+index,POPULAR_PRODUCTS:value+"-"+index,KEYWORD_SUGGESTION:value+"-"+index,TOP_SEARCH_QUERIES:value+"-"+index,POPULAR_PRODUCTS_FILTERED:value+"-"+index,PROMOTED_SUGGESTION:value+"-"+index};return types[params.autosuggest_type]},trackclassical:function(type,obj){var key=this.options.integrations["classical"],eventAction=this.getEventAction(obj.autosuggestParams.autosuggest_type),eventLabel=this.getEventLabel(obj),value=1;if(key){if(key===true)key="_gaq";if(window[key])window[key].push(["_trackEvent","U_Autocomplete",eventAction,eventLabel,value,true])}},trackuniversal:function(type,obj){var key=this.options.integrations["universal"],eventAction=this.getEventAction(obj.autosuggestParams.autosuggest_type),eventLabel=this.getEventLabel(obj),value=1;if(key){if(key===true)key="ga";if(window[key])window[key]("send","event","U_Autocomplete",eventAction,eventLabel,value,{nonInteraction:1})}},showResults:function(){if(this.options.width){this.options.mainWidth=this.options.width}var posSelector=this.options.inputContainerSelector?$(this.options.inputContainerSelector):this.$input;var pos=posSelector.offset();var totalWidth="";var mwidth="";if(this.options.platform=="io"){totalWidth=this.options.preferInputWidthTotalContent?posSelector.outerWidth():this.options.sideContentOn&&this.options.sideContentOn==="left"?pos.left+posSelector.outerWidth():document.body.clientWidth-pos.left;if(totalWidth>document.body.clientWidth){totalWidth=document.body.clientWidth}if(totalWidth>788&&totalWidth<2e3){totalWidth=this.options.totalWidthPercent?this.options.totalWidthPercent*totalWidth/100:70*totalWidth/100}else if(totalWidth>2e3){totalWidth=45*totalWidth/100}if(this.options.isMobile&&this.options.isMobile()||isMobile.any()){this.options.template=this.options.mobile.template;this.options.mainTpl=this.options.mobile.mainTpl;this.options.popularProducts.count=this.options.mobile.popularProducts.count}else{this.options.template=this.options.desktop.template.column;this.options.mainTpl=this.options.desktop.mainTpl;this.options.popularProducts.count=this.options.desktop.popularProducts.count}if(this.options.template=="1column"){var preferInputWidthMainContent=this.options.preferInputWidthMainContent;if(isDesktop.call(this)){preferInputWidthMainContent=this.options.desktop.template[this.options.desktop.template.column].preferInputWidthMainContent;$(".unbxd-as-popular-product-info").addClass("unbxd-1column-popular-product-desktop")}mwidth=preferInputWidthMainContent?posSelector.outerWidth():60*totalWidth/100}else{mwidth=this.options.mainWidthPercent?this.options.mainWidthPercent*totalWidth/100:30*totalWidth/100}}var iWidth=this.options.mainWidth>0?this.options.mainWidth:totalWidth?mwidth:posSelector.innerWidth(),bt=parseInt(posSelector.css("border-top-width"),10),bb=parseInt(posSelector.css("border-bottom-width"),10),bl=parseInt(posSelector.css("border-left-width"),10),br=parseInt(posSelector.css("border-right-width"),10),pb=parseInt(posSelector.css("padding-bottom"),10),fwidth=parseInt(iWidth)-2+bl+br,fpos={top:pos.top+(isNaN(bt)?0:bt+bb)+posSelector.innerHeight()+"px",left:pos.left+"px"};var trendingWidth=this.options.trendingSearches.preferInputWidthTrending?posSelector.outerWidth():fwidth;this.$results.find("ul.unbxd-as-maincontent").css("width",fwidth+"px");this.$results.find("ul.unbxd-as-maincontent").css("box-sizing","border-box");this.$results.find("ul.unbxd-as-maincontent.unbxd-as-trending").css("width",trendingWidth+"px");if(this.scrollbarWidth==null){this.setScrollWidth()}if(this.options.template=="2column"){var swidth=this.options.sideWidth!==this.default_options.sideWidth?this.options.sideWidth:totalWidth?totalWidth-fwidth:this.options.sideWidth;this.$results.find("ul.unbxd-as-sidecontent").css("width",swidth+"px");this.$results.find("ul.unbxd-as-sidecontent").css("box-sizing","border-box");this.$results.removeClass("unbxd-as-extra-left unbxd-as-extra-right");this.$results.addClass("unbxd-as-extra-"+this.options.sideContentOn);if(this.$results.find("ul.unbxd-as-sidecontent").length>0&&this.options.sideContentOn=="left"){var lwidth=pos.left+posSelector.outerWidth()>document.body.clientWidth?document.body.clientWidth:pos.left+posSelector.outerWidth();fpos.left=lwidth-fwidth-swidth;if(fpos.left<0){fpos.left=0}if(this.$results.find("ul.unbxd-as-maincontent").length==0){fpos.left=fpos.left+fwidth}fpos.left=fpos.left+"px"}if(this.options.popularProducts.view==="grid"&&this.options.popularProducts.rowCount){this.$results.find("ul li.unbxd-as-popular-product-grid").css("width",100/this.options.popularProducts.rowCount+"%")}}if(this.options.showCarts)this.$results.find(".unbxd-as-popular-product-cart-button").css("background-color",this.options.theme);if(typeof this.options.processResultsStyles=="function"){fpos=this.options.processResultsStyles.call(this,fpos)}this.$results.css(fpos).show()},setScrollWidth:function(){var scrollDiv=document.createElement("div");scrollDiv.setAttribute("style","width: 100px;height: 100px;overflow: scroll;position: absolute;top: -9999px;");document.body.appendChild(scrollDiv);this.scrollbarWidth=scrollDiv.offsetWidth-scrollDiv.clientWidth;document.body.removeChild(scrollDiv)},hideResults:function(){if(this.timeout)clearTimeout(this.timeout);var self=this;this.timeout=setTimeout(function(){self.hideResultsNow()},200)},hideResultsNow:function(){this.log("hideResultsNow");if(this.timeout)clearTimeout(this.timeout);this.$input.removeClass(this.options.loadingClass);if(this.$results.is(":visible")){this.$results.hide()}if(this.ajaxCall)this.ajaxCall.abort()},addFilter:function(field,value){if(!(field in this.params.filters))this.params.filters[field]={};this.params.filters[field][value]=field;return this},removeFilter:function(field,value){if(value in this.params.filters[field])delete this.params.filters[field][value];if(Object.keys(this.params.filters[field]).length==0)delete this.params.filters[field];return this},clearFilters:function(){this.params.filters={};return this},onChange:function(){if(this.lastKeyPressCode==46||this.lastKeyPressCode>8&&this.lastKeyPressCode<32){if(this.lastKeyPressCode==27&&typeof this.input.lastSelected=="object"){this.$input.val(this.input.lastSelected.value)}return this.$results.hide()}var v="";if(params&&params.selfServe){v="*"}else{v=this.$input.val()}if(v==this.previous)return;this.params.q=v;this.previous=v;this.currentResults={KEYWORD_SUGGESTION:[],TOP_SEARCH_QUERIES:[],POPULAR_PRODUCTS:[],IN_FIELD:[],SORTED_SUGGESTIONS:[],PROMOTED_SUGGESTION:[]};if(this.inCache(v)){this.log("picked from cache : "+v);this.currentResults=this.getFromCache(v);this.productInfo.popularProductsCount=this.currentResults.POPULAR_PRODUCTS.length;if(this.options.filtered){var ppHeader=this.getPopularProductsHeader(this);var cmpldHeader=Handlebars.compile(ppHeader);this.compiledPopularProductHeader=cmpldHeader({hoverSuggestion:v})}this.$results.html(this.prepareHTML());this.showResults()}else{if(this.ajaxCall)this.ajaxCall.abort();if(v.length>=this.options.minChars){this.$input.addClass(this.options.loadingClass);this.requestData(v)}else{this.$input.removeClass(this.options.loadingClass);if(!(this.options.trendingSearches.enabled&&this.clickResults.TRENDING_QUERIES.length>0&&v==="")){this.$results.hide()}}}},getClass:function(object){return Object.prototype.toString.call(object).match(/^\[object\s(.*)\]$/)[1]},requestData:function(q){var self=this,url=self.autosuggestUrl();this.log("requestData",url);var params=this.getAjaxParams();params.url=url;params.cache=true;this.ajaxCall=$.ajax(params).done(function(d){self.receiveData(d)}).fail(function(f){self.$input.removeClass(self.options.loadingClass);self.$results.hide()})},getHostDomainName:function(){if(this.options.platform==="com"){return"//search.unbxdapi.com/"}else{return this.options.searchEndPoint+"/"}},getAjaxParams:function(){var params={};if(this.options.platform==="io"){params={dataType:"json",method:"get"}}else{params={dataType:"jsonp",jsonp:"json.wrf"}}return params},autosuggestUrl:function(){var host_path=this.getHostNPath();var query=this.params.q;if(this.options.customQueryParse&&typeof this.options.customQueryParse==="function"){query=this.options.customQueryParse(this.params.q)}var url="q="+encodeURIComponent(query);if(this.options.maxSuggestions){url+="&inFields.count="+this.options.maxSuggestions+"&topQueries.count="+this.options.maxSuggestions+"&keywordSuggestions.count="+this.options.maxSuggestions+"&popularProducts.count="+this.options.popularProducts.count+"&promotedSuggestion.count="+this.options.maxSuggestions+"&indent=off"}else{url+="&inFields.count="+this.options.inFields.count+"&topQueries.count="+this.options.topQueries.count+"&keywordSuggestions.count="+this.options.keywordSuggestions.count+"&popularProducts.count="+this.options.popularProducts.count+"&promotedSuggestion.count="+this.options.promotedSuggestions.count+"&indent=off"}if(this.options.popularProducts.fields.length>0){var popularProductFields=this.options.popularProducts.fields.join(",");url=url+"&popularProducts.fields="+popularProductFields}if(this.options.removeDuplicates){url=url+"&variants=true"}for(var x in this.params.filters){if(this.params.filters.hasOwnProperty(x)){var a=[];for(var y in this.params.filters[x]){if(this.params.filters[x].hasOwnProperty(y)){a.push((x+':"'+encodeURIComponent(y.replace(/(^")|("$)/g,""))+'"').replace(/\"{2,}/g,'"'))}}url+="&filter="+a.join(" OR ")}}var extraParams=this.options.extraParams||{};var extraParamsKeys=Object.keys(extraParams);if(extraParamsKeys.length){extraParamsKeys.forEach(key=>{url=url+"&"+key+"="+extraParams[key]})}return host_path+"?"+url},getHostNPath:function(){return this.getHostDomainName()+this.options.APIKey+"/"+this.options.siteName+"/autosuggest"},receiveData:function(data){if(data){this.$input.removeClass(this.options.loadingClass);this.$results.html("");if(!this.hasFocus&&(params?!params.selfServe:true)||data.response.numberOfProducts==0||"error"in data){if(!this.options.noResultTpl){return this.hideResultsNow(this)}}this.processData(data);this.addToCache(this.params.q,this.currentResults);this.$results.html(this.prepareHTML());this.showResults()}else{this.hideResultsNow(this)}},max_suggest:function(data){var infield_result=0,topquery_result=0,keyword_result=0,promoted_result=0;var infield_sugg=Math.floor(this.options.maxSuggestions*.2);var keyword_sugg=Math.floor(this.options.maxSuggestions*.3);var topquery_sugg=Math.ceil(this.options.maxSuggestions*.3);var promoted_sugg=Math.floor(this.options.maxSuggestions*.2);var keyword_rem=0,topquery_rem=0,promoted_rem=0;for(var x=0;x<data.response.products.length;x++){if(data.response.products[x].doctype=="IN_FIELD"){infield_result++}else if(data.response.products[x].doctype=="KEYWORD_SUGGESTION"){keyword_result++}else if(data.response.products[x].doctype=="TOP_SEARCH_QUERIES"){topquery_result++}else if(data.response.products[x].doctype=="PROMOTED_SUGGESTION"){promoted_result++}}if(infield_result<infield_sugg){var infield_rem=infield_sugg-infield_result;while(infield_rem>0){if(keyword_result>keyword_sugg){if(keyword_result-keyword_sugg>=infield_rem){keyword_sugg=keyword_sugg+infield_rem;infield_rem=0}else{infield_rem=infield_rem-keyword_result+keyword_sugg;keyword_sugg=keyword_result}}else if(topquery_result>topquery_sugg){if(topquery_result-topquery_sugg>=infield_rem){topquery_sugg=topquery_sugg+infield_rem;infield_rem=0}else{infield_rem=infield_rem-topquery_result+topquery_sugg;topquery_sugg=topquery_result}}else if(promoted_result>promoted_sugg){if(promoted_result-promoted_sugg>=infield_rem){promoted_sugg=promoted_sugg+infield_rem;infield_rem=0}else{infield_rem=infield_rem-promoted_result+promoted_sugg;promoted_sugg=promoted_result}}else infield_rem=0}infield_sugg=infield_result}if(topquery_result<topquery_sugg){var topquery_rem=topquery_sugg-topquery_result;while(topquery_rem>0&&keyword_result>keyword_sugg){if(keyword_result>keyword_sugg){if(keyword_result-keyword_sugg>=topquery_rem){keyword_sugg=keyword_sugg+topquery_rem;topquery_rem=0}else{topquery_rem=topquery_rem-keyword_result+keyword_sugg;keyword_sugg=keyword_result}}else if(promoted_result>promoted_sugg){if(promoted_result-promoted_sugg>=topquery_rem){promoted_sugg=promoted_sugg+topquery_rem;topquery_rem=0}else{topquery_rem=topquery_rem-promoted_result+promoted_sugg;promoted_sugg=promoted_result}}}topquery_sugg=topquery_result}if(keyword_result<keyword_sugg){keyword_rem=keyword_sugg-keyword_result;while(keyword_rem>0&&topquery_result>topquery_sugg){if(topquery_result>topquery_sugg){if(topquery_result-topquery_sugg>=keyword_rem){topquery_sugg=topquery_sugg+keyword_rem;keyword_rem=0}else{keyword_rem=keyword_rem-topquery_result+topquery_sugg;topquery_sugg=topquery_result}}else if(promoted_result>promoted_sugg){if(promoted_result-promoted_sugg>=keyword_rem){promoted_sugg=promoted_sugg+keyword_rem;keyword_rem=0}else{keyword_rem=keyword_rem-promoted_result+promoted_sugg;promoted_sugg=promoted_result}}}keyword_sugg=keyword_result}if(promoted_result<promoted_sugg){promoted_rem=promoted_sugg-promoted_result;while(promoted_rem>0){if(topquery_result>topquery_sugg){if(topquery_result-topquery_sugg>=promoted_rem){topquery_sugg=topquery_sugg+promoted_rem;promoted_rem=0}else{promoted_rem=promoted_rem-topquery_result+topquery_sugg;topquery_sugg=topquery_result}}else if(keyword_result>keyword_sugg){if(keyword_result-keyword_sugg>=promoted_rem){keyword_sugg=keyword_sugg+promoted_rem;promoted_rem=0}else{promoted_rem=promoted_rem-keyword_result+keyword_sugg;keyword_sugg=keyword_result}}else promoted_rem=0}promoted_sugg=promoted_result}var count={};count["infields"]=infield_sugg;count["topquery"]=topquery_sugg;count["promoted"]=promoted_sugg;count["keyword"]=keyword_sugg;count["key_rem"]=keyword_rem;count["top_rem"]=topquery_rem;count["promo_rem"]=promoted_rem;return count},isUnique:function(autosuggest,arr){try{autosuggest=autosuggest.toLowerCase();var unique=true;for(var k=0;k<arr.length;k++){var suggestion=arr[k];if(Math.abs(suggestion.length-autosuggest.length)<3&&(suggestion.indexOf(autosuggest)!=-1||autosuggest.indexOf(suggestion)!=-1)){unique=false;break}}if(unique)arr.push(autosuggest);return unique}catch(e){return true}},isTempUnique:function(autosuggest,arr){autosuggest=autosuggest.toLowerCase();return arr.indexOf(autosuggest)===-1?arr.push(autosuggest):false},getfilteredPopularProducts:function(){var query=this.params.q;if(this.options.customQueryParse&&typeof this.options.customQueryParse==="function"){query=this.options.customQueryParse(this.params.q)}var self=this,urlPath=this.getHostDomainName()+this.options.APIKey+"/"+this.options.siteName+"/search",defaultSearchParams="indent=off&facet=off&analytics=false&redirect=false",url=urlPath+"?q="+encodeURIComponent(query)+"&rows="+this.options.popularProducts.count+"&"+defaultSearchParams;if(self.options.popularProducts.fields.length>0){var popularProductFields="&fields="+self.options.popularProducts.fields.join(",");url=url+popularProductFields}if(self.options.removeDuplicates){url=url+"&variants=true"}var extraParams=self.options.extraParams||{};var extraParamsKeys=Object.keys(extraParams);if(extraParamsKeys.length){extraParamsKeys.forEach(key=>{url=url+"&"+key+"="+extraParams[key]})}var params=this.getAjaxParams();params.url=url;params.cache=true;$.ajax(params).done(function(d){var query=self.params.q;self.processfilteredPopularProducts(query,d)});for(var i in this.currentResults){if(i!="POPULAR_PRODUCTS"&&this.currentResults.hasOwnProperty(i)){for(var j in this.currentResults[i]){if(this.currentResults[i].hasOwnProperty(j)){if(this.currentResults[i][j]["filtername"]){url=urlPath+"?q="+encodeURIComponent(this.currentResults[i][j]["autosuggest"])+"&filter="+this.currentResults[i][j]["filtername"]+':"'+encodeURIComponent(this.currentResults[i][j]["filtervalue"])+'"&rows='+this.options.popularProducts.count+popularProductFields+"&"+defaultSearchParams}else{url=urlPath+"?q="+encodeURIComponent(this.currentResults[i][j]["autosuggest"])+"&rows="+this.options.popularProducts.count+popularProductFields+"&"+defaultSearchParams}var params=this.getAjaxParams();params.url=url;params.cache=true;$.ajax(params).done(function(d){var query=d.searchMetaData.queryParams.q+(d.searchMetaData.queryParams.filter?":"+d.searchMetaData.queryParams.filter.replace(/"/g,""):"");self.processfilteredPopularProducts(query,d)})}}}}},processfilteredPopularProducts:function(query,d){this.currentTopResults[query]=[];if(d.hasOwnProperty("response")&&d.response.hasOwnProperty("products")&&d.response.products.length){for(var k=0;k<d.response.products.length;k++){var doc=d.response.products[k];var o={_original:doc,type:"POPULAR_PRODUCTS_FILTERED",src:query,pid:doc.uniqueId||""};if(this.options.popularProducts.name&&this.options.popularProducts.nameFunctionOrKey){o.autosuggest=doc[this.options.popularProducts.nameFunctionOrKey]}else if(this.options.popularProducts.autosuggestName&&doc[this.options.popularProducts.autosuggestName]){o.autosuggest=doc[this.options.popularProducts.autosuggestName]}else if(this.options.popularProducts.title&&doc[this.options.popularProducts.title]){o.autosuggest=doc[this.options.popularProducts.title]}else if(doc.title){o.autosuggest=doc.title}else{o.autosuggest=""}o.highlighted=this.highlightStr(o.autosuggest);if(this.options.popularProducts.price){if(typeof this.options.popularProducts.priceFunctionOrKey==="function"){o.price=this.options.popularProducts.priceFunctionOrKey(doc)}else if(typeof this.options.popularProducts.priceFunctionOrKey==="string"&&this.options.popularProducts.priceFunctionOrKey){o.price=this.options.popularProducts.priceFunctionOrKey in doc?doc[this.options.popularProducts.priceFunctionOrKey]:null}else{o.price="price"in doc?doc["price"]:null}if(this.options.popularProducts.currency)o.currency=this.options.popularProducts.currency}if(this.options.popularProducts.salePrice&&this.options.popularProducts.salePriceKey){o.salePrice=this.options.popularProducts.salePriceKey in doc?doc[this.options.popularProducts.salePriceKey]:null}if(this.options.popularProducts.image){if(typeof this.options.popularProducts.imageUrlOrFunction==="function"){o.image=this.options.popularProducts.imageUrlOrFunction(doc)}else if(typeof this.options.popularProducts.imageUrlOrFunction==="string"&&this.options.popularProducts.imageUrlOrFunction){o.image=this.options.popularProducts.imageUrlOrFunction in doc?doc[this.options.popularProducts.imageUrlOrFunction]:null}}this.currentTopResults[query].push(o)}}},processTopSearchQuery:function(doc){var o={autosuggest:doc.autosuggest,highlighted:this.highlightStr(doc.autosuggest),type:"TOP_SEARCH_QUERIES",_original:doc.doctype};this.currentResults.TOP_SEARCH_QUERIES.push(o)},processTrendingQueries:function(doc){var o={autosuggest:doc.autosuggest,highlighted:this.highlightStr(doc.autosuggest),type:"TRENDING_QUERIES",_original:doc,source:doc.unbxdAutosuggestSrc||""};this.trendingQueries.push(o)},processKeywordSuggestion:function(doc){var o={autosuggest:doc.autosuggest,highlighted:this.highlightStr(doc.autosuggest),type:"KEYWORD_SUGGESTION",_original:doc,source:doc.unbxdAutosuggestSrc||""};this.currentResults.KEYWORD_SUGGESTION.push(o)},processPromotedSuggestion:function(doc){var o={autosuggest:doc.autosuggest,highlighted:this.highlightStr(doc.autosuggest),type:"PROMOTED_SUGGESTION",_original:doc,source:doc.unbxdAutosuggestSrc||""};this.currentResults.PROMOTED_SUGGESTION.push(o)},setDefaultPopularProductsOptions:function(){if(!this.options.popularProducts.autosuggestName){this.options.popularProducts.autosuggestName="title"}if(!this.options.popularProducts.title){this.options.popularProducts.title="autosuggest"}if(!this.options.popularProducts.fields){this.options.popularProducts.fields=[]}if(!this.options.popularProducts.rowCount&&this.options.platform==="io"){this.options.popularProducts.rowCount=this.options.popularProducts.count/2}},setDefaultOptions:function(){if(!this.options.inFields.type){this.options.inFields.type="separate"}if(!this.options.inFields.noOfInfields){this.options.inFields.noOfInfields=3}if(!this.options.inFields.showDefault){this.options.inFields.showDefault=false}if(!this.options.desktop){this.options.desktop={template:{column:this.options.template,"1column":{preferInputWidthMainContent:this.options.preferOneColumnFullWidth},"2column":{preferInputWidthMainContent:this.options.preferInputWidthMainContent}},mainTpl:this.options.mainTpl,popularProducts:{count:this.options.popularProducts.count}}}},getPopularProductFields:function(){var popularProductsFields=["doctype"];this.options.popularProducts.fields.push(this.options.popularProducts.title);if(this.options.popularProducts.price&&typeof this.options.popularProducts.priceFunctionOrKey=="string"&&this.options.popularProducts.priceFunctionOrKey){popularProductsFields.push(this.options.popularProducts.priceFunctionOrKey)}if(this.options.popularProducts.image){if(typeof this.options.popularProducts.imageUrlOrFunction=="string"&&this.options.popularProducts.imageUrlOrFunction){popularProductsFields.push(this.options.popularProducts.imageUrlOrFunction)}}if(this.options.popularProducts.fields.length>0){this.options.popularProducts.fields=popularProductsFields.concat(this.options.popularProducts.fields)}else{this.options.popularProducts.fields=popularProductsFields}var ppHeader=this.getPopularProductsHeader(this);this.compiledPopularProductHeader=ppHeader},processPopularProducts:function(doc){var o={type:doc.doctype,pid:doc.uniqueId.replace("popularProduct_",""),_original:doc};if(this.options.popularProducts.name){o.autosuggest=doc[this.options.popularProducts.nameFunctionOrKey]?doc[this.options.popularProducts.nameFunctionOrKey]:doc[this.options.popularProducts.title]?doc[this.options.popularProducts.title]:""}else{o.autosuggest=""}o.highlighted=this.highlightStr(o.autosuggest);if(this.options.popularProducts.price){if(typeof this.options.popularProducts.priceFunctionOrKey=="function"){o.price=this.options.popularProducts.priceFunctionOrKey(doc)}else if(typeof this.options.popularProducts.priceFunctionOrKey=="string"&&this.options.popularProducts.priceFunctionOrKey){o.price=this.options.popularProducts.priceFunctionOrKey in doc?doc[this.options.popularProducts.priceFunctionOrKey]:null}else{o.price="price"in doc?doc["price"]:null}}if(this.options.popularProducts.salePrice&&this.options.popularProducts.salePriceKey){o.salePrice=this.options.popularProducts.salePriceKey in doc?doc[this.options.popularProducts.salePriceKey]:null}if(this.options.popularProducts.currency){o.currency=this.options.popularProducts.currency}if(this.options.popularProducts.image){if(typeof this.options.popularProducts.imageUrlOrFunction=="function"){o.image=this.options.popularProducts.imageUrlOrFunction(doc)}else if(typeof this.options.popularProducts.imageUrlOrFunction=="string"&&this.options.popularProducts.imageUrlOrFunction){o.image=this.options.popularProducts.imageUrlOrFunction in doc?doc[this.options.popularProducts.imageUrlOrFunction]:null}}this.currentResults.POPULAR_PRODUCTS.push(o);this.productInfo.popularProductsCount=this.currentResults.POPULAR_PRODUCTS.length;if(this.options.filtered){var ppHeader=this.getPopularProductsHeader(this);var cmpldHeader=Handlebars.compile(ppHeader);this.compiledPopularProductHeader=cmpldHeader({hoverSuggestion:this.params.q})}},processInFields:function(doc){var ins={},asrc=" "+doc.unbxdAutosuggestSrc+" ",highlightedtext=this.highlightStr(doc.autosuggest);if(this.options.inFields.showDefault){var that=this;Object.keys(doc).forEach(function(item){if(item.length>=3&&item.substring(item.length-3)==="_in"){var a=item.split("_in")[0];ins[a]=doc[a+"_in"].slice(0,parseInt(that.options.inFields.noOfInfields))}})}else{for(var a in this.options.inFields.fields){if(a+"_in"in doc&&doc[a+"_in"].length&&asrc.indexOf(" "+a+" ")==-1){ins[a]=doc[a+"_in"].slice(0,parseInt(this.options.inFields.fields[a]));if(this.options.inFields.removeDuplicateKeyword){var ind=ins[a].indexOf(doc.autosuggest.trim());if(ind>=0){ins[a].splice(ind,1)}}}}}var sortedInfields=[];if(this.options.sortByLength){var k=0;for(var i in ins){for(var j=0;j<ins[i].length;j++){sortedInfields[k]={filterName:i,filterValue:ins[i][j]};k++}}sortedInfields.sort(function(a,b){return customSort(a.filterValue,b.filterValue)})}if(!$.isEmptyObject(ins)){this.currentResults.IN_FIELD.push({autosuggest:doc.autosuggest,highlighted:highlightedtext,type:"keyword",source:doc.unbxdAutosuggestSrc});var that=this;if(this.options.sortByLength){for(var i=0;i<sortedInfields.length;i++){if(sortedInfields[i].filterValue!==""){this.currentResults.IN_FIELD.push({autosuggest:doc.autosuggest,highlighted:this.options.inFields.type==="separate"?that.prepareinFieldsKeyword(sortedInfields[i].filterValue):that.highlightStr(doc.autosuggest)+" in "+that.prepareinFieldsKeyword(sortedInfields[i].filterValue),type:doc.doctype,filtername:sortedInfields[i].filterName,filtervalue:sortedInfields[i].filterValue,_original:doc,source:doc.unbxdAutosuggestSrc})}}}else{for(var a in ins){for(var b=0;b<ins[a].length;b++){if(ins[a][b]!==""){this.currentResults.IN_FIELD.push({autosuggest:doc.autosuggest,highlighted:this.options.inFields.type==="separate"?that.prepareinFieldsKeyword(ins[a][b]):that.highlightStr(doc.autosuggest)+" in "+that.prepareinFieldsKeyword(ins[a][b]),type:doc.doctype,filtername:a,filtervalue:ins[a][b],_original:doc,source:doc.unbxdAutosuggestSrc})}}}}}else{this.currentResults.KEYWORD_SUGGESTION.push({autosuggest:doc.autosuggest,highlighted:highlightedtext,type:"KEYWORD_SUGGESTION",source:doc.unbxdAutosuggestSrc})}},sortSuggestionsBylength:function(){this.currentResults.SORTED_SUGGESTIONS=this.currentResults.KEYWORD_SUGGESTION.concat(this.currentResults.TOP_SEARCH_QUERIES,this.currentResults.PROMOTED_SUGGESTION);this.currentResults.SORTED_SUGGESTIONS.sort(function(a,b){return customSort(a.autosuggest,b.autosuggest)});this.currentResults.IN_FIELD.sort(function(a,b){return customSort(a.autosuggest,b.autosuggest)})},processData:function(data){var count;if(this.options.maxSuggestions){count=this.max_suggest(data)}this.currentResults={KEYWORD_SUGGESTION:[],TOP_SEARCH_QUERIES:[],POPULAR_PRODUCTS:[],IN_FIELD:[],SORTED_SUGGESTIONS:[],PROMOTED_SUGGESTION:[]};this.clickResults={TRENDING_QUERIES:[]};var infieldsCount=0;var key_count=0,uniqueInfields=[],uniqueSuggestions=[];for(var x=0;x<data.response.products.length;x++){var doc=data.response.products[x],o={};if(this.options.maxSuggestions){if("TOP_SEARCH_QUERIES"==doc.doctype&&count["topquery"]>this.currentResults.TOP_SEARCH_QUERIES.length&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processTopSearchQuery(doc)}else if("IN_FIELD"==doc.doctype&&count["infields"]+count["key_rem"]+count["top_rem"]>infieldsCount&&this.isUnique(doc.autosuggest,uniqueInfields)&&this.isUnique(doc.autosuggest,uniqueSuggestions)){if(count["infields"]>infieldsCount){infieldsCount++;this.processInFields(doc)}else if(count["key_rem"]+count["top_rem"]>this.currentResults.KEYWORD_SUGGESTION.length&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processKeywordSuggestion(doc)}}else if("KEYWORD_SUGGESTION"==doc.doctype&&count["keyword"]>this.currentResults.KEYWORD_SUGGESTION.length&&this.isUnique(doc.autosuggest,uniqueInfields)){this.processKeywordSuggestion(doc)}else if("POPULAR_PRODUCTS"==doc.doctype&&this.options.popularProducts.count>this.currentResults.POPULAR_PRODUCTS.length){this.processPopularProducts(doc)}else if("PROMOTED_SUGGESTION"==doc.doctype&&count["promoted"]>this.currentResults.PROMOTED_SUGGESTION.length&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processPromotedSuggestion(doc)}}else{if("TOP_SEARCH_QUERIES"==doc.doctype&&this.options.topQueries.count>this.currentResults.TOP_SEARCH_QUERIES.length&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processTopSearchQuery(doc)}else if("IN_FIELD"==doc.doctype&&this.options.inFields.count>infieldsCount&&this.isTempUnique(doc.autosuggest,uniqueInfields)&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processInFields(doc)}else if("KEYWORD_SUGGESTION"==doc.doctype&&this.options.keywordSuggestions.count>this.currentResults.KEYWORD_SUGGESTION.length&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processKeywordSuggestion(doc)}else if("POPULAR_PRODUCTS"==doc.doctype&&this.options.popularProducts.count>this.currentResults.POPULAR_PRODUCTS.length){this.processPopularProducts(doc)}else if("PROMOTED_SUGGESTION"==doc.doctype&&this.options.promotedSuggestions.count>this.currentResults.PROMOTED_SUGGESTION.length&&this.isUnique(doc.autosuggest,uniqueSuggestions)){this.processPromotedSuggestion(doc)}}}if(this.options.filtered){this.getfilteredPopularProducts()}if(this.options.sortByLength){this.sortSuggestionsBylength()}var outLength=this.currentResults.POPULAR_PRODUCTS.length+this.currentResults.IN_FIELD.length;if(this.options.sortSuggestionsOnLength){for(var doc_type in this.currentResults){if(doc_type.toLowerCase()!="in_field"){this.currentResults[doc_type].sort(function(x,y){return x.autosuggest.length>y.autosuggest.length?1:-1})}}}},escapeStr:function(str){return str.replace(/([\\{}()|.?*+\-\^$\[\]])/g,"\\$1")},highlightStr:function(str){var output=str,q=$.trim(this.params.q+"");if(q.indexOf(" ")){var arr=q.split(" ");for(var k in arr){if(!arr.hasOwnProperty(k))continue;var l=output.toLowerCase().lastIndexOf("</strong>");if(l!=-1)l+=9;output=output.substring(0,l)+output.substring(l).replace(new RegExp(this.escapeStr(arr[k]),"gi"),function($1){return"<strong>"+$1+"</strong>"})}}else{var st=output.toLowerCase().indexOf(q);output=st>=0?output.substring(0,st)+"<strong>"+output.substring(st,st+q.length)+"</strong>"+output.substring(st+q.length):output}return output},prepareinFieldsKeyword:function(str){if(this.options.customInfieldsFilter&&typeof this.options.customInfieldsFilter==="function"){str=this.options.customInfieldsFilter(str)}return'<span class="unbxd-as-suggestions-infields">'+str+"</span>"},prepareinFieldsHTML:function(){if(this.options.inFields.type==="inline"){return"{{#if data.IN_FIELD}}"+(this.options.inFields.header?'<li class="unbxd-as-header">'+this.options.inFields.header+"</li>":"")+"{{#each data.IN_FIELD}}"+'{{#unbxdIf type "keyword"}}'+"{{else}}"+'<li data-index="{{@index}}" data-type="{{type}}" data-value="{{autosuggest}}" data-filtername="{{filtername}}" data-filtervalue="{{filtervalue}}"  data-source="{{source}}">'+(this.options.inFields.tpl?this.options.inFields.tpl:this.default_options.inFields.tpl)+"</li>"+"{{/unbxdIf}}"+"{{/each}}"+"{{/if}}"}else{return"{{#if data.IN_FIELD}}"+(this.options.inFields.header?'<li class="unbxd-as-header">'+this.options.inFields.header+"</li>":"")+"{{#each data.IN_FIELD}}"+'{{#unbxdIf type "keyword"}}'+'<li class="unbxd-as-keysuggestion" data-index="{{@index}}" data-value="{{autosuggest}}" data-type="IN_FIELD" data-source="{{source}}">'+(this.options.inFields.tpl?this.options.inFields.tpl:this.default_options.inFields.tpl)+"</li>"+"{{else}}"+'<li class="unbxd-as-insuggestion" style="color:'+this.options.theme+';" data-index="{{@index}}" data-type="{{type}}" data-value="{{autosuggest}}" data-filtername="{{filtername}}" data-filtervalue="{{filtervalue}}"  data-source="{{source}}">'+"in "+(this.options.inFields.tpl?this.options.inFields.tpl:this.default_options.inFields.tpl)+"</li>"+"{{/unbxdIf}}"+"{{/each}}"+"{{/if}}"}},preparekeywordSuggestionsHTML:function(){return"{{#if data.KEYWORD_SUGGESTION}}"+(this.options.keywordSuggestions.header?'<li class="unbxd-as-header">'+this.options.keywordSuggestions.header+"</li>":"")+"{{#each data.KEYWORD_SUGGESTION}}"+'<li class="unbxd-as-keysuggestion" data-value="{{autosuggest}}" data-index="{{@index}}" data-type="{{type}}"  data-source="{{source}}">'+(this.options.keywordSuggestions.tpl?this.options.keywordSuggestions.tpl:this.default_options.keywordSuggestions.tpl)+"</li>"+"{{/each}}"+"{{/if}}"},prepareTrendingQueriesHTML:function(){return'<ul class="unbxd-as-maincontent unbxd-as-suggestions-overall unbxd-as-trending">'+(this.options.trendingSearches.header?'<li class="unbxd-as-header">'+this.options.trendingSearches.header+"</li>":"")+"{{#each data1}}"+'<li class="unbxd-as-keysuggestion" data-value="{{autosuggest}}" data-index="{{@index}}" data-type="{{type}}"  data-source="{{source}}">'+(this.options.trendingSearches.tpl?this.options.trendingSearches.tpl:this.default_options.trendingSearches.tpl)+"</li>"+"{{/each}}"+"</ul>"},preparepromotedSuggestionsHTML:function(){return"{{#if data.PROMOTED_SUGGESTION}}"+(this.options.promotedSuggestions.header?'<li class="unbxd-as-header">'+this.options.promotedSuggestions.header+"</li>":"")+"{{#each data.PROMOTED_SUGGESTION}}"+'<li class="unbxd-as-keysuggestion" data-value="{{autosuggest}}" data-index="{{@index}}" data-type="{{type}}"  data-source="{{source}}">'+(this.options.promotedSuggestions.tpl?this.options.promotedSuggestions.tpl:this.default_options.promotedSuggestions.tpl)+"</li>"+"{{/each}}"+"{{/if}}"},preparetopQueriesHTML:function(){return"{{#if data.TOP_SEARCH_QUERIES}}"+(this.options.topQueries.header?'<li class="unbxd-as-header">'+this.options.topQueries.header+"</li>":"")+"{{#each data.TOP_SEARCH_QUERIES}}"+'<li class="unbxd-as-keysuggestion" data-type="{{type}}" data-index="{{@index}}" data-value="{{autosuggest}}">'+(this.options.topQueries.tpl?this.options.topQueries.tpl:this.default_options.topQueries.tpl)+"</li>"+"{{/each}}"+"{{/if}}"},preparefilteredPopularProducts:function(){return(this.compiledPopularProductHeader?'<li class="unbxd-as-header unbxd-as-popular-product-header">'+this.compiledPopularProductHeader+"</li>":"")+"{{#data}}"+'<li class="unbxd-as-popular-product '+(this.options.popularProducts.view==="grid"?"unbxd-as-popular-product-grid":"")+'" data-value="{{autosuggest}}" data-index="{{@index}}" data-type="{{type}}" data-pid="{{pid}}" data-src="{{src}}">'+(this.options.popularProducts.tpl?this.options.popularProducts.tpl:this.default_options.popularProducts.tpl)+"</li>"+"{{/data}}"},preparepopularProductsHTML:function(){return"{{#if data.POPULAR_PRODUCTS}}"+(this.compiledPopularProductHeader?'<li class="unbxd-as-header unbxd-as-popular-product-header">'+this.compiledPopularProductHeader+"</li>":"")+"{{#data.POPULAR_PRODUCTS}}"+'<li class="unbxd-as-popular-product '+(this.options.popularProducts.view==="grid"?"unbxd-as-popular-product-grid":"")+'" data-value="{{autosuggest}}" data-index="{{@index}}" data-type="{{type}}" data-pid="{{pid}}" >'+(this.options.popularProducts.tpl?this.options.popularProducts.tpl:this.default_options.popularProducts.tpl)+"</li>"+"{{/data.POPULAR_PRODUCTS}}"+"{{/if}}"},standardizeKeys:function(key){if(key==="inFields"){key="IN_FIELD"}else if(key==="popularProducts"){key="POPULAR_PRODUCTS"}else if(key==="topQueries"){key="TOP_SEARCH_QUERIES"}else if(key==="promotedSuggestions"){key="PROMOTED_SUGGESTION"}else key="KEYWORD_SUGGESTION";return key},prepareSortedSuggestionsHTML:function(){return"{{#if data.SORTED_SUGGESTIONS}}"+"{{#each data.SORTED_SUGGESTIONS}}"+'<li class="unbxd-as-sorted-suggestion" data-type="{{type}}" data-index="{{@index}}" data-value="{{autosuggest}}" data-sorted="true">'+(this.options.sortedSuggestions.tpl?this.options.sortedSuggestions.tpl:this.default_options.sortedSuggestions.tpl)+"</li>"+"{{/each}}"+"{{/if}}"},preprocessHTML:function(){if(this.options.isMobile&&this.options.isMobile()||isMobile.any()){this.options.template=this.options.mobile.template;this.options.mainTpl=this.options.mobile.mainTpl;this.options.popularProducts.count=this.options.mobile.popularProducts.count}},prepareHTML:function(){this.preprocessHTML();var html="";if(this.options.template==="1column"&&this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){html+='<ul class="unbxd-as-maincontent unbxd-as-suggestions-overall unbxd-as-view-more">'}else{html+='<ul class="unbxd-as-maincontent unbxd-as-suggestions-overall">'}var mobileHtml='<ul class="unbxd-as-maincontent unbxd-as-suggestions-overall unbxd-as-mobile-view">';var sideHtml="";var mainHtml="";var noResults=false;var self=this,mainlen=0,sidelen=0;if(this.options.template==="1column"){if(this.options.suggestionsHeader&&(self.currentResults["IN_FIELD"].length||self.currentResults["KEYWORD_SUGGESTION"].length||self.currentResults["TOP_SEARCH_QUERIES"].length)){mainHtml=mainHtml+'<li class="unbxd-as-header unbxd-as-suggestions-header">'+this.options.suggestionsHeader+"</li>"}}if(!self.currentResults["IN_FIELD"].length&&!self.currentResults["KEYWORD_SUGGESTION"].length&&!self.currentResults["POPULAR_PRODUCTS"].length&&!self.currentResults["TOP_SEARCH_QUERIES"].length&&!self.currentResults["PROMOTED_SUGGESTION"].length&&this.options.noResultTpl){noResults=true;if(typeof this.options.noResultTpl==="function"){html=html+"<li>"+this.options.noResultTpl.call(self,encodeURIComponent(self.params.q))+"</li></ul>"}else if(typeof this.options.noResultTpl=="string"){html=html+"<li>"+this.options.noResultTpl+"</li></ul>"}}this.options.mainTpl.forEach(function(key){key=self.standardizeKeys(key);mainlen=mainlen+self.currentResults[key].length});this.options.sideTpl.forEach(function(key){if(key==="inFields"){key="IN_FIELD"}else if(key==="popularProducts"){key="POPULAR_PRODUCTS"}else if(key==="topQueries"){key="TOP_SEARCH_QUERIES"}else if(key==="promotedSuggestions"){key="PROMOTED_SUGGESTION"}else key="KEYWORD_SUGGESTION";sidelen=sidelen+self.currentResults[key].length});if(this.options.template==="2column"&&!this.options.sideTpl.length&&!this.options.mainTpl){this.options.sideTpl=["keywordSuggestions","topQueries"];this.options.mainTpl=["inFields","popularProducts"]}if(this.options.template==="2column"){if(mainlen==0&&sidelen!=0){html='<ul class="unbxd-as-sidecontent">';this.options.sideTpl.forEach(function(key){if(self.options.sortByLength&&(key=="topQueries"||key=="keywordSuggestions"||key=="promotedSuggestions")){return}key="prepare"+key+"HTML";html=html+self[key]()});if(this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){html=html+this.options.popularProducts.viewMore.tpl}html=html+"</ul>"}else{if(mainlen>0&&sidelen!=0){if(this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){sideHtml='<ul class="unbxd-as-sidecontent unbxd-as-view-more">'}else{sideHtml='<ul class="unbxd-as-sidecontent">'}this.options.sideTpl.forEach(function(key){if(self.options.sortByLength&&(key=="topQueries"||key=="keywordSuggestions"||key=="promotedSuggestions")){return}key="prepare"+key+"HTML";sideHtml=sideHtml+self[key]()});if(this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){sideHtml=sideHtml+this.options.popularProducts.viewMore.tpl}sideHtml=sideHtml+"</ul>";mainHtml=mainHtml+'<ul class="unbxd-as-maincontent unbxd-as-suggestions-overall">';if(this.options.suggestionsHeader){mainHtml=mainHtml+'<li class="unbxd-as-header unbxd-as-suggestions-header">'+this.options.suggestionsHeader+"</li>"}}}}if(!noResults&&mainlen>0){if(this.options.sortByLength){mainHtml=mainHtml+self["prepareSortedSuggestionsHTML"]()}this.options.mainTpl.forEach(function(key){if(self.currentResults[self.standardizeKeys(key)].length&&topQuery===""){topQuery=self.currentResults[self.standardizeKeys(key)][0]["autosuggest"]}if(self.options.sortByLength&&(key=="topQueries"||key=="keywordSuggestions"||key=="promotedSuggestions")){return}key="prepare"+key+"HTML";mainHtml=mainHtml+self[key]()});if(this.options.popularProducts.viewMore&&this.options.popularProducts.viewMore.enabled){mainHtml=mainHtml+this.options.popularProducts.viewMore.tpl}mainHtml=mainHtml+"</ul>";if(this.options.isMobile&&this.options.isMobile()){html=mobileHtml+mainHtml}else if(isMobile.any()){html=mobileHtml+mainHtml}else if(this.options.template==="1column"){html=html+mainHtml+"</ul>"}else if(this.options.sideContentOn==="right"){if(mainlen>0&&sidelen===0){html=html+mainHtml+"</ul>"}else{html=mainHtml+sideHtml}}else{html=sideHtml+mainHtml}}var cmpld=Handlebars.compile(html);this.log("prepraing html :-> template : "+this.options.template+" ,carts : "+this.options.showCarts+" ,cartType : "+this.options.cartType);this.log("html data : ",this.currentResults);return cmpld({data:this.currentResults,showCarts:this.options.showCarts,cartType:this.options.cartType})},addToCache:function(q,processedData){if(!(q in this.cache))this.cache[q]=$.extend({},processedData)},inCache:function(q){return q in this.cache&&this.cache.hasOwnProperty(q)},getFromCache:function(q){return this.cache[q]},destroy:function(self){self.$input.unbind(".auto");self.input.lastSelected=null;self.$input.removeAttr("autocomplete","off");self.$results.remove();self.$input.removeData("autocomplete")},setOption:function(name,value){var a=name.split(".");if(a.length>1){var o=this.options;for(var i=0;i<a.length-1;i++){if(!(a[i]in o))o[a[i]]={};o=o[a[i]]}o[a[a.length-1]]=value}else this.options[name]=value;this.previous="";this.$results.html("");this.cache={};this.cache.length=0},log:function(){}});$.fn.unbxdautocomplete=function(options){return this.each(function(){var self=this;try{this.auto=new autocomplete(this,options)}catch(e){}})}};
function getSiteName() {
  return "ss-unbxd-gcp-prod-furniturefair18951689870499";
}

function getApiKey() {
  return "4f254fd469b5c8b191a02e5e9e5ed44c";
}

/* helper variables and consts */
let hidePagesBorder = false;
const removeQueryParam = (paramName) => {
  const currentURL = new URL(window.location.href);

  // Check if the parameter exists in the URL
  if (currentURL.searchParams.has(paramName)) {
    currentURL.searchParams.delete(paramName);

    // Update the page's URL without a page reload
    window.history.replaceState(null, "", currentURL);
  }
};
let intialLeft = "";
const getUidCookie = document.cookie.match("\\bunbxd.userId=([^;]*)\\b");
const uidCookie = getUidCookie ? getUidCookie[1] : null;

const customRequestsCache = {
  search: {},
  autosuggest: {},
  blogs: {},
  pages: {},
};

const headerQuantityValues = {};
const defaultImageUrl =
  "https://libraries.unbxdapi.com/sdk-assets/defaultImage.svg";

/* * * ANALYTICS CONFIGURATION * * */
var UnbxdSiteName = getSiteName();
var UnbxdApiKey = getApiKey();

/* Analytics library is added in theme.liquid in shopify theme */

const unbxdAnalytics = (type, payload) => {
  // convert undefined to null
  for (const key in payload) {
    if (payload[key] === undefined) {
      payload[key] = null;
    }
  }
  // convert pid and qty to string
  if (payload.pid != undefined) {
    payload.pid = String(payload.pid);
  }
  if (payload.qty != undefined) {
    payload.qty = String(payload.qty);
  }
  if (type != undefined && Unbxd && typeof Unbxd.track === "function") {
    Unbxd.track(type, payload);
  } else {
    console.error("unbxdAnalytics.js is not loaded!");
  }
};
const experienceImpressionAnalytic = (templateData, widgetMapSelector) => {
  const pids = [];
  const widget = templateData.analyticsData.widgetNum.toUpperCase();
  if (widgetMapSelector[widget] == null) {
    return;
  }
  for (const product of templateData.recommendations) {
    pids.push(product.uniqueId);
  }

  const payload = {
    requestId: templateData.analyticsData.requestId,
    pids_list: pids,
    experience_pagetype: templateData.analyticsData.pageType,
    experience_widget: widget,
  };
  unbxdAnalytics("experience_impression", payload);
};

const addToCartAnalytics = (productMain) => {
  const addToCartAnalyticsPayload = getAddToCartAnalyticsPayload(productMain);
  unbxdAnalytics("addToCart", addToCartAnalyticsPayload);
};

const getAddToCartAnalyticsPayload = (productMain) => {
  const productId =
    productMain.querySelector(".gallery-cell").dataset.productId;

  const queryString = new URLSearchParams(location.search);
  const variantId = queryString.get("variant");

  const quantity = productMain.querySelector("#quantity").value;
  const price = productMain.querySelector(".money").innerHTML.replace("$", "");

  headerQuantityValues[productId] = quantity;

  return {
    pid: productId ?? null,
    variantId: variantId,
    qty: quantity,
    price: price,
  };
};

const addSearchAnalyticAttr = ({ input, button }) => {
  if (input != null) {
    input.setAttribute("unbxdattr", "sq");
  }
  if (button != null) {
    button.setAttribute("unbxdattr", "sq_bt");
  }
};

function unbxdRecsFnc(
  productType,
  productIds,
  widgetIdFirst,
  widgetIdSecond,
  widgetIdThird,
  uidCookie
) {
  let allWidgets = [
    {
      name: "widget1",
      selector: widgetIdFirst,
    },
    {
      name: "widget2",
      selector: widgetIdSecond,
    },
    {
      name: "widget3",
      selector: widgetIdThird,
    },
  ];

  const widgetMapSelector = {};
  for (const widget of allWidgets) {
    if (widget.selector == null) {
      continue;
    }
    widgetMapSelector[widget.name.toUpperCase()] = widget.selector;
  }

  window.getUnbxdRecommendations({
    widgets: allWidgets,
    userInfo: {
      userId: uidCookie,
      siteKey: getSiteName(),
      apiKey: getApiKey(),
    },
    pageInfo: {
      pageType: productType,
      productIds: productIds,
      boutiqueButton: true,
    },
    itemClickHandler: function (product) {},
    dataParser: function (templateData) {
      experienceImpressionAnalytic(templateData, widgetMapSelector);

      return templateData;
    },
  });
}

const [pageType] = location.href
  .substring(window.location.origin.length + 1)
  .split("/");
if (pageType != undefined && pageType.toLowerCase() == "products") {
  const shopifyRecsEl = document.querySelector(
    ".shopify-section--recommended-products"
  );
  const productId = document.querySelector(`[name="product-id"]`).value ?? "";

  shopifyRecsEl != null &&
    shopifyRecsEl.insertAdjacentHTML(
      "afterend",
      `<div id="UNX-pdp-recs" class="shopify-section unbxdRECSSplide"></div>
      <div id="UNX-pdp-recs-cross-sell" class="shopify-section unbxdRECSSplide"></div>`
    );
  unbxdRecsFnc(
    "PRODUCT",
    [productId],
    null,
    "UNX-pdp-recs",
    "UNX-pdp-recs-cross-sell",
    uidCookie
  );
}

if (pageType != undefined && document.querySelector("body.index") != null) {
  const UNXhomePage = document.querySelector(
    "body.index #s-a80db67a-0928-4ecf-80b9-310d37b52cc3"
  );
  if (UNXhomePage != null) {
    UNXhomePage.insertAdjacentHTML(
      "beforebegin",
      `<div id="UNX-homePage-RECS-1" class="unbxdRECSSplide"></div>`
    );
    unbxdRecsFnc("HOME", null, null, "UNX-homePage-RECS-1", null, uidCookie);
  }
}

let window_width = $(window).width();
let windowInnerWidth = window.innerWidth;
let changeWindowWidthMobileLayout = false;
if (windowInnerWidth <= 798) {
  changeWindowWidthMobileLayout = true;
}

let isMobile = {
  Android: function () {
    return navigator.userAgent.match(/Android/i);
  },
  BlackBerry: function () {
    return navigator.userAgent.match(/BlackBerry/i);
  },
  iOS: function () {
    return navigator.userAgent.match(/iPhone|iPad|iPod/i);
  },
  Opera: function () {
    return navigator.userAgent.match(/Opera Mini/i);
  },
  Windows: function () {
    return navigator.userAgent.match(/IEMobile/i);
  },
  any: function () {
    return (
      isMobile.Android() ||
      isMobile.BlackBerry() ||
      isMobile.iOS() ||
      isMobile.Opera() ||
      isMobile.Windows()
    );
  },
};
let searchInputSelector =
  ".header .main-nav > .search-container .unbxd-auto-suggest-input";
let autosuggest_input_element = $(
  ".header .main-nav > .search-container .unbxd-auto-suggest-input"
);
let changeASLayoutToMobile = false;
if (window_width < 799) {
  changeASLayoutToMobile = true;
}

if (changeASLayoutToMobile) {
  autosuggest_input_element = $(".mobile-search .unbxd-auto-suggest-input");
  searchInputSelector = ".mobile-search .unbxd-auto-suggest-input";
}

const currency = "$";
const getUnbxdASConfig = () => {
  let unbxd_as_config = {
    siteName: getSiteName(),
    APIKey: getApiKey(),
    resultsClass: "unbxd-as-wrapper unbxd-as-wrapper-default",
    minChars: 1,
    platform: "io",
    searchEndPoint: "//search.unbxd.io",
    delay: 100,
    loadingClass: "unbxd-as-loading",
    mainWidth: autosuggest_input_element.outerWidth() * 0.6,
    sideWidth: autosuggest_input_element.outerWidth() * 1.2,
    zIndex: 10000,
    position: "absolute",
    template: "2column",
    mainTpl: ["promotedSuggestions", "keywordSuggestions", "topQueries"],
    sideTpl: ["popularProducts"],
    sideContentOn: "right",
    suggestionsHeader: "Suggestions",
    topQueries: {
      count: 3,
    },
    keywordSuggestions: {
      count: 3,
      header: "",
      tpl: "",
    },
    inFields: {
      count: 0,
    },
    promotedSuggestions: {
      count: 3,
      header: "Promoted Suggestions",
      tpl: "",
    },
    hbsHelpers: function () {
      Handlebars.registerHelper("getSkuUI", function (product) {
        let SkuUI = "";
        if (
          product.variants[0] != undefined &&
          product.variants[0].v_sku != undefined
        ) {
          SkuUI = `<p class="unbxd-auto-suggest-sku">SKU: ${product.variants[0].v_sku}</p>`;
        }
        return SkuUI;
      });

      Handlebars.registerHelper("getImageUrl", function (product) {
        return product.imageUrl != undefined
          ? product.imageUrl
          : defaultImageUrl;
      });

      Handlebars.registerHelper("getPriceUI", function (product) {
        const { price, compareAtPrice, vendor } = product;
        let priceUI;

        if (["Smith Brothers", "L and J.G. Stickley Inc"].includes(vendor)) {
          return "";
        }

        const getNormalPriceHTML = (price) => {
          return `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;`;
        };

        if (
          (price == 0 || price == undefined) &&
          (compareAtPrice == 0 || compareAtPrice == undefined)
        ) {
          /* price & compareAtPrice both doesn't exists */
          priceUI = getNormalPriceHTML(0);
        } else if (
          (price == 0 || price == undefined) &&
          compareAtPrice != 0 &&
          compareAtPrice != undefined
        ) {
          /* price doesn't exists; compareAtPrice exists */
          priceUI = getNormalPriceHTML(compareAtPrice);
        } else if (
          (compareAtPrice == 0 || compareAtPrice == undefined) &&
          price != 0 &&
          price != undefined
        ) {
          /* compareAtPrice doesn't exists; price exists */
          priceUI = getNormalPriceHTML(price);
        } else if (price == compareAtPrice) {
          /* both prices exists and are equal */
          priceUI = getNormalPriceHTML(price);
        } else {
          /* both prices exists but not equal */
          priceUI = `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;
				<s>${currency}${compareAtPrice}</s>`;
        }
        const priceUIContainer = `
      <p class="unbxd-auto-suggest-price-p">
        ${priceUI}
      </p>`;
        return priceUIContainer;
      });
    },
    popularProducts: {
      fields: [
        "title",
        "uniqueId",
        "productUrl",
        "imageUrl",
        "vendor",
        "price",
        "compareAtPrice",
        "v_sku",
      ],
      price: true,
      priceFunctionOrKey: "price",
      image: true,
      imageUrlOrFunction: "imageUrl",
      name: true,
      nameFunctionOrKey: "title",
      currency: currency,
      header: "Popular Products",
      view: "grid",
      tpl: [
        `
          <a title="{{ _original.title }}" href="{{ _original.productUrl }}">
            <div class="unbxd-as-popular-product-info">
                <div class="unbxd-as-popular-product-image-container">
                  <img src="{{ getImageUrl _original }}" alt="{{ _original.title }}">
                </div>
                <div class="unbxd-as-popular-product-name">{{ _original.title }}</div>
                <p class="unbxd-auto-suggest-vendor">{{ _original.vendor }}</p>
                <div class="unbxd-as-popular-product-price">{{{ getPriceUI _original }}}</div>
            </div>
          </a>`,
      ].join(""),
    },
    onItemSelect: function (data, original) {
      window.location =
        window.location.origin + "/search?q=" + encodeURIComponent(data.value);
    },
    onSimpleEnter: function (e) {
      e.preventDefault();
      let data = jQuery(this.input).val();
      data = $.trim(data);
      if (data.length > 0) {
        const payload = {
          query: data,
        };
        if (Unbxd && typeof Unbxd.track === "function") {
          Unbxd.track("search", payload);
        } else {
          console.error("unbxdAnalytics.js is not loaded!");
        }
        window.location =
          window.location.origin + "/search?q=" + encodeURIComponent(data);
      }
      e.stopPropagation();
    },
    noResultTpl: function (query) {
      const decodedQuery = decodeURIComponent(query);
      if (query.trim() == "") {
        setTimeout(() => {
          const unbxdAsMainContent = document.querySelector(
            ".unbxd-as-wrapper-default .unbxd-as-maincontent"
          );
          unbxdAsMainContent &&
            unbxdAsMainContent.style.setProperty("display", "none");
        });
        return "";
      }
      setTimeout(() => {
        const noResultElem = document.querySelector(
          `.boost-pfs-search-suggestion-header-view-all`
        );
        if (noResultElem != null) {
          noResultElem.classList.add("hide");
        }
      });
      return `<div class="boost-pfs-search-suggestion-no-result" data-group="empty"
            data-label="No Results: ${decodedQuery}" data-value="${decodedQuery}" aria-label="No Results">
              <p>Sorry, nothing found for "<strong>${decodedQuery}</strong>".</p>
            </div>`;
    },
    extraParams: {
      filter: `-content_type:"PAGES"&filter=-content_type:"BLOGS"`,
    },
    removeDuplicates: true,
  };
  if (window.innerWidth <= 798 || isMobile.any()) {
    unbxd_as_config.filtered = false;
    unbxd_as_config.template = "1column";
    unbxd_as_config.zIndex = 999999;
    unbxd_as_config.mainTpl = [
      "promotedSuggestions",
      "keywordSuggestions",
      "topQueries",
      "popularProducts",
    ];
    unbxd_as_config.popularProducts.count = 4;
  } else {
    unbxd_as_config.filtered = true;
    unbxd_as_config.template = "2column";
    unbxd_as_config.mainTpl = [
      "promotedSuggestions",
      "keywordSuggestions",
      "topQueries",
    ];
    unbxd_as_config.sideTpl = ["popularProducts"];
    unbxd_as_config.popularProducts.count = 6;
  }
  return unbxd_as_config;
};
/* Update header cart helpers START */

const updateHeaderQuantityValues = () => {
  const cartItems = document.querySelectorAll(`.header .mini-cart__item`);
  for (const cartItem of cartItems) {
    headerQuantityValues[
      cartItem.querySelector(".mini-cart__product-id").innerText
    ] = cartItem.querySelector(`[data-cart-quantity-input]`).value;
  }
};

const headerCartQuantityChangeHandler = (e) => {
  const target = e.target;
  /* changed quantity */
  if (e.type == "change" && e.target.dataset.cartQuantityInput == "mini-cart") {
    const liCartItem = e.target.closest(".mini-cart__item");
    const productId = liCartItem.querySelector(
      ".mini-cart__product-id"
    ).innerText;

    const previousQuantity = headerQuantityValues[productId];
    const changedQuantity = e.target.value;

    const variantId = liCartItem.dataset.variantId;

    const moneyElem =
      liCartItem.querySelector(".money.sale") ??
      liCartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const quantityDiff = changedQuantity - previousQuantity;

    const cartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 0,
      price: price,
    };

    if (quantityDiff > 0) {
      cartAnalyticsPayload.qty = quantityDiff;
      unbxdAnalytics("addToCart", cartAnalyticsPayload);
    } else {
      cartAnalyticsPayload.qty = Math.abs(quantityDiff);
      unbxdAnalytics("cartRemoval", cartAnalyticsPayload);
    }
    updateHeaderQuantityValues();
  }

  /* clicked on plus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-plus") ||
      e.target.classList.contains("icon-plus"))
  ) {
    const liCartItem = e.target.closest(".mini-cart__item");

    const productId = liCartItem.querySelector(
      ".mini-cart__product-id"
    ).innerText;
    const variantId = liCartItem.dataset.variantId;

    const moneyElem =
      liCartItem.querySelector(".money.sale") ??
      liCartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const addToCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("addToCart", addToCartAnalyticsPayload);
    headerQuantityValues[productId]++;
  }

  /* clicked on minus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-minus") ||
      e.target.classList.contains("icon-minus"))
  ) {
    const liCartItem = e.target.closest(".mini-cart__item");

    const productId = liCartItem.querySelector(
      ".mini-cart__product-id"
    ).innerText;
    const variantId = liCartItem.dataset.variantId;

    const moneyElem =
      liCartItem.querySelector(".money.sale") ??
      liCartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const removeFromCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("cartRemoval", removeFromCartAnalyticsPayload);
    headerQuantityValues[productId]--;
  }
};

const cartPageCartQuantityChangeHandler = (e) => {
  /* clicked on plus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-plus") ||
      e.target.classList.contains("icon-plus"))
  ) {
    const cartItem = e.target.closest(".cart__item");

    const productId = cartItem.dataset.productId;
    const variantId = cartItem.dataset.variantId;

    const moneyElem =
      cartItem.querySelector(".money.sale") ?? cartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const addToCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("addToCart", addToCartAnalyticsPayload);
    headerQuantityValues[productId]++;
  }

  /* clicked on minus */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    (e.target.classList.contains("product-minus") ||
      e.target.classList.contains("icon-minus"))
  ) {
    const cartItem = e.target.closest(".cart__item");

    const productId = cartItem.dataset.productId;
    const variantId = cartItem.dataset.variantId;

    const moneyElem =
      cartItem.querySelector(".money.sale") ?? cartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const removeFromCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: 1,
      price: price,
    };
    unbxdAnalytics("cartRemoval", removeFromCartAnalyticsPayload);
    headerQuantityValues[productId]--;
  }

  /* clicked on remove */
  if (
    e.type == "click" &&
    e.target.tagName == "SPAN" &&
    e.target.classList.contains("remove-text")
  ) {
    const cartItem = e.target.closest(".cart__item");

    const productId = cartItem.dataset.productId;
    const variantId = cartItem.dataset.variantId;

    const moneyElem =
      cartItem.querySelector(".money.sale") ?? cartItem.querySelector(".money");
    const price = moneyElem.innerText.replace("$", "");

    const quantity = cartItem.querySelector(".quantity").value;

    const removeFromCartAnalyticsPayload = {
      pid: productId ?? null,
      variantId: variantId,
      qty: quantity,
      price: price,
    };
    unbxdAnalytics("cartRemoval", removeFromCartAnalyticsPayload);
    headerQuantityValues[productId]--;
  }
};
/* Update header cart helpers END */

async function unbxdAPI(type, query) {
  let response;
  if (query in customRequestsCache[type]) {
    return customRequestsCache[type][query];
  }
  switch (type) {
    case "search":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/${type}?q=${query}`
      );
      break;

    case "autosuggest":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/${type}?q=${query}`
      );
      break;

    case "blogs":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/autosuggest?q=${query}&filter=-content_type:"PRODUCT"&filter=-content_type:"PAGE"&fields=title,imageUrl,productUrl,doctype,autosuggest,content_type&keywordSuggestions.count=0&topQueries.count=0&promotedSuggestion.count=0&inFields.count=0&popularProducts.count=3&sourceFields=category_handle&sourceField.category_handle.count=3`
      );
      break;
    case "pages":
      response = await fetch(
        `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/autosuggest?q=${query}&filter=-content_type:"PRODUCT"&filter=-content_type:"BLOG"&fields=title,imageUrl,productUrl,doctype,autosuggest,content_type&keywordSuggestions.count=0&topQueries.count=0&promotedSuggestion.count=0&inFields.count=0&popularProducts.count=3&sourceFields=category_handle&sourceField.category_handle.count=0`
      );
      break;
  }
  const responseJson = await response.json();
  customRequestsCache[type][query] = responseJson;
  return responseJson;
}
async function getBlogsData(query) {
  let result = await unbxdAPI("blogs", query);
  return result.response;
}

async function getPagesData(query) {
  let result = await unbxdAPI("pages", query);
  return result.response;
}

async function getTotalNumberOfProducts(query) {
  let result = await unbxdAPI("search", query);
  return result.response.numberOfProducts;
}

const addHTMLToRightAs = (
  rightSectionContainer,
  pagesAr,
  containerClass,
  header
) => {
  let pagesHTMLStr = "";
  let pagesUl = "";
  let counter = 0;
  for (const pageHTML of pagesAr) {
    counter++;
    if (counter > 6) {
      break;
    }
    pagesHTMLStr += pageHTML;
  }
  pagesUl = `<ul class="${containerClass}">
                    <li class="boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header" aria-label="Pages">${header}</li>
                      ${pagesHTMLStr}
                  </ul>`;
  const unbxdRightAspages = rightSectionContainer.querySelector(
    `.${containerClass}`
  );
  if (unbxdRightAspages != null) {
    unbxdRightAspages.remove();
  }
  rightSectionContainer.insertAdjacentHTML("beforeend", pagesUl);
};

const addCollectionHTMLToRightAs = (
  rightSectionContainer,
  pagesAr,
  containerClass,
  header
) => {
  let pagesHTMLStr = "";
  let pagesUl = "";
  for (const pageHTML of pagesAr) {
    pagesHTMLStr += pageHTML;
  }
  pagesUl = `<ul class="${containerClass}">
                    <li class="boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header" aria-label="collection">${header}</li>
                      ${pagesHTMLStr}
                  </ul>`;
  const unbxdRightAspages = document.querySelector(`.${containerClass}`);
  if (unbxdRightAspages != null) {
    unbxdRightAspages.remove();
  }
  rightSectionContainer.insertAdjacentHTML("beforeend", pagesUl);
};

function getAsRightSectionData(blogsData) {
  let rightSection = {};
  let titleCss = "";
  rightSection.blogs = [];
  rightSection.pages = [];
  rightSection.category = [];
  for (const blog of blogsData.products) {
    let blogHTML = "";
    let blogTitle = blog.title != undefined ? blog.title : blog.autosuggest;
    let productUrl = blog.productUrl != undefined ? blog.productUrl : "#";

    if (blog.doctype == "category_handle") {
      let collectionTitle = blog.autosuggest;
      blogTitle = collectionTitle.replace(/-/g, " ");
      productUrl = `${window.location.origin}/collections/${collectionTitle}`;
      titleCss = `style=text-transform:capitalize;`;
    }

    blogHTML = `<li ${titleCss} class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
                    aria-label="pages: ${blogTitle}" role="option"
                    data-title="${blogTitle}">
                    <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${blogTitle}</a>
                </li>`;

    if (blog.content_type == "BLOG") {
      rightSection.blogs.push(blogHTML);
    } else if (blog.content_type == "PAGE") {
      rightSection.pages.push(blogHTML);
    } else if (blog.doctype == "category_handle") {
      rightSection.category.push(blogHTML);
    }
  }
  return rightSection;
}

const appendResultsCountHTML = async (inputSelector) => {
  try {
    const query = getSearchQuery(inputSelector);
    const viewMoreContainer = document.querySelector(
      ".boost-pfs-search-suggestion-header-view-all"
    );
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
      `.unbxd-as-maincontent`
    );
    const unbxdAsSideContent = unbxd_as_wrapper.querySelector(
      `.unbxd-as-sidecontent`
    );
    if (viewMoreContainer == null) {
      let viewMoreHTML = `<div class="boost-pfs-search-suggestion-header-view-all boost-pfs-search-suggestion-header" data-group="view-all" aria-label="View All">
      <a class="view-more-query" href="">
      <span>View all&nbsp;<span class="unbxd-as-number-of-products UNX-as-result-count">...</span>&nbsp;products<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.1657 7.43443L10.1657 3.43443C9.8529 3.12163 9.3473 3.12163 9.0345 3.43443C8.7217 3.74723 8.7217 4.25283 9.0345 4.56563L11.6689 7.20003H2.4001C1.9577 7.20003 1.6001 7.55843 1.6001 8.00003C1.6001 8.44163 1.9577 8.80003 2.4001 8.80003H11.6689L9.0345 11.4344C8.7217 11.7472 8.7217 12.2528 9.0345 12.5656C9.1905 12.7216 9.3953 12.8 9.6001 12.8C9.8049 12.8 10.0097 12.7216 10.1657 12.5656L14.1657 8.56563C14.4785 8.25283 14.4785 7.74723 14.1657 7.43443" fill="#5C5F62"></path></svg></span></a>
    </div>`;

      const viewMoreQueryElem =
        unbxd_as_wrapper.querySelector(`.view-more-query`);
      if (viewMoreQueryElem != null) {
        viewMoreQueryElem.setAttribute("href", `/search?q=${query}`);
      }
      if (changeWindowWidthMobileLayout) {
        unbxdAsMainContent &&
          unbxdAsMainContent.insertAdjacentHTML("beforeend", viewMoreHTML);
      } else {
        unbxdAsSideContent &&
          unbxdAsSideContent.insertAdjacentHTML("beforeend", viewMoreHTML);
      }
    }
  } catch (error) {
    console.error(
      `Could not add "view more button" in auto suggestion.\n`,
      error
    );
  }
};
const updateResultCount = async (inputSelector) => {
  try {
    const query = getSearchQuery(inputSelector);
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    if (query == "") {
      return false;
    }
    let totalNumberOfProducts = await getTotalNumberOfProducts(query);
    if (totalNumberOfProducts > 0) {
      const resultCountEl = document.querySelector(`.UNX-as-result-count`);
      resultCountEl != null &&
        (resultCountEl.textContent = totalNumberOfProducts);
    }
  } catch (error) {
    console.error(
      `Could not update results count in "view more button".\n`,
      error
    );
  }
};
const getSearchQuery = (inputSelector) => {
  const elem = document.querySelector(inputSelector);
  let query = "";
  if (elem != null) {
    query = elem.value.trim();
  }
  return query;
};
async function getOtherAutoSuggHTML() {
  const query = getSearchQuery(searchInputSelector)
  // param `query` should be string with minimum 1 character
  if (query == "") {
    return;
  }
  var padingCss = 'style="padding: 10px 10px 12px;"';
  let blogsAutoSuggHTML = `<li ${padingCss} class="UNX-blogs-heading boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header" aria-label="Pages">Learning Center</li>`;
  let pageAutoSuggHTML = `<li ${padingCss} class="UNX-blogs-heading boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header unbxd-ac-selected" aria-label="Pages">Pages</li>`;
  let collectionAutoSuggHTML = `<li ${padingCss} class="UNX-blogs-heading boost-pfs-search-suggestion-header-pages boost-pfs-search-suggestion-header unbxd-ac-selected" aria-label="Pages">Collections</li>`;

  const blogsData = await getBlogsData(query);
  const pagesData = await getPagesData(query);

  let blogsAutoSuggData = blogsData.products;
  let pagesAutoSuggData = pagesData.products;

  let blogsExists = false;
  let collectionsExists = false;
  let pagesExists = false;
  var padingliCss = 'style="padding:6px 10px;"';
  for (const pageData of pagesAutoSuggData) {
    pagesExists = true;
    const productUrl = pageData.productUrl;
    const pageTitle = pageData.title;

    pageAutoSuggHTML += `<li ${padingliCss} class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
        aria-label="pages: ${pageTitle}" role="option"
        data-title="${pageTitle}">
        <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${pageTitle}</a>
    </li>`;
  }
  for (const blogData of blogsAutoSuggData) {
    const productUrl = blogData.productUrl;
    const blogTitle = blogData.title;
    const titleCss = "";

    if (blogData.doctype == "category_handle") {
      collectionsExists = true;
      const collectionTitle = blogData.autosuggest;
      const blogTitle = collectionTitle.replace(/[_-]/g, " ");
      const productUrl = `${window.location.origin}/collections/${collectionTitle}`;
      const titleCss = 'style="text-transform: capitalize; padding: 6px 10px;"';

      collectionAutoSuggHTML += `<li ${titleCss} class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
              aria-label="pages: ${blogTitle}" role="option"
              data-title="${blogTitle}">
              <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${blogTitle}</a>
          </li>`;
    } else {
      blogsExists = true;
      blogsAutoSuggHTML += `<li ${titleCss} ${padingliCss}class="boost-pfs-search-suggestion-item boost-pfs-ui-item"
          aria-label="pages: ${blogTitle}" role="option"
          data-title="${blogTitle}">
          <a tabindex="-1" href="${productUrl}" class="UNX-as-blogs">${blogTitle}</a>
      </li>`;
    }
  }
  if (!collectionsExists) {
    collectionAutoSuggHTML = "";
  }
  if (!blogsExists) {
    blogsAutoSuggHTML = "";
  }
  if (!pagesExists) {
    pageAutoSuggHTML = "";
  }

  return {
    collections: collectionAutoSuggHTML,
    pages: pageAutoSuggHTML,
    blogs: blogsAutoSuggHTML,
  };
}

function addBlogsInAs(blogsAutoSuggHTML) {
  try {
    if (blogsAutoSuggHTML == undefined || blogsAutoSuggHTML == "") {
      return;
    }
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    if (
      unbxd_as_wrapper.querySelector(
        `.boost-pfs-search-suggestion-group-collection`
      ) == null
    ) {
      const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
        `.unbxd-as-maincontent`
      );
      const collectionContainerHTML = `<div class="UNX-collection-blogs boost-pfs-search-suggestion-group-collection" data-group="collections" aria-label="collections">
      </div>`;
      const blogsContainerHTML = `<div class="boost-pfs-search-suggestion-group ${
        hidePagesBorder ? "hide-border" : ""
      }" data-group="pages" aria-label="Pages">
        </div>`;
      if (changeWindowWidthMobileLayout) {
        const unbxdAsPopularProductHeading = unbxdAsMainContent.querySelector(
          ".unbxd-as-popular-product-header"
        );
        unbxdAsPopularProductHeading &&
          unbxdAsPopularProductHeading.insertAdjacentHTML(
            "beforebegin",
            collectionContainerHTML
          );
      } else {
        unbxdAsMainContent &&
          unbxdAsMainContent.insertAdjacentHTML(
            "beforeend",
            collectionContainerHTML
          );
      }
    }
    if (
      changeASLayoutToMobile &&
      document.querySelector(".UNX-mobile-as-lower") == null
    ) {
      const unbxdMainContentMobile = document.querySelector(
        `.unbxd-as-wrapper-default.unbxd-as-wrapper-mobile .unbxd-as-maincontent`
      );
      unbxdMainContentMobile.insertAdjacentHTML(
        "beforeend",
        `<div class="UNX-mobile-as-lower boost-pfs-search-suggestion-group-collection" data-group="collections" aria-label="collections">
        </div>`
      );
      const unbxdAsMobileLower = document.querySelector(`.UNX-mobile-as-lower`);
      unbxdAsMobileLower.innerHTML = "";
    }

    const unbxdBlogsWrapper = document.querySelector(
      `.UNX-collection-blogs.boost-pfs-search-suggestion-group-collection`
    );
    unbxdBlogsWrapper.innerHTML = "";

    for (let [key, value] of Object.entries(blogsAutoSuggHTML)) {
      if (changeASLayoutToMobile && ["pages", "blogs"].includes(key)) {
        const unbxdAsMobileLower =
          document.querySelector(`.UNX-mobile-as-lower`);
        unbxdAsMobileLower.innerHTML += value;
      } else {
        unbxdBlogsWrapper.innerHTML += value;
      }
    }
  } catch (error) {
    console.error(`Error in adding blogs in autosuggestion\n${error}`);
  }
}

/* driver code */

/* param type conflicts with SEO friendly URL in search sdk */
removeQueryParam("type");

/* Analytics  */

/* update header cart */
updateHeaderQuantityValues();

document
  .querySelector(".header")
  .addEventListener("change", headerCartQuantityChangeHandler);
document
  .querySelector(".header")
  .addEventListener("click", headerCartQuantityChangeHandler);

if (document.querySelector(".cart__wrapper > div:first-child") != null) {
  document
    .querySelector(".cart__wrapper > div:first-child")
    .addEventListener("click", cartPageCartQuantityChangeHandler);
}

/* Add to cart for PDP page START */
const addToCartButton = document.querySelector(`[data-label="Add to Cart"]`);
if (addToCartButton != null) {
  addToCartButton.addEventListener("click", () => {
    const productMain = document.querySelector(".product-main");
    addToCartAnalytics(productMain);
  });
}
const setupMtObToCenterAs = () => {
  const unbxdAsMtObConfig = {
    childList: true,
    subtree: true,
  };

  const unbxd_as_wrapper = document.querySelector(
    ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
  );
  const observer = new MutationObserver(async function (
    mutationsList,
    observer
  ) {
    /* disconnect observer before making any changes in DOM to avoid infinite loop */
    observer.disconnect();
    for (const mutation of mutationsList) {
      if (mutation.type === "childList") {
        centerAlignUnxdWrapper();
      }
    }
    observer.observe(unbxd_as_wrapper, unbxdAsMtObConfig);
  });
  observer.observe(unbxd_as_wrapper, unbxdAsMtObConfig);
};
/* Add to cart for PDP page END */
jQuery(document).ready(function () {
  unbxdAutoSuggestFunction(jQuery, Handlebars);
  const unbxd_as_config = getUnbxdASConfig();
  autosuggest_input_element.unbxdautocomplete(unbxd_as_config);
  setupMtObToCenterAs();
  const unbxd_as_wrapperOuter = document.querySelector(
    ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
  );

  const unbxdAsMtObConfig = {
    childList: true,
    subtree: true,
  };
  const observer = new MutationObserver(async function (
    mutationsList,
    observer
  ) {
    const unbxd_as_wrapper = document.querySelector(
      ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
    );
    /* disconnect observer before making any changes in DOM to avoid infinite loop */
    observer.disconnect();
    for (const mutation of mutationsList) {
      if (mutation.type === "childList") {
        if (changeASLayoutToMobile) {
          unbxd_as_wrapper.classList.add("unbxd-as-wrapper-mobile");
          if (isMobile.iOS()) {
            unbxd_as_wrapper.classList.add("mobile-ios");
          }
        }
        const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
          `.unbxd-as-maincontent`
        );
        const mainAsNoResultElem = unbxd_as_wrapper.querySelector(
          ".boost-pfs-search-suggestion-no-result"
        );

        /* no result found in main autosuggestion */
        if (changeASLayoutToMobile) {
          if (mainAsNoResultElem != null) {
            mainAsNoResultElem.parentNode.classList.add("hide");
            hidePagesBorder = true;
          }
        } else {
          if (unbxdAsMainContent != null) {
            if (mainAsNoResultElem != null) {
              unbxdAsMainContent.classList.add("hide");
            } else {
              unbxdAsMainContent.classList.remove("hide");
            }
          }
        }
        appendResultsCountHTML(searchInputSelector);
        updateResultCount(searchInputSelector);
        
        const othersAutoSuggHTML = await getOtherAutoSuggHTML();
        addBlogsInAs(othersAutoSuggHTML);
      }
    }
    observer.observe(unbxd_as_wrapper, unbxdAsMtObConfig);
  });

  // mutations types to observe
  if (unbxd_as_wrapperOuter != null) {
    observer.observe(unbxd_as_wrapperOuter, unbxdAsMtObConfig);
  }
});

setTimeout(() => {
  if (changeASLayoutToMobile) {
    document
      .querySelector(".icon-cross.close-search")
      .addEventListener("touchstart", (e) => {
        const unbxdAsWrapperMobile = document.querySelector(
          ".unbxd-as-wrapper-mobile"
        );
        if (unbxdAsWrapperMobile != null) {
          unbxdAsWrapperMobile.style.setProperty("display", "none");
        }
      });
  }
}, 500);

/* header > search */
headerSearchElems = {
  input: document.querySelector(".header .unbxd-auto-suggest-input"),
  button: document.querySelector(".header .search-container .search-submit"),
};
// addSearchAnalyticAttr(headerSearchElems);

/* main content > search */
mainContentSearchElems = {
  input: document.querySelector(".search__wrapper .boost-pfs-search-box"),
  button: document.querySelector(".search__wrapper .search__button"),
};
// addSearchAnalyticAttr(mainContentSearchElems);

/* prevent search on empty query */
headerSearchElems.input.addEventListener("keydown", (e) => {
  if (e.key == "Enter" && headerSearchElems.input.value.trim() == "") {
    e.preventDefault();
  }
});

/* prevent empty query search Desktop */
headerSearchElems.button.addEventListener("click", (e) => {
  let input = headerSearchElems.input;
  if (input.value.trim() == "") {
    e.target.disabled = true;
  } else {
    e.target.disabled = false;
    let input = $(".header .unbxd-auto-suggest-input");
    let inputValue = input.val();

    const data = $.trim(inputValue);
    if (data.length > 0) {
      const payload = {
        query: data,
      };
      if (Unbxd && typeof Unbxd.track === "function") {
        Unbxd.track("search", payload);
      } else {
        console.error("unbxdAnalytics.js is not loaded!");
      }
      window.location =
        window.location.origin + "/search?q=" + encodeURIComponent(data);
    }
  }
});

// Function to initialize Yotpo widget
function initializeYotpoWidget() {
  // Check if the Yotpo widget is available
  if (typeof yotpo !== "undefined" && typeof yotpo.initWidgets === "function") {
    yotpo.initWidgets();
  } else {
    // Yotpo script hasn't fully loaded, wait and retry
    setTimeout(initializeYotpoWidget, 100); // Adjust the delay as needed
  }
}

// Re-initialize Yotpo widget on page change
window.onpopstate = function () {
  // You might want to add a slight delay to allow the DOM to update before re-initializing
  setTimeout(function () {
    initializeYotpoWidget();
  }, 1000); // Adjust the delay as needed
};

let PDPSplideSlider;
const revertSplideConfig = (splide) => {
  const splideList = splide.Components.Elements.list;
  splideList.style.removeProperty("justify-content");
  splide.Components.Arrows.arrows.next.style.setProperty("display", "flex");
  splide.Components.Arrows.arrows.prev.style.setProperty("display", "flex");
  splide.Components.Drag.disable(false);
};
const updateSplideConfig = (splide) => {
  const slidesLength = splide.Components.Slides.getLength();
  const splideList = splide.Components.Elements.list;
  splideList.style.setProperty("justify-content", "center");
  splide.Components.Arrows.arrows.next.style.setProperty("display", "none");
  splide.Components.Arrows.arrows.prev.style.setProperty("display", "none");
  splide.Components.Move.jump(slidesLength);
  splide.Components.Drag.disable(true);
};
const makeSplideResponsive = (splide) => {
  if (splide == undefined || splide == null) {
    return;
  }
  const windowWidth = window.innerWidth;
  const slidesLength = splide.Components.Slides.getLength();
  let updateConfig = 0;
  if (windowWidth <= 480 && slidesLength == 1) {
    updateSplideConfig(splide);
    updateConfig = 1;
  }
  if (windowWidth <= 798 && slidesLength <= 2) {
    updateSplideConfig(splide);
    updateConfig = 1;
  }
  if (windowWidth > 798 && slidesLength <= 6) {
    updateSplideConfig(splide);
    updateConfig = 1;
  }
  if (!updateConfig) {
    revertSplideConfig(splide);
  }
};

$(window).resize(function () {
  intialLeft = "";
  calculation();
  centerAlignUnxdWrapper();
});

function addScriptDynamically(src) {
  var script = document.createElement("script");
  script.src = src;
  document.head.insertAdjacentElement("afterbegin", script);
}

document.addEventListener("DOMContentLoaded", () => {
  addScriptDynamically(
    "https://cdnjs.cloudflare.com/ajax/libs/splidejs/4.1.4/js/splide.min.js"
  );

  if (pageType != undefined && pageType.toLowerCase() == "products") {
    const findPDPRecsInterval = setInterval(() => {
      if (
        document.querySelector(`#UNX-pdp-recs`) != null &&
        document.querySelector("#UNX-pdp-recs .splide") != null
      ) {
        clearInterval(findPDPRecsInterval);
        const PDPSplideSlider = new Splide("#UNX-pdp-recs .splide", {
          type: "slide",
          trimSpace: "move",
          perPage: 3,
          focus: "center",
        });

        PDPSplideSlider.mount();

        PDPSplideSlider.on("mounted refresh move resize", () => {
          makeSplideResponsive(PDPSplideSlider);
        });

        initializeYotpoWidget();
      }
    }, 200);

    const findPDPRecsCrossSellInterval = setInterval(() => {
      if (
        document.querySelector(`#UNX-pdp-recs-cross-sell`) != null &&
        document.querySelector("#UNX-pdp-recs-cross-sell .splide") != null
      ) {
        clearInterval(findPDPRecsCrossSellInterval);
        const PDPSplideSlider = new Splide("#UNX-pdp-recs-cross-sell .splide", {
          type: "slide",
          trimSpace: "move",
          perPage: 3,
          focus: "center",
        });

        PDPSplideSlider.mount();

        PDPSplideSlider.on("mounted refresh move resize", () => {
          makeSplideResponsive(PDPSplideSlider);
        });

        initializeYotpoWidget();
      }
    }, 200);
  }
  if (document.querySelector("body.index") != null) {
    const findHomeRecsCrossSellInterval = setInterval(() => {
      if (
        document.querySelector(`#UNX-homePage-RECS-1`) != null &&
        document.querySelector("#UNX-homePage-RECS-1 .splide") != null
      ) {
        clearInterval(findHomeRecsCrossSellInterval);
        const PDPSplideSlider = new Splide("#UNX-homePage-RECS-1 .splide", {
          type: "slide",
          trimSpace: "move",
          perPage: 3,
          focus: "center",
        });

        PDPSplideSlider.mount();

        PDPSplideSlider.on("mounted refresh move resize", () => {
          makeSplideResponsive(PDPSplideSlider);
        });

        initializeYotpoWidget();
      }
    }, 200);
  }
});

function centerAlignUnxdWrapper() {
  const unbxdAsWrapper = document.querySelector(
    ".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest"
  );
  if (
    autosuggest_input_element != null &&
    unbxdAsWrapper != null &&
    unbxdAsWrapper.offsetWidth > autosuggest_input_element.width()
  ) {
    // Calculate offset based on input width and autosuggest container width
    const autosuggestOffset =
      (unbxdAsWrapper.offsetWidth - autosuggest_input_element.width()) / 2;
    const getAutoElLeft = parseInt(unbxdAsWrapper.style.left);

    if (intialLeft == "") {
      intialLeft = getAutoElLeft;
    }
    const calculateLeft = intialLeft - autosuggestOffset;
    // Set the left position of the autosuggest container
    unbxdAsWrapper.style.left = `${calculateLeft}px`;
  }
}

function calculation() {
  const location = autosuggest_input_element.offset();
  const left = location.left;
  $(".unbxd-as-wrapper-default.unbxd-as-overall-autosuggest").css({
    position: "absolute",
    left: left + "px",
  });
}

// fix redirection to blank search page when clicked on search icon of stick header
const findStickHeaderSearch = setInterval(() => {
  if (
    document.querySelector(
      ".sticky_nav .nav--combined .icon-search.dropdown_link"
    ) != null
  ) {
    clearInterval(findStickHeaderSearch);
    const stickyHeaderSearch = document.querySelector(
      ".sticky_nav .nav--combined .icon-search.dropdown_link"
    );
    stickyHeaderSearch != null &&
      stickyHeaderSearch.addEventListener("click", (e) => {
        e.preventDefault();
        $("html, body").animate(
          {
            scrollTop: 0,
          },
          100
        );
        $(".unbxd-auto-suggest-input") != null &&
          $(".unbxd-auto-suggest-input").focus();
      });
  }
}, 100);


async function addAsStaticOtherContent() {
  let blogsData = await getBlogsData("*");
  let pagesData = await getPagesData("*");
  let combinedProducts = [...blogsData.products, ...pagesData.products];

  const rightSection = getAsRightSectionData({
    products: combinedProducts,
  });
  const unbxd_as_wrapper = document.querySelector(".unbxd-custom-as");
  if (
    unbxd_as_wrapper.querySelector(".boost-pfs-search-suggestion-group") ==
    null
  ) {
    const blogsContainerHTML = `<div class="boost-pfs-search-suggestion-group" data-group="pages" aria-label="Pages">
                                </div>`;
    const collectionContainerHTML = `<div class="boost-pfs-search-suggestion-group-collection" data-group="collections" aria-label="collections">
                                </div>`;
    const unbxdAsMainContent = unbxd_as_wrapper.querySelector(
      ".unbxd-as-maincontent"
    );
    if (changeWindowWidthMobileLayout) {
      const unbxdAsPopularProductHeading = unbxdAsMainContent.querySelector(
        ".unbxd-as-popular-product-header"
      );
      unbxdAsPopularProductHeading &&
        unbxdAsPopularProductHeading.insertAdjacentHTML(
          "beforebegin",
          collectionContainerHTML
        );
      unbxdAsMainContent &&
        unbxdAsMainContent.insertAdjacentHTML(
          "beforeend",
          blogsContainerHTML
        );
    } else {
      unbxdAsMainContent &&
        unbxdAsMainContent.insertAdjacentHTML(
          "beforeend",
          blogsContainerHTML
        );
    }
  }
  const blogsContainer = unbxd_as_wrapper.querySelector(
    ".boost-pfs-search-suggestion-group"
  );
  const collectionContainer = unbxd_as_wrapper.querySelector(
    ".boost-pfs-search-suggestion-group-collection"
  );
  if (changeWindowWidthMobileLayout) {
    addHTMLToRightAs(
      collectionContainer,
      rightSection.category,
      "UNX-right-as-category",
      "Collections"
    );
  } else {
    addHTMLToRightAs(
      blogsContainer,
      rightSection.category,
      "UNX-right-as-category",
      "Collections"
    );
  }

  addHTMLToRightAs(
    blogsContainer,
    rightSection.pages,
    "UNX-right-as-pages",
    "Pages"
  );
  addHTMLToRightAs(
    blogsContainer,
    rightSection.blogs,
    "UNX-right-as-blogs",
    "Learning Center"
  );
}

/* Autosuggestion results on click of search box without typing query */

$(document).ready(function () {
  let productsHtml = "",
    suggestionHtml = "",
    headerHtml = "",
    productHeaderHtml = "",
    parentHtml = "";
  let popularProductCount = 6;
  if (screen.width <= 798) {
    popularProductCount = 4;
  }

  $.ajax({
    url: `https://search.unbxd.io/${getApiKey()}/${getSiteName()}/autosuggest?q=*&topQueries.count=5&promotedSuggestion.count=5&keywordSuggestions.count=0&inFields.count=0&popularProducts.count=${popularProductCount}&filter=-content_type:"PAGES"&filter=-content_type:"BLOGS"`,
    type: "GET",
  })
    .done(function (res) {
      const searchedQuery = res.searchMetaData.queryParams.q;
      const products = res.response.products;
      $.each(products, function (key, value) {
        const UNXautosuggest = value.autosuggest;
        if (value.content_type == "PRODUCT") {
          const unxProductUrl = value.productUrl;
          const unxImageUrl =
            value.imageUrl ||
            "https://libraries.unbxdapi.com/sdk-assets/defaultImage.svg";
          const title = value.title || "";
          const vendor = value.vendor || "";
          const doctype = value.doctype;
          const uniqueId = value.uniqueId;
          let price = value.price;
          const compareAtPrice = value.compareAtPrice;
          let priceUI;

          if (["Smith Brothers", "L and J.G. Stickley Inc"].includes(vendor)) {
            price = "";
          }

          const getNormalPriceHTML = (price) => {
            return `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;`;
          };

          if (
            (price == 0 || price == undefined) &&
            (compareAtPrice == 0 || compareAtPrice == undefined)
          ) {
            /* price & compareAtPrice both doesn't exists */
            priceUI = getNormalPriceHTML(0);
          } else if (
            (price == 0 || price == undefined) &&
            compareAtPrice != 0 &&
            compareAtPrice != undefined
          ) {
            /* price doesn't exists; compareAtPrice exists */
            priceUI = getNormalPriceHTML(compareAtPrice);
          } else if (
            (compareAtPrice == 0 || compareAtPrice == undefined) &&
            price != 0 &&
            price != undefined
          ) {
            /* compareAtPrice doesn't exists; price exists */
            priceUI = getNormalPriceHTML(price);
          } else if (price == compareAtPrice) {
            /* both prices exists and are equal */
            priceUI = getNormalPriceHTML(price);
          } else {
            /* both prices exists but not equal */
            priceUI = `<span class="unbxd-auto-suggest-price">${currency}${price}</span>&nbsp;
				                <s>${currency}${compareAtPrice}</s>`;
          }

          const priceUIContainer = `<p class="unbxd-auto-suggest-price-p"> ${priceUI} </p>`;

          productsHtml += `<li class="unbxd-as-popular-product unbxd-as-popular-product-grid UNX-product-click-event" data-value="${title}"
          data-type="${doctype}" data-pid="${uniqueId}" data-prank="${
            key + 1
          }" data-query="${searchedQuery}">
          <a title="${title}" href="${unxProductUrl}">
            <div class="unbxd-as-popular-product-info">
              <div class="unbxd-as-popular-product-image-container">
                <img src="${unxImageUrl}" alt="${title}">
              </div>
              <div class="unbxd-as-popular-product-name">${title}</div>
              <p class="unbxd-auto-suggest-vendor">${vendor}</p>
              <div class="unbxd-as-popular-product-price">
              ${
                vendor == "Smith Brothers" ||
                vendor == "L and J.G. Stickley Inc"
                  ? ""
                  : priceUIContainer
              }
              </div>
            </div>
          </a>
        </li>`;
        } else {
          suggestionHtml += `<a href="/search?q=${value.autosuggest}">
            <li class="unbxd-as-sorted-suggestion UNX-static-as-suggestion" data-value="${value.autosuggest}" data-type="${value.doctype}"
            data-source="" data-query="${searchedQuery}" data-field-name="autosuggest" data-sorted="true">${UNXautosuggest}</li>
          </a>`;
        }
      });

      // -----Trending Headers div-----
      headerHtml += `<li class="unbxd-as-header unbxd-as-suggestions-header">Suggestions</li>`;

      // // Trending Product Header
      productHeaderHtml += `<li class="unbxd-as-header unbxd-as-popular-product-header">Popular Products</li>`;

      let desktopSearchContainer = $(
        ".header .main-nav > .search-container .search__form"
      );
      let mobileSearchContainer = $(
        ".mobile-search .search-form.search-popup__form"
      );

      // merged div's
      if (window.innerWidth <= 798 || isMobile.any()) {
        parentHtml += `<div id="unbxd-custom-mobile-autosuggestion" class="unbxd-custom-as unbxd-as-wrapper unbxd-as-overall-autosuggest unbxd-as-wrapper-mobile mobile-ios" style="position: absolute; z-index: 999999; top: 54px; left: 20px;">
        <ul class="unbxd-as-maincontent unbxd-as-suggestions-overall unbxd-as-mobile-view" style="width: 234px; box-sizing: border-box;">
        ${headerHtml}
        ${suggestionHtml}
        ${productHeaderHtml}
        ${productsHtml}
        </ul></div>`;
        mobileSearchContainer.append(parentHtml);
      } else {
        parentHtml += `<div id="unbxd-custom-autosuggestion" class="unbxd-as-wrapper unbxd-as-overall-autosuggest unbxd-as-extra-right unbxd-custom-as" style="position: absolute;z-index: 10000;top: 100% !important; display:none; left: 50%; transform: translate(-50%);">
        <ul class="unbxd-as-maincontent unbxd-as-suggestions-overall" style="width: 300px; box-sizing: border-box;">
        ${headerHtml}
        ${suggestionHtml}
        </ul>
        <ul class="unbxd-as-sidecontent-custom" style="width: 600px; box-sizing: border-box;">
        ${productHeaderHtml}
        ${productsHtml}
        </ul>
      </div>`;
        desktopSearchContainer.append(parentHtml);
      }
      addAsStaticOtherContent();

      if (changeASLayoutToMobile) {
        document
          .querySelector(".mobile-search .search-form .close-search")
          .addEventListener("touchstart", (e) => {
            const unbxdAsWrapperMobile = document.querySelector(
              ".unbxd-as-wrapper-default"
            );
            if (unbxdAsWrapperMobile != null) {
              unbxdAsWrapperMobile.style.setProperty("display", "none");
            }
          });
      }
      document.addEventListener("click", (e) => {
        if (
          e.target.closest(
            ".header .main-nav > .search-container .search__form"
          ) == null
        ) {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
        }
      });

      $(document).on("focus click", autosuggest_input_element, function () {
        let inputValue = autosuggest_input_element.val();
        if (inputValue == "") {
          if (window.innerWidth <= 1024) {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "block");
          } else {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "flex");
          }
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "block");
        } else {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        }
      });
      $(document).on("focus click", "input#filterZip", function () {
        let inputValue = autosuggest_input_element.val();
        if (inputValue == "") {
          if (window.innerWidth <= 1024) {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "none");
          } else {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "none");
          }
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        } else {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        }
      });
      $(document).on("input", autosuggest_input_element, function () {
        let inputValue = autosuggest_input_element.val();
        if (inputValue == "") {
          if (window.innerWidth <= 1024) {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "block");
          } else {
            desktopSearchContainer
              .find(".unbxd-as-wrapper.unbxd-custom-as")
              .css("display", "none");
          }
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "block");
        } else {
          desktopSearchContainer
            .find(".unbxd-as-wrapper.unbxd-custom-as")
            .css("display", "none");
          mobileSearchContainer
            .find("#unbxd-custom-mobile-autosuggestion")
            .css("display", "none");
        }
      });
      // analytics events
      // product click
      const staticAsProducts = document.querySelectorAll(
        ".unbxd-custom-as .UNX-product-click-event"
      );
      for (const staticAsProduct of staticAsProducts) {
        const { pid, prank, query, type, value } = staticAsProduct.dataset;

        staticAsProduct.addEventListener("click", () => {
          const payload = {
            query: value,
            autosuggestParams: {
              autosuggest_type: type,
              pid: String(pid),
              unbxdprank: Number(prank),
              internal_query: query,
            },
          };
          unbxdAnalytics("search", payload);
        });
      }

      // suggestion click
      const staticAsSuggestions = document.querySelectorAll(
        ".UNX-static-as-suggestion"
      );
      for (const staticAsSuggestion of staticAsSuggestions) {
        const { type, fieldName, value, query } = staticAsSuggestion.dataset;

        staticAsSuggestion.addEventListener("click", () => {
          const autosuggestParams = {
            autosuggest_type: type,
            autosuggest_suggestion: value,
            field_name: fieldName,
            field_value: value,
            src_field: "",
            internal_query: query,
          };
          const payload = {
            query: value,
          };
          payload.autosuggestParams = autosuggestParams;
          unbxdAnalytics("search", payload);
        });
      }
    })
    .fail(function (res) {
      console.log("error occurs");
    });
});




```