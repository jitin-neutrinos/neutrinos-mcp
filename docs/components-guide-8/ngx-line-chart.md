# Line Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ngx-line-chart>

## Line Chart

### Overview

A-Line** Chart** is a chart that plots the data values using a line and connects those points using a straight line. It does not contain any background color.

### Usage

A-Line** Chart** is widely used in comparing trending data such as stock market shares. The use case for a line chart depends on the scope where it is being used. For example, industries use a line chart to display the report of all their products used by clients from different geographical regions, IT (Information Technology) companies use this chart for the analysis of the products and services used by their clients. Similarly, in the health domain, this chart is used for treatment analysis and new drug research data analysis. In all these scopes of the domain, the main use of a line chart is for the comparison of data categorized on different parameters. There are some other popular use cases where a line chart is used. Some of them are:

- Insurance companies
- Industries
- Health centers
- Data analysis

### How to Use

- Drag and drop the **Ngx Line**** Chart** from the **Ngx **Charts category.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[gradient] (Color/color hexadecimal code): **Gradient is a combination of different color patterns and styles. For example, Copy CodeCSSbackground: linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%)

- **Show xAxis (True/False):** This attribute diplays the x-axis points. If it is true, it will display otherwise it does not. For example, [xAxis] = 'True' or [xAxis] = 'False'.

- **Show yAxis (True/False):** This attribute displays the y-axis points. If it is true, it will display otherwise it does not. For example, [yAxis] = 'True' or [yAxis] = 'False'.

- **Show Legends (Boolean):** It displays the categories of data that are used in plotting the line chart. If it is true, it shows the legends otherwise it does not show.
- **[xAxisLabel] (String):** It gives the name to the x-axis. For example, [xAxisLabel] = "Country".
- **[yAxisLabel] (String): **It gives the name to the y-axis. For example, [yAxisLabel] = "No. of Clients".
- **showXAxisLabel (True/False):** It displays the name that is given to the [xAxisLabel]. If it is true, it will display otherwise it does not. For example, [showXAxisLabel] = 'True' or [showXAxisLabel] = 'False'.

- **showYAxisLabel (True/False): **It displays the name that is given to the [yAxisLabel]. If it is true, it will display otherwise it does not. For example, [showYAxisLabel] = 'True' or [showYAxisLabel] = 'False'.

- **[view]:** Specify the dimensions of the chart by referring to a variable and mentioning the name of the variable in the attribute window.
- **Scheme Type:** Used to specify the color of the scale and the values can either be ordinal or linear.
- **[customColors]: **This is used to override a custom color for a specific value by defining them inside the TS editor by creating an object.
- **Animation: **This is used to enable animations.
- **[rangeFillOpacity]: **Specify the opacity of the shadow around the line indication of the (optional) min and max values. The range shadow is only displayed if min and max values are provided with the data. The color of the shadow is always the color of the central line.
- **[legendTitle]: **Specify a title for the legend.
- **Show Grid Lines: **Specify whether to hide or show the gridlines.
- **Round Domains: **When set to true, the bars of the chart is aligned with the grids.
- **[xAxisTicks]:** This is the predefined list of x-Axis Tick values.
- **[yAxisTicks]:** This is the predefined list of y-Axis Tick values.
- **[xAxisTickFormatting]: **The function defined to format the x-Axis Ticks.
- **[yAxisTickFormatting]:** The function defined to format the y-Axis Ticks.
- **Timeline(True/False): **Used to display a timeline control under the chart. Only available if the x scale is linear or time.
- **AutoScale:** Used to set the minimum value of the y-axis with the minimum data value, instead of 0 (ignored if yScaleMin is defined).
- **Tooltip Disabled: **Used to show or hide the tooltip.
- **[referenceLines]: **This is an array of reference lines to be shown behind the chart. Every reference line should be of format {name, value}.
- **Show Reference Lines: **Specify whether to show or hide the reference Lines.
- **Show Reference Label: **Specify whether to show or hide the reference labels.
- **[xScaleMin]: **Used to define the minimum value of the x-Axis scale.
- **[xScaleMax]:** Used to define the maximum value of the x-Axis scale.
- **[yScaleMin]: **Used to define the minimum value of the y-Axis scale.
- **[yScaleMax]: **Used to define the maximum value of the y-Axis scale.
- **select (Events): **It takes a click event which is done on the bars of the chart. It displays some results on click or on hover of the mouse. For example, displaying data points or labels on click of individual lines.
- **scheme:** It is a color scheme for the chart. For example,

- **Results (object[]):** It provides data to the chart which is plotted on a graph using lines. For example, Copy CodeJavaScriptdataSet = [
   {
    "name": "Germany",
    "series": [
    {
    "name": "2010",
    "value": 7300000
    }
    ,
    {
    "name": "2011",
    "value": 8940000
    }
    ]
   }
   ,
   {
    "name": "USA",
    "series": [
    {
    "name": "2010",
    "value": 7870000
    }
    ,
    {
    "name": "2011",
    "value": 8270000
    }
    ]
   }
   ];

- **fxLayout:** It is a flex layout provided to the chart. It provides different orientations such as row orientation, column orientation to the chart. For example, fxLayout = 'row' or fxLayout = 'column'.

- **fxFlex:** It is a directive for fxLayout which is used on it for resizing the elements within the flexbox container flow. It provides three options i.e fxFlex Grow, fxFlex shrink, and fxFlex basis. Here is an example of the implementation of fxFlex.

### Example

Consider an Insurance company that records the data of its clients from different countries. The company plots the data on a line chart to get a better comparison of variations in the number of clients from different countries. For example,

| Country | Germany | USA |
| --- | --- | --- |
| 2010 | 4168 | 5481 |
| 2011 | 4529 | 5181 |
| 2012 | 6575 | 3860 |

Perform the following steps:

1. In the **Page Flow Designer **of the page, add a Script node to the On init flow and enter the following code:
2. Copy CodeJavaScriptpage.lineChartData: Array<any> =[{"name": "Germany","series": [{"value": 4168,"name":2010 },{"value": 4529,"name":2011 },{"value": 6575,"name":2012 },]},{"name": "USA","series": [{"value": 5481,"name":2010},{"value": 5881,"name":2011},{"value": 3860,"name":2012},]}];
3. In the Page Variable node of the On Init flow, add the following variables:
4. **Page Variable**
   **Default Value**
   lineChartDataSelect **page**. and enter **lineChartData**
5. Create a **mycharclick **flow. This flow displays an alert pop-up on click of the chart.
6. Drag and drop a **Start **node and name it **mycharclick**.
7. Drag and drop a **Script node and add **alert("chart clicked");
8. Connect the nodes.
9. Navigate to the UI designer of the page.
10. Drag and drop an **Ngx Line Chart** component and set the following properties:
  1. [result]: page.lineChartData
  2. (chartClick): mychartClick
  3. fxFlex: 50
11. Save and run the page.
