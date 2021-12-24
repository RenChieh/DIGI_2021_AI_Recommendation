#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:27:22 2021

@author: debby
"""

from bokeh.models import ColumnDataSource, DatetimeTickFormatter, RadioButtonGroup, BoxAnnotation, Div, Panel, Tabs, LabelSet
from bokeh.plotting import figure, curdoc,output_file, show
from bokeh.models.widgets import Select
from bokeh.layouts import column, row, layout
from bokeh.io import output_notebook,output_file, show
from math import pi
import datetime
import pandas as pd
import numpy as np


df_us=pd.read_csv('data/VM-Usage.csv')
pricesheet=pd.read_csv('data/azure-retail-multi-price-2021-07-01.csv')

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

p = figure(plot_width=1450, plot_height=650, x_axis_type='datetime'\
           ,x_axis_label='Date',y_axis_label='Consumed Quantity (hr)'\
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
p.title.text_font_size = "24px"
p.min_border_top = 150





#第一個下拉選單
select = Select(title="Resource Group",  options=['A',
        'B','C','D','E','F',\
            'G','H'])


#第二個下拉選單
select2 = Select(title="Service Type", options=['Virtual Machine'])

#第三個下拉選單
select3 = Select(title="Sku Name",  options=['D2 v3','E8 v3','D8 v3',\
    'D4 v3','M32ms','E20 v3','E4 v3','D16 v3','D2 v2','D1 v2',\
    'E32 v3','E16 v3','M32ts','E48 v3','B2s','F8s v2','F8'])

#下拉選單置預設值
select.value, select2.value, select3.value= 'A', 'Virtual Machine','D2 v3'    
    
#第一個下拉選單的callback
def update_plot(attrname, old, new):
    newSource = df1
    if select.value == 'A' and select3.value == 'D2 v3':
        newSource = df1
    if select.value == 'A' and select3.value == 'E8 v3':
        newSource = df2
    if select.value == 'A' and select3.value == 'D8 v3':
        newSource = df3
    if select.value == 'A' and select3.value == 'D4 v3':
        newSource = df4
    if select.value == 'A' and select3.value == 'M32ms':
        newSource = df5    
    if select.value == 'A' and select3.value == 'E16 v3':
        newSource = df6
    if select.value == 'A' and select3.value == 'M32ts':
        newSource = df7
    if select.value == 'A' and select3.value == 'E48 v3':
        newSource = df8
    if select.value == 'B' and select3.value == 'D2 v3':
        newSource = df9  
    if select.value == 'B' and select3.value == 'D16 v3':
        newSource = df10  
    if select.value == 'B' and select3.value == 'D2 v2':
        newSource = df11
    if select.value == 'B' and select3.value == 'D4 v3':
        newSource = df12
    if select.value == 'C' and select3.value == 'D2 v3':
        newSource = df13 
    if select.value == 'D' and select3.value == 'D2 v3':
        newSource = df14 
    if select.value == 'E' and select3.value == 'D2 v3':
        newSource = df15 
    if select.value == 'E' and select3.value == 'B2s':
        newSource = df16
    if select.value == 'F' and select3.value == 'F8s v2':
        newSource = df17 
    if select.value == 'F' and select3.value == 'F8':
        newSource = df18 
    if select.value == 'G' and select3.value == 'D2 v3':
        newSource = df19 
    if select.value == 'H' and select3.value == 'D2 v2':
        newSource = df20 

    source.data =  newSource


source.data = df1
r = p.line(x='DATE', y='ConsumedQuantity', line_width=2, line_color='#81968F'\
           , source = source)

#第一個下拉選單動作
select.on_change('value', update_plot)
#第二個下拉選單動作data
select3.on_change('value', update_plot)

###Div
div_title1 = Div(text='Recommendation System', style={'font-size': '300%'}, width=600)
div_space = Div(text=' ',width = 675, height=50)
div_space1 = Div(text=' ',width = 675, height=150)
div_space2 = Div(text=' ',width = 675, height=25)
div1 = Div(text='', width=100)
div2 = Div(text='', width=200)
div5 = Div(text='', width=25)
#把表單放入網頁的佈局
layout_plot =column(div_space2, row([div_space, div_title1]), row(div5, column([div1, select, select2, select3], width=210, height=250), p), div_space1)
curdoc().add_root(layout_plot)






###博儒的圖
series_idx = pd.date_range(start='2021-07-15', end='2021-08-31', freq='D')
series = pd.DataFrame({'num': np.zeros(len(series_idx))})
series.index = series_idx
series.index.name = 'DATE'
past1 = pd.read_csv('recommendation/results/2021-07-27_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-13:]
past2 = pd.read_csv('recommendation/results/2021-08-03_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-20:]
past3 = pd.read_csv('recommendation/results/2021-08-10_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-27:]
past4 = pd.read_csv('recommendation/results/2021-08-17_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-34:]
past5 = pd.read_csv('recommendation/results/2021-08-24_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-41:]
past_ani = [past1, past2, past3, past4, past5]

forecast1_lstm = pd.read_csv('recommendation/results/2021-07-27_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast2_lstm = pd.read_csv('recommendation/results/2021-08-03_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast3_lstm = pd.read_csv('recommendation/results/2021-08-10_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast4_lstm = pd.read_csv('recommendation/results/2021-08-17_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast5_lstm = pd.read_csv('recommendation/results/2021-08-24_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast_ani_lstm = [forecast1_lstm, forecast2_lstm, forecast3_lstm, forecast4_lstm, forecast5_lstm]
forecast_2_ani_lstm = [forecast1_lstm[1:], forecast2_lstm[1:], forecast3_lstm[1:], forecast4_lstm[1:], forecast5_lstm[1:]]

forecast1_prophet = pd.read_csv('recommendation/results/2021-07-27 forcast plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast2_prophet = pd.read_csv('recommendation/results/2021-08-03 forcast plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast3_prophet = pd.read_csv('recommendation/results/2021-08-10 forcast plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast4_prophet = pd.read_csv('recommendation/results/2021-08-17 forcast plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast5_prophet = pd.read_csv('recommendation/results/2021-08-24 forcast plot.csv', index_col='DATE', parse_dates=['DATE'])
forecast_ani_prophet = [forecast1_prophet, forecast2_prophet, forecast3_prophet, forecast4_prophet, forecast5_prophet]
forecast_2_ani_prophet = [forecast1_prophet[1:], forecast2_prophet[1:], forecast3_prophet[1:], forecast4_prophet[1:], forecast5_prophet[1:]]

source_range_ani = ColumnDataSource(series)
source_past_ani = ColumnDataSource(past1)
source_forecast_ani_lstm_ani = ColumnDataSource(forecast1_lstm)
source_forecast_2_lstm_ani = ColumnDataSource(forecast1_lstm[1:])
source_forecast_ani_prophet_ani = ColumnDataSource(forecast1_prophet)
source_forecast_2_prophet_ani = ColumnDataSource(forecast1_prophet[1:])

p1_lstm_ani = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity (hr)', plot_width=800, plot_height=450, tools='')
p1_lstm_ani.xaxis.axis_label_text_font_style = 'normal'
p1_lstm_ani.yaxis.axis_label_text_font_style = 'normal'
p1_lstm_ani.title.text = 'Forecast of Consumed Quantity in one Week'
p1_lstm_ani.title.align = "center"
p1_lstm_ani.title.text_font_size = '24px'
p1_lstm_ani.xaxis.axis_label_text_font_size = '14pt'
p1_lstm_ani.xaxis.major_label_text_font_size = '14px'
p1_lstm_ani.yaxis.axis_label_text_font_size = '14pt'
p1_lstm_ani.yaxis.major_label_text_font_size = '14px'

p1_lstm_ani.line('DATE', 'num', source=source_range_ani)
p1_lstm_ani.line('DATE', 'ConsumedQuantity', line_color='gray', legend_label='Past Value', source=source_past_ani, line_width=2)
p1_lstm_ani.line('DATE', 'ConsumedQuantity', line_color='orange', legend_label='Forecast', source=source_forecast_ani_lstm_ani, line_width=2)
p1_lstm_ani.circle('DATE','ConsumedQuantity', line_color='orange', source=source_forecast_2_lstm_ani, fill_alpha=0.8, fill_color='darkorange', size=6)

p1_prophet_ani = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity (hr)', plot_width=800, plot_height=450, tools='')
p1_prophet_ani.xaxis.axis_label_text_font_style = 'normal'
p1_prophet_ani.yaxis.axis_label_text_font_style = 'normal'
p1_prophet_ani.title.text = 'Forecast of Consumed Quantity in one Week'
p1_prophet_ani.title.align = "center"
p1_prophet_ani.title.text_font_size = '24px'
p1_prophet_ani.xaxis.axis_label_text_font_size = '14pt'
p1_prophet_ani.xaxis.major_label_text_font_size = '14px'
p1_prophet_ani.yaxis.axis_label_text_font_size = '14pt'
p1_prophet_ani.yaxis.major_label_text_font_size = '14px'

p1_prophet_ani.line('DATE', 'num', source=source_range_ani)
p1_prophet_ani.line('DATE', 'ConsumedQuantity', line_color='gray', legend_label='Past Value', source=source_past_ani, line_width=2)
p1_prophet_ani.line('DATE', 'ConsumedQuantity', line_color='orange', legend_label='Forecast', source=source_forecast_ani_prophet_ani, line_width=2)
p1_prophet_ani.circle('DATE','ConsumedQuantity', line_color='orange', source=source_forecast_2_prophet_ani, fill_alpha=0.8, fill_color='darkorange', size=6)

t = 1
def update():
    global t
    idx = t%5
    source_past_ani.data = past_ani[idx]
    source_forecast_ani_lstm_ani.data = forecast_ani_lstm[idx]
    source_forecast_2_lstm_ani.data = forecast_2_ani_lstm[idx]
    source_forecast_ani_prophet_ani.data = forecast_ani_prophet[idx]
    source_forecast_2_prophet_ani.data = forecast_2_ani_prophet[idx]
    t += 1
###

past = pd.read_csv('recommendation/results/2021-08-24_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-23:]
forecast_lstm = pd.read_csv('recommendation/results/2021-08-24_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
recom_lstm = pd.read_csv('recommendation/results/2021-08-24_LSTM_recommendation.csv', index_col=0)
forecast_prophet = pd.read_csv('recommendation/results/2021-08-24_Prophet_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
recom_prophet = pd.read_csv('recommendation/results/2021-08-24_Prophet_recommendation.csv')

labels = ['Reserved Instance (1 year)', 'Reserved Instance (3 year)']
radio_button_group = RadioButtonGroup(labels=labels, active=0)

source_past = ColumnDataSource(past)
source_forecast_1_lstm = ColumnDataSource(forecast_lstm)
source_forecast_2_lstm = ColumnDataSource(forecast_lstm[1:])
source_forecast_1_prophet = ColumnDataSource(forecast_prophet)
source_forecast_2_prophet = ColumnDataSource(forecast_prophet[1:])

p1_lstm = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity (hr)', plot_width=800, plot_height=450, tools='')
p1_lstm.xaxis.axis_label_text_font_style = 'normal'
p1_lstm.yaxis.axis_label_text_font_style = 'normal'
p1_lstm.title.text = 'Forecast of Consumed Quantity in one Week & RI Coverage'
p1_lstm.title.align = "center"
p1_lstm.title.text_font_size = '24px'
p1_lstm.xaxis.axis_label_text_font_size = '14pt'
p1_lstm.xaxis.major_label_text_font_size = '14px'
p1_lstm.yaxis.axis_label_text_font_size = '14pt'
p1_lstm.yaxis.major_label_text_font_size = '14px'

p1_lstm.line('DATE', 'ConsumedQuantity', line_color='gray', legend_label='Past Value', source=source_past, line_width=2)
p1_lstm.line('DATE', 'ConsumedQuantity', line_color='orange', legend_label='Forecast', source=source_forecast_1_lstm, line_width=2)
p1_lstm.circle('DATE','ConsumedQuantity', line_color='orange', source=source_forecast_2_lstm, fill_alpha=0.8, fill_color='darkorange', size=6)

amounts_lstm = recom_lstm.iloc[:,0].values
R1_lstm = recom_lstm.iloc[:,1].values
R3_lstm = recom_lstm.iloc[:,2].values

color_line = range(min(amounts_lstm), max(amounts_lstm)+1)[np.argmin(R1_lstm)]*24

low_box_lstm = BoxAnnotation(top=color_line, fill_alpha=0.1, fill_color='lime')
p1_lstm.add_layout(low_box_lstm)

p1_prophet = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity (hr)', plot_width=800, plot_height=450, tools='')
p1_prophet.xaxis.axis_label_text_font_style = 'normal'
p1_prophet.yaxis.axis_label_text_font_style = 'normal'
p1_prophet.title.text = 'Forecast of Consumed Quantity in one Week & RI Coverage'
p1_prophet.title.align = "center"
p1_prophet.title.text_font_size = '24px'
p1_prophet.xaxis.axis_label_text_font_size = '14pt'
p1_prophet.xaxis.major_label_text_font_size = '14px'
p1_prophet.yaxis.axis_label_text_font_size = '14pt'
p1_prophet.yaxis.major_label_text_font_size = '14px'

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

p2_lstm = figure(x_range = data_recom_lstm['label'], y_range=(0, 500), plot_width=600, plot_height=450, title="Pricing per Month", tools='', x_axis_label='Option', y_axis_label='Pricing')
p2_lstm.title.align = "center"
p2_lstm.xaxis.axis_label_text_font_style = 'normal'
p2_lstm.yaxis.axis_label_text_font_style = 'normal'
p2_lstm.title.text_font_size = '24px'
p2_lstm.xaxis.axis_label_text_font_size = '14pt'
p2_lstm.xaxis.major_label_text_font_size = '14px'
p2_lstm.yaxis.axis_label_text_font_size = '14pt'
p2_lstm.yaxis.major_label_text_font_size = '14px'

p2_lstm.vbar(x='label', width=0.35, top='RI', source=source_recom_lstm, fill_color='darkgreen')

labels_lstm = LabelSet(x='label', y='RI', text='chr', y_offset=7, source=source_recom_lstm, text_align='center')
p2_lstm.add_layout(labels_lstm)

data_recom_prophet = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_prophet.iloc[0,1], recom_prophet.iloc[1,1], recom_prophet.iloc[2,1]],
        'chr' : [str(int(recom_prophet.iloc[0,1])), str(int(recom_prophet.iloc[1,1])), str(int(recom_prophet.iloc[2,1]))]}
source_recom_prophet = ColumnDataSource(data=data_recom_prophet)

p2_prophet = figure(x_range = data_recom_prophet['label'], y_range=(0, 500), plot_width=600, plot_height=450, title="Pricing per Month", tools='', x_axis_label='Option', y_axis_label='Pricing')
p2_prophet.title.align = "center"
p2_prophet.xaxis.axis_label_text_font_style = 'normal'
p2_prophet.yaxis.axis_label_text_font_style = 'normal'
p2_prophet.title.text_font_size = '24px'
p2_prophet.xaxis.axis_label_text_font_size = '14pt'
p2_prophet.xaxis.major_label_text_font_size = '14px'
p2_prophet.yaxis.axis_label_text_font_size = '14pt'
p2_prophet.yaxis.major_label_text_font_size = '14px'

p2_prophet.vbar(x='label', width=0.35, top='RI', source=source_recom_prophet, fill_color='darkgreen')

labels_prophet = LabelSet(x='label', y='RI', text='chr', y_offset=7, source=source_recom_prophet, text_align='center')
p2_prophet.add_layout(labels_prophet)

div1 = Div(text='', width=100)
div2 = Div(text='', width=200)
div3 = Div(text='', width=170)
divh = Div(text='<br>', width=320)
div4 = Div(text='', width=490)
div5 = Div(text='', width=25)


div_pricing = Div(text='<br><br><br>Pricing:<br> On-demand: $0.13 / hour<br> Reserved Instance (1 year): $52.92 / month<br> Reserved Instance (3 year): $33.61 / month', style={'font-size': '130%'}, width=400)

div3_lstm = Div(text='''<b>Recommend: {} (1 year) plan </b><hr><br> On-demand Price is ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br>* Recommendation of the two models are the same.'''.format(source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])], int(recom_lstm.iloc[0,3]), int(recom_lstm.iloc[0,3]-min(source_recom_lstm.data['RI'])), source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])]), style={'font-size': '150%'}, width=600)

div3_prophet = Div(text='''<b>Recommend: {} (1 year) plan </b><hr><br> On-demand Price is ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br>* Recommendation of the two models are the same.'''.format(source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])], int(recom_prophet.iloc[0,3]), int(recom_prophet.iloc[0,3]-min(source_recom_prophet.data['RI'])), source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])]), style={'font-size': '150%'}, width=600)


def update_vbar(attr, old, new):
    if radio_button_group.active == 0: 
        source_recom_lstm.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_lstm.iloc[0,1], recom_lstm.iloc[1,1], recom_lstm.iloc[2,1]],
        'chr': [str(int(recom_lstm.iloc[0,1])), str(int(recom_lstm.iloc[1,1])), str(int(recom_lstm.iloc[2,1]))]}
        source_recom_prophet.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_prophet.iloc[0,1], recom_prophet.iloc[1,1], recom_prophet.iloc[2,1]],
        'chr' : [str(int(recom_prophet.iloc[0,1])), str(int(recom_prophet.iloc[1,1])), str(int(recom_prophet.iloc[2,1]))]}
        div3_lstm.text = '''<b>Recommend: {} (1 year) plan</b><hr><br> On-demand Price is ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br>* Recommendation of the two models are the same.'''.format(source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])], int(recom_lstm.iloc[0,3]), int(recom_lstm.iloc[0,3]-min(source_recom_lstm.data['RI'])), source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])])
        div3_prophet.text = '''<b>Recommend: {} (1 year) plan</b><hr><br> On-demand Price is ${} / month.<br>
You can save at most ${} / month by buying {} (1 year).<br>* Recommendation of the two models are the same.'''.format(source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])], int(recom_prophet.iloc[0,3]), int(recom_prophet.iloc[0,3]-min(source_recom_prophet.data['RI'])), source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])])
    else:
        source_recom_lstm.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_lstm.iloc[0,2], recom_lstm.iloc[1,2], recom_lstm.iloc[2,2]],
        'chr': [str(int(recom_lstm.iloc[0,2])), str(int(recom_lstm.iloc[1,2])), str(int(recom_lstm.iloc[2,2]))]}
        source_recom_prophet.data = {'label' : ['5 RI', '6 RI', '7 RI'],
        'RI' : [recom_prophet.iloc[0,2], recom_prophet.iloc[1,2], recom_prophet.iloc[2,2]],
        'chr' : [str(int(recom_prophet.iloc[0,2])), str(int(recom_prophet.iloc[1,2])), str(int(recom_prophet.iloc[2,2]))]}
        div3_lstm.text = '''<b>Recommend: {} (3 year) plan </b><hr><br> On-demand Price is ${} / month.<br>
You can save at most ${} / month by buying {} (3 year).<br>* Recommendation of the two models are the same.'''.format(source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])], int(recom_lstm.iloc[0,3]), int(recom_lstm.iloc[0,3]-min(source_recom_lstm.data['RI'])), source_recom_lstm.data['label'][np.argmin(source_recom_lstm.data['RI'])])
        div3_prophet.text = '''<b>Recommend: {} (3 year) plan</b><hr><br> On-demand Price is ${} / month.<br>
You can save at most ${} / month by buying {} (3 year).<br>* Recommendation of the two models are the same.'''.format(source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])], int(recom_prophet.iloc[0,3]), int(recom_prophet.iloc[0,3]-min(source_recom_prophet.data['RI'])), source_recom_prophet.data['label'][np.argmin(source_recom_prophet.data['RI'])])

radio_button_group.on_change('active', update_vbar)

tab1 = Panel(child=layout([[div_space], [div4, p1_lstm_ani], [div_space1], [div1, radio_button_group], [div_space], [div3, p1_lstm, div1, p2_lstm], [divh], [div_space2], [div2, div3_lstm, div5, div_pricing], [div_space2], [div_space1]]), title='AI Model')
tab2 = Panel(child=layout([[div_space], [div4, p1_prophet_ani], [div_space1], [div1, radio_button_group], [div_space], [div3, p1_prophet, div1, p2_prophet], [divh],  [div_space2], [div2, div3_prophet, div5, div_pricing], [div_space2], [div_space1]]), title='Statistics Model')
final_layout =Tabs(tabs=[tab1, tab2])

curdoc().add_periodic_callback(update, 1500)
curdoc().add_root(final_layout)
show(final_layout)