import streamlit as st



def calculator_body():

    #divides app logic from the data
    st.write('---')

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        num1 = st.number_input(label = 'enter the first integer', step = 1)

    with col2:
        num2 = st.number_input(label = 'enter the second integer', step = 2)

    with col3:
        operator = st.select_box(label = 'select an operator', options= ['Add', 'Subtract', 'Divide', 'Multiply'])

    # add the logic

    if st.button('Click here for result'):
        if num2 == 0 and operator == 'Divide':
            st.error('Cannot divide by zero')
        else:
             calculator_function(num1, num2, operator)



def calculator_function(num1, num2, operator):
    if operator == 'Add': result = num1 + num2
    elif operator == 'Subtract': result = num1 - num2
    elif operator == 'Divide': result = num1/num2
    elif operator == 'Multiply': result = num1 * num2
    st.success(f'Your result is **{result}**')


