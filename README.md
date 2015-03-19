PwnChA - Captcha Breaker Demo
========

![PwnCha](http://img15.hostingpics.net/pics/205986pwncha.png)

Installation
---

1. Upload <i>website</i> folder content into your web server
2. Edit ```capcap.py``` file with correct website URL (currently targeting localhost)
3. Set ```looperBenchmark.sh``` executable with :
```Shell
chomd +x looperBenchmark.sh
```

4. Run

```Shell
./looperBenchmark
```

Output file will be override each loop with OCR result and test this result into a POST request on website as the captcha field.

Requirement
---

* [(Tesseract OCR)](https://code.google.com/p/tesseract-ocr/)
* [(Python 2.X)](https://www.python.org/downloads/)

Result
---

At this time, we managed to get <b>30%</b> of success.

Licence
---

```
This work is under the MIT License (MIT)
```
