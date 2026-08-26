# HTTP Requests

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/http-requests>

## HTTP Requests

These recipes address problems specific to **HTTP requests **and shows by example how they can be solved using the capabilities of Modelr .

[Simple GET request](/articles/neutrinos-modelr-guide/http-requests/a/h1__563904887)


 [Set the URL of a request](/articles/neutrinos-modelr-guide/http-requests/a/h1__296250831)




 [Set the URL of a request using a template](/articles/neutrinos-modelr-guide/http-requests/a/seturlrequestusingtemplate)





 [Set the query string parameters in a URL](/articles/neutrinos-modelr-guide/http-requests/a/setqueryparametersurl)




 [Get a parsed JSON Response](/articles/neutrinos-modelr-guide/http-requests/a/h1_1711691569)




 [Get binary response](/articles/neutrinos-modelr-guide/http-requests/a/h1__1790261390)




 [Set a request header](/articles/neutrinos-modelr-guide/http-requests/a/h1_1253060557)






 Simple GET request


  Problem


 You want to make a simple GET request to a web site and extract useful information.


  Solution


 Use the `**HTTP Request**` node to make an HTTP request and an `**HTML**` node to extract elements from the retrieved html document.


 Example


 ![](https://cookbook.nodered.org/images/http/simple-get-request.png)


 To find content on a web page, the Chrome browser’s **Inspect Element** can be a useful tool. Using the browser, right click on a page element to see the tags, ids, and classes applied to an element.



 Set the URL of a request


 ** Problem**


 You want to set the URL of an HTTP request node dynamically.


  Solution


 Set the URL property of the `**HTTP Request**` node.


 Example


 ![](https://cookbook.nodered.org/images/http/set-request-url.png)


 The `**Inject**` node generates a string URL, and the `**Change**` node sets the msg.URL property. In this flow, the URL is set to:Copy CodeHTMLhttp://vancouver.craigslist.org/search/sss?format=rss&query=cars


 To return an RSS feed for cars for sale in Vancouver on Craigslist. It returns something like the following XML content in the debug window:Copy CodeXML<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 xmlns="http://purl.org/rss/1.0/"
 xmlns:enc="http://purl.oclc.org/net/rss_2.0/enc#"
 xmlns:ev="http://purl.org/rss/1.0/modules/event/"
 xmlns:content="http://purl.org/rss/1.0/modules/content/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:syn="http://purl.org/rss/1.0/modules/syndication/"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:taxo="http://purl.org/rss/1.0/modules/taxonomy/"
 xmlns:admin="http://webns.net/mvcb/" >
<channel rdf:about="https://vancouver.craigslist.ca/search/sss?format=rss&#x26;query=cars">
 <title>
 craigslist vancouver, BC | for sale search "cars"
 </title>
 <link>
 https://vancouver.craigslist.ca/search/sss?query=cars
 </link>
 <description></description>
 <dc:language>en-us</dc:language>
 <dc:rights>copyright 2017 craiglist</dc:rights>
 <dc:publisher>robot@craigslist.org</dc:publisher>
 <dc:creator>robot@craigslist.org</dc:creator>
 <dc:source>https://vancouver...


 ** Discussion**


  An `**XML**` node can be added after the `**HTTP Request**` to change the XML RSS content returned to a JavaScript object for easy access to the data.



 Set the URL of a request using a template


  Problem


 You want to dynamically set the URL of an HTTP request where only parts of the url change between requests.


  Solution


 Configure the `**HTTP Request**` node to generate a URL dynamically using a [mustache](http://mustache.github.io/mustache.5.html) URL template.


 Example


 ![](https://cookbook.nodered.org/images/http/set-request-url-template.png)


 In this flow, the `**Inject**` node sends an id for a post we would like to request from an API. The `**Change**` node changes this to `msg.post`. The `**HTTP Request**` node generates a URL by substituting `msg.post` of the URL property configured as shown:Copy CodeHTMLhttps://jsonplaceholder.typicode.com/posts/{{post}}


 The JSON output from this API in the debug panel will look as follows:Copy CodeHTML{ "userId": 1, "id": 2, "title": "qui est esse", "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla" }


  Discussion


 To ensure HTML escaping is not used in your URL use `{{{triple}}}` braces.



 Set the query string parameters in a URL


 Problem


 You want to set the query string parameters of a URL for an HTTP request.


  Solution


 Use the `**HTTP Request**` node’s support for the [mustache](http://mustache.github.io/mustache.5.html) to substitute query parameter strings in URLs directly.


 Example


 ![](https://cookbook.nodered.org/images/http/set-query-string.png)


 The `**Inject**` node generates a query string that is to be sent in the URL. The `**Change**` node changes this to `msg.query` which is substituted in the mustache template in the `**HTTP Request**` node URL property configured as shown:Copy CodeHTMLhttps://query.yahooapis.com/v1/public/yql?q={{{query}}}&format=json


 The returned JSON content is the sunset in Hawaii:Copy CodeHTML"{"query":{"count":1,"created":"2017-01-22T01:31:07Z","lang":"en-US","results":{"channel":{"astronomy":{"sunset":"6:9 pm"}}}}}"


 **Discussion**


 By default, mustache will escape any HTML entities in the values it substitutes. To ensure HTML escaping is not used in your URL use `{{{triple}}}` braces.



 Get a parsed JSON Response


  Problem


 You want to return the JSON response of an HTTP request as a parsed Javascript object.


  Solution


 The `**HTTP Request**` node will return a the body of a JSON response in the `msg.payload` as a string by default. Change the `Return` configuration of this node to `a parsed JSON object` to parse the JSON response in the `msg.payload` that can be easily accessed by downstream nodes.


 Example


 ![](https://cookbook.nodered.org/images/http/parse-json-response.png)


 We have reconfigured the flow from the [Set the URL of a Request URL recipe](https://cookbook.nodered.org/http/set-request-url.html) by changing the `**HTTP Request **`node configuration. The `**Debug**` node has been modified to display only the `title` property of the parsed JSON response:Copy CodeHTML"qui est esse"


  Discussion


 If your HTTP request returns XML, the `**XML**` node can be used to parse Javascript objects from XML documents.



 Get a binary response


  Problem


 You want to get a binary HTTP response from an HTTP request.


  Solution


 The `**HTTP Request**` node will return the body of a response in the `msg.payload` as a string by default. Change the `Return` configuration of this node to `a binary buffer` to return the response as a binary buffer in the `msg.payload`.


 Example


 ![](https://cookbook.nodered.org/images/http/get-binary-response.png)


 We have modified the flow from the [Set the URL of a Request URL recipe](https://cookbook.nodered.org/http/set-request-url.html) by changing the `**HTTP Request**` node `Return` configuration to `a binary buffer`. The `**Debug**` node will display the payload as a binary buffer such as:Copy CodeHTML[ 80, 75, 3, 4, 20, 0, 6, 0, 8, 0 … ]



 Set a request header


  Problem


 You need to send an HTTP request with specific request headers.


  Solution


 Set the `msg.headers` field to the field value pairs of the request headers you would like to include in the message sent to the `**HTTP request**` node.


 Example


 ![](https://cookbook.nodered.org/images/http/set-request-header.png)


 In this example, we set the `X-Auth-User` and `X-Auth-Key` request headers to call a private HTTP input node on the FRED Node-RED cloud service.


 The code in the `**Function**` node below adds these additional message fields by adding a `msg.headers` object, and setting the header field/values in this object as shown.



 Copy CodeHTMLmsg.payload = "data to post"; msg.headers = {}; msg.headers['X-Auth-User'] = 'mike'; msg.headers['X-Auth-Key'] = 'fred-key'; return msg;
