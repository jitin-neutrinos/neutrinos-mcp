# Add Main Menu

<https://documentation.neutrinos.com/articles/#!pulse-publication/navigation-editor-wf-cm>

A Workbench user can navigate within the Neutrinos Alpha Workbench or to external links using two methods: the **Main Menu** and **Headers**.

- **Main Menu**: The Main Menu enables users to navigate to various sections within the application, access external links, or even call any API. This menu is displayed in the side navigation bar of the Workbench.
- **Headers**: Headers are specifically used for navigating to links.

![navigation-mainmenu-headers](/resources/Storage/pulse-publication/images/navigation-mainmenu-headers.png)

## Add Main Menu

Follow the steps below to add Main menu in the Workflow Studio:

1. Navigate to **Config** editor > Select **Main Menu **editor.
2. In the **Main Menu** editor, click the **Add** button to create a new menu entry.
3. Enter the details below:
    **Field**
    **Description**
    Type
    Select the navigation type from the dropdown. You can choose to navigate to either a Global Page or a Link.
    **Global Page**: Select from the list of available global pages.
    **Link**: Choose an external link or an API endpoint.
    List
    Displays a list of available Global Pages to choose from.
    Navigation
    Select how to navigate to the Global Page: in the same tab or a new tab.
    Groups
    Select the user group that can access this main menu.
    Hide the Menu
    Toggle button to hide the menu from the sidebar. By default, this is disabled.
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    To add a link to the Main Menu, select **Link** from the **Type** dropdown instead of **Global Page**. The link can be an external URL or an environment variable that triggers an API call.
4. Click the **Save** button.

The GIF below illustrates how to add a global page to Main Menu:

![main-menu-add-gif](/resources/Storage/pulse-publication/images/workflow-studio-config-main-menu-add-gif.gif)

## Add Header

Follow the steps below to add Headers in the Workflow Studio:

1. Navigate to **Config** editor > Select **Headers**.
2. On the Header Config page, click **Add Header** if no menu exists. Otherwise, click **Add Menu** to add a new menu item
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    To add a new menu item as a child menu under an existing menu, click the plus (+) icon next to the desired menu.
    Enter the details below:
    Field
    Description
    Label
    Specify the value to be used as the display text for the header
    URL
    Specify the URL of the page the user needs to navigate to.
    Groups
    Specify the user groups that can view the header.
3. Click the **Save** button.

The GIF below illustrates adding menu items for Headers:

![header-add-gif](/resources/Storage/pulse-publication/images/workflow-studio-config-header-add-gif.gif)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | The toggle at the end of each header row controls whether the header URL opens in a new tab. By default, the URL opens in the same tab. Enabling the toggle will open it in a new tab. |
| --- | --- |
