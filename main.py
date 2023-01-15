
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

file = open("C:/Users/user/Desktop/DS3/NetflixOriginals.csv")
base = pd.read_csv(file)
jours=[]
mois=[]
annees=[]


for i in base["Premiere"]:
    mois.append(i.split(" ")[0])
    jours.append(int((i.split(" ")[1])[0:1]))
    annees.append(int(i.split(" ")[2]))


nb_jours={}
nb_mois={}
nb_annees={}

jours.sort()
mois.sort()
annees.sort()


for j in jours:
    if j in nb_jours:
        nb_jours[j]+=1
    else:
        nb_jours[j] =1

for m in mois:
    if m in nb_mois:
        nb_mois[m] += 1
    else:
        nb_mois[m] = 1
for a in annees:
    if a in nb_annees:
        nb_annees[a] += 1
    else:
        nb_annees[a] = 1


options = ['Par Jour', 'Par Mois', 'Par Année']
option = st.selectbox('Période', options)

if option == 'Par Jour':
    st.write(option)
    data = pd.DataFrame.from_dict(nb_jours.items())
    data.columns = ['Jour', 'Nombre de publications']
    data.set_index('Jour', inplace=True)
    st.bar_chart(data)


elif option == 'Par Mois':
    st.write(option)
    data = pd.DataFrame.from_dict(nb_mois.items())
    data.columns = ['Mois', 'Nombre de publications']
    data.set_index('Mois', inplace=True)
    st.bar_chart(data)

elif option == 'Par Année':
    st.write(option)
    data = pd.DataFrame.from_dict(nb_annees.items())
    data.columns = ['Annees', 'Nombre de publications']
    data.set_index('Annees', inplace=True)
    st.bar_chart(data)

expander = st.expander("Voir explication du graphe ")
expander.write("On calcule le nombre des series et films sortis en fonction de "+option[4::])


gen = []
for g in base["Genre"]:
    if g not in gen:
        gen.append(g)



maxscore = max(base['IMDB Score'])
minscore = min(base['IMDB Score'])



values = st.slider(
    'Select a range of values',
    minscore,maxscore,(3.0,5.0))

score_genre = {}
for i in base["Genre"]:
    score_genre[i]=0.0
score=[]

for i in base["IMDB Score"]:
    score.append(i)

j=0
for i in score_genre.keys():
    score_genre[i]=score[j]
    j+=1



selected={}
for x,y in score_genre.items():
    if y <= max(values) and y >= min(values):
        selected[x]=y



labels = selected.keys()
sizes = selected.values()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',textprops={'color':"w"})
ax1.axis('equal')
fig1.set_facecolor('#0e1117')

st.pyplot(fig1)
expander = st.expander("Voir explication du graphe ")
expander.write("Ce graphe visualise les pourcentages des series et films existants sur Netflix selon le score donnée d'aprés IMDB.")



options2 = st.multiselect(
'Choisir votre languages preferer',
base['Language'].unique(),
['French','English'])

lang_time = []
lang_acc={}
k=1
for i in base["Language"]:
    lang_time.append([i,0])
    if i in lang_acc:
        lang_acc[i]+=1
    else:
        lang_acc[i]=1
    k+=1
j=0
for i in base["Runtime"]:
    (lang_time[j])[1]=i
    j+=1


selected_lang=[]
for i in range(len(lang_time)):
    if (lang_time[i])[0] in options2:
        selected_lang.append(lang_time[i])



x = []
y = []
for i in selected_lang:
    x.append(i[0])
for j in selected_lang:
    y.append(j[1])
    
    
#creation d'un dictionaire des valeurs selctionnees (languages) avec les durees de chaque film 
selected_dict={}
for i in range(len(x)):
    selected_dict[x[i]]=y[i]



data =  pd.DataFrame.from_dict(selected_dict.items())
data.columns = ['languages', 'durées dees filmes par languages']
data.set_index('languages', inplace = True)


labels = selected_dict.keys()
sizes = selected_dict.values()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',textprops={'color':"w"})
ax1.axis('equal')
fig1.set_facecolor('#0e1117')

st.pyplot(fig1)


expander = st.expander("Voir explication du graphe ")
expander.write("Ce graphe visualise les durées des series et films existants sur Netflix selon les languages.")


