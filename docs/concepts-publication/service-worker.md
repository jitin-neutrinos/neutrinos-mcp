# Service Worker

<https://documentation.neutrinos.com/articles/#!concepts-publication/service-worker>

A service worker is a script that runs in the web browser and manages caching for an application. It functions as a network proxy. It intercepts all outgoing HTTP requests made by the application and can choose how to respond to them. For example, the service worker can query a local cache and deliver a cached response if one is available.

Unlike the other scripts that make up an application, the service worker is preserved after the user closes the tab. The next time that browser loads the application, the service worker loads first, and can intercept every request for resources to load the application.

Service worker also reduces dependency on the network and can significantly improve the user experience. It essentially acts like a proxy server that sits between web applications, the browser, and the network (when available). It enables the creation of effective offline experiences, intercepts network requests and takes appropriate action based on whether the network is available, and updates assets residing on the server.

It also allows access to push notifications and background sync APIs.

See [Service Worker APIs](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) to learn more.
