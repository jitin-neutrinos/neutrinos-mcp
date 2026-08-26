# Gauge Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ngx-gauge-chart>

## Gauge Chart

### Overview

A **Guage Chart** uses needles to show the information about the data values on a speedometer. Each section in the gauge needle is colored with a different color and placed on a different axis.

### Usage

A **Guage Chart** is widely used in executive dashboard reports to show key business indicators. They are useful for comparing a small number of variables using multiple needles within the speedometer space.

### How to use

- Drag and drop the** Ngx ****Gauge**** Chart** from the **Ngx **Charts category.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **[angleSpan] (Number):** It is the angle provided to the gauge spans. The unit is in degrees and the default value is 240 degrees.
- **[startAngle] (Number):** It is the angle that the chart is rotated by. It is measured in degrees and the default value is -120 degrees. Usually, the negative half of the spanning angle (angleSpan) is taken to centralize the chart.
- **[units] (S****tring): **It is the text displayed under the value of the chart data.
- **[bigSegments] (Number):** It is the number of big segments given on the axis collected from the given data set.
- **[smallSegments] (number): **It is the number of small segments that appear in between every big segment.
- **[min] (number):** It is the starting point of the scale on the chart from where every data set point starts getting plotted.
- **[max] (number):** It is the ending point of the scale in the gauge on which the data set values are plotted.
- **[view]: **Specify the dimensions of the chart in the TS editor by referring to a variable and mentioning the name of the variable in the attribute window.
- **[customColors]:** This is used to override a custom color for a specific value.
- **Animation: **This is used to enable animations.
- **Show Legends:** Used to show or hide the legend.
- **[legendTitle]: **Specify a title for the legend.
- **Show Axis: **Used to specify whether to show or hide the Axis
- **[axisTickFormatting]:** The function defined in the Ts editor to format the Axis Ticks.
- **Tooltip Disabled: **Used to show or hide the tooltip.
- **select (Events):** It takes a click event that is performed on a segment of the chart. It displays some results on click or on hover of the mouse. For example, displaying data points or the label on click of an individual segment.
- **scheme: **It is a color scheme for the chart. For example, Copy CodeJavaScriptlet colorSets = [
   {
   name: 'vivid',
   selectable: true,
   group: 'Ordinal',
   domain: ['#647c8a', '#3f51b5', '#2196f3', '#00b862', '#afdf0a', '#a7b61a', '#f3e562', '#ff9800', '#ff5722', '#ff4514'
   ]
   } ];

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below. Copy CodeCSS.class1 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }
   .class2 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }

- **Results (object[]): **It provides data to the chart which is plotted on a graph. For example, Copy CodeJavaScriptngxGaugeChartData = [
   {
   "name": "Germany",
   "value": 40632
   },
   {
   "name": "United States",
   "value": 49737
   },
   {
   "name": "France",
   "value": 36745
   }
   ]
- **fxLayout:** It is a flex layout provided to the chart. It provides different orientation such as row orientation and column orientation to the chart. For example, fxLayout = 'row' or fxLayout = 'column'.

- **fxFlex:** It is a directive for fxLayout which is used for resizing the elements within the flexbox container flow. It provides three options i.e fxFlex Grow, fxFlex shrink, and fxFlex basis. Here is an example of the implementation of fxFlex.

### Example

Consider an IT company that wants a dashboard report to show key business performance indicators of its different branches so that it can be compared easily with KPI (Key Performance Indicator). Here is an example,

| Parameters | KPI |
| --- | --- |
| Germany | 406323 |
| USA | 49737 |
| France | 36745 |

Perform the following steps:

1. In the **Page Flow Designer **of the page, add a Script node to the On init flow and enter the following code:
2. Copy CodeJavaScriptpage.GaugeChartData = [{"name": "Germany","value": 400},{"name": "United States","value": 730},{"name": "France","value": 675}, ];
3. In the Page Variable node of the On Init flow, add the following variables:
4. **Page Variable**
   **Default Value**
   GaugeChartData Select **page**. and enter GaugeChartData
5. Create a **mycharclick **flow. This flow displays an alert pop-up on click of the chart.
6. Drag and drop a **Start **node and name it **mycharclick**.
7. Drag and drop a **Script node and add **alert("chart clicked");
8. Connect the nodes.
9. Navigate to the UI designer of the page.
10. Drag and drop an **Ngx Gauge Chart** component and set the following properties:
  1. [result]: page.GaugeChartData
  2. (chartClick): mychartClick
  3. fxFlex: 50
11. Save and run the page.
