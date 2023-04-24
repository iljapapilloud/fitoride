#!/usr/bin/python
import math

print("""
                                 Fitoride

                   Willkommen zu Fitoride-App für Bike-Fitting!

Basiert auf Ergebnissen der Forschung in der Biomeachanik, der Medizin,
und der Kinematik gibt ihnen diese App in weniger Zeit ein zuverlässiges
Bikefit auf der Grundlage von vier Messungen, und zwar:

 - Innennaht/Innenbeinlänge vom Boden zum Pelvis in Zentimetern
 - Innenwinkel zwischen dem Sattelrohr und einer Grade
 - Länge des Sattels
 - Länge von der Sattelmitte bis zum Mittelpunkt der horizontalen Lenkersstange

Die App führt Sie Schritt für Schritt im Prozess des Bike-Fitting und empfiehlt Ihnen Maßnahmen, die Sie
berücksichtigen können, um Ihr Setup zu verbessern. Am Ende sitzen Sie auf Ihrem Fahrrad in einer ergonomischen
guten und biomechanischen effizienten Position.

""")

print("""\n

                                  1. Stufe

Die Länge vom Innennaht bzw. vom Innenbein können Sie wie folgt durchführen. Barfuß, mit der
passenden Sportbekleidung und mit einem Buch zwischen den Beinen, dessen Oberkante den Innennaht
berührt (ohne Druck) stehen Sie gegenüber einer Wand. Mit einem Kugelschreiber zeichnen Sie einen Strich
an der Wand in der Höhe des oberer Kante vom Buch. Dann messen Sie die Länge vom Boden bis zum
Strich. Dies ist die Länge von Ihrem Innenbein.

""")

innennaht = input("\nGeben Sie die Länge von Ihrem Innenbein in Zentimetern (etwa 83.4): ")

winkelsattelr = input("\nGeben Sie den Winkel vom Stattelrohr am Fahrrad im Verhältnis zu einer Gerade (etwa 19.4): ")

sattelhoehe = 7.41 + (0.82*float(innennaht)) - 0.1*28 + 0.003*(float(innennaht)*float(winkelsattelr))
sattelhoehemax = 7.41 + (0.82*float(innennaht)) - 0.1*26 + 0.003*(float(innennaht)*float(winkelsattelr))
sattelhoehemin = 7.41 + (0.82*float(innennaht)) - 0.1*30 + 0.003*(float(innennaht)*float(winkelsattelr))

print("\nIn Ihrem Fall ist die optimale Sattelhöhe vom Kurbelachse zur Spitze vom Sattel", sattelhoehe, "Zentimeter.")

print("\nDie Toleranz um diese optimale Sattelhöhe ist die Folgende. Wenn Sie am liebsten mit einem nicht so stark gestrecktes Bein fahren möchten, dann können Sie die Höhe des Sattels auf", sattelhoehemin, "stellen, ohne dabei die Ergonomie und die Performanz zu schwächen. Wenn Sie eher mit mehr gestrecktem Bein fahren möchten, sollten sie den Sattel nicht höher als", sattelhoehemax, "Zentimeter stellen.")

print("""
                                  2. Stufe

Die Sattelhöhe steht. Jetzt müssen wir den Sattel in die Position bringen, die für diese Höhe die optimale Position ist.

""")

sattellang = input("Geben Sie die Länge von ihrem Sattel in Zentimetern (etwa 27.5): ")

sattelmittep = float(sattellang)/2
sattelgravit = (float(sattellang)*2)/3
sattelgp = sattelgravit - sattelmittep

print("\nIn Ihrem Fall müssen Sie den Sattelpunkt in der Entfernung von", sattelmittep, "Zentimetern von der Sattelspitze in der Mitte des Sattelrohrs positionieren. Dabei achten Sie bitte darauf, dass der Sattel gerade und parallel zum Boden positioniert ist.")

print("\nWenn Sie lieber mit dem Sattel mehr nach vorne fahren möchten, können Sie den Sattel bis höchstens", sattelgp, "Zentimeter nach vorne schieben. Dabei werden die Oberschenkelmuskeln mehr beansprucht, ohne jedoch dass das Fahren signifikativ im Sinne der Durchschnittsgeschwindigkeit verbessert wird.")

print("""
                                  3. Stufe

Der Sattel steht. Jetzt berechnen wir die optimale Sitzposition im Bezug auf Ihrer Biegung auf dem Rad.
Diese Messung gilt für gewöhnliche Fahrräder wie Citybike, Mountainbike, Gravelbike und Rennräder.
Für andere Fahrräder, bei denen Ihr Rücken nicht oder sehr wenig gebogen wird, kann diese Stufe
ignoriert werden.


""")

sattellenker = input("Bitte tragen Sie die Länge in Zentimeter vom Mittelpunkt des Sattels bis zur Mitte der horizontalen Lenkerstange ein (etwa 64.3): ")

armlenkeropt = (float(sattellenker)/math.sin(math.radians(105)))*math.sin(math.radians(45))

armlenkermin = (float(sattellenker)/math.sin(math.radians(100)))*math.sin(math.radians(40))

armlenkermax = (float(sattellenker)/math.sin(math.radians(110)))*math.sin(math.radians(50))

print("\nIn Ihrem Fall ist die Länge vom Innenchulternaht bis zum Handgelenk von", armlenkeropt, "Zentimetern optimal. Dabei muss Ihr Arm nicht vollkommen gestreckt sein bzw. Ihr Schulter nicht nach vorne gehen.")

print("\nDiese Länge kann zwischen", armlenkermin, "und", armlenkermax, "Zentimetern variieren, und je nach der Montage des Lenkers am Fahrrad, kann eine Annäherung an der optimalen Position mit einem angepassten entsprechenden Vorbau am Lenkrad erreicht werden. Dabei muss jedoch beachtet werden, dass der Vorbau nicht kürzer als 8 Zentimeter und nicht länger als 12 Zentimeter sein muss.")

print("\nWenn die Länge vom Innenchulternaht bis zum Handgelenk kleiner als", armlenkermin, "ist, dann ist der Fahrradrahmen zu groß für Sie. Wenn sie mehr als", armlenkermax, "beträgt, dann ist der Fahrradrahmen zu klein für Sie.")

print("""

                                  Bike-Fitting beendet. Viel Spass beim Fahrradfahren!


""")
