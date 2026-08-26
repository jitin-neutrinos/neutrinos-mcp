# Panel

<https://documentation.neutrinos.com/articles/#!pulse-publication/layout-components-pages-wf-cm>

Layout components act as containers for controls and other form elements (also referred to as leaf components) that collectively define the structure of a page or form. The available layout components include Panel, Columns (1 Column, 2 Columns, and 3 Columns), and Reuse Page.

## Panel

A Panel is the outermost container that acts as a placeholder for all other components added to a form.




 To add a Panel to the page, drag and drop the Panel component from the Components panel onto the page canvas. After adding the Panel, you can configure its properties as required. The table below lists all available Panel properties along with the supported values for each property.

| **Property** | **  Value** |
| --- | --- |
| Title | Accepts a string value. Example: Personal Details |
| Icon | Select an icon from the available options in the dropdown list. |
| Collapsible | Accepts a Boolean value, controlled using a toggle switch. By default, this option is disabled. When enabled, the Panel becomes collapsible, allowing users to expand or collapse it with a click. You can also configure the Panel to remain collapsed by default when the form loads. |

#### Dependencies

A Panel can be mapped to a CO, Case Instance, Task Instance, or a local object. You can also define conditions to control the Panel's visibility, allowing it to be shown or hidden dynamically based on specified criteria. The following image illustrates the Panel component and its configurable properties.

## Column

A Column organizes the components within a form into a vertically stacked layout. It helps structure the form by defining how components are arranged horizontally and vertically within a panel.




 You can choose from three column configurations:

- **Single Column**: All components are arranged vertically, one below the other. This layout is ideal for simple forms that require a linear flow.
- **Two Columns**: The panel is divided into two vertical sections. This configuration allows you to place two components side by side horizontally, while still maintaining a vertically stacked arrangement within each column. It is useful for optimizing space and grouping related fields.
- **Three Columns**: The panel is divided into three vertical sections. This layout enables you to position up to three components side by side horizontally, with each column supporting vertically stacked components. It is suitable for complex forms that require denser information display.

To add a Column component to the form, drag and drop the required column layout (Single, Two, or Three Columns) from the Components panel onto the form. After adding the Columns, you can configure their properties as required. The table below lists all available Column properties and their supported values.

| **Property  ** | **  Value** |
| --- | --- |
| Title | Accepts a string value. Example: Personal Details |
| Icon | Select an icon from the available options in the dropdown list. |

#### Dependencies

A Column can be mapped to a CO, Case Instance, Task Instance, or a local object. The following image illustrates the Column component and its configurable properties.




 ![column-component](/resources/Storage/pulse-publication/images/column-component.png)
