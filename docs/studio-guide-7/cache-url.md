# Cache URLs in Service Worker

<https://documentation.neutrinos.com/articles/#!studio-guide-7/cache-url>

After converting your app to a PWA, you can cache your app pages so that (after the first access) they can be viewed even when the device is offline.

Use the **Cache Config** editor to define the policy by which matching requests should be cached. Perform the following tasks:

1. On the [Studio Application](/smart/project-concepts/studio-application-page) page, click **Settings** and select **PWA**.
2. In the PWA editor, scroll down to access **Cache Config**. Click the **+** icon next to **Cache config** to add a cache configuration.
3. In the pop-up editor, enter the following details:
  - **Name: **The name of the cache configuration.
  - **Strategy: **The Strategy to access data resources.
    - **Performance - **Used in situations where performance is a priority. If the requested data exists in the cache, the service worker fetches it and responds back. If the data does not exist, the service worker makes a network request. This strategy will have some staleness in data, depending on the **Max age**, in exchange for better performance. Use it to fetch resources that don't change often.
    - **Freshness -** Used in situations where the accuracy of data is a priority. The service worker fetches the requested data from the network. Only if the network times out, according to timeout, does the request fall back to the cache. This strategy is useful for resources that change frequently.
  - **Timeout:** The network timeout. It is how long the service worker will wait for the network to respond before using a cached response, if configured to do so. Enter a duration string using the following unit suffixes:
      For example, the string 5s30u will translate to five seconds and 30 milliseconds of network timeout.
    - d: days
    - h: hours
    - m: minutes
    - s: seconds
    - u: milliseconds
  - **Max size:** The maximum number of entries, or responses, in the cache.
  - **Max age:** The maximum duration allowed for responses to remain in the cache before being considered invalid and evicted. Enter a duration string using the unit suffixes.
  - **URL:** A list of URLs. Click the **+** icon to add one or more URLs. URLs that match these patterns are cached. Note that only non-mutating requests (GET and HEAD) are cached.
4. Click **Add** to save the configuration.
