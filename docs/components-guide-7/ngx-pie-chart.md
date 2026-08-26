# Pie Chart

<https://documentation.neutrinos.com/articles/#!components-guide-7/ngx-pie-chart>

## Pie Chart

### Overview

**Pie Chart** is a circular chart which is divided into different slices each of which represents the corresponding data values.

### Usage

A **Pie Chart **is widely used in the business world, mass media, product analysis, survey, and experimental analysis, etc. Consider a health center scenario where a particular hospital wants to plot a chart for the record of its patients admitted to different wards. The chart should indicate the overall hospital and be divided into different sections which represent the wards of the hospital. This can be achieved using a pie chart where a complete pie represents the hospital and divided slices of the pie represent the wards of the hospital. Some of the other popular use cases of line chart are:

- Pharmaceutical Industries (indicating the different section of drugs)
- Industries (for providing information on different products and services )
- Government offices (like revenue department)
- Retails (for different types of products they provide)

### How to use

1. Open the newly created page.
2. Drag and drop a **Pie Chart** from the **Ngx Charts** palette section.
3. Switch to the Ts editor of the page and then declare the variable and provide values for the dataset. A sample is given below:
  - Dataset which consists of all other parameters like labels, and legends: Copy CodeJavaScriptngxpieChartData = [
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
     },
     {
     "name": "United Kingdom",
     "value": 36240
     },
     {
     "name": "Spain",
     "value": 33000
     },
     {
     "name": "Italy",
     "value": 35800
     }
     ]
4. Now switch back to the Html editor of the page and provide the dataset array name in the [datasets] attribute. For example, [results] = ngxpieChartData.
5. X-axis and Y-axis labels can be shown or hidden by providing, [labels] = true or [labels] = false.
6. Legends can be shown or hidden by providing, [legend] = true or [legend] = false.
7. Save the page and run the application.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Show Legends (Boolean):** It displays the categories of data that are used in plotting the chart. If it is true, it shows the legends otherwise it does not show- [legend] = true;
- **xAxisLabel (String): **It gives the name to the x-axis. For example, [xAxisLabel] = "Country".
- **Show Labels (True/false):** It gives the name to the x-axis and y-axis. These levels are selected from the dataset. If it is true, it shows the x-axis and y-axis levels otherwise it does not show.
- **Explode Slices (True/false):** It gives the radius to each slice. The radius of the slice will be proportional to its value. If it is true, it makes the radius proportional to its values and if it is false, normal slice division is made.
- **Doughnut (True / False): **This attribute provides a hollow space at the center of the pie chart. If it is true, the hollow space will be inserted into the chart otherwise not.
- **[view]:** Specify the dimensions of the chart in the TS editor by referring to a variable and mention the name of the variable in the attribute window.
- **[customColors]:** This is used to override a custom color for a specific value.
- **Animation:** This is used to enable animations.
- **[legendTitle]: **Specify a title for the legend.
- **[legendPosition]: **Used to define the Position of the legend for example,' right' 'below'.
- **[gradient]:** Used to fill elements with a gradient instead of a solid color.
- **[arcwidth]:** Specify the radius of the outer fraction
- **Tooltip Disabled: **Used to show or hide the tooltip.
- **[tooltipText]: **Used to format the tooltip text.
- **[labelFormatting]: **Specify the function that is used to format the labels of the chart.
- **Trim Labels:** Used to trim the labels beyond a certain maximum length.
- **[maxLabelLength]:** Specify the maximum length of the labels. In case the trim label is true, labels over this length will be trimmed.
- **select (Events):** It takes a click event which is done on the slice of the chart. It displays some results on click or on hover of the mouse. For example, displaying data points or the label on click of an individual slice.
- scheme: It is a color scheme for the chart. For example, Copy CodeJavaScriptlet colorSets = [
   {
   name: 'vivid',
   selectable: true,
   group: 'Ordinal',
   domain: ['#647c8a', '#3f51b5', '#2196f3', '#00b862', '#afdf0a', '#a7b61a', '#f3e562', '#ff9800', '#ff5722', '#ff4514'
   ]
   } ];

- **Results (object[]): **It provides data to the chart which is plotted on a graph. For example, Copy CodeJavaScriptngxpieChartData = [
   {
   "name": "Germany",
   "value": 730000
   },
   {
   "name": "USA",
   "value": 7870000
   },
   {
   "name": "Spain",
   "value": 1569558
   },
   {
   "name": "France",
   "value": 1645553
   },
   {
   "name": "Nepal",
   "value": 1058048
   },
   {
   "name": "India",
   "value": 1546488
   }
   ]

- **fxLayout:** It is a flex layout provided to the chart. It provides different orientation such as row orientation, column orientation to the chart. For example, fxLayout = 'row' or fxLayout = 'column'.

- **fxFlex:** It is a directive for fxLayout which is used on it for resizing the elements within the flexbox container flow. It provides three options i.e fxFlex Grow, fxFlex shrink, and fxFlex basis. Here is an example of the implementation of fxFlex.

### Example

Consider an IT industry which makes a survey on how many users use their products from different parts of the world. The sample data can be recorded as follows:

| Country | Users |
| --- | --- |
| Germany | 7300000 |
| USA | 7870000 |
| Spain | 1569558 |
| France | 1645553 |
| Nepal | 1058048 |
| India | 1546488 |

Perform the following steps:

1. Drag and drop a **Pie Chart** to the page container.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScriptpieChartData: Array<any> = [{ "name": "Germany", "value": 40632,},{ "name": "United States", "value": 50000, },{ "name": "France", "value": 36745,},{"name": "Spain", "value": 33000, },{"name": "Italy", "value": 35800, }];
   pieTooltipText({ data }) {const label = data.name;const val = data.value;
   return {<span class="tooltip-label">${label}</span><span class="tooltip-val">${val}</span><span class="tooltip-val">${val}</span>};}
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[result]
   pieChartData [tooltipText]
   pieTooltipText
5. Save and run the page.
