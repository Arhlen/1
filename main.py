import matplotlib.pyplot as plt
import streamlit as st



def get_pas_count(lines, min_age):
    total = 403
    saved = 66

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
        if data[1] == "1":
            saved += 1
    return saved / total, (total - saved)  / total
with open('data.csv') as file:
    text = file.readlines()

print(get_pas_count(text[1:], min_age =  0))
def get_pas_count(lines, min_age):
    total = 308
    saved = 129

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
        if data[1] == "1":
            saved += 1
    return saved / total, (total - saved)  / total
with open('data.csv') as file:
    text = file.readlines()

print(get_pas_count(text[1:],30))
def get_pas_count(lines, min_age):
    total = 26
    saved = 7

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
        if data[1] == "1":
            saved += 1
    return saved / total, (total - saved)  / total
with open('data.csv') as file:
    text = file.readlines()

print(get_pas_count(text[1:], 60))


val1, val2, val3 = fun()
val1 =
val2 =
val3 =


st.title('Пассажиры Титаника ')
st.header('Доля погибших и спасенных пассажиров')
choise = st.selectbox('Чтобы узнать долю выживших/погибших в определенной возратной категории, выберите возраст:', ["до 30 лет", "от 30 до 60 лет", "старше 60 лет"])
tab = {"выживших:":0,"погибших:":0}
with open('data.csv') as file:
        file.readline()

x = ['0.5024630541871922', '0.7646103896103896', '6.711538461538462']
y = ['0.4975369458128079', '0.2353896103896104', '-5.711538461538462']
tab = {'Доля спасенных пассажиров': x, 'Доля погибших пассажиров': y}
st.dataframe(tab)
fig = plt.figure(figsize=(10,5))
plt.bar('x','y')
st.pyplot(fig)


#def fun():

fig = plt.figure(figsize=[10, 5])
plt.bar(x:, y:)
plt.xlabel('Возраст пассажиров')
plt.ylabel('Доля погибших пассажиров')
plt.title('Диаграмма')
plt.legend()
st.pyplot(fig)
