#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:39:54 2021

@author: debby
"""
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, RadioButtonGroup, BoxAnnotation, Div, Panel, Tabs, LabelSet
from bokeh.plotting import figure, curdoc,output_file, show, save
from bokeh.models.widgets import Select
from bokeh.layouts import column, row, layout
from bokeh.io import output_notebook,output_file, show
from math import pi
import datetime
import pandas as pd
import numpy as np
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

df_us=pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/data/VM-Usage.csv')
pricesheet=pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/data/azure-retail-multi-price-2021-07-01.csv')

usage= df_us.rename(columns={'MeterId': 'meterId'})

usage['RG'] = usage['InstanceId'].str.split('/', expand=True).pop(4)
usage['ServiceType'] = usage['InstanceId'].str.split('/', expand=True).pop(7)

meter_sku= pd.merge(usage, pricesheet, on='meterId', how='left')

meter_sku.drop(['InstanceId','ResourceLocation','UnitOfMeasure',
                'meterName','productId','productName','skuId',
                'serviceName','serviceId','serviceFamily',
                'armSkuName','armRegionName','effectiveStartDate',
                'currencyCode','tierMinimumUnits','unitOfMeasure',
                'armSkuSpec','armSkuSpecRaw','operatingSystem',
                'retailPrice','devtestPrice','riPrice1Y','spotPrice',
                'detailJSON','updateTime','location', 'riPrice3Y','Cost'],
               axis=1, inplace=True)
#print(list(meter_sku.columns))

meter_sku['DATE']= pd.to_datetime(meter_sku['DATE'])
df = meter_sku.sort_values(by='DATE')


#圖的資料
d1 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='D2 v3')]
d1 = d1.groupby(['DATE'])["ConsumedQuantity"].sum()
df1 = pd.DataFrame(d1)
d2 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='E8 v3')]
d2 = d2.groupby(['DATE'])["ConsumedQuantity"].sum()
df2 = pd.DataFrame(d2)
d3 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='D8 v3')]
d3 = d3.groupby(['DATE'])["ConsumedQuantity"].sum()
df3 = pd.DataFrame(d3)
d4 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='D4 v3')]
d4 = d4.groupby(['DATE'])["ConsumedQuantity"].sum()
df4 = pd.DataFrame(d4)
d5 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='M32ms')]
d5 = d5.groupby(['DATE'])["ConsumedQuantity"].sum()
df5 = pd.DataFrame(d5)
d6 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='E16 v3')]
d6 = d6.groupby(['DATE'])["ConsumedQuantity"].sum()
df6 = pd.DataFrame(d6)
d7 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='M32ts')]
d7 = d7.groupby(['DATE'])["ConsumedQuantity"].sum()
df7 = pd.DataFrame(d7)
d8 = df.loc[(df['RG']=='FARGLORY_SAP')& (df['skuName']=='E48 v3')]
d8 = d8.groupby(['DATE'])["ConsumedQuantity"].sum()
df8 = pd.DataFrame(d8)
d9 = df.loc[(df['RG']=='FG_VPN')& (df['skuName']=='D2 v3')]
d9 = d9.groupby(['DATE'])["ConsumedQuantity"].sum()
df9 = pd.DataFrame(d9)
d10 = df.loc[(df['RG']=='FG_VPN')& (df['skuName']=='D16 v3')]
d10 = d10.groupby(['DATE'])["ConsumedQuantity"].sum()
df10 = pd.DataFrame(d10)
d11 = df.loc[(df['RG']=='FG_VPN')& (df['skuName']=='D2 v2')]
d11 = d11.groupby(['DATE'])["ConsumedQuantity"].sum()
df11 = pd.DataFrame(d11)
d12 = df.loc[(df['RG']=='FG_VPN')& (df['skuName']=='D4 v3')]
d12 = d12.groupby(['DATE'])["ConsumedQuantity"].sum()
df12 = pd.DataFrame(d12)
d13 = df.loc[(df['RG']=='FARGLORY_AD')& (df['skuName']=='D2 v3')]
d13 = d13.groupby(['DATE'])["ConsumedQuantity"].sum()
df13 = pd.DataFrame(d13)
d14 = df.loc[(df['RG']=='FG_SMT_IT')& (df['skuName']=='D2 v3')]
d14 = d14.groupby(['DATE'])["ConsumedQuantity"].sum()
df14 = pd.DataFrame(d14)
d15 = df.loc[(df['RG']=='FG_FSM')& (df['skuName']=='D2 v3')]
d15 = d15.groupby(['DATE'])["ConsumedQuantity"].sum()
df15 = pd.DataFrame(d15)
d16 = df.loc[(df['RG']=='FG_FSM')& (df['skuName']=='B2s')]
d16 = d16.groupby(['DATE'])["ConsumedQuantity"].sum()
df16 = pd.DataFrame(d16)
d17 = df.loc[(df['RG']=='FARGLORY_WAKEUP')& (df['skuName']=='F8s v2')]
d17 = d17.groupby(['DATE'])["ConsumedQuantity"].sum()
df17 = pd.DataFrame(d17)
d18 = df.loc[(df['RG']=='FARGLORY_WAKEUP')& (df['skuName']=='F8')]
d18 = d18.groupby(['DATE'])["ConsumedQuantity"].sum()
df18 = pd.DataFrame(d18)
d19 = df.loc[(df['RG']=='FG_WEBEDS')& (df['skuName']=='D2 v3')]
d19 = d19.groupby(['DATE'])["ConsumedQuantity"].sum()
df19 = pd.DataFrame(d19)
d20 = df.loc[(df['RG']=='FGCLOUD')& (df['skuName']=='D2 v2')]
d20 = d20.groupby(['DATE'])["ConsumedQuantity"].sum()
df20 = pd.DataFrame(d20)

frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12,\
          df13, df14, df15, df16, df17, df18, df19, df20]

result = pd.concat(frames)


#設定數據資料來源
source = ColumnDataSource(result)
source.data = result


#配圖
#output_file(filename="plot.html", title="Date ＆ Consumed Quantity Plot")

p = figure(plot_width=1500, plot_height=600, x_axis_type='datetime'\
           ,x_axis_label='Date',y_axis_label='Consumed Quantity'\
           ,title='Date ＆ Consumed Quantity'\
           )
    
p.xaxis.formatter=DatetimeTickFormatter(
        days=["%Y/%m/%d"],
        months=["%Y/%m/%d"],
        years=["%Y/%m/%d"])

p.xaxis.major_label_orientation = pi/4
p.xaxis.axis_label_text_font_style = "normal"
p.xaxis.axis_label_text_font_size = "18px"
p.yaxis.axis_label_text_font_style = "normal"
p.yaxis.axis_label_text_font_size = "18px"
p.xaxis.axis_line_width = 2
p.yaxis.axis_line_width = 2
p.xaxis.major_label_text_font_size = "14px"
p.yaxis.major_label_text_font_size = "14px"
p.title.align = "center"
p.title.text_font_size = "30px"
#p.x_range = Range1d(datetime.date(2019, 1, 1), datetime.date(2021, 9, 2))
#p.image_url(url=['/Users/debby/DIGI/DIGI_TCA_2021/data/plot.gif']\
#            , x=0, y=1, w=0.8, h=0.6)



#第一個下拉選單
select = Select(title="Resource Group",  options=['FARGLORY_SAP',
        'FG_VPN','FARGLORY_AD','FG_SMT_IT','FG_FSM','FARGLORY_WAKEUP',\
            'FG_WEBEDS','FGCLOUD'])

#第二個下拉選單
select2 = Select(title="Service Type", options=['Virtual Machine'])

#第三個下拉選單
select3 = Select(title="Sku Name",  options=['D2 v3','E8 v3','D8 v3',\
    'D4 v3','M32ms','E20 v3','E4 v3','D16 v3','D2 v2','D1 v2',\
    'E32 v3','E16 v3','M32ts','E48 v3','B2s','F8s v2','F8'])

#下拉選單置預設值
select.value, select2.value, select3.value= 'FARGLORY_SAP', 'Virtual Machine','D2 v3'    
    
#第一個下拉選單的callback
def update_plot(attrname, old, new):
    newSource = df1
    if select.value == 'FARGLORY_SAP' and select3.value == 'D2 v3':
        newSource = df1
    if select.value == 'FARGLORY_SAP' and select3.value == 'E8 v3':
        newSource = df2
    if select.value == 'FARGLORY_SAP' and select3.value == 'D8 v3':
        newSource = df3
    if select.value == 'FARGLORY_SAP' and select3.value == 'D4 v3':
        newSource = df4
    if select.value == 'FARGLORY_SAP' and select3.value == 'M32ms':
        newSource = df5    
    if select.value == 'FARGLORY_SAP' and select3.value == 'E16 v3':
        newSource = df6
    if select.value == 'FARGLORY_SAP' and select3.value == 'M32ts':
        newSource = df7
    if select.value == 'FARGLORY_SAP' and select3.value == 'E48 v3':
        newSource = df8
    if select.value == 'FG_VPN' and select3.value == 'D2 v3':
        newSource = df9  
    if select.value == 'FG_VPN' and select3.value == 'D16 v3':
        newSource = df10  
    if select.value == 'FG_VPN' and select3.value == 'D2 v2':
        newSource = df11
    if select.value == 'FG_VPN' and select3.value == 'D4 v3':
        newSource = df12
    if select.value == 'FARGLORY_AD' and select3.value == 'D2 v3':
        newSource = df13 
    if select.value == 'FG_SMT_IT' and select3.value == 'D2 v3':
        newSource = df14 
    if select.value == 'FG_FSM' and select3.value == 'D2 v3':
        newSource = df15 
    if select.value == 'FG_FSM' and select3.value == 'B2s':
        newSource = df16
    if select.value == 'FARGLORY_WAKEUP' and select3.value == 'F8s v2':
        newSource = df17 
    if select.value == 'FARGLORY_WAKEUP' and select3.value == 'F8':
        newSource = df18 
    if select.value == 'FG_WEBEDS' and select3.value == 'D2 v3':
        newSource = df19 
    if select.value == 'FGCLOUD' and select3.value == 'D2 v2':
        newSource = df20 

    source.data =  newSource


source.data = df1
r = p.line(x='DATE', y='ConsumedQuantity', line_width=2, line_color='#81968F'\
           , source = source)

#第一個下拉選單動作
select.on_change('value', update_plot)
#第二個下拉選單動作
select3.on_change('value', update_plot)


#把表單放入網頁的佈局
layout_plot = row(column([select, select2, select3], width=225, height=200), p)
curdoc().add_root(layout_plot)


#嵌入影片
# div = Div(text="""
#     <video width="300px" height="150px" loop="true" autoplay="autoplay" controls="controls" id="vid" muted>
#     <source src="https://www.youtube.com/watch?v=5GJWxDKyk3A" type="video/mp4">
#     </video> <script> document.getElementById('vid').play();</script>
#     """)

past = pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/recommendation/results/2021-08-24_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-23:]
forecast_lstm = pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/recommendation/results/2021-08-24_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
recom_lstm = pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/recommendation/results/2021-08-24_LSTM_recommendation.csv', index_col=0)
forecast_prophet = pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/recommendation/results/2021-08-24_Prophet_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
recom_prophet = pd.read_csv('/Users/debby/DIGI/DIGI_TCA_2021/recommendation/results/2021-08-24_Prophet_recommendation.csv')

labels = ['RI (1 year)', 'RI (3 year)']
radio_button_group = RadioButtonGroup(labels=labels, active=0)

source_past = ColumnDataSource(past)
source_forecast_1_lstm = ColumnDataSource(forecast_lstm)
source_forecast_2_lstm = ColumnDataSource(forecast_lstm[1:])
source_forecast_1_prophet = ColumnDataSource(forecast_prophet)
source_forecast_2_prophet = ColumnDataSource(forecast_prophet[1:])

p1_lstm = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity', plot_width=700, plot_height=500, tools='')
p1_lstm.xaxis.axis_label_text_font_style = 'normal'
p1_lstm.yaxis.axis_label_text_font_style = 'normal'
p1_lstm.title.text = 'Forecast of Consumed Quantity in one Week & RI Coverage'
p1_lstm.title.align = "center"
p1_lstm.title.text_font_size = '16pt'
p1_lstm.xaxis.axis_label_text_font_size = '14pt'
p1_lstm.xaxis.major_label_text_font_size = '12pt'
p1_lstm.yaxis.axis_label_text_font_size = '14pt'

