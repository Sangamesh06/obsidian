complete landmark 
complete tatamotors order pagveiw
	 Order: {
                uniqueSelectors: {
                    selectors: ['.order-2 .btn-brand[title = "Click here for Confirm Booking"]']
                }
            }
            
complete pedders page veiw

  


const PuppySpotStage = {
        search: {
            inputBox: ".search .style-module__input--8Dj0T",
            queryBtn: ".search .track_top_search_bar",
            urlParam: "search",
        },
        productClickGrid: {
            productElemWrapper: ".puppies-for-sale__results .puppies-for-sale__puppy-list a .card",
            pidSelector: ".puppies-for-sale__results .puppies-for-sale__puppy-list a .card .card__image",
            productPidAttr: "src",
            getPidFromCB : function  (pidString) {
                const parts = pidString.split('/');
                 return(parts[parts.length - 3]);
            },
            source: "PRODUCT_CLICK_GRID"
        },
        addToCartFromPDP: {
            addToCartBtnSelector: ".puppy-profile__information .puppy-profile__cta a",
            pidSelector: ".puppy-profile__information .puppy-profile__cta .js-add-to-cart",
            productPidAttr: "data-puppy",            
            source: "ADD_TO_CART_PDP",
        },
        addToCartFromCartPage: {
            cartItemWrapper: "",
            pidSelector: "",
            productPidAttr: "",
            qtySelector: "",
            qtyPlusSelector: "",
            qtyMinusSelector: "",
            qtyDelay: "",
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
            qtyDelay: "2000",
            // for 2sec
            priceSelector: "",
            productPriceAttr: "",
            source: "ORDER_FROM_CHECKOUT",
        },
        pageView: {
            delay: "1500",
            events: {
                home: {
                    uniqueSelectors: {
                        selectors: ['.homepage .hero-module__hero--fxGmC .hero-module__heroContent--x5Q7B'],
                    },
                    urlIdentifiers: {
                        urls: ["https://consumer-stage-05.puppyspot.com/"],
                        exactMatch: true,
                    },
                },
                search: {
                    uniqueSelectors: {
                        selectors: ['.puppies-for-sale-header .breed-searchbar__breed-tag--search'],
                    },
                    urlIdentifiers: {
                        urls: ["puppies-for-sale?search"],
                        exactMatch: false,
                    },
                },
                category: {
                    urlIdentifiers: {
                        urls: ["puppies-for-sale?breed_slug"],
                        exactMatch: false,
                    },
                },
                productDisplay: {
                    uniqueSelectors: {
                        selectors: ['.puppy-profile  .puppy-profile__sub-details'],
                    },
                     urlIdentifiers: {
                        urls: ["puppies-for-sale/breed/"],
                        exactMatch: false,
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
