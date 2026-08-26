# Step 2: Configure Cache Settings

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/step2-configure-cache-settings>

After converting your app to a PWA, you can also cache your application pages so that, after the first access, they can be viewed even when the device is offline. Use the **Cache Config** editor to define the policy by which matching requests should be cached.

In this tutorial, we will be caching the weather details of the city **Varanasi**. If a user searches the weather details of city Varanasi when the app is offline, the cached page will be fetched from the [service worker](/smart/project-concepts/service-worker) and displayed to the user. Perform the following steps:

1. Click the **+** icon next to **Cache config** to add a new cache configuration.
2. Enter the following details:
  - **Name: **The name of the cache configuration. Enter the name as **weather**.
  - **Strategy: **The strategy to access data resources. Select **Performance** as the strategy from the drop-down list.
  - **Timeout: **The network timeout. Enter **20s **as the timeout.
  - **Max Size: **The maximum number of entries, or responses, in the cache. Enter **1000**.
  - **Max Age: **The maximum duration allowed for responses to remain in the cache before being considered invalid and evicted. Enter 3d as the value for this field.
  - **URL:** Enter the URL as http://localhost:8081/api/weather?cityName=varanasi
3. Click Add to save the settings.

![Add cache settings for the PWA](/resources/Storage/tutorial-create-a-pwa/step2-configure-cache-settings-2021-04-07.png)

To learn more about these fields, see [Cache URLs in Service Worker](/smart/project-sample-how-to-guide/cache-url).