p1_lstm.line('DATE', 'ConsumedQuantity', line_color='gray', legend_label='Past Value', source=source_past, line_width=2)
p1_lstm.line('DATE', 'ConsumedQuantity', line_color='orange', legend_label='Forecast', source=source_forecast_1_lstm, line_width=2)
p1_lstm.circle('DATE','ConsumedQuantity', line_color='orange', source=source_forecast_2_lstm, fill_alpha=0.8, fill_color='darkorange', size=6)

amounts_lstm = recom_lstm.iloc[:,0].values
R1_lstm = recom_lstm.iloc[:,1].values
R3_lstm = recom_lstm.iloc[:,2].values

color_line = range(min(amounts_lstm), max(amounts_lstm)+1)[np.argmin(R1_lstm)]*24

low_box_lstm = BoxAnnotation(top=color_line, fill_alpha=0.1, fill_color='lime')
p1_lstm.add_layout(low_box_lstm)

p1_prophet = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity', plot_width=700, plot_height=500, tools='')
p1_prophet.xaxis.axis_label_text_font_style = 'normal'
p1_prophet.yaxis.axis_label_text_font_style = 'normal'
p1_prophet.title.text = 'Forecast of Consumed Quantity in one Week & RI Coverage'
p1_prophet.title.text_font_size = '16pt'
p1_prophet.title.align = "center"
p1_prophet.xaxis.axis_label_text_font_size = '14pt'
p1_prophet.xaxis.major_label_text_font_size = '12pt'
p1_prophet.yaxis.axis_label_text_font_size = '14pt'

