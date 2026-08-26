# Bubble Chart

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/ngx-bubble-chart>

## Bubble Chart

### Overview

It plots the point using a bubble in three dimensions at the same time. The place to plot the data value is determined by the first two dimensions and the corresponding horizontal and vertical axes. The third dimension of the chart represents the size of the individual bubble which depends on the data values.

### Usage

A **Bubble Chart** is widely used in the business world, mass media, product analysis, survey, experimental analysis, etc. Consider a health center scenario where a particular hospital wants to plot a chart to record the number of patients admitted to different wards. The chart should indicate the overall hospital and should be divided into different sections which represent the wards of the hospital. This can be achieved using a bubble chart. Some of the other popular use cases of bubble chart are:

- Pharmaceutical Industries (indicating the different types of drugs)
- Industries (for providing information on different products and services )
- Government offices (like revenue department)
- Retail (for different types of products provided)

### How to use

1. Open the newly created page.
2. Drag and drop the **Bubble Chart** from the **Ngx Charts** category.
3. Switch to the Ts file of the page and then declare the variable and provide values for the dataset. A sample is given below:
4. Dataset which consists of all other parameters like labels, and legends. For example, Copy CodeJavaScriptngxbubbleChartData = [
    {
    "name": "USA",
    "series": [
    {
    "name": "2010",
    "x": 49737,
    "y": 78.8,
    "r": 310
    },
    {
    "name": "2000",
    "x": 45986,
    "y": 76.9,
    "r": 283
    },
    {
    "name": "1990",
    "x": 3706,
    "y": 75.4,
    "r": 253
    }
    ]
    },
    {
    "name": "France",
    "series": [
    {
    "name": "2010",
    "x": 36745,
    "y": 81.4,
    "r": 63
    },
    {
    "name": "2000",
    "x": 34774,
    "y": 79.1,
    "r": 59.4
    },
    {
    "name": "1990",
    "x": 29476,
    "y": 77.2,
    "r": 56.9
    }
    ]
    }
   ]
5. Now switch back to the Html file of the page and provide the dataset array name in the [datasets] attribute. For example, [results] = ngxbubbleChartData.
6. X-axis label can be shown or hidden by providing [xAxis]= true OR [xAxis]= false.
7. Y-axis label can be shown or hidden by providing [yAxis]= true OR [yAxis]= false.
8. Legends can be shown or hidden by providing [legend]= true OR [legend]= false.

### Associated Attributes

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

- X-axis label can be shown or hidden by providing, Copy CodeJavaScript[
   xAxis
   ]
   = trueOR [
   xAxis
   ]
   = false.

- Y-axis label can be shown or hidden by providing, Copy CodeJavaScript[
   yAxis
   ]
   = trueOR [
   yAxis
   ]
   = false
- Legends can be shown or hidden by providing, Copy CodeJavaScript[
   legend
   ]
   = trueOR [
   legend
   ]
   = false.

- **[legendTitle] (String):** It gives a title name for the legend which is displayed for the chart.
- **show Grid Lines (True/False): I**t shows or hides the grid lines in the chart. If it is true, it shows lines in the chart otherwise it does not. By default it is true.
- **RoundDomains (True/False): **It rounds the domain for aligned gridlines in the chart. By default it is false.
- **[minRadius] (number):** It is the minimum bubble radius that is fixed to the chart. It is measured in px.
- **[maxRadius] (number):** It is the maximum bubble radius that is fixed to the chart. It is measured in px.
- **[xAxis] (True/False): **This attribute displays the x-axis points. If it is true, it will display otherwise it does not. For example, Copy CodeJavaScript[
    xAxis
   ]
   = 'True' OR [
    xAxis
   ]
   = 'False

- **[yAxis] (True/False):** This attribute displays the y-axis points. If it is true, it will display otherwise it does not. For example, Copy CodeJavaScript[
    yAxis
   ]
   = 'True' OR [
    yAxis
   ]
   = 'False

- **[xAxisLabel] (String): **It gives the name to the x-axis. For example, [xAxisLabel] = "Country".
- **[yAxisLabel] (String):** It gives the name to the y-axis. For example, [yAxisLabel] = "No. of Clients".

