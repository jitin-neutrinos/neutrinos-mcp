# Designing App Layouts - Best Practices

<https://documentation.neutrinos.com/articles/#!best-practices/designing-app-layouts-best-practices>

# Designing App Layouts - Best Practices

---

When you create an app, you have to make sure that the app uses responsive layouts to respond to the user’s behavior and environment based on the screen size, platform, and orientation. To do that, we recommend that you follow the best practices documented in [Best Practices for using Responsive Layouts](/articles/best-practices/best-practices-for-using-responsive-layouts) which explains how to leverage properties and behaviors of **flex-layout** directives to get responsive layouts.

Apart from using flex-layouts, you can also use various responsive design patterns that are popular for web design. You can create these design patterns using the fundamental layout components that are already available in Neutrinos Studio. Popular design patterns include:

- Toggle Menu Layout
- Grid Layout
- Tabbed Layout

### Toggle Menu Layout

The toggle Menu based layout can be achieved by using two components from the **Navigation** section of the palette list:

- Sidenav Container
- Sidenav

A **Sidenav Container** component can have multiple** Sidenav **components. To learn how to use the **Sidenav Container** and Sidenav components, see:

- [Sidenav Container documentation](/articles/components-guide-for-release-6/sidenav-container)
- [Sidenav documentation](/articles/components-guide-for-release-6/sidenav)

### Columned Layouts

Most designers prefer using columned layouts while designing apps. Using this layout, the number of columns changes based on screen sizes. For example, a small mobile screen will only have a single column based layout with all of the contents of the column stacked one below the other. While in an iPad you may want a three-column layout where contents are spread over three columns.

These form factor specific layouts can be achieved by following the best practices covered in [Responsive Layout Best Practices](/articles/best-practices/best-practices-for-using-responsive-layouts).

### Grid Layout

Grid is a two-dimensional layout that the user configures using Grid components. Such layouts are preferable when a single action grid-item with minimum information is to be displayed. For example, when you create an Image Gallery app.

To create a grid layout, you use the **Grid List** and **Grid Tile** components, where each **Grid Tile** represents the content section of the **Grid List**. You can also configure how much space a single **Grid Tile** can take within a **Grid List**. To learn how to create a grid layout, see:

- [Grid List documentation](/articles/components-guide-for-release-6/grid-list)
- [Grid Tile documentation](/articles/components-guide-for-release-6/grid-tile)

### Tabbed Layout

A Tabbed Layout provides a horizontal layout to display tabs. To create a tabbed layout, you drag and drop the Tabs component to the app page and add multiple tabs within it. To learn how to configure a Tabbed Layout, see [Tabs documentaton](/articles/components-guide-for-release-6/tabs).
