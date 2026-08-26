# Navigation

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/navigation>

Neutrinos navigation guard nodes are objects which instructs the router whether or not it should allow navigation to a requested route. Based on the logic specified in the navigation service flows, it returns a boolean (true/false) value which determines if an user is allowed to navigate in or out to a certain route.

There are three different types of guards and each of them can be called in a particular sequence. The router’s behavior is modified differently depending on which guard is used. The guards are:

1. [Guard-In-Routing](/articles/client-services-designer-9/guard-in-routing)
2. [Guard-Out-Routing](/articles/client-services-designer-9/guard-out-routing)
3. [Resolve](/articles/client-services-designer-9/resolver-node)
