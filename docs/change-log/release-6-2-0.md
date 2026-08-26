# 6.2.0

<https://documentation.neutrinos.com/articles/#!change-log/release-6-2-0>

## 6.2.0

#### Date: (2019-09-25)

#### Features and Enhancements

- Added a keyboard shortcut - **Ctrl/Cmd + W **to close tabs in Neutrinos Studio.
- When a user switches between pages, or between the TypeScript editor and the HTML page, the scroll state is saved across tabs, TS editor, and HTML pages.
- Enhanced the **Select **dropdown list in all the Attribute window of all the components.
- Added advanced options to the attributes window of the **Select** component.
- Merged **Tab Group** and **Tab** components to a single **Tabs** component. Also, added new attributes to the **Tabs** component.
- Added advanced options to the attributes window of the **DatePicker** component.
- Added more types in the properties drop-down list of the **Start** node.
- An option is added to Neutrinos Studio using which you can add blank terminals.
- Monaco editor is updated to version 0.17.1.
- IntelliSense is added for Monaco editor in UI Services.
- Autocomplete is added for **bh.** lookups in attribute windows.
- Plugins Manager: The UI of the **Add Dependency **window is enhanced.
- Added the following new nodes to UI Services:
  - Navigation
  - Storage
  - Service Variables
  - Environment
  - Snack Bar

**Bug Fixes**

- On mouse hover, showing the **Collapse** icon when editor pane is already collapsed.
- Studio Application page misaligned after deleting a UI service.
- Views refreshing in multiple open pages after a new page is created.
- kill is not a function on macOS running node 12
- Cannot drag some components outside the **Html 5** component.
- Change detection is not fired in routes after deleting the page.
- In a few instances, the palette list is empty when a page opens.
- Error when an advanced component is minimized and copied.
- The **Ctrl+ S** shortcut is inactive if a dialog is open.
- Assets Editor folder becomes empty on dragging a sub-folder in the tree.
- Components get pasted on top of the paste target if the paste target is minimized.
- Pressing the Enter/Return key deletes the focused route in Routes editor.
- Palette components get dropped as icons.
- The HTML editor becomes droppable outside of **Html 5** component.
- The wrong mat-error message is displayed while creating an app.
- Migration steps are added to handle changes made to the **Select **component's attributes.
- **class** and **style** attributes not applied to card title & subtitle.
- If the paste target is minimized, components get pasted on top of the paste target.
- Monaco editor doesn't re-layout after closing tabs.
- In the **Add Select **option, the disable field gets updated by default the if the **Update** button is not clicked.
- Wrong attribute window is being displayed in the **Card** and **Table **components.
- When the attributes window of a component is open, if you press (ctrl + X) to cut the component, the attributes window of the component should get closed.
- When a palette component is dragged and dropped, it gets dropped as an icon.

Related Topics:

- [What's New in 6.2.0?](/smart/project-sample-how-to-guide/what-s-new)
- [Migration Guide](/articles/neutrinos-studio-migration-guide/get-started)
