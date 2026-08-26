# Working with Functions

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/writing-functions>

## Working with Functions

The Function node allows JavaScript code to be run against the messages that are passed through it. The message is passed in as an object called msg. By convention, it will have a msg.payload property containing the body of the message.

- [Writing a Function](/articles/neutrinos-modelr-guide/writing-functions/a/h3_1519923485)
- [Sending to multiple outputs](/articles/neutrinos-modelr-guide/writing-functions/a/h3__1177040932)
- [Sending multiple messages](/articles/neutrinos-modelr-guide/writing-functions/a/h3_1077748506)
- [Sending messages asynchronously](/articles/neutrinos-modelr-guide/writing-functions/a/sending_msgs)
- [Logging events](/articles/neutrinos-modelr-guide/writing-functions/a/h3__1078339613)
- [Handling errors](/articles/neutrinos-modelr-guide/writing-functions/a/h3_1318256357)
- [Storing data (context)](/articles/neutrinos-modelr-guide/writing-functions/a/h3_79866783)
- [Get/Set multiple values](/articles/neutrinos-modelr-guide/writing-functions/a/h3_1005679739)
- [Asynchronous context access](/articles/neutrinos-modelr-guide/writing-functions/a/h3__762805005)
- [Multiple context stores](/articles/neutrinos-modelr-guide/writing-functions/a/h3__1561526169)
- [API Reference](/articles/neutrinos-modelr-guide/writing-functions/a/h3_953674995)

### Write a Function

The code entered into the Function node represents the body of the function. The most simple function simply returns the message exactly as-is:

```java
return msg;
```

If the function returns null, then no message is passed on and the flow ends.

Note that the function must always return a msg object. Returning a number or string will result in an error. The returned message object does not need to be the same object as was passed in; the function can construct a completely new object before returning it. For example:

```java
var newMsg = { payload: msg.payload.length };return newMsg;
```

| ![Information](/resources/Storage/neutrinos-modelr-guide/info.png) | Constructing a new message object will lose any message properties of the received message. This will break some flows, for example, the HTTP In/Response flow requires the msg.req and msg.res properties to be preserved end-to-end.  In general, function nodes should return the message object they were passed having made any changes to its properties. |
| --- | --- |

---

### Multiple Outputs

The function edit dialog allows the number of outputs to be changed. If there is more than one output, an array of messages can be returned by the function to send to the outputs.

This makes it easy to write a function that sends the message to different outputs depending on some condition. For example, this function would send anything on the topic Neutrinos to the second output rather than the first:

```java
if (msg.topic === "Neutrinos") {return [ null, msg ];} else {return [ msg, null ];}
```

The following example passes the original message as-is on the first output and a message containing the payload length is passed to the second output:

```java
var newMsg = { payload: msg.payload.length };return [msg, newMsg];
```

---

### Multiple Messages

A function can return multiple messages on output by returning an array of messages within the returned array. When multiple messages are returned for an output, subsequent nodes will receive the messages one at a time in the order they were returned.

In the following example, msg1, msg2, msg3 will be sent to the first output. msg4 will be sent to the second output.

```java
var msg1 = { payload:"first out of output 1" };var msg2 = { payload:"second out of output 1" };var msg3 = { payload:"third out of output 1" };var msg4 = { payload:"only message from output 2" };return [ [ msg1, msg2, msg3 ], msg4 ];
```

The following example splits the received payload into individual words and returns a message for each of the words.

```java
var outputMsgs = [];var words = msg.payload.split(" ");for (var w in words) {outputMsgs.push({payload:words[w]});}return [ outputMsgs ];
```

---

### Send Messages Asynchronously

If the function needs to perform an asynchronous action before sending a message it cannot return the message at the end of the function. Instead, it must make use of the node.send() function, passing in the message(s) to be sent. For example:

```java
doSomeAsyncWork(msg, function(result) {node.send({payload:result});});return;
```

If you do use asynchronous callback code in your functions then you may need to tidy up any outstanding requests, or close any connections, whenever the flow gets re-deployed. You can do this by adding a close event handler.

```java
node.on('close', function() {// tidy up any async code here - shutdown connections and so on.});
```

---

### Log Events

If a node needs to log something to the console, it can use one of the following functions:

```java
node.log("Something happened");node.warn("Something happened you should know about");node.error("Oh no, something bad happened");
```

