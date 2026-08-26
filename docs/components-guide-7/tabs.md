# Tabs

<https://documentation.neutrinos.com/articles/#!components-guide-7/tabs>

## Tabs

### Overview

**Tabs** is an advanced component that is used to contain one or more Tab contents within it. **Tabs **help organize content into separate views where only one view (or Tab) can be visible at a time. Each tab's label is shown in the tab header and the active tab's label is designated with the animated ink bar like this:

When the list of tab labels exceeds the width of the header, pagination controls appear to let the user scroll left and right across the labels.

The active tab may be set using the selectedIndex input or when the user selects one of the tab labels in the header.

| ![Information](/resources/Storage/components-guide-7/info.png) | You cannot minimize the tab content within Tabs. Also, you cannot copy the tab content. |
| --- | --- |

### Usage

The **Tabs** component is used whenever you need to show content in different tabs and allow the user to choose between the tabs. A tab cannot exist outside of the** Tabs **component.

### How to Use

1. Drag and drop the **Tabs** component from the Layout category.
2. Click the **+ New Tab** button inside the component to add more tabs.
3. Double click the **Tabs** component and enter a Label.
4. Double-click the individual **Tab** to open its respective attributes window and set its properties.
5. Enter a **Label** for the tab. This is the value that gets displayed on the tab when the page is rendered.
6. Save the changes.

### Associated Attributes

#### Tabs Component

- **Tab label:** Specify the display name of Tabs.

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

- **animationDuration: **Allows you to control the duration of the tab's animation. This value must be a valid CSS value (For example, 600ms). If you want to disable the animation completely, you can do so by setting the properties to 0ms.
- **backgroundColor:** The background color of the Tab navigation.
- **color:** Theme color of the navigation bar.
- **Align Tabs:** Allows you to align tabs towards the start, center, or the end of the container.

- **Disable Ripple: **If set to** True**, will disable the ripple effect in Tabs for both- to indicate the point of touch, and to confirm that touch input was received.
- **Dynamic Height:** If set to **True**, Tabs should grow to the size of the active tab.
- **Tab Header Position: **Decides the position of the **Tab header** to be above or below.
- **selectedIndex:** The index of the active tab.
- **(animationDone): **The event emitted when the tab animation has completed.
- **(focusChange): **The event emitted when the focus has changed within Tabs.
- **(selectedIndexChange): **The event emitted when the selected index of the respective tab is changed.
- **(selectedTabChange): **The event emitted when the tab selection has changed.
- **Stretch Tabs: **If set to **True**, stretches the Tabs to fill the width of the screen.

#### Tab Content

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

- **label:** The display name of the tab content. This name gets displayed when the page is rendered.
- **Disabled:** If set to **True**, disables the tab content.
- **leftTabIcon:** The icon which should appear to the left of the tab label.
- **leftIconClick:** The action that is to be performed on the click of the left icon.
- **rightTabIcon: **The icon which should appear to the right of the tab label.
- **rightIconClick:** The action that is to be performed on click of the right icon.
- **tabIconClass:** The class with CSS styling that you want to apply to your tab icon.
- **Enable lazy loading:** By default, the tab contents are eagerly loaded. Eagerly loaded tabs will initialize the child components, but will not inject them into the DOM until the tab is activated. If the tab contains several complex child components or the tab's contents rely on DOM calculations during initialization, it is advised to enable lazy loading of the tab's content. By default, this property is set to False.
- **Dynamic tab: **If set to **True**, it will enable dynamic contents to be displayed in tab contents. This is defined in the user-defined location. If enabled, this property will display the following additional attributes (which are mandatory) in the attributes window.
  - **tabDataSource:** Provide the array which is used to handle the dynamic tab content where the user has initialized the tabs.
  - **tabLabels:** To provide the tab labels, in the background, an object reference called tab is created. Using this object reference, a user can navigate to the object keys inside the array that you have defined above.

![Information](/resources/Storage/components-guide-7/info.png)


 If you enable dynamic tabs and add dynamic content to your tab, the content gets displayed in all tabs within the Tabs component.

### Example

1. Drag and drop the** Tabs** component from the layout category.
2. Add 3 tabs inside the Tabs component by clicking the** + New Tab **button.
3. Set the value of the label property of first, second, and third Tabs as **Tab1**, **Tab2**, and **Tab3 **respectively.
4. Drag and drop a **Card **component (from **Layout **category) within each tab.
5. Set the height of each card to 1**00px**. For example: style = height:100px;
6. Set the color of each card. For example: color: pink;
7. Save the changes.
8. Now the tabs can be navigated.
