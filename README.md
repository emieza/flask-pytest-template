# Exercici Python Web

Fes una aplicació flask en un arxiu `hello.py` que contingui:

  * **/** (root) : Ha de mostrar el text **"Pràctica Flask"**
  * **/formulari** (GET) : ha de mostrar un formulari amb un sol camp i un botó de submit. Si omplim el camp amb **"Ramona"**, quan enviem el contingut ens ha de sortir una pàgina que ens digui: **"Salut i força, Ramona"**.

Tens enunciat i pistes a:

  * https://bytes.cat/python_web
  * https://bytes.cat/python_web_test

Per a inicialitzar:

    $ python3 -m venv env
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt

Per a desenvolupar, crear arxiu `hello.py` i fer:

    $ source env/bin/activate
    (env) flask --app hello run

Per als tests ens caldrà disposar de Chrome o bé de Firefox-ESR (el Firefox-snap que ve amb Ubuntu no funciona):

    # snap remove firefox
    # apt install software-properties-common -y
    # add-apt-repository ppa:mozillateam/ppa
    # apt install firefox-esr

Per a provar els tests:

    (env) $ pytest --driver Firefox .test

