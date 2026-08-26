# Area Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ngx-area-chart>

## Area Chart

### Overview

An** Area Chart **is based on a line chart. The area between the axes and line are colored with different colors, textures, and hatchings.

### Usage

An ** Area Chart **is widely used in comparing data such as the rise and fall of stock market shares. Industries use area charts to display the report of product sales in different geographical regions. IT (Information Technology) companies use this chart for the analysis of the products and services used by their clients. Similarly, in the health domain, this chart is used to analyze treatment data. In all these domains, the main use of an area chart is to compare the data categorized by different parameters. There are some other popular use cases where an area chart is used. Some of them are:

- Insurance companies
- Industries
- Health centers
- Data analysis

### How to Use

- Drag and drop the **Ngx ****Area Chart** from the Ngx Charts category in the Page UI Designer.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {border-radius:10px;flex-basis:10%;height:100px;}.class2 {border-radius:10px;flex-basis:10%;height:100px;}
```

- **[gradient] (Color/color hexadecimal code): **Gradient is a combination of different colors in a pattern. It is used to fill the plotted area in the chart. For example, background: linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%).
- **Show xAxis (True/False): **This attribute displays the x-axis points. If it is true, the points will be displayed otherwise it won't. For example, [xAxis]= 'True' or [xAxis]= 'False'.

- **Show yAxis (True/False): **This attribute displays the y-axis points. If it is true, the points will be displayed otherwise it won't. For example,  [yAxis]= 'True' or [yAxis]= 'False'

- **Show Legends (Boolean):** It displays the different categories within the data that are used in plotting the area chart. If the value is true, it shows the legends otherwise it does not show.
- **[xAxisLabel] (String): **It gives the name to the x-axis. For example, [xAxisLabel] = "Country".
- **[yAxisLabel] (String):** It gives the name to the y-axis. For example, [yAxisLabel] = "No. of Clients".
- **Scheme Type: **Used to specify the color of the scale and the values can either be ordinal or linear.
- **Show Grid Lines: **Specify whether to hide or show the gridlines.
- **[legendTitle]:** Specify a title for the legend.
- **[legendPosition]:** Used to define the Position of the legend. The possible values that can be given for this attribute are ' right' and 'below'.
- **[view]:** Specify the dimensions (height and width) of the chart by referring to a variable or define it directly in the syntax [height, width]. For Example: [1000,300]
- **AutoScale (Boolean):** Used to set the minimum value of the y-axis with the minimum data value, instead of 0 (ignored if yScaleMin is defined)
- **[xScaleMin]:** Used to define the minimum value of the x-Axis scale.
- **[xScaleMax]:** Used to define the maximum value of the x-Axis scale.
- **[yScaleMin]: **Used to define the minimum value of the y-Axis scale.
- **[yScaleMax]:** Used to define the maximum value of the y-Axis scale.
- **Animation(Boolean):** This is used to enable animations.
- **[customColors]: **This is used to override a custom color for a specific value.
- **Timeline:** Used to display a timeline control under the chart. Only available if the x scale is linear or time.
- **tooltip Disabled:** Used to show or hide the tooltip.
- **[xAxisTicks]:** This is the predefined list of x-Axis Tick values.
- **[yAxisTicks]: **This is the predefined list of y-Axis Tick values.
- **[xAxisTickFormatting]:** The function defined to format the x-Axis Ticks.
- **yAxisTickFormatting]:** The function defined to format the y-Axis Ticks.
- **showXAxisLabel (True/False): **It displays the name that is given to the [xAxisLabel]. If it is true, it will display otherwise it does not. For example, [showXAxisLabel]= 'True' or [showXAxisLabel]= 'False'.

- **showYAxisLabel (True/False):** It displays the name that is given to the [yAxisLabel]. If it is true, it will display otherwise it does not. For example, [showYAxisLabel]= 'True' or [showYAxisLabel]= 'False'.

- **(select) (Events): **It takes a click event which is done on the bars of the chart. It displays some results on the click or hover of the mouse. For example, displaying data points and the label when clicking on individual plotted points.
- **scheme: **It is a color scheme for the chart. Select the scheme from the drop down or you can provide a custom scheme by defining it in the Script node of the page flows. For example, Copy CodeJavaScriptpage.colorScheme = {
    domain: ['red', 'black', '#C7B42C', '#AAAAAA'],
    };

- **[Results] (object[]):** It provides data to the chart which is plotted on a graph. For example, Copy CodeJavaScriptpage.dataSet = [
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
   ]
   ;

- **fxLayout: **It is a flex layout provided to the chart. It provides different orientations such as row orientation and column orientation to the chart.

- **fxFlex:** It is a directive for fxLayout which is used for resizing the elements within the flexbox container flow. It provide three options i.e fxFlex Grow, fxFlex shrink, and fxFlex basis. Here is an example of the implementation of fxFlex.

### Example

Consider an industry that records the data of its product sales from different countries. The company plots the data on the area chart to get a better understanding of variations in the sales of products from different countries. For example,

| Country | Grenada | Congo | Thailand |
| --- | --- | --- | --- |
| 2010 | 5465 | 2629 | 4168 |
| 2011 | 2201 | 3415 | 4529 |
| 2012 | 5129 | 5004 | 6575 |
| 2013 | 2129 | 2994 | 3575 |

Perform the following steps:

1. In the **Page Flow Designer **of the page, add a Script node to the On init flow and enter the following code:
2. Copy CodeJavaScriptpage.areaChartData = {"name": "Grenada","series": [{"value": 5465,"name":2010 },{"value": 2201,"name":2011 },{"value": 5129,"name":2012 },{"value": 2129,"name":2013 },]},{"name": "Congo","series": [{"value": 2629,"name":2010},{"value": 3415, "name":2011 },{"value": 5994,"name":2012},{"value": 2994,"name":2013},]},
   {"name": "Thailand","series": [{"value": 4168,"name":2010 },{"value": 4529,"name":2011 },{"value": 6575,"name":2012 },{"value": 3575,"name":2013 },]}];
3. Create a **mycharclick **flow. This flow displays an alert pop-up on click of the chart.
  1. Drag and drop a **Start **node and name it **mycharclick**.
  2. Drag and drop a **Script node and add **alert("chart clicked");
  3. Connect the nodes.
4. Navigate to the UI designer of the page.
5. Drag and drop an **Ngx Area Chart** component and set the following properties:
  1. [result]: page.areaChartData
  2. style: background:lightblue;height:500px;
  3. (select): Click the Pick a Flow mat chip. Open the Flow Picker editor, select the Services tab and select the mycharclick flow.
  4. fxFlex: 50
6. Save and run the page.
