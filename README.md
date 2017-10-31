# turbamap
Mapeo de la turba en redes sociales que ataca a la familia de Santiago Maldonado. Work in progress.

# Proceso
1. Se compiló un corpus de tuits que incluyeran insultos o ataques directos a los familiares de Santiago Maldonado en twitter. Esto está en el archivo corpus.txt

2. Se extrajo el nombre de los usuarios mediante regular expressions y quedó en twusers.txt

3. Se utilizó twarc(https://github.com/DocNow/twarc) por línea de comando para obtener información sobre los usuarios. Esto quedó en userinfo.jsonl en formato jsonlines.

4. Se convirtió el formato jsonlines a csv utilizando el script jsonlines2csv.py obtenido de https://gist.github.com/pmlandwehr/704f095debfc5d02b465529e83792a32 con modificaciones para soportar caracteres unicode.

5. Se ejecutó el script all_followers.py para compilar un listado de los seguidores de cada usuario, utilizando twarc como librería. Esto quedó en el archivo followers.csv que incluye un listado de id de follower, coma, nombre del usuario seguido.

6. Se ejecutó el script all_ids.py para convertir los nombres de usuarios a id de usuario y esto queda en followers_ids.csv

7. Se cargan los dagos en gephi para realizar un gráfico, pero la performance no es suficiente para lograrlo con tantos nodos. Esto queda en tw.gephi

Futuro:
* Quizás había que traer los friends y no los followers
* Probar visualizar los followers pero filtrando sólo aquellos se salgan de los ususarios del corpus
* Probar visualizar con otra herramienta
