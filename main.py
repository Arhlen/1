import matplotlib.pyplot as plt
import streamlit as st



def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
            if data[1] == "1":
                saved += 1
    return saved / total*100, (total - saved)  / total*100
with open('data.csv') as file:
    text = file.readlines()
    print(get_pas_count(text[1:], min_age =  0))

def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
            if data[1] == "1":
                saved += 1
    return saved / total*100, (total - saved)  / total*100
with open('data.csv') as file:
    text = file.readlines()
    print(get_pas_count(text[1:],30))

def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age):
            total += 1
            if data[1] == "1":
                saved += 1
    return saved / total*100, (total - saved)  / total*100
with open('data.csv') as file:
    text = file.readlines()

    print(get_pas_count(text[1:],60))


columns = ['до 30 лет', 'от 30 до 60 лет', 'старше 60 лет']
st.title('Пассажиры Титаника')
st.write('Для просмотра информации о доле выживших/погибших пассажиров выберите возраст:')
choice = st.selectbox('Выберите возраст:', columns)
index = columns.index(choice)


with open('data.csv') as file:
    lines = file.readlines()[1:]

min_age, val = get_pas_count(lines,index)
data = {'Возраст':['Выжившие', 'Погибшие'], 'Доля,%': [min_age,val]}
st.table(data)

x = [min_age]
y = [val]
plt.bar(choice, val)

fig = plt.figure(figsize=[10, 5])

plt.xlabel('Возраст пассажиров')
plt.ylabel('Доля выживших пассажиров')
plt.title('Диаграмма')
plt.legend()
st.pyplot(fig)


#def fun():


