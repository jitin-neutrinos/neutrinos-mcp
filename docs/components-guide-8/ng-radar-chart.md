# Radar Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ng-radar-chart>

## Radar Chart

### Overview

A radar chart is a way of showing multiple data points and the variation between them. They are often useful for comparing the points of two or more different data sets.

### Usage

Radar Charts are used to compare two or more items or groups on various features or characteristics. Example: Compare two anti-depressant drugs on features such as efficacy for severe depression, the prevalence of specific side effects, interaction with alcohol, a continuation of relief over time, the cost to the consumer, etc.

### How to Use

- Drag and drop the **Ng Radar Chart** from the Ng Charts category.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **[label] (String Array):** Labels are the identity of the data series in a chart. It appears in the legend and tooltips. It gives a specific name to each section of the chart area. For example, Copy CodeJavaScriptpage.radarChartLabels = [
   ] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ]
   ;

- **[datasets] (JSON Objects Array):** It is data of the chart, framed on different sectors. For example, Copy CodeJavaScriptpage.radarChartDat = [
    {
    data: [
    25,
    11,
    8,
    9,
    18,
    29
    ]
    }
   ];

- **chartHover **and** chartClick (mouse Events): **It is an event that appears when the mouse is clicked or placed over the sector of the radar area chart. For example, displaying label and point value when the mouse is clicked on the sector of the chart or mouse is moved over it.
- **Show Legends (Boolean): **It is a name given to the same category of data that is used in plotting the radar area chart. If it is true, it shows the legends otherwise it does not show.
- **[colors] (Color/color hexadecimal code): **This property provides the user's desired color to the radar chart. For example, background-color: #92a8d1;.
- **[data]: **Specify the name of the array in which the custom data is embedded for the radar Chart. For example, [data]= page.radarareaData.
- **fxflex:** This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as **flex-grow, flex-basis, flex-shrink,flex-grow**.
- **fxlayout: **Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=column wrap.
- **[options]: **Specify the name of an array that is defined in the Script node of the page flows from which the drop-down list of options must be displayed.
- **Style: **It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below. Copy CodeCSS.class1 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }
   .class2 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }

### Example

Consider an example where a hospital wants to plot a chart to record the patients admitted to the different wards of the hospital such as emergency & casualty, labor ward, Endoscopy Ward, Coronary Care ward, and Surgical Ward.

| Hospital Wards | Emergency & Casualty | Labor Ward | Endoscopy Ward | Coronary Ward | Surgical Ward | General Ward |
| --- | --- | --- | --- | --- | --- | --- |
| Patients(%) | 25 | 11 | 8 | 9 | 18 | 29 |

Perform the following steps:

1. In the **Page Flow Designer** of the page, add a **Script node** to the On init flow and enter the following code:
2. Copy CodeJavaScriptpage.radarChartData = [{
    data:[300, 500, 100]}
    ];
   page.radarChartLabels = ['Download Sales', 'In-Store Sales', 'Mail Sales'];
   page.radarChartOptions = {
    responsive: true
   }
3. Navigate to the UI designer of the page.
4. Drag and drop an Ng Radar Chart component and set the following properties:
5. AttributeValue[labels]
   page.radarChartLabels[datasets]
   page.radarChartData [options]page.radarChartOptions
   fxFlex
   50
6. Save and run the page.