- **AutoScale: **Used to set the minimum value of the y-axis with the minimum data value, instead of 0 (ignored if yScaleMin is defined)
- **Scheme Type:** Used to specify the color of the scale and the values can either be ordinal or linear.
- **[legendPosition]:** Used to define the Position of the legend for example,' right' 'below'.
- **[view]: **Specify the dimensions of the chart in the TS editor by referring to a variable and mention the name of the variable in the attribute window.
- **[xScaleMin]: **Used to define the minimum value of the x-Axis scale.
- **[xScaleMax]:** Used to define the maximum value of the x-Axis scale.
- **[yScaleMin]: **Used to define the minimum value of the y-Axis scale.
- **[yScaleMax]: **Used to define the maximum value of the y-Axis scale.
- **Animation: **This is used to enable animations.
- **[customColors]: **This is used to override a custom color for a specific value.
- **Timeline:** Used to display a timeline control under the chart. Only available if the x scale is linear or time.
- **Tooltip Disabled:** Used to show or hide the tooltip.
- **[xAxisTicks]: **This is the predefined list of x-Axis Tick values.
- **[yAxisTicks]:** This is the predefined list of y-Axis Tick values.
- **[xAxisTickFormatting]: **The function defined in the TS editor to format the x-Axis Ticks.
- **[yAxisTickFormatting]:** The function defined in the TS editor to format the y-Axis Ticks.
- **[showXAxisLabel] (True/False):** It displays the name that is given to the [xAxisLabel]. If it is true, it will display otherwise it does not. For example, Copy CodeJavaScript[
    showXAxisLabel
   ]
   = 'True' OR [
    showXAxisLabel
   ]
   = 'False

- **[showYAxisLabel] (True/False):** It displays the name that is given to the [yAxisLabel]. If it is true, it will display otherwise it does not. For example, Copy CodeJavaScript[
    showYAxisLabel
   ]
   = 'True' OR [
    showYAxisLabel
   ]
   = 'False

- **select (Events): **It takes a click event that is performed on the bars of the chart. It displays some results on click or on hover of the mouse. For example, displaying data points and the label when clicking on individual bars.
- **scheme: **It is a color scheme for the chart. For example, Copy CodeJavaScriptlet colorSets = [
   {
    name: 'vivid',
    selectable: true,
    group: 'Ordinal',
    domain: ['#647c8a', '#3f51b5', '#2196f3', '#00b862', '#afdf0a', '#a7b61a', '#f3e562', '#ff9800', '#ff5722', '#ff4514'
    ]
   }
   ];

- **Results (object[]): **It provides data to the chart which is plotted on a graph using bubbles. For example, Copy CodeJavaScriptngxbubbleChartData = [
    {
    "name": "USA",
    "series": [
    {
    "name": "2010",
    "x": 49737,
    "y": 78.8,
    "r": 310
    },
    {
    "name": "2000",
    "x": 45986,
    "y": 76.9,
    "r": 283
    },
    {
    "name": "1990",
    "x": 3706,
    "y": 75.4,
    "r": 253
    }
    ]
    },
    {
    "name": "France",
    "series": [
    {
    "name": "2010",
    "x": 36745,
    "y": 81.4,
    "r": 63
    },
    {
    "name": "2000",
    "x": 34774,
    "y": 79.1,
    "r": 59.4
    },
    {
    "name": "1990",
    "x": 29476,
    "y": 77.2,
    "r": 56.9
    }
    ]
    }
   ]
   ;

- **fxLayout:** It is a flex layout provided to the chart. It provides different orientations such as row orientation and column orientation to the chart.

- **fxFlex: **It is a directive for fxLayout which is used for resizing the elements within the flexbox container flow. It provides three options i.e fxFlex Grow, fxFlex shrink and fxFlex basis. Here is an example of the implementation of fxFlex.

### Example

Consider an insurance company which made a survey of its client located in different parts of the country. The number of clients in a particular area needs to be displayed on a country map using a bubble. For example,

| Data/Area | X | Y | Radius of Circle |
| --- | --- | --- | --- |
| Area1 | 100 | 50 | 20 |
| Area2 | 60 | 30 | 10 |
| Area3 | 80 | 65 | 15 |

Perform the following steps:

1. Drag and drop a **Bubble****Chart** to the page container.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScriptbubbleChartData: Array<any> =[{"name": "USA","series": [{"name": "2010","x": 197,"y": 75,"r": 310},{"name": "2000","x": 201,"y": 20,"r": 283},{"name": "1990","x": 270,"y": 30,"r": 253}]},{"name": "France","series": [{"name": "2010","x": 367,"y": 81.4,"r": 63},{"name": "2000","x": 347,"y": 79.1,"r": 59.4},{"name": "1990","x": 294,"y": 77.2,"r": 56.9}]}];
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[result]
   bubbleChartData showlegend
   true
   [legendTitle]'countries'
   [legendposition]right
5. Save and run the page.
