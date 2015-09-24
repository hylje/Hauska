Miniohtuprojekti "Hauska"
---

Asenna:
===

* Python (versio 2.7). Python on valmiiksi asennettu useimmissa Linuxeissa ja Maceissa.
* Flask (http://flask.pocoo.org/docs/0.10/installation/)

Loput käytetyt jutut tulevat Pythonin mukana, tässä niiden dokumentaatio:

* Unittest (JUnitin tapainen): https://docs.python.org/2/library/unittest.html#assert-methods
* Sqlite (SQL-kanta tiedostossa): https://docs.python.org/2/library/sqlite3.html

Testaa:
===

    $ python -m unittest discover
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.010s

    OK

Käynnistä kehityssserveri:
===

    $ python run.py

Osoita selain localhost:5000 niin sovelluksen etusivun (route "/")
pitäisi näkyä.

Kehitä:
===

* Jos teet uusia .py-tiedostoja, laita niihin ekalle riville seuraava loitsu jotta ääkköset toimivat tekstissä: `# -*- encoding: utf-8 -*-`
* Tee uusille palikoille testit tests-hakemistoon. Jos teet uuden testimoduulin, sen pitää olla nimetty muodossa "test_<testinimi>.py" jotta discover löytää sen.
* Käynnistä kehitysserveri uudestaan, jotta koodimuutokset näkyvät. Kokeile toimiiko muutokset selaimessa.