p1_prophet.line('DATE', 'ConsumedQuantity', line_color='gray', legend_label='Past Value', source=source_past, line_width=2)
p1_prophet.line('DATE', 'ConsumedQuantity', line_color='orange', legend_label='Forecast', source=source_forecast_1_prophet, line_width=2)
p1_prophet.circle('DATE','ConsumedQuantity', line_color='orange', source=source_forecast_2_prophet, fill_alpha=0.8, fill_color='darkorange', size=6)

amounts_prophet = recom_prophet.iloc[:,0].values
R1_prophet = recom_prophet.iloc[:,1].values
R3_prophet = recom_prophet.iloc[:,2].values

color_line = range(min(amounts_prophet), max(amounts_prophet)+1)[np.argmin(R1_prophet)]*24

low_box_prophet = BoxAnnotation(top=color_line, fill_alpha=0.1, fill_color='lime')
p1_prophet.add_layout(low_box_prophet)

def update_box_annotate(attr, old, new):
    if radio_button_group.active == 0: 
        low_box_lstm.top = range(min(amounts_lstm), max(amounts_lstm)+1)[np.argmin(R1_lstm)]*24
        low_box_prophet.top = range(min(amounts_prophet), max(amounts_prophet)+1)[np.argmin(R1_prophet)]*24
    else:
        low_box_lstm.top = range(min(amounts_lstm), max(amounts_lstm)+1)[np.argmin(R3_lstm)]*24
        low_box_prophet.top = range(min(amounts_prophet), max(amounts_prophet)+1)[np.argmin(R3_prophet)]*24

radio_button_group.on_change('active', update_box_annotate)

data_recom_lstm = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_lstm.iloc[0,1], recom_lstm.iloc[1,1], recom_lstm.iloc[2,1]],
        'chr': [str(int(recom_lstm.iloc[0,1])), str(int(recom_lstm.iloc[1,1])), str(int(recom_lstm.iloc[2,1]))]}
source_recom_lstm = ColumnDataSource(data=data_recom_lstm)

p2_lstm = figure(x_range = data_recom_lstm['label'], y_range=(0, 500), plot_width=700, plot_height=500, title="Pricing per Month", tools='', x_axis_label='Option', y_axis_label='Pricing')
p2_lstm.xaxis.axis_label_text_font_style = 'normal'
p2_lstm.yaxis.axis_label_text_font_style = 'normal'
p2_lstm.title.text_font_size = '16pt'
p2_lstm.title.align = "center"
p2_lstm.xaxis.axis_label_text_font_size = '14pt'
p2_lstm.xaxis.major_label_text_font_size = '12pt'
p2_lstm.yaxis.axis_label_text_font_size = '14pt'

p2_lstm.vbar(x='label', width=0.35, top='RI', source=source_recom_lstm, fill_color='darkgreen')

labels_lstm = LabelSet(x='label', y='RI', text='chr', y_offset=7, source=source_recom_lstm, text_align='center')
p2_lstm.add_layout(labels_lstm)

data_recom_prophet = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_prophet.iloc[0,1], recom_prophet.iloc[1,1], recom_prophet.iloc[2,1]],
        'chr' : [str(int(recom_prophet.iloc[0,1])), str(int(recom_prophet.iloc[1,1])), str(int(recom_prophet.iloc[2,1]))]}
source_recom_prophet = ColumnDataSource(data=data_recom_prophet)

p2_prophet = figure(x_range = data_recom_prophet['label'], y_range=(0, 500), plot_width=700, plot_height=500, title="Pricing per Month", tools='', x_axis_label='Option', y_axis_label='Pricing')
p2_prophet.xaxis.axis_label_text_font_style = 'normal'
p2_prophet.yaxis.axis_label_text_font_style = 'normal'
p2_prophet.title.text_font_size = '16pt'
p2_prophet.title.align = "center"
p2_prophet.xaxis.axis_label_text_font_size = '14pt'
p2_prophet.xaxis.major_label_text_font_size = '12pt'
p2_prophet.yaxis.axis_label_text_font_size = '14pt'

