"""
This module creates a rudimentary form entering system within an ipython 
notebook and creates a food stack plot with the entered data.
"""


import ipywidgets as widgets
from IPython.display import clear_output
from stack_plotting import stack_plot, food_stack_plot

# a list of lists of values to be plotted in each row
plot_list = []
# a list of values to be plotted in a row
row_vals = []

# set up all the widgets for the form
colFood = widgets.Text(
    value='',
    placeholder='Type the food you\'d like to add',
    description='Food:',
    disabled=False
)

colCals = widgets.Text(
    value='',
    placeholder='How many kCals does it have?',
    description='kCals:',
    disabled=False
)

colCO2 = widgets.Text(
    value='',
    placeholder='How much CO2e does it produce?',
    description='CO2e:',
    disabled=False
)

submit_button = widgets.Button(
    description='Add to stack plot',
    disabled=False,
    button_style='success',
    tooltip='Add to stack plot',
    icon='check'
)

clear_button = widgets.Button(
    description='Clear form',
    disabled=False,
    button_style='warning',
    tooltip='Clear submitted values',
    icon='check'
)

clearall_button = widgets.Button(
    description='Clear everything and start over',
    disabled=False,
    button_style='danger',
    tooltip='Clear everything',
    icon='check'
)

# At this point, limiting users to only three columns
def check_length(alist):    
    if len(alist) == 3:
        print('Add {} with {} kCals and {} CO2e cost to stack plot?'.format(
            alist[1], alist[0], alist[2]))
        display(submit_button) 
    if len(alist) > 3:
        print('You entered too many values! Try again.')
        row_vals.clear()
        display(colFood)

# x: text widget object
def add_to_foodlist(x):
    print('Adding food: {}, please enter kCals below...'.format(x.value))
    row_vals.append(x.value)
    check_length(row_vals)
    display(colCals)
    
def add_to_calslist(x):
    try:
        a = int(x.value)
        print('{} has {} kCals, please add CO2e below...'.format(row_vals[0], 
                                                             x.value))
        row_vals.append(a)
        check_length(row_vals)
        display(colCO2)
    except ValueError: 
        print('Please enter an integer value:') and display(colCals)
    
def add_to_CO2list(x):
    try:
        a = int(x.value)
        row_vals.insert(0, a)
        check_length(row_vals)
    except ValueError: 
        print('Please enter an integer value:') and display(colCO2)

def submit_row(x):
    a = list(row_vals)
    plot_list.append(a)
    print('Added!')
    plot = food_stack_plot(["CO2e", "Food", "kCals"], plot_list)
    plot
    display(clearall_button)
    
def clear_row(x):
    row_vals.clear()
    colFood.value = ''
    colCals.value = ''
    colCO2.value = ''
    print('Cleared.')
    clear_output()
    
    display(clear_button)
    display(clearall_button)
    display(colFood)
    
def clear_all(x):
    row_vals.clear()
    plot_list.clear()
    colFood.value = ''
    colCals.value = ''
    colCO2.value = ''
    print('Reset all.')
    clear_output()
    
    display(clear_button)
    display(colFood)
    
colFood.on_submit(add_to_foodlist)
colCals.on_submit(add_to_calslist)
colCO2.on_submit(add_to_CO2list)
submit_button.on_click(submit_row)
clear_button.on_click(clear_row)
clearall_button.on_click(clear_all)