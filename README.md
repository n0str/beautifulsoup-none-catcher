# Monads for beautifulsoup

It allows you to catch errors in one line and get rid of annoying 'NoneType' object is not callable.

### Why

Some people have 'NoneType' issues while scraping a website where each tag can have or have not contents. This is quite dummy example, however it is illustrative.
```
<div class="article"><div>Author is John</div><p>Article #1</p></div>
<div class="article"><div>Author is John<span>and Amy</span></div><p>Article #2</p></div>
<div class="article"><p>Article #3</p></div>
```
There are could be zero, one or two authors for each article.
How to parse it?
```
for article in soup.find_all("div", {"class": "article"}):
    print("Article: ", article.text)
    print("Author #1: ", article.find("div").text)
    print("Author #2: ", article.find("div").find("span").text)
```
If we run this example, we will get `AttributeError: 'NoneType' object has no attribute 'text'`

There several workarounds.
1. Use xpath. `Sometimes it is not an option, because query can be too ugly in code`
2. Use if/else. `It is ugly!`
```
    a1 = article.find("div")
    if a1:
        print("Author #1: ", a1.text)
        a2 = a1.find("span")
        if a2:
            print("Author #2: ", a2.text)
```
3. Use try/except `It is ugly!`
```
    try:
        print("Author #1: ", article.find("div").text)
        print("Author #2: ", article.find("div").find("span").text)
    except:
        pass
```
We usually have to understand where the error is and it can eventually become like this
```
try:
    ...
except:
    ...
try:
    ...
except:
    ...
try:
    ...
except:
    ...
```

## Solution

Simple and awesome. Just wrap your soup in **Maybe()**.
```
from maybe import Maybe
for article in soup.find_all("div", {"class": "article"}):
    print("Article: ", article.text)
    print("Author #1: ", Maybe(article).find("div").text)
    print("Author #2: ", Maybe(article).find("div").find("span").text)
```

Result:
```
Article:  Author is JohnArticle #1
Author #1:  Author is John
Author #2:  None
Article:  Author is Johnand AmyArticle #2
Author #1:  Author is Johnand Amy
Author #2:  and Amy
Article:  Article #3
Author #1:  None
Author #2:  None
```

You can even do this in one line and it return result or None without exceptions:
```
Maybe(soup).find('div').find('span').find('p').find('a').text
```

## Installation

```
pip install
```
