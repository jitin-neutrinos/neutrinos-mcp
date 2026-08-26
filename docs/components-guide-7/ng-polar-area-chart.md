# Polar Area Chart

<https://documentation.neutrinos.com/articles/#!components-guide-7/ng-polar-area-chart>

## Polar Area Chart

### Overview

The** Polar Area Chart** provides detailed comparison information. The radius of the sector differs according to the value in data sets whereas, in the **Pie Chart **the radius of each slice is the same. In this chart, the difference in data can be found easily by looking at the radius of the slice.

### Usage

A ** Polar Area Chart **is used as an alternative to the pie chart in different fields such as hospitals, retails, industries, data science, and analytics, etc. Let us consider a health center scenario where a particular hospital wants to plot a chart to record the patients admitted to different wards. The chart should indicate the overall hospital and should be divided into different sections which represent the wards of the hospital. This can be done by using a pie chart however it would not provide proper readability. Therefore, in this case, if the polar area chart is used, it would provide global understanding just from the structure of the chart. There are some other popular use cases. Some of them are:

- Industries
- Government offices
- Hospitals
- Government surveys
- Experimental surveys

### How to Use

1. Open the newly created page.

2. Drag and drop a ** Polar Area Chart **from the **Ng Charts **category.

3. Switch to the** Ts** file of the page and then declare the variable and provide values for the following in the component class:

- A dataset array (contains y-axis values and labels of the legend). For example, Copy CodeJavaScriptpublic polarChartData: Array<any> = [
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
   ]
   ;

- A labels array (contains x-axis values). For example, Copy CodeJavaScriptpublic polarChartLabels:string [
   ] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ];

- **Legend value:** Enter either true or false. For example, public legend=false;.
- Options value. For example, Copy CodeJavaScriptpublic polarChartOptions:any = {
    responsive: true
    };

4. Now switch back to the **Html** file of the page and provide the dataset array name in the** [datasets] **attribute. For example, [datasets] = polarChartData.

5. Provide the labels name in the **[labels]** attribute. For example, [labels] = polarChartLabels.

6. Provide the options name in the **[options] **attribute. For example, [options] = polarChartOptions.

7. Provide the legend name in the** [legend]** attribute. For example, [legend] = legend.

8. Save the page and run the application.

### Associated Attributes

- **[label] (String Array):** Labels are the identity of the data series in a chart. It appears in the legend and tooltips. It gives a specific name to each section of the chart area. For example, Copy CodeJavaScriptpublic polarChartLabels:string [
   ] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ]
   ;

- **[datasets] (JSON Objects Array):** It is data of the chart, framed on different sectors. For example, Copy CodeJavaScriptpublic polarChartData: Array<any> = [
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

- **chartHover **and** chartClick (mouse Events): **It is an event that appears when the mouse is clicked or placed over the sector of the polar area chart. For example, displaying label and point value when the mouse is clicked on the sector of the chart or mouse is moved over it.
- **Show Legends (Boolean): **It is a name given to the same category of data that is used in plotting the polar area chart. If it is true, it shows the legends otherwise it does not show.
- **[colors] (Color/color hexadecimal code): **This property provides the user's desired color to the polar chart. For example, background-color: #92a8d1;.
- **[data]: **Specify the name of the array in which the custom data is embedded for the Polar Area Chart. For example, [data]= polarareaData.
- **fxflex:** This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as **flex-grow, flex-basis, flex-shrink,flex-grow**.
- **fxlayout: **Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=column wrap.
- **[options]: **Specify the name of an array which is defined in the TS editor from which the drop-down list of options must be displayed.
- **Style: **It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (example: background: orange; height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (example: class1 class2) which are defined in the **Style** tab as shown below. Copy CodeCSS.class1 {
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

1. Drag and drop a **Polar Area Chart** to the page container.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScriptpolarareaChartLabels: string[] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ];
    polarareaChartData: number[] = [25, 11, 8, 9, 18, 29];
   polarareaChartType: string = 'polararea';
    polarareaChartOptions: any = {
    responsive: true
    };
   mycharclick(){
    alert("chart clicked");
    }
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[labels]
   polarareaChartLabels [datasets]
   polarareaChartData [options]polarareaChartOptions
   chartClickmycharclick()
5. Save and run the page.
