from bokeh.io import curdoc, show
from bokeh.models import RadioButtonGroup, ColumnDataSource, BoxAnnotation, Div, Panel, Tabs, LabelSet
from bokeh.plotting import figure
from bokeh.layouts import layout

import numpy as np
import pandas as pd

past = pd.read_csv('results/2021-08-24_past_plot.csv', index_col='DATE', parse_dates=['DATE'])[-23:]
forecast_lstm = pd.read_csv('results/2021-08-24_LSTM_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
recom_lstm = pd.read_csv('results/2021-08-24_LSTM_recommendation.csv', index_col=0)
forecast_prophet = pd.read_csv('results/2021-08-24_Prophet_forecast_plot.csv', index_col='DATE', parse_dates=['DATE'])
recom_prophet = pd.read_csv('results/2021-08-24_Prophet_recommendation.csv')

labels = ['RI (1 year)', 'RI (3 year)']
radio_button_group = RadioButtonGroup(labels=labels, active=0)

source_past = ColumnDataSource(past)
source_forecast_1_lstm = ColumnDataSource(forecast_lstm)
source_forecast_2_lstm = ColumnDataSource(forecast_lstm[1:])
source_forecast_1_prophet = ColumnDataSource(forecast_prophet)
source_forecast_2_prophet = ColumnDataSource(forecast_prophet[1:])

p1_lstm = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity', plot_width=600, plot_height=400, tools='')
p1_lstm.xaxis.axis_label_text_font_style = 'normal'
p1_lstm.yaxis.axis_label_text_font_style = 'normal'
p1_lstm.title.text = 'Forecast of Consumed Quantity in one Week & RI Coverage'
p1_lstm.title.text_font_size = '12.5pt'
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

p1_prophet = figure(x_axis_type='datetime', y_range=(100, 180), x_axis_label='Date', y_axis_label='Consumed Quantity', plot_width=600, plot_height=400, tools='')
p1_prophet.xaxis.axis_label_text_font_style = 'normal'
p1_prophet.yaxis.axis_label_text_font_style = 'normal'
p1_prophet.title.text = 'Forecast of Consumed Quantity in one Week & RI Coverage'
p1_prophet.title.text_font_size = '12.5pt'
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

p2_lstm = figure(x_range = data_recom_lstm['label'], y_range=(0, 500), plot_width=500, plot_height=400, title="Pricing per Month", tools='', x_axis_label='Option', y_axis_label='Pricing')
p2_lstm.xaxis.axis_label_text_font_style = 'normal'
p2_lstm.yaxis.axis_label_text_font_style = 'normal'
p2_lstm.title.text_font_size = '12.5pt'
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

p2_prophet = figure(x_range = data_recom_prophet['label'], y_range=(0, 500), plot_width=500, plot_height=400, title="Pricing per Month", tools='', x_axis_label='Option', y_axis_label='Pricing')
p2_prophet.xaxis.axis_label_text_font_style = 'normal'
p2_prophet.yaxis.axis_label_text_font_style = 'normal'
p2_prophet.title.text_font_size = '12.5pt'
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
show(final_layout)