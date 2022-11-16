# Nichtlineare Optimierung [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ahudde/nonlinear_programming/HEAD)

![newplot](https://user-images.githubusercontent.com/60978072/150697749-3bf39092-d7b7-4ff3-8c2b-a50b096422bb.png)

Dieses Notebook führt in die grundlegenden Ideen der nichtlinearen Optimierung ein. Anhand von interaktiven Plots werden das Gradientenverfahren für die Optimierung, sowie das Penalty-Verfahren für die Berücksichtigung von Nebenbedingungen erklärt. 
Weiterhin wird gezeigt, wie sich nichtlineare Optimierung mit dem Python-Paket `Scipy` durchführen lässt, und es kommt noch ein Ausblick in die automatic differention mit dem Python-Paket `Autograd`.

## Zugriff über Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ahudde/nonlinear_programming/HEAD)

Sie können auf das Notebook über Binder mit dem Link [https://mybinder.org/v2/gh/ahudde/nonlinear_programming/HEAD](https://mybinder.org/v2/gh/ahudde/nonlinear_programming/HEAD) zugreifen.

## Lokale Ausführung

Man benötigt die Python-Anaconda Distribution (https://www.anaconda.com/products/individual). Zusätzlich sollte man noch die Pakete `plotly` und `autograd` installieren (`conda install plotly` und `conda install autograd` in den Anaconda-Prompt eingeben).

## Start

Laden Sie die Dateien `Matrixexponentiation.ipynb`  sowie die '.svg'-Dateien, und legen Sie diese im gleichen Ordner ab. Nun starten Sie Jupyter Notebook, z.B. indem Sie `jupyter notebook` in den Anaconda Prompt eingeben, und navigieren Sie zu der Datei.

Nun können sie die einzelnen Zellen des Notebooks ausführen und sich so in das Thema nichtlineare Optimierung einarbeiten. Viele Python-Zellen lassen sich mehrmals hintereinander ausführen, wobei jeweils ein neuer Interationsschritt gezeigt wird. Am besten probiert man das einfach aus.

Viel Spaß beim Lernen!
