# Ngx Vertical Bar Chart

<https://documentation.neutrinos.com/articles/#!components-guide-7/ngx-vertical-bar-chart>

## Ngx Vertical Bar Chart

### Overview

A **Vertical Bar Chart** is a graph that visually displays data using bars going up from the bottom, whose lengths are proportional to quantities you represent. It can be used when one axis cannot have a numerical scale.

### Usage

A** Vertical Bar Chart **is widely used in industries, health centers, Data analysis, IT companies, etc. The use case for a **Vertical Bar Chart** depends on the scope where it is being used. For example, the insurance companies use this chart to display the report of all the insured clients categorized under male or female in particular year or months, IT (Information Technology) companies use this chart for the analysis of the products and services used by their clients. Similarly, in the health domain, this chart is used for the treatment analysis and new drug research data analysis. In all these scopes of the domain, the main use of a stacked vertical bar chart is for comparison of data categorized on different parameters. There are some other popular use cases where a stacked vertical bar chart is used. Some of them are:

- Insurance companies
- Industries
- Health centers
- Data analysis

### How to use

1. Open the newly created page.
2. Drag and drop the **Ngx Vertical Bar Chart **from the** Ngx Charts** category.
3. Switch to the **Ts** editor of the page and then declare the variable and provide values for the dataset. A sample is given below: Copy CodeJavaScriptdataSet = [
   {
   "name": "Germany",
   "series": [
   {
   "name": "2010",
   "value": 7300000
   },
   {
   "name": "2011",
   "value": 8940000
   }
   ]
   },
   {
   "name": "USA",
   "series": [
   {
   "name": "2010",
   "value": 7870000
   },
   {
   "name": "2011",
   "value": 8270000
   }
   ]
   }
   ];
4. Dataset which consists of all other parameters like labels, and legends.
5. Now switch back to the editor of the page and provide the dataset array name in the [datasets] attribute. For example, [results] = dataSet.
6. X-axis label can be shown or hidden by providing, [xAxis] = true or [xAxis] = false.
7. Y-axis label can be shown or hidden by providing, [yAxis] = true or [yAxis] = false.
8. Legends can be shown or hidden by providing, [legend] = true or [legend] = false.
9. Save the page and run the application.

### Associated Attributes

- **Vertical Bar Chart Label: **Labels are the identity of the data series in a chart. It appears in the legend and tooltips. The name for the vertical bar chart.

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (For example- background: orange; height:200px;).
- **Class**: The **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the "**Style**" tab which is opened by selecting the "**Style**" side menu. The "Class" attribute accepts space-separated class names (eg. class1 class2) which are defined in the "Style" tab as shown below.
   Copy CodeCSS.class1 {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }
   .class2 {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }

**[gradient] (Color/color hexadecimal code):** Gradient is a combination of different colors in a pattern. It is used to fill the plotted area in the chart. For example, background: linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%);

**Show x-Axis (True/False):** This attribute diplays the x-axis points. If it is true, the points will be displayed otherwise it won't. For example, [xAxis] = 'True' OR [xAxis] = 'False'.

**Show y-Axis (True/False):** This attribute displays the y-axis points. If it is true, the points will be displayed otherwise it won't. For example, [yAxis] = 'True' OR [yAxis] = 'False'.

**ShowLegends (Boolean):** It displays the different categories within the data that are used in plotting the area chart. If the value is true, it shows the legends otherwise it does not show.

**show XAxisLabel (True/False):** It displays the name that is given to the** [xAxisLabel]**. If it is true, it will display otherwise it does not. For example, Copy CodeJavaScript[showXAxisLabel] = 'True' OR [showXAxisLabel] = 'False';

- **show YAxisLabel (True/False): **It displays the name that is given to the **[yAxisLabel]**. If it is true, it will display otherwise it does not. For example,
   Copy CodeJavaScript[showYAxisLabel] = 'True' OR [showYAxisLabel] = 'False';
- **[yAxisLabel] (String):** It gives the name to the y-axis. For example,  [yAxisLabel] = "No. of Clients".

- **[xAxisLabel] (String): **It gives the name to the x-axis. For example,** [xAxisLabel] = "Country".
   **
- **(select): **It takes a click event which is done on the bars of the chart. It displays some results on click or on hover of the mouse. For example, displaying data points and/or the labels on click of individual bars.
- **scheme: **It is a color scheme for the chart. For example:
   Copy CodeJavaScriptlet colorSets = [
   {
   name: 'vivid',
   selectable: true,
   group: 'Ordinal',
   domain: ['#647c8a', '#3f51b5', '#2196f3', '#00b862', '#afdf0a', '#a7b61a', '#f3e562', '#ff9800', '#ff5722', '#ff4514'
   ]
   } ];

- **[results] (object[]):** It provides data to the chart which is plotted on a graph using vertical bars. For example,
   Copy CodeJavaScriptdataSet=[
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

### Example

Consider an industry scenario which records the number of clients who use their products and services. The company plots the data on the stacked vertical bar chart to get a better comparison. For example:

| Country | 2010 | 2000 | 1990 |
| --- | --- | --- | --- |
| USA | 49737 | 45986 | 37060 |
| Germany | 40632 | 36938 | 31476 |

Perform the following steps:

1. Drag and drop a **Vertical Bar ****Chart** to the page container.
2. In the TS editor of the page, enter the following code:
   Copy CodeJavaScriptsverticalbarChartData: Array<any> = [
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
   click(){
    alert("clicked")
    }
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[result]
   sverticalbarChartData style
   background:lightblue;width:100%;height:500px; [yAxisLabel] 'country'
   [xAxisLabel]
   'GDP per capita'
   (select)
   click()
   fxflex
   50fxlayout column/row
5. Save and run the page.
