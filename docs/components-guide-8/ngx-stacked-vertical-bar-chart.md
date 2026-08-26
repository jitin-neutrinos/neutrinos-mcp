# Stacked Vertical Bar Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ngx-stacked-vertical-bar-chart>

## Stacked Vertical Bar Chart

### Overview

A **Stacked Vertical Bar Chart** is similar to the normal bar chart with a difference that in a stacked vertical bar chart, the data values are plotted using a vertical bar (column direction). It provides a good comparison of the data which is placed in the column direction.

### Usage

A **Stacked Vertical Bar Chart **is widely used in industries, health centers, Data analysis, IT companies, etc. The use case for a **Stacked Vertical Bar Chart** depends on the scope where it is being used. For example, the insurance companies use this chart to display the report of all the insured clients categorized under male or female in particular year or months, IT (Information Technology) companies use this chart for the analysis of the products and services used by their clients. Similarly, in the health domain, this chart is used for treatment analysis and new drug research data analysis. In all these scopes of the domain, the main use of a stacked vertical bar chart is for the comparison of data categorized on different parameters. There are some other popular use cases where a stacked vertical bar chart is used. Some of them are:

- Insurance companies
- Industries
- Health centers
- Data analysis

### How to use

- Drag and drop the **Ngx Stacked Vertical Bar**** Chart** from the Ngx Charts category.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **[gradient] (Color/color hexadecimal code):** Gradient is a combination of different colors in a pattern. It is used to fill the plotted area in the chart. For example, background: linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%);
- **Show x-Axis (True/False):** This attribute displays the x-axis points. If it is true, the points will be displayed otherwise it won't. For example, [xAxis] = 'True' OR [xAxis] = 'False'.
- **Show y-Axis (True/False):** This attribute displays the y-axis points. If it is true, the points will be displayed otherwise it won't. For example, [yAxis] = 'True' OR [yAxis] = 'False'.
- **ShowLegends (Boolean):** It displays the different categories within the data that are used in plotting the area chart. If the value is true, it shows the legends otherwise it does not show.
- **[xAxisLabel] (String):** It gives the name to the x-axis. For example, [xAxisLabel] = "Country".
- **[yAxisLabel] (String):** It gives the name to the y-axis. For example,  [yAxisLabel] = "No. of Clients".
- **show XAxisLabel (True/False):** It displays the name that is given to the** [xAxisLabel]**. If it is true, it will display otherwise it does not. For example,

- **show YAxisLabel (True/False): **It displays the name that is given to the **[yAxisLabel]**. If it is true, it will display otherwise it does not. For example, Copy CodeJavaScript[showYAxisLabel] = 'True' OR [showYAxisLabel] = 'False';

- **Style**: It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (For example- background: orange; height:200px;).
- Class: The **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the "**Style**" tab which is opened by selecting the "**Style**" side menu. The "Class" attribute accepts space-separated class names (eg. class1 class2) which are defined in the "Style" tab as shown below. Copy CodeJavaScript.class1 {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }
   .class2 {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }

- **(select): **It takes a click event which is done on the bars of the chart. It displays some results on click or on hover of the mouse. For example, displaying data points and/or the labels on click of individual bars.
- **scheme: **It is a color scheme for the chart. For example: Copy CodeJavaScriptlet colorSets = [
   {
   name: 'vivid',
   selectable: true,
   group: 'Ordinal',
   domain: ['#647c8a', '#3f51b5', '#2196f3', '#00b862', '#afdf0a', '#a7b61a', '#f3e562', '#ff9800', '#ff5722', '#ff4514'
   ]
   } ];

- **[results] (object[]):** It provides data to the chart which is plotted on a graph using vertical bars. For example, Copy CodeJavaScriptdataSet=[
   {
   "name": "India",
   "value": 135148
   },
   {
   "name": "United States",
   "value": 121652
   },
   {
   "name": "Germany",
   "value": 157885
   },
   {
   "name": "France",
   "value": 965782
   },
   {
   "name": "United Kingdom",
   "value": 987564
   }
   ]

- **fxLayout:** It is a flex layout provided to the chart. It provides different orientations such as row orientation, column orientation to the chart. For example, fxLayout = 'row' or fxLayout = 'column'.

- **fxFlex:** It is a directive for fxLayout which is used on it for resizing the elements within the flexbox container flow. It provides three options i.e fxFlex Grow, fxFlex shrink, and fxFlex basis. Here is an example of the implementation of fxFlex: <div fxFlex="<grow> <shrink> <basis>"></div>.

- **[view]:** Specify the dimensions of the chart in the Script node of the page flows by referring to a variable and mentioning the name of the variable in the attribute window. For example, [500,500]
- **Scheme Type:** Specify the color scale type. It can either be ordinal or linear. By default, ordinal is selected.
- **Round Domains: **When set to true, the bars of the chart are aligned with the grids.
- **[customColors]:** Used to override the color for a specific value. Create a function or an object in the ts editor and specify the name of the object in the attribute window.
- **Animation:** Set this property to true to apply animations to the chart.
- **[legendTitle]: **Specify the title for the legend.
- **[xAxis Ticks]: **This is the predefined list of x-Axis Tick values.
- **[yscaleMax]:** Specify the maximum value that the y-axis can hold.
- **[barPadding]: **Specify the padding between the bars of the chart in pixels.
- **Tooltip Disabled(true/false):** Used to show or hide the tooltip.
- **Show data label(true/false):** This is used to display the number value next to the bar of the chart.
- **[yAxis Tick Formatting]:** The function defined to format the y-Axis Ticks.
- **[xAxis Tick Formatting]: **The function defined to format the x-Axis Ticks.
- **[yAxis Ticks]: **This is the predefined list of y-Axis Tick values.

### Example

Consider an industry scenario that records the number of clients who use their products and services. The company plots the data on the stacked vertical bar chart to get a better comparison. For example:

| Country | 2010 | 2000 | 1990 |
| --- | --- | --- | --- |
| USA | 49737 | 45986 | 37060 |
| Germany | 40632 | 36938 | 31476 |

1. In the **Page Flow Designer **of the page, add a Script node to the On init flow and enter the following codeCopy CodeJavaScriptsverticalbarChartData: Array<any> = [
    {
    "name": "Germany",
    "series": [{"name": "2010","value": 40632},
    {"name": "2000","value": 36953},
    {"name": "1990","value": 31476} ]},
    {
    "name": "United States",
    "series": [{"name": "2010","value": 49737},
    {"name": "2000","value": 45986},
    {"name": "1990","value": 37060}]},
   ];
2. In the Page Variable node of the On Init flow, add the following variables:
3. **Page Variables**
   **Default Value**
   sverticalbarChartData
   page.sverticalbarChartData
4. Navigate to the UI designer of the page.
5. Drag and drop an **Ngx Stacked Vertical Bar Chart** component and set the following properties:
  1. **style**: background:lightblue;width:100%;height:500px;
  2. **[result]**: page.sverticalbarChartData
  3. **[yaxisLabel]**: 'country'
  4. **[xaxisLabel]**: 'GDP per capita'
  5. **fxFlex**: 50
6. Save and run the page.
