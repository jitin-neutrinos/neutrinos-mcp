# 6.0.0

<https://documentation.neutrinos.com/articles/#!change-log/next-tutorial>

## 6.0.0

#### Date: (2019-06-28)

### Features:

- You can minimize and maximize the view of a dropable and advanced component in the page container by using **Minimize** and **maximize** buttons.

![Minimize](/resources/Storage/change-log/min.png)

![Maximize a component](/resources/Storage/change-log/max.png)

- After dragging & dropping components to a page, you can perform the following shortcuts on the page container:
    **Action**
    **Keyboard Shortcuts on Windows and Linux**
    **Keyboard Shortcuts on MAC**
    Delete a component
    Ctrl + Delete
    Command + Delete
    Cut a component
    Ctrl + X
    Command + X
    Paste a component
    Ctrl + V
    Command + V
    Save a page
    Ctrl + S
    Command + S

The Neutrinos Studio landing page is updated with a new UI.

![Neutrinos Studio home page](/resources/Storage/change-log/studio%20home.png)

- The **Edit App Details** window is updated with a new UI. You can directly access Neutrinos Store from this window by clicking the **+** button.

![Enter App Details window](/resources/Storage/change-log/add_app.png)

- The Studio Application page is updated with descriptive palette components. Each window within the Application page can be resized, and collapsed, giving you more space to design your app. Use the toggle buttons at the bottom right of the page to collapse and expand windows. Also, the highlight feature is added to show the active or newly added component.

![Neutrinos Studio Application page](/resources/Storage/change-log/application%20page.png)

- **Views**- Refresh the Attribute Window of a view to fetch its latest Input/Output Attributes.
- **Notifications**- Any changes you’ve made to the app, can be viewed from your notification bar. You can click the bell icon to see the latest changes made to your app.

- The Angular material icons are updated and are migrated to the latest version.

**Updates**

- If you want to use splash screens for the iOS build, you have to create them with the specifications mentioned below. Also, the splash screens have to be uploaded to the **splash** folder under the **iOS** > **Resources** folder of the Assets Editor.

```xml
<splash height="480" src="src/assets/iOS/Resources/splash/Default~iphone.png" width="320"/><splash height="960" src="src/assets/iOS/Resources/splash/Default@2x~iphone.png" width="640"/><splash height="1024" src="src/assets/iOS/Resources/splash/Default-Portrait~ipad.png" width="768"/><splash height="2048" src="src/assets/iOS/Resources/splash/Default-Portrait@2x~ipad.png" width="1536"/><splash height="768" src="src/assets/iOS/Resources/splash/Default-Landscape~ipad.png" width="1024"/><splash height="1536" src="src/assets/iOS/Resources/splash/Default-Landscape@2x~ipad.png" width="2048"/><splash height="1136" src="src/assets/iOS/Resources/splash/Default-568h@2x~iphone.png" width="640"/><splash height="1334" src="src/assets/iOS/Resources/splash/Default-667h.png" width="750"/><splash height="2208" src="src/assets/iOS/Resources/splash/Default-736h.png" width="1242"/>
```

**Bug Fixes**

- Neutrinos-module is migrated to 0.0.41
- When you delete a legacy service, Neutrinos does not deletes file from the filesystem.

**Deprecations**

- H1, H2, H3, H4, H5, H6, Paragraph and Custom HTML drag and drop components have been deprecated. As an alternative Html 5 advanced component is added, which will provide all popular HTML 5 elements along with deprecated components.
