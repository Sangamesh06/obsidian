
the data from previous page that is available in current page is this
```run-javascript

let prevPageView = {
  name: "",
  uniqueInfo: "",
  url: "",
  title: ""
};

```

```run-javascript
 Unbxd.loadeventConfigScript = function loadeventConfigScript(url, callback) {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    document.getElementsByTagName('head')[0].appendChild(script);
  };
```

loadeventconfigscript is not using callback
make sure to use ccallback so that function that depend on this script un only after fetching this script

gethash is not secure

Throttling is a technique used to control the rate at which an operation or process occurs. In the context of web analytics and API calls, it's used to limit the number of actions or requests that can be made within a specific time frame.



```
parse: JSON.parse.bind(JSON),
stringify: JSON.stringify.bind(JSON),
```
- - `parse`: This binds `JSON.parse` to `Unbxd.JSON.parse`. `JSON.parse` converts JSON strings into JavaScript objects. This is essential in analytics to parse incoming JSON data from APIs, logs, or data files into usable objects.
    - `stringify`: Similarly, `JSON.stringify` is bound to `Unbxd.JSON.stringify`. `JSON.stringify` converts JavaScript objects into JSON strings. In analytics, this is used to prepare data for storage or transmission, such as saving processed data back into a database or sending it to another service.
- 


```run-javascript

  Unbxd.JSON = {
    parse: JSON.parse.bind(JSON),
    stringify: JSON.stringify.bind(JSON),//next function is used for custmosing stringify in versionless 1.7 arraytojson got changed so this is used (stringify function is diffrent so)
    u_stringify: function (value) {
      var arrayToJSON = Array.prototype.toJSON;
      try {
        if (
          typeof Prototype !== 'undefined' &&
          parseFloat(Prototype.Version.substr(0, 3)) < 1.7 &&
          typeof arrayToJSON !== 'undefined'
        ) {
          delete Array.prototype.toJSON;
          var r = JSON.stringify(value);
          Array.prototype.toJSON = arrayToJSON;
          return r;
        }
      } catch (ex) { }
      return JSON.stringify(value);
    }
  };
```

parse: JSON.parse.bind(JSON), 
stringify: JSON.stringify.bind(JSON), 
make parse function of unbxd same as in one json library and similaryly for stringify
