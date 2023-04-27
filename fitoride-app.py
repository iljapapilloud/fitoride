import streamlit as st
import math

### Streamlit dashboard mit multipages -- hiermit benutzen wir radio buttons und if Bedingungen, um die Seiten zu simulieren

st.set_page_config(layout="wide") # um die Webseite breiter zu machen

#st.title("Vorstellung erster Ergebnisse") # Haupttitle nicht im Zentrum der Seite

st.markdown("<h1 style='text-align: center; color: YellowGreen;'>Fitoride</h1>", unsafe_allow_html=True) # Jetzt Haupttitle zentriert

st.markdown("Bike-Fitting statique pour hommes et femmes à partir de 15 ans. Vous avez besoin d'un centimètre, d'un livre, de quelques clés Allen - inbus")

button = st.sidebar.radio("**Procédez au Bike-Fitting étape par étape en commançant par l'étape 1. A chaque étape, procédez aux réglages voulus avant de passer à l'étape suivante**", ('Etape 1', 'Etape 2', 'Etape 3'))
#button2 = st.sidebar.radio("**PF-I Gesamt**", ('Topics', 'Trends'))

if button == 'Etape 1':
    st.markdown("<h4 style='text-align: left; color: YellowGreen;'>Hauteur de selle</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("Pieds nus avec votre tenue de sport, mettre un livre entre vos jambes et se mettre contre un mur. Le livre doit toucher, non pas presser, le pelvis.")
        st.markdown("A l'aide d'un crayon, faire un trait contre le mur à la hauteur de la tranche supérieure du livre.")
        innennaht = st.number_input(label = "Reporter la distance du sol au trait en centimètres et millimètres (p.ex. 83,4): ")
        st.markdown("A l'aide d'une app de mesure d'angles, mesurer l'angle entre le tube de selle et une droite imaginaire.")
        winkelsattelr = st.number_input(label = "Reporter l'angle en degré (p.ex. 19,4): ")
        sattelhoehe = 7.41 + (0.82*float(innennaht)) - 0.1*28 + 0.003*(float(innennaht)*float(winkelsattelr))
        sattelhoehemax = 7.41 + (0.82*float(innennaht)) - 0.1*26 + 0.003*(float(innennaht)*float(winkelsattelr))
        sattelhoehemin = 7.41 + (0.82*float(innennaht)) - 0.1*30 + 0.003*(float(innennaht)*float(winkelsattelr))
        st.write("\nVotre hauteur de selle optimale en cm est: ", sattelhoehe)
        st.write("\nVotre hauteur de selle en cm ne doit pas être inférieure à:  ", sattelhoehemin)
        st.write("\nVotre hauteur de selle en cm ne doit pas être supérieure à:  ", sattelhoehemax)

    with col2:
        st.image("Beinc.png",width=150, caption='Longeur interne de la jambe')
        st.image("bike3ac.png",width=150, caption='Angle tube de selle/droite')
        st.image("bike2ac.png",width=150, caption='Hauteur de selle axe pédalier/sommet selle')

if button == 'Etape 2':
    st.markdown("<h4 style='text-align: left; color: YellowGreen;'>Selle en avant/en arrière</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        sattellang = st.number_input("Longueur de la selle en centimètres et millimètres (p.ex. 27.5): ")
        sattelmittep = float(sattellang)/2
        sattelgravit = (float(sattellang)*2)/3
        sattelgp = sattelgravit - sattelmittep
        st.markdown("Placer la selle de sorte que le centre de la selle (Z) soit au centre du tube de selle.")
        st.write("Vous pouvez avancer la selle jusqu'au point (G), en cm au maximum de ", sattelgp)
        st.markdown("Votre selle doit être parallèle au sol, ne pas pencher vers le bas ou monter vers le haut.")


    with col2:
        st.image("Sattelc.png",width=200, caption='Selle en avant/en arrière, centre(Z), gravité(G)')

if button == 'Etape 3':
    st.markdown("<h4 style='text-align: left; color: YellowGreen;'>Haut du corps</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        arm = st.number_input("Longueur de votre bras du poignet (jonction main-poignet) à la base de l'épaule (jonction épaule-torse) en centimètres: ")
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

        st.markdown("Si vous préférez rouler avec les bras plus tendus, alors...")

        st.write("... la distance optimale du centre de la selle au centre du guidon en cm est de:", armlenkeropt)
        st.write("... du centre de la selle au centre du guidon, cette distance en cm ne devrait pas être supérieure à:", armlenkermin)
        st.write("... du centre de la selle au centre du guidon, cette distance en cm ne devrait pas être inférieure à:", armlenkermax)


        st.markdown("Si vous préférez rouler avec les bras moins tendus, alors...")

        st.write("... la distance optimale du centre de la selle au centre du guidon en cm est de:", armlenkersopt)
        st.write("... du centre de la selle au centre du guidon, cette distance en cm ne devrait pas être supérieure à:", armlenkersmin)
        st.write("... du centre de la selle au centre du guidon, cette distance en cm ne devrait pas être inférieure à:", armlenkersmax)

    with col2:
        st.image("armc.png",width=200,caption='Longueur du bras')