p2_prophet.vbar(x='label', width=0.35, top='RI', source=source_recom_prophet, fill_color='darkgreen')

labels_prophet = LabelSet(x='label', y='RI', text='chr', y_offset=7, source=source_recom_prophet, text_align='center')
p2_prophet.add_layout(labels_prophet)

div1 = Div(text='', width=20)
div2 = Div(text='', width=200)
div3 = Div(text='', width=100)
divh = Div(text='<br>', width=320)

div_pricing = Div(text='Pricing:<br>EA: $0.13 / hour<br>RI (1 year): $52.92 / month<br>RI (3 year): $33.61 / month', style={'font-size': '150%'}, width=300)

div3_lstm = Div(text='''EA Price: ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br><br>* Recommendation of the two models are the same.'''.format(int(recom_lstm.iloc[0,3]), int(recom_lstm.iloc[0,3]-min(source_recom_lstm.data['RI'])), source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])]), style={'font-size': '150%'}, width=550)

div3_prophet = Div(text='''EA Price: ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br><br>* Recommendation of the two models are the same.'''.format(int(recom_prophet.iloc[0,3]), int(recom_prophet.iloc[0,3]-min(source_recom_prophet.data['RI'])), source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])]), style={'font-size': '150%'}, width=550)

def update_vbar(attr, old, new):
    if radio_button_group.active == 0: 
        source_recom_lstm.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_lstm.iloc[0,1], recom_lstm.iloc[1,1], recom_lstm.iloc[2,1]],
        'chr': [str(int(recom_lstm.iloc[0,1])), str(int(recom_lstm.iloc[1,1])), str(int(recom_lstm.iloc[2,1]))]}
        source_recom_prophet.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_prophet.iloc[0,1], recom_prophet.iloc[1,1], recom_prophet.iloc[2,1]],
        'chr' : [str(int(recom_prophet.iloc[0,1])), str(int(recom_prophet.iloc[1,1])), str(int(recom_prophet.iloc[2,1]))]}
        div3_lstm.text = '''EA Price: ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br><br>* Recommendation of the two models are the same.'''.format(int(recom_lstm.iloc[0,3]), int(recom_lstm.iloc[0,3]-min(source_recom_lstm.data['RI'])), source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])])
        div3_prophet.text = '''EA Price: ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br><br>* Recommendation of the two models are the same.'''.format(int(recom_prophet.iloc[0,3]), int(recom_prophet.iloc[0,3]-min(source_recom_prophet.data['RI'])), source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])])
    else:
        source_recom_lstm.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_lstm.iloc[0,2], recom_lstm.iloc[1,2], recom_lstm.iloc[2,2]],
        'chr': [str(int(recom_lstm.iloc[0,2])), str(int(recom_lstm.iloc[1,2])), str(int(recom_lstm.iloc[2,2]))]}
        source_recom_prophet.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_prophet.iloc[0,2], recom_prophet.iloc[1,2], recom_prophet.iloc[2,2]],
        'chr' : [str(int(recom_prophet.iloc[0,2])), str(int(recom_prophet.iloc[1,2])), str(int(recom_prophet.iloc[2,2]))]}
        div3_lstm.text = '''EA Price: ${} / month.<br>
You can save at most ${} / month by buying {} (3 year).<br><br>* Recommendation of the two models are the same.'''.format(int(recom_lstm.iloc[0,3]), int(recom_lstm.iloc[0,3]-min(source_recom_lstm.data['RI'])), source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])])
        div3_prophet.text = '''EA Price: ${} / month.<br>
You can save at most ${} / month by buying {} (3 year).<br><br>* Recommendation of the two models are the same.'''.format(int(recom_prophet.iloc[0,3]), int(recom_prophet.iloc[0,3]-min(source_recom_prophet.data['RI'])), source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])])

radio_button_group.on_change('active', update_vbar)

tab1 = Panel(child=layout([[radio_button_group], [p1_lstm, div1, p2_lstm], [divh], [div2, div_pricing, div3, div3_lstm]]), title='CNN-LSTM Model')
tab2 = Panel(child=layout([[radio_button_group], [p1_prophet, div1, p2_prophet], [divh], [div2, div_pricing, div3, div3_prophet]]), title='Prophet Model')
final_layout = Tabs(tabs=[tab1, tab2])

curdoc().add_root(final_layout)


#path = r"/Users/debby/DIGI/DIGI_TCA_2021/plot.html"
#save(obj=layout, filename=path, title="Date ＆ Consumed Quantity Plot")
