# Ng Bubble Chart

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/ng-bubble-chart>

## Ng Bubble Chart

### Overview

It plots the point using a bubble in three dimensions at the same time. The place to plot the data value is determined by the first two dimensions and the corresponding horizontal and vertical axes. The third dimension of the chart represents the size of the individual bubble which depends on the data values.

### Usage

**Bubble charts** are widely used in industries. Let's consider a use case where the industry wants to show the services and products it provides, in the different parts of the country. The collected data needs to be plotted on a map of the country region. The bubble graph displays the services provided by the corresponding industry in the different parts of the country. There are some other popular use cases where a bubble chart is used. Some of them are:

- Government Survey
- Healthcare center
- Experimental surveys

### How to use

1. Open the newly created page.
2. Drag and drop the** Bubble Chart **from the **Ng Charts **category.
3. Switch to **Ts** file of the page and then declare the variable and provide values for the following in the component class.
4. A dataset array (contains y-axis values and labels of the legend). For example, Copy CodeJavaScriptpublic bubbleChartData: Array<any> =
   [
    {
    label: [
    'Deer Population'
    ],
    data: [
    {
    x: 100,
    y: 5,
    r: 10
    },
    {
    x: 60,
    y: 30,
    r: 20
    },
    {
    x: 40,
    y: 60,
    r: 25
    },
    {
    x: 80,
    y: 80,
    r: 50
    }
    ]
    }
   ];
5. A labels array (contains x-axis values). For example, Copy CodeJavaScriptpublic bubbleChartLabels:string [
   ] = [
    'Deer Population'
   ]
   ;
6. Legend value (either **true** or **false**). For example, public legend=false;.
7. Options value. For example: Copy CodeJavaScriptpublic bubbleChartOptions:any = {
    responsive: true
   };
8. Now switch back to the Html file of the page and provide the dataset array name in the [datasets] attribute. For example, [datasets] = bubbleChartData.
9. Provide the labels name in [labels] attribute. For example, Copy CodeJSON[
    labels
   ]
   = radarChartLabels
10. Provide the legend name in [legend] attribute. For example, [legend]=legend.
11. Provide the option name in [Options] attributes. For example, [legend]=legend.
12. Save the page and run the application.

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

- **[options]:** Specify the name of an array which is defined in the TS editor from which the drop-down list of options must be displayed. For Example, [options]=bubblechartOptions
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

1. Drag and drop a **Bubble Chart **component from the **NG Charts** section.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScript bubbleChartData: Array<any> =
    [ {
   label: ['Deer Population'],
   data: [{x: 100,y: 5,r: 10},{x: 70,y: 30,r: 20},{x: 53,y: 5,r: 10},{x: 80,y: 52,r: 20}],
    }];
   bubbleChartLabels: string[] = ['Deer Population']
   bubbleChartColors: Array<any> = [
    {
    backgroundColor: '#ff0000',
    borderColor: 'rgba(148,159,177,1)',
    pointBackgroundColor: 'rgba(148,159,177,1)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    }
    ];
3. Navigate back to the HTML editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[labels]
   bubbleChartLabels
   [datasets]
   bubbleChartData
   [options]bubbleChartOptions
   [color]
   bubbleChartColors
   fxflex
   50style
   background:grey;
5. Save and run the page.
