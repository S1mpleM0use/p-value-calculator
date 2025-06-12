from tkinter import *
from tkinter import scrolledtext
import re
from scipy.stats import f

def create_tab(parent_notebook):
    frame = Frame(parent_notebook)

    def get_input(window_entry):
        try:
            input_val = window_entry.get('1.0', 'end-1c')
            clean_input = re.split(r'[,\n]', input_val)
            for i in clean_input:
                if i == '':
                    clean_input.remove(i)
            int_input = [float(i) for i in clean_input]
            return int_input
        except ValueError:
            results_contents = StringVar()
            p_val_f_stat_label['textvariable'] = results_contents
            results_contents.set('Format your data correctly')


    def calculate_dispersion(input_list : list):
        try:
            sample_average = sum(input_list) / len(input_list)
            d = [(x-sample_average)**2 for x in input_list]
            dispersion = sum(d)/(len(input_list)-1)
            return dispersion
        except ZeroDivisionError:
            results_contents = StringVar()
            p_val_f_stat_label['textvariable'] = results_contents
            results_contents.set('Your values are incomplete')

    def calculate_f_stat():
        try:
            if calculate_dispersion(get_input(data_entry_1)) > calculate_dispersion(get_input(data_entry_2)):
                result = calculate_dispersion(get_input(data_entry_1)) / calculate_dispersion(get_input(data_entry_2))
                return result
            if calculate_dispersion(get_input(data_entry_1)) < calculate_dispersion(get_input(data_entry_2)):
                result = calculate_dispersion(get_input(data_entry_1)) / calculate_dispersion(get_input(data_entry_2))
                return result
        except TypeError:
            return None


    def calculate_p_val_f_stat():
        try:
            df1 = len(get_input(data_entry_1))-1
            df2 = len(get_input(data_entry_2))-1
            p = (1-f.cdf(calculate_f_stat(), df1, df2))
            results_contents = StringVar()
            p_val_f_stat_label['textvariable'] = results_contents
            results_contents.set(f'f-stat: {calculate_f_stat():.3f}\n'
                                 f'df1: {df1}\n'
                                 f'df2: {df2}\n'
                                 f'p-value: {p:.3f}')
            return p
        except TypeError:
            return None

    data_label_1 = Label(frame, text='First set of data', font=('Consolas', 15))
    data_label_1.grid(column=0, row=0)
    data_entry_1 = scrolledtext.ScrolledText(frame, width=30, height=20, font=('Consolas', 10))
    data_entry_1.grid(column=0, row=1)

    data_label_2 = Label(frame, text='Second set of data', font=('Consolas', 15))
    data_label_2.grid(column=1, row=0)
    data_entry_2 = scrolledtext.ScrolledText(frame, width=30, height=20, font=('Consolas', 10))
    data_entry_2.grid(column=1, row=1)

    calculate_data = Button(frame, width=25, text='Calculate p value',
                            command =calculate_p_val_f_stat, font=('Consolas', 10))
    calculate_data.grid(column=0, row=2, sticky='S', columnspan=2)

    p_val_f_stat_label = Label(frame, font=('Consolas', 10))
    p_val_f_stat_label.grid(column=0, row=3, sticky='N', columnspan=2)


    return frame