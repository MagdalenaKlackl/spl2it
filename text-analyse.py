# text-analyse.py

text = "Dürr, der im Jänner in einer TV-Dokumentation über seine früheren Blutdopingpraktiken ausgesagt und damit den Fall und die „Operation Aderlass“ ins Rollen gebracht hatte, gab nach seiner Festnahme am Dienstag laut Staatsanwaltschaft zu, bis zuletzt Eigenblutdoping betrieben zu haben. Der 31-Jährige hat diesbezüglich laut der Anklagebehörde ein Geständnis abgelegt. Trotzdem wurde Dürr nach der Vernehmung noch in den späten Dienstagabendstunden wieder enthaftet, „da nach derzeitigem Ermittlungsstand nicht anzunehmen ist, dass er auf freiem Fuß die Ermittlungen beeinträchtigen würde. Der 2014 bei einem Heimaturlaub während der Olympischen Spiele in Sotschi des EPO-Dopings überführte Langläufer war am Dienstag wegen des Verdachts des Sportbetrugs in Innsbruck festgenommen worden. Die Staatsanwaltschaft verdächtigte den Langläufer, dass er nicht nur andere Sportler an einen ebenfalls festgenommenen Erfurter Sportmediziner vermittelt habe, sondern auch, dass Dürr selbst bis vor Kurzem Eigenblutdoping betrieben habe und sich dabei von ebendiesem Arzt behandeln ließ. Weil Dürr zur Finanzierung seines geplanten Comebacks Crowdfunding betrieben habe, bestehe der Verdacht des Sportbetrugs. Dass er sich mit dem Eigenblutdoping unrechtmäßig bereichert habe, bestritt der Niederösterreicher, weil er für finanzielle Unterstützungen auch jeweils entsprechende Leistungen erbracht habe. Der Verdacht des Sportbetrugs werde weiter zu prüfen sein, hieß es seitens der Staatsanwaltschaft. Die Ermittlungen seien noch nicht abgeschlossen. Für alle Genannten gilt die Unschuldsvermutung."

text = text.replace("!", ".")
text = text.replace("?", ".")

saetze = text.split(".")

print (len(saetze))
print (saetze)


