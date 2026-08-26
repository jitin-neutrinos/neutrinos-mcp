# Page Designer

<https://documentation.neutrinos.com/articles/#!studio-guide-8/version-8-0-0>

Here is a list of new features introduced in Neutrinos Studio version 8.0:

### Page Designer

Before Neutrinos Studio 8.0, you would design the business logic of the page by hand-coding it in the TypeScript editor and use the components from the [component palette list](/smart/project-concepts/palette/a/h4_1518247481) to design the Page UI. Starting with Neutrinos Studio 8.0, you design the pages of your application using the Page Designer which comprises the following designers:

- **Page UI Designer (UI)** - This is where you design the HTML view of the page by dragging and dropping components to the [canvas](/smart/project-concepts/services-designer-elements/a/h3__455959634). The feature remains the same as the previous versions of Neutrinos Studio.

![page ui designer](/resources/Storage/studio-guide-8/log_ui.png)

- **Page Flow Designer (Flow)** - This is a replacement for the TypeScript editor, using which you drag and drop nodes on the canvas to create page flows and design the business logic of the page, instead of hand-coding.

![Page flow designer](/resources/Storage/studio-guide-8/log_flow.png)

The page Flow designer comprises of nodes that allows the page to:

- [Listen to DOM events](/smart/project-page-services-designer-guide/host-listener-node)
- [Manage the lifecycle of a page](/smart/project-page-services-designer-guide/lifecycle-events)
- [Open a page as a dialog window](/smart/project-page-services-designer-guide/dialog)
- [Import an npm or Angular dependency on a page](/smart/project-page-services-designer-guide/use-dependency-node)
- and do much more!

See the [Page designer guide](/smart/project-page-services-designer-guide/page-service-designer-preface) to view the complete documentation of nodes that are available as part of the page flow designer. Alternatively, click the ![help icon](/resources/Storage/studio-guide-8/help_icon.png) on the attribute's window of a node to open its respective documentation.

Apart from the UI and Flow Designers, the page designer also provides:

#### Enhanced Page Explorer

The page explorer is enhanced to provide you with a tree-view structure. Using the page explorer, you can:

- Create application pages
- Organize application pages into different folders
- Access the UI and Flow designers of the page
- and more

See the following topics to learn more:

- [Page Explorer](/articles/studio-guide-8/page-explorer)
- [Manage folders](/articles/studio-guide-8/manage-folders)
- [Manage Pages](/articles/studio-guide-8/manage-pages)

#### Flow Picker

New in 8.0, this editor allows you to pick an already defined page or client service flow and bind it to the component’s attribute. The flow gets executed when the user performs some action associated with that component's attribute.

See the following topics to learn more:

- [Bind a page flow to a component's attribute](/articles/studio-guide-8/bind-page-flows-to-components)
- [Bind a client service flow to a component's attribute](/articles/studio-guide-8/import-client-services-to-the-page-ui)

---

**Search Nodes**

You can now use the Keyboard shortcut Ctrl + P to view the list of nodes used in your application. From the list, you can click a node to quickly navigate to it on the respective designer.

- **Up** and **Down** arrow keys can be used to move through the list items.
- On pressing **Enter**, the user is navigated to the designer on which the node resides, and the node is highlighted.

The Search nodes list can also b accessed by clicking **Edit > Node Search** on the top menu of the Studio Application page.

### Create Page Nodes

The Plugin Builder is enhanced with capabilities to allow users to create custom, reusable page nodes. Once created, these nodes can be used by the [page flow designer](/smart/project-concepts/page-designer/a/h3_520216706) to design the business logic of the page.

See [Add a Page Node](/smart/project-node-builder-guide/add-a-page-node) to learn more.

### Dark Mode Theme

An experimental Dark Mode theme is introduced in Studio to provide visual ergonomics to developers. The dark theme reduces the luminance emitted by device screens, while still meeting minimum color contrast ratios. It reduces the strain on the eyes by adjusting the brightness to current lighting conditions and facilitates screen use in dark environments – all while conserving battery power.

Click **View > Invert Colors** on the top-navigation to switch the Studio to dark mode. You can click the same option again to switch back to the original theme.

### Bug Fixes

To learn about bug fixes and other enhancements, see [Release 8.0.0](/articles/change-log/release-8-0-0)
