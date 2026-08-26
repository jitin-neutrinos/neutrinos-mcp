# Top Menu

<https://documentation.neutrinos.com/articles/#!concepts-publication/studio-application-page>

After creating an app, you click the app to open the Studio Application page. You use this page to design, configure, and deploy your app.

The page contains the following elements:

### Top Menu

**Edit: **The Edit menu allows you to perform specific actions on the Studio Application page.

- **Save Current Tab:** Save the current tab.
- **Close Current Tab**: Close the current tab.
- **Toggle Html<> Ts**: Used to switch between the HTML and Ts editor.
- **Undo:** Undo last change.
- **Cut:** Cut the selected component.
- **Copy: **Copy selected component.
- **Paste:** Paste the copied component.
- **Paste and Match Style:** Paste the copied component to match the style of the existing component.
- **Select All**: Select all the components.
- Search Nodes: Opens a search bar and displays a list of nodes to quickly navigate to a node.e

**Plugins: **The Plugins menu allows you to download and manage app dependencies.

- **[Plugins Builder](/articles/concepts-publication/plugins-builder)**
- **Manage Plugins:** Allows you to manage app plugins and dependencies.
- **Go to store:** Links to Neutrinos Store.

**Window: **The Window menu allows you to open additional windows.

- **New Window: **Opens Neutrinos Studio in a new window.
- **New Plugin Builder: **Opens the Plugin Builder of Neutrinos Studio in a new window.

**View: **The View menu allows you to change the studio theme.

- Invert Colors (Experimental Dark Mode): Opens Studio in a dark mode theme. You can click the same option again to change the Studio to its default theme.

**Help: **The Help menu provides help documents. It provides the following options:

- **Learn More:** Links to Neutrinos Knowledge center which hosts the product documentation.
- **About: **Displays the version of Neutrinos Studio installed on your machine.

### Side Menu/Editor Pane

The editor pane provides you the Studio editors to visually design and builds your app:

**Settings: **Manage IDS, logger, and PM2 settings.
**Routes**: Connect pages by creating and configuring routes for apps.**Pages**: Create responsive pages by defining page layouts using a variety of components j the palette list and configure properties.**Config XML**: Manage application resources such as Cordova plugins, splash screens for multiple devices, etc.**Styles**: Apply CSS or SaSS app styles.**Models**: Create data models to identify the data, data attributes, and relationships or associations with other data. **Environments**: Create multiple environments and configure environment variables. **Assets Editor**: Upload and store the app assets**Services**: Add client and server services to your app.The menu also contains the following options:![](/resources/Storage/concepts-publication/project-sample-how-to-guide/understanding-the-application-home-page-2019-04-16-10.png): Opens and closes the TypeScript window.![](/resources/Storage/concepts-publication/project-sample-how-to-guide/palette_icon.png): Opens and closes the palette list.
![](/resources/Storage/concepts-publication/project-sample-how-to-guide/understanding-the-application-home-page-2019-04-16-12.png): Opens and closes the terminal window.
![](/resources/Storage/concepts-publication/project-sample-how-to-guide/understanding-the-application-home-page-2019-04-16-13.png): Opens and closes the editor pane.

### Palette List

The palette list provides a list of components to design your app pages. The components are categorized based on sections such as layout, charts, etc.

Expand a palette section to view the components. Or, search the component by name using the **Search** bar.

### Attributes window

The Attributes window allows you to configure the properties of a component. You can also add custom properties (attributes, and Key/value) by using the **New Property** field.

- **Basic Attributes:** Default attributes whose values can be modified as necessary but cannot be deleted
- **Custom Attributes:** User-defined attributes whose values can be modified/deleted. Click **Add** to add a new attribute. You can add an **Attribute** or **Key/Value** property to a component.

Click the ![](/resources/Storage/concepts-publication/project-sample-how-to-guide/help_icon.png) icon in the Attributes window to access the respective component's documentation.

### Task Drop-down list

The task drop-down list allows you to execute a few common commands without typing the commands on the terminal window. These commands are called **custom tasks**. There are a few default custom tasks already created on Neutrinos Studio. They are:

- **Initialize:** Initializes the web app by executing npm install on the terminal window.
- **Initialize Android: **Initializes the mobile app for android by executing npm run initialize-android command. If you are building a web app, use the **Initialize** option.
- **Initialize iOS**: Initializes the mobile app for iOS by executing npm run initialize-ios command.
- **Live View:** Allows you to view the app changes on a browser. This command runs npm start -- -o command on the client terminal and npm run start-dev command on the server terminal to render a live view of the app and start the development server that you have configured for the app.
- **Android Emulate:** Creates an android build of your app and starts the emulator by executing npm run build-mobile && cordova emulate andriod.
- **IOS Emulate:** Creates an IOS build of your app and starts the emulator by executing npm run build-mobile && cordova emulate ios.
- **Android Build:** Creates an android build of your app by executing npm run build-mobile && cordova build andriod.
- **IOS Build:** Creates an IOS build of your app by executing npm run build-mobile && cordova build ios.
- **Custom Task: **Allows you to define your own custom task.

### Canvas

The area where you drag and drop components to design your app pages.

### Other Icons

![](/resources/Storage/concepts-publication/project-sample-how-to-guide/understanding-the-application-home-page-2019-04-16-9.png)

1. Click the **1-click Deploy** icon to deploy your app.
2. Click the **Delete** icon to delete changes performed on the app.
3. Click the **Save** icon to save the changes performed on the app.