The warn and error messages also get sent to the flow editor **debug** tab.

For finer grained logging, node.trace() and node.debug() are also available. If there is no logger configured to capture those levels, they will not be seen.

---

### Handle Errors

If the function encounters an error that should halt the current flow, it should return nothing. To trigger a **Catch** node on the same tab, the function should call node.error with the original message as a second argument:

```java
node.error("hit an error", msg);
```

---

### Store Data

Aside from the msg object, the function can also store data in the context store. In the **Function** node there are three predefined variables that can be used to access context:

- **context** - the node’s local context
- **flow **- the flow scope context
- **global** - the global scope context

The following examples use flow **context** but apply equally well to context and global.

There are two modes for accessing context; either synchronous or asynchronous. The built-in context stores provide both modes. Some stores may only provide asynchronous access and will throw an error if they are accessed synchronously.

To get a value from context:

```java
var myCount = flow.get("count");
```

To set a value:

```java
flow.set("count", 123);
```

The following example maintains a count of how many times the function has been run:

```java
// initialise the counter to 0 if it doesn't exist alreadyvar count = context.get('count')||0;count += 1;// store the value backcontext.set('count',count);// make it part of the outgoing msg objectmsg.count = count;return msg;
```

---

### Get/Set Multiple Values

You can also get or set multiple values in one go:

```java
// Node-RED 0.19 or latervar values = flow.get(["count", "colour", "temperature"]);// values[0] is the 'count' value// values[1] is the 'colour' value// values[2] is the 'temperature' value// Node-RED 0.19 or laterflow.set(["count", "colour", "temperature"], [123, "red", "12.5"]);
```

In this case, any missing values are set to null.

---

### Asynchronous Context Access

If the context store requires asynchronous access, the get and set functions require an extra callback parameter.

```java
// Get single valueflow.get("count", function(err, myCount) { ... });// Get multiple valuesflow.get(["count", "colour"], function(err, count, colour) { ... })// Set single valueflow.set("count", 123, function(err) { ... })// Set multiple valuesflow.set(["count", "colour", [123, "red"], function(err) { ... })
```

The first argument passes to the callback, err is only set if an error occurred when accessing context.

The asynchronous version of the count example becomes:

```java
context.get('count', function(err, count) {if (err) {node.error(err, msg);} else {// initialise the counter to 0 if it doesn't exist alreadycount = count || 0;count += 1;// store the value backcontext.set('count',count, function(err) {if (err) {node.error(err, msg);} else {// make it part of the outgoing msg objectmsg.count = count;// send the messagenode.send(msg);}});}});
```

---

### Multiple Context Stores

You can configure multiple context stores. For example, both a memory and a file-based store could be used.

The get/set context functions accept an optional parameter to identify the store to use.

```java
// Get value - syncvar myCount = flow.get("count", storeName);// Get value - asyncflow.get("count", storeName, function(err, myCount) { ... });// Set value - syncflow.set("count", 123, storeName);// Set value - asyncflow.set("count", 123, storeName, function(err) { ... })
```

---

### API Reference

The following objects are available within the **Function** node.

**node**

- node.id : the id of the Function node
- node.name : the name of the Function node
- node.log(..) : log a message
- node.warn(..) : log a warning message
- node.error(..) : log an error message
- node.debug(..) : log a debug message
- node.trace(..) : log a trace message
- node.on(..) : register an event handler
- node.status(..) : update the node status
- node.send(..) : send a message

**context**

- context.get(..) : get a node-scoped context property
- context.set(..) : set a node-scoped context property
- context.keys(..) : return a list of all node-scoped context property keys
- context.flow : same as flow
- context.global : same as global

**flow**

- flow.get(..) : get a flow-scoped context property
- flow.set(..) : set a flow-scoped context property
- flow.keys(..) : return a list of all flow-scoped context property keys

**global**

- global.get(..) : get a global-scoped context property
- global.set(..) : set a global-scoped context property
- global.keys(..) : return a list of all global-scoped context property keys

**RED**

- RED.util.cloneMessage(..) : safely clones a message object so it can be reused

| ![Information](/resources/Storage/neutrinos-modelr-guide/info.png) | The function node automatically clears any outstanding timeouts or interval timers whenever it is stopped or re-deployed. |
| --- | --- |
