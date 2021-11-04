import streamlit as st 
import pandas as pd 


st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:150px !important;
}
</style>
""", unsafe_allow_html=True)

col1, mid, col2 = st.columns([1,1,35])
with col1:
    st.image('6.png', width=60)
with col2:
    new_title = '<p style="font-family:sans-serif; color:#3d9be9; font-size: 42px;">ZHome</p>'
    st.markdown(new_title, unsafe_allow_html=True)



col1,col2,col3 = st.columns(3)

col1.header('House/Villa')
col1.image('villa1.jpg',width=220)
vil=col1.checkbox('click')

col2.header('Appartment')
col2.image('appartment1.jpg',width=220)
app=col2.checkbox('click ')

col3.header('vacation_House')
col3.image('vacation1.jpg',width=220)
vac=col3.checkbox('click  ')

Rooms = pd.DataFrame({
	'First column':[0,2,3,4,5,6,7,8,9,10]
	})





if vil==True:
	option_room = st.selectbox(
	'How many Rooms ?',
	Rooms['First column'])
elif app==True:
	option_room = st.selectbox(
	'How many Rooms ?',
	Rooms['First column'])

elif vac==True:
	option_room = st.selectbox(
	'How many Rooms ?',
	Rooms['First column'])



door_window=0
motion_sensor=0
smart_AC = 0
smart_Meter = 0 
voice_ass=0
smart_intercom=0
smart_light=0


st.write('_____________________________________________________________')



if vil or app or vac ==True:

	st.markdown("""
	<div style="text-align: center; color:#3d9be9; font-size: 42px"> ZHome service </div>

	""",unsafe_allow_html=True)
	colu1,colu2,colu3,colu4,colu5 = st.columns(5)

	colu1.write('Home security')
	colu1.image('security1.jpg')
	sec=colu1.checkbox('click    ')

	colu2.write('Energy managment')
	colu2.image('energy1.jpg')
	eng=colu2.checkbox('click     ')

	colu3.write('Access control')
	colu3.image('access1.jpg')
	con=colu3.checkbox('click      ')

	colu4.write('Voice assistant')
	colu4.image('voice1.jpg')
	voi=colu4.checkbox('click       ')

	colu5.write('Smart lighting')
	colu5.image('light1.jpg')
	lig=colu5.checkbox('click        ')




	if sec==True:
		door_window = option_room*1500 
		motion_sensor = option_room*1600
		contain = st.container()
		co1,co2,co3= st.columns(3)
		with contain:
			with co1:
				co1.image('motion2.jpg',width=150)
			with co2:
				st.header('Motion ensor')
			with co3:
				st.header('1600 LE ')

		contain1 = st.container()
		co1,co2,co3= st.columns(3)
		with contain1:
			with co1:
				co1.image('door.jpg',width=150)
			with co2:
				st.header('Door/Window sensor')
			with co3:
				st.header('1500 LE ')
	
	if eng==True:
		smart_AC = option_room*1700
		smart_Meter = 2500
		contain3 = st.container()
		co1,co2,co3= st.columns(3)
		with contain3:
			with co1:
				co1.image('meter.jpg',width=150)
			with co2:
				st.header('Smart Meter')
			with co3:
				st.header('2500 LE ')

		contain4 = st.container()
		co1,co2,co3= st.columns(3)
		with contain4:
			with co1:
				co1.image('AC.jpg',width=150)
			with co2:
				st.header('Smart AC')
			with co3:
				st.header('950~2500 LE ')

	if con==True:
		smart_intercom = 8500
		contain5 = st.container()
		co1,co2,co3= st.columns(3)
		with contain5:
			with co1:
				co1.image('inter.jpg',width=150)
			with co2:
				st.header('Smart intercom')
			with co3:
				st.header('5000~12000 LE ')

	if voi==True:
		voice_ass = 3000 
		contain6 = st.container()
		co1,co2,co3= st.columns(3)
		with contain6:
			with co1:
				co1.image('v.jpg',width=150)
			with co2:
				st.header('Voice assistant ')
			with co3:
				st.header('1500 LE ')

	if lig==True:
		smart_light = option_room*2000
		contain7 = st.container()
		co1,co2,co3= st.columns(3)
		with contain7:
			with co1:
				co1.image('lig.jpg',width=150)
			with co2:
				st.header('Smart lightness ')
			with co3:
				st.header('1500 LE ')

	contain8 = st.container()
	co1,co2,co3= st.columns(3)
	with contain8:
		with co1:
			co1.image('hub.jpg',width=150)
		with co2:
			st.header('Smart Hub ')
		with co3:
			st.header('5700~8500 LE ')

	price = st.button('Get price')

	if price:
		total = 7000+door_window+motion_sensor+smart_light+smart_intercom+smart_Meter+smart_AC+voice_ass
		st.write(option_room,'room need',total,'LE')
		

