from tkinter import *
from tkinter import scrolledtext
import re, math

def create_tab(parent_notebook):
    frame = Frame(parent_notebook)

    def get_input():
        try:
            input_val = data_entry.get('1.0', 'end-1c')
            clean_input = re.split(r'[,\n]', input_val)
            for i in clean_input:
                if i == '':
                    clean_input.remove(i)
            int_input = [float(i) for i in clean_input]
            return int_input
        except ValueError:
            results_contents = StringVar()
            sample_average_label['textvariable'] = results_contents
            results_contents.set('Remove irregular spacings from your data')

    def calculate_sample_average():
        try:
            sample_average = sum(get_input()) / len(get_input())
            results_contents = StringVar()
            sample_average_label['textvariable'] = results_contents
            results_contents.set(f'Sample average is: {sample_average:.3f}')
            return sample_average
        except ZeroDivisionError:
            results_contents = StringVar()
            sample_average_label['textvariable'] = results_contents
            results_contents.set('Your values are incomplete')

    def calculate_z_stat():
        try:
            z = ((calculate_sample_average() - float(entry_for_population_mean.get())) /
                (float(entry_for_population_standard_deviation.get())/ math.sqrt(len(get_input()))))
            results_contents = StringVar()
            z_test_label['textvariable'] = results_contents
            results_contents.set(f'Z-stat: {z:.3f}')
            return z
        except ValueError:
            results_contents = StringVar()
            z_test_label['textvariable'] = results_contents
            results_contents.set('Your values are incomplete')

    def calculate_p_val_z_stat():
        try:
            phi = 0.5 * (1 + math.erf(calculate_z_stat()/math.sqrt(2)))
            results_contents = StringVar()
            p_val_by_z_label['textvariable'] = results_contents
            results_contents.set(f'p-value: {2*min(phi, 1-phi):.3f}')
            return 2*min(phi, 1-phi)
        except TypeError:
            results_contents = StringVar()
            p_val_by_z_label['textvariable'] = results_contents
            results_contents.set('Your values are incomplete')


    data_label = Label(frame, text='Enter data below', font=('Consolas', 20))
    data_label.grid(column= 0, row = 0)

    data_entry = scrolledtext.ScrolledText(frame, width=30, height=20, font=('Consolas', 10))
    data_entry.grid(column= 0, row = 1, padx=10)

    label_for_population_mean = Label(frame, text= 'Enter the Population Mean (μ)', font=('Consolas', 10))
    label_for_population_mean.grid(column= 1, row = 0)
    entry_for_population_mean = Entry(frame, font=('Consolas', 10))
    entry_for_population_mean.grid(column= 1, row = 1, sticky='N')

    label_for_population_standard_deviation = Label(frame, text= 'Enter the Population Standard Deviation (σ):',
                                                    font=('Consolas', 10))
    label_for_population_standard_deviation.grid(column= 2, row = 0, padx = 30)
    entry_for_population_standard_deviation = Entry(frame, font=('Consolas', 10))
    entry_for_population_standard_deviation.grid(column= 2, row = 1, sticky='N')

    calculate_data = Button(frame, width=35, text='Calculate sample average',
                            command=calculate_sample_average, font=('Consolas', 10))
    calculate_data.grid(column= 0, row = 2)

    sample_average_label = Label(frame, font = ('Consolas', 10))
    sample_average_label.grid(column= 0, row = 3)

    z_test = Button(frame, width=30, text='Z-test data',
                    command=calculate_z_stat, font=('Consolas', 10))
    z_test.grid(column= 1, row = 2)
    z_test_label = Label(frame, font=('Consolas', 10))
    z_test_label.grid(column=1, row = 3)

    p_val_by_z = Button(frame, width=30, text='Calculate p-value from Z-test',
                        command = calculate_p_val_z_stat, font=('Consolas', 10))
    p_val_by_z.grid(column= 2, row = 2)
    p_val_by_z_label = Label(frame, font=('Consolas', 10))
    p_val_by_z_label.grid(column=2, row = 3)

    return frame
