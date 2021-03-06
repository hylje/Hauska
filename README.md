Miniohtuprojekti "Hauska"
===

[![Build Status](https://travis-ci.org/hylje/Hauska.svg?branch=master)](https://travis-ci.org/hylje/Hauska)

[![Coverage Status](https://coveralls.io/repos/hylje/Hauska/badge.svg?branch=master&service=github)](https://coveralls.io/github/hylje/Hauska?branch=master)

[Projektin Trello-lauta](https://trello.com/b/RsZjXJTB/hauska-ryhma)

[Miniohtu-raportti](https://drive.google.com/file/d/0B_b_5sryDhjubTRhUTRRdmFkaGs/view) [PDF]

Asenna:
---

* Python (versio 2.7). Python on valmiiksi asennettu useimmissa Linuxeissa ja Maceissa.
* Flask (http://flask.pocoo.org/docs/0.10/installation/)
* WTForms

Loput käytetyt jutut tulevat Pythonin mukana, tässä niiden dokumentaatio:

* Unittest (JUnitin tapainen): https://docs.python.org/2/library/unittest.html#assert-methods
* Sqlite (SQL-kanta tiedostossa): https://docs.python.org/2/library/sqlite3.html

Testaa:
---

    $ python -m unittest discover
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.010s

    OK

Käynnistä kehityssserveri:
---

    $ python run.py

Osoita selain localhost:5000 niin sovelluksen etusivun (route "/")
pitäisi näkyä.

Kehitä:
---

* Jos teet uusia .py-tiedostoja, laita niihin ekalle riville seuraava loitsu jotta ääkköset toimivat tekstissä: `# -*- encoding: utf-8 -*-`
* Tee uusille palikoille testit tests-hakemistoon. Jos teet uuden testimoduulin, sen pitää olla nimetty muodossa "test_*\<testinimi\>*.py" jotta discover löytää sen.
* Käynnistä kehitysserveri uudestaan, jotta koodimuutokset näkyvät. Kokeile toimiiko muutokset selaimessa.
* Valmiit muutokset omaan branchiin ja pull requestilla masteriin. Travis tsekkaa menevätkö testit vielä läpi.