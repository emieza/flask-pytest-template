
# Exercici Python Web

Fes una aplicació flask en un arxiu `hello.py` que contingui:

  * **/** (root) : Ha de mostrar el text **"Pràctica Python Web"**
  * **/formulari** (GET) : ha de mostrar un formulari amb un sol camp i un botó de submit. Si omplim el camp amb **"Ramona"**, quan enviem el contingut ens ha de sortir una pàgina que ens digui: **"Salut i força, Ramona"**.

Tens enunciat i pistes a:

  * https://bytes.cat/python_web
  * https://bytes.cat/python_web_test

Per desenvolupar (primer cop, després només cal el `source`):

    $ python3 -m venv env
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt

Per provar els tests:

    (env) $ pytest --driver Firefox .test

