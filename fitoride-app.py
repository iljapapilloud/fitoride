import streamlit as st
import math

### Streamlit dashboard mit multipages -- hiermit benutzen wir radio buttons und if Bedingungen, um die Seiten zu simulieren

st.set_page_config(layout="wide") # um die Webseite breiter zu machen

#st.title("Vorstellung erster Ergebnisse") # Haupttitle nicht im Zentrum der Seite

#st.markdown("<h1 style='text-align: center; color: YellowGreen;'>Fitoride</h1>", unsafe_allow_html=True) # Jetzt Haupttitle zentriert

st.markdown("Static Bike-Fitting unisex 15-75 years old. You nead a measuring tape, a book, and some Allen keys")

with st.sidebar:
	col1, col2 = st.columns(2)
	with col1:
		st.image('logo.png', width=180)
	with col2:
		st.markdown('')
		st.markdown('')
		st.markdown('')
		st.markdown("<h1 style='float: left; color: YellowGreen;'>Fitoride</h1>", unsafe_allow_html=True)
	
	
  #st.markdown("<h1 style='text-align: center; color: YellowGreen;'>Fitoride</h1>", unsafe_allow_html=True) # 
  #st.image("logo.png", width=150)
  #st.markdown("Static Bike-Fitting unisex 15-75 years old. You nead a measuring tape, a book, and some Allen keys")

button = st.sidebar.radio("Static Bike-Fitting unisex 15-75 years old. You nead a measuring tape, a book, and some Allen keys.\n\n **Do the Bike-Fitting step by step, from first step onwards. At each step, apply the result before going to the next step**", ('Etape 1', 'Etape 2', 'Etape 3'))
#button2 = st.sidebar.radio("**PF-I Gesamt**", ('Topics', 'Trends'))

if button == 'Etape 1':
    st.markdown("<h4 style='text-align: left; color: YellowGreen;'>Saddle height</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("Barefoot with your bicycle outfit on you, face against a wall, put the book between your legs touching, not pressing, the pelvis.")
        st.markdown("With a pencile, mark on the wall where the top edge of the book touch the wall.")
        innennaht = st.number_input(label = "Input the distance (in cm) from the ground to the mark on the wall here (f.ex. 83.4): ")
        st.markdown("With a app, notice the angle between your saddle tube and an imaginary vertical straight line.")
        winkelsattelr = st.number_input(label = "Report this angle here (p.ex. 19.4): ")
        sattelhoehe = 7.41 + (0.82*float(innennaht)) - 0.1*28 + 0.003*(float(innennaht)*float(winkelsattelr))
        sattelhoehemax = 7.41 + (0.82*float(innennaht)) - 0.1*26 + 0.003*(float(innennaht)*float(winkelsattelr))
        sattelhoehemin = 7.41 + (0.82*float(innennaht)) - 0.1*30 + 0.003*(float(innennaht)*float(winkelsattelr))
        st.write("\nYour optimal saddle height in cm is: ", sattelhoehe)
        st.write("\nYour saddle height should not be under:  ", sattelhoehemin)
        st.write("\nYour saddle height should not exceed:  ", sattelhoehemax)

    with col2:
        st.image("Beinc.png",width=150, caption='Inseam length')
        st.image("bike3ac.png",width=150, caption='Angle saddle tube/imaginary straight line')
        st.image("bike2ac.png",width=150, caption='Saddle height from middle of the chainring/bottom of saddle')

if button == 'Etape 2':
    st.markdown("<h4 style='text-align: left; color: YellowGreen;'>Saddle forth/back</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        sattellang = st.number_input("Report the lenght of your saddle in cm (p.ex. 27.5): ")
        sattelmittep = float(sattellang)/2
        sattelgravit = (float(sattellang)*2)/3
        sattelgp = sattelgravit - sattelmittep
        st.markdown("Move the saddle until its middle point (Z) is at the middle point of the saddle tube.")
        st.write("You can move the saddle forward until (G) ", sattelgp)
        st.markdown("You saddle must be parallel to the ground. It should not point up or down.")


    with col2:
        st.image("Sattelc.png",width=200, caption='Saddle forth/back, centre(Z), gravity(G)')

if button == 'Etape 3':
    st.markdown("<h4 style='text-align: left; color: YellowGreen;'>Torso and arms</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        arm = st.number_input("Arm length from your wrist (jonction hand-wrist) to shoulder (jonction shoulder-torso) in cm: ")
        armcorrup = (float(arm)*0.04)
        armcorrdown = (float(arm)*0.08)
        armup = float(arm) - float(armcorrup)
        armdown = float(arm) - float(armcorrdown)

        armlenkeropt = (float(armup)/math.sin(math.radians(45)))*math.sin(math.radians(105))
        armlenkermin = (float(armup)/math.sin(math.radians(40)))*math.sin(math.radians(100))
        armlenkermax = (float(armup)/math.sin(math.radians(50)))*math.sin(math.radians(110))

        armlenkersopt = (float(armdown)/math.sin(math.radians(45)))*math.sin(math.radians(105))
        armlenkersmin = (float(armdown)/math.sin(math.radians(40)))*math.sin(math.radians(100))
        armlenkersmax = (float(armdown)/math.sin(math.radians(50)))*math.sin(math.radians(110))

        st.markdown("If you want to drive with outstreched arms, then...")

        st.write("... the optimal distance from the middle of the saddle to the middle of the handlebars is (in cm):", armlenkeropt)
        st.write("... the distance from the middle of the saddle to the middle of the handlebars (in cm) should not exceed:", armlenkermin)
        st.write("... the distance from the middle of the saddle to the middle of the handlebars (in cm) should not be less than:", armlenkermax)


        st.markdown("If you prefer driving with arms less outstreched, then...")

        st.write("... the optimal distance from the middle of the saddle to the middle of the handlebars is (in cm):", armlenkersopt)
        st.write("... the distance from the middle of the saddle to the middle of the handlebars (in cm) should not exceed:", armlenkersmin)
        st.write("... the distance from the middle of the saddle to the middle of the handlebars (in cm) should not be less than:", armlenkersmax)

    with col2:
        st.image("armc.png",width=200,caption='Arm length')
