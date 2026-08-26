# Ng Bubble Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ng-bubble-chart>

## Ng Bubble Chart

### Overview

It plots the point using a bubble in three dimensions at the same time. The place to plot the data value is determined by the first two dimensions and the corresponding horizontal and vertical axes. The third dimension of the chart represents the size of the individual bubble which depends on the data values.

### Usage

**Bubble charts** are widely used in industries. Let's consider a use case where the industry wants to show the services and products it provides, in the different parts of the country. The collected data needs to be plotted on a map of the country region. The bubble graph displays the services provided by the corresponding industry in the different parts of the country. There are some other popular use cases where a bubble chart is used. Some of them are:

- Government Survey
- Healthcare center
- Experimental surveys

### How to use

- Drag and drop the Ng **Bubble Chart** from the Ng Charts category.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **Label (String Array)**: Labels are the identity of the data series in a chart. It appears in the legend and tooltips. It gives a specific name to each data plotted in a circular shape. For example,

```json
public bubbleChartLabels:string [] = [  'Deer Population'];
```

- **[datasets] (JSON Objects Array)**: It is a data of the chart which is framed on the bubble chart. For example,

```json
public bubbleChartData: Array<any> =  [{label: ['Deer Population'],data: [{ x: 100, y: 5, r: 10}, { x: 60, y: 30, r: 20}, { x: 40, y: 60, r: 25}, { x: 80, y: 80, r: 50}]}];
```

- **[Color] (Color/color hexadecimal code):** This property provides user's desired color to the chart. For example,

```html
background-color: #92a8d1;
```

- **[options]:** Specify the name of an array that is defined in the script node in the page flows from which the drop-down list of options must be displayed. For Example, [options]=bubblechartOptions
- **fxLayout:** Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=column wrap
- **fxFlex**: This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as flex-grow, flex-basis, flex-shrink,flex-grow.
- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

### Example

Consider a survey on the population, in different parts of the country. The population in a particular area needs to be displayed on a country map using a bubble chart.

| Data/Area | X | Y | Radius of Circle |
| --- | --- | --- | --- |
| Area1 | 100 | 50 | 20 |
| Area2 | 60 | 30 | 10 |
| Area3 | 80 | 65 | 15 |

To do that, perform the following steps:

1. In the **Page Flow Designer **of the page, add a **Script **node to the** On init **flow and enter the following code:
2. Copy CodeJavaScript
   page.bubbleChartData =
    [ {
   label: ['Deer Population'],
   data: [{x: 100,y: 5,r: 10},{x: 70,y: 30,r: 20},{x: 53,y: 5,r: 10},{x: 80,y: 52,r: 20}],
    }];
   page.bubbleChartLabels = ['Deer Population']
   page.bubbleChartColors = [
    {
    backgroundColor: '#ff0000',
    borderColor: 'rgba(148,159,177,1)',
    pointBackgroundColor: 'rgba(148,159,177,1)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    }
    ];
3. In the Page Variable node of the **On Init** flow, add the following variables:
4. **Page Variable**
   **Default Value**
   bubbleChartLabels
   Select **page**. and enter **bubbleChartLabels**
   bubbleChartColors
   Select **page**. and enter **bubbleChartColors**bubbleChartData
   Select **page**. and enter **bubbleChartData**
5. Navigate to the UI designer of the page.
6. Drag and drop an **Ng Bubble Chart** component and set the following properties:
  1. **style**: background:889EAF;
  2. **[datasets]**: page.bubbleChartData
  3. **[options]**: page.bubbleChartOptions
  4. **[labels]**: page.bubbleChartLabels
  5. **[colors]**: page.bubbleChartColors
  6. **fxFlex**: 50
7. Save and run the page.
