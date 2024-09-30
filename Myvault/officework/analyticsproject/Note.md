in analytics for selecting the element  always use
classname first and then id if they both target single element
wrong
```
#myBody[class*="cat"]#myBody
```
correct
[class*="cat"]#myBody

and generally if there are many classname for single elemet and you want to select element based on its classname starts with cat then first classname has to start with  cat otherwise it will not select the element
[class^="cat"]#myBody(wrong if first classname is store_products  and second classname is cat3)
to select above element use selector like this
[class*="cat"]#myBody




