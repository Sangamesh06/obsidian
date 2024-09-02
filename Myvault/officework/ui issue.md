a tag

```
a_("", "{{productUrl}}", _d('title-apmex'), "{{getTrimmedText title 38}}")
```

```
<a class="" href="product/189172/american-silver-eagles-random-year-20-coin-mintdirectR-tube" data-title-apmex="189172">American Silver Eagles (Random Year, 2...</a>
```

a : class , href , _d(attributename) = data-attribute-naeme = "attribute_value" , value

div tag

```
div_("product_item_image", "",

img_("lazy", '{{checkImageUrl imageUrl}}', 'alt="{{title}}" height="136" width="136" title="{{title}}"')

),
```

```
div_("product_item_image", "",
a_("", "{{productUrl}}", _d('title-apmex'), 
img_("lazy", '{{checkImageUrl imageUrl}}', 'alt="{{title}}" height="136" width="136" title="{{title}}"')
)
),
```

```
<div class="product_item_image"><img class="lazy" src="https://www.images-apmex.com/images/Catalog%20Images/Products/189172_slab.jpg?v=20200806140648&amp;width=130&amp;height=130" alt="American Silver Eagles (Random Year, 20-Coin MintDirect® Tube)" height="136" width="136" title="American Silver Eagles (Random Year, 20-Coin MintDirect® Tube)"></div>
```

 div : class , style  , content

final product
```
<div class="product_item_image"><a class="" href="product/189172/american-silver-eagles-random-year-20-coin-mintdirectR-tube" data-title-apmex="189172"><img class="lazy" src="https://www.images-apmex.com/images/Catalog%20Images/Products/189172_slab.jpg?v=20200806140648&amp;width=130&amp;height=130" alt="American Silver Eagles (Random Year, 20-Coin MintDirect® Tube)" height="136" width="136" title="American Silver Eagles (Random Year, 20-Coin MintDirect® Tube)"></a></div>
```





```

div : class , style , inner content

Sure! Dot.js (also known as doT.js) is a fast and lightweight templating engine for JavaScript. It uses a concise syntax for embedding JavaScript code within HTML templates.

Here are some basic examples and syntax guidelines for doT.js:

### Template Delimiters

- `{{ ... }}`: For JavaScript code.
- `{{= ... }}`: For outputting a value (HTML-escaped).
- `{{! ... }}`: For outputting a value (not HTML-escaped).
- `{{# ... }} ... {{## ... }} {{# ... /#}}`: For defining partials.
- `{{? ... }} ... {{?}}`: For conditional rendering (if).
- `{{~ ... :value:index}} ... {{~}}`: For looping through arrays.

### Example Templates

1. **Basic Value Output**

html

Copy code

`<div>{{= it.name }}</div>`

Given a data object `{ name: "John" }`, this will render:

html

Copy code

`<div>John</div>`

2. **Conditional Rendering**

html

Copy code

`{{? it.isAdmin }}   <div>Admin Panel</div> {{?}}`

Given a data object `{ isAdmin: true }`, this will render:

html

Copy code

`<div>Admin Panel</div>`

3. **Looping Through Arrays**

html

Copy code

`<ul>   {{~ it.items :item:index }}     <li>{{= item }}</li>   {{~}} </ul>`

Given a data object `{ items: ["Item 1", "Item 2", "Item 3"] }`, this will render:

html

Copy code

`<ul>   <li>Item 1</li>   <li>Item 2</li>   <li>Item 3</li> </ul>`

4. **Defining Partials**

Define a partial:

html

Copy code

`{{##def.snippet:   <div>{{= it.message }}</div> #}}`

Use the partial:

html

Copy code

`{{#def.snippet}}`

Given a data object `{ message: "Hello, world!" }`, this will render:

html

Copy code

`<div>Hello, world!</div>`

5. **Inline JavaScript Code**

html

Copy code

`{{ var total = it.price * it.quantity; }} <div>Total: {{= total }}</div>`

Given a data object `{ price: 10, quantity: 2 }`, this will render:

html

Copy code

`<div>Total: 20</div>`



```
<a class="" href="product/189172/american-silver-eagles-random-year-20-coin-mintdirectR-tube" data-title-apmex="189172"><div class="product_item_image"><img class="lazy" src="https://www.images-apmex.com/images/Catalog%20Images/Products/189172_slab.jpg?v=20200806140648&amp;width=130&amp;height=130" alt="American Silver Eagles (Random Year, 20-Coin MintDirect® Tube)" height="136" width="136" title="American Silver Eagles (Random Year, 20-Coin MintDirect® Tube)"></div></a>
```
```



git commit -m "chore(apmex):adding bundled files for search.js" 


grunt bundlecss --custom=prod-autoSuggestcss
grunt uploadjs --custom=prod-searchjs  
grunt invalidatejs --custom=prod-searchjs




