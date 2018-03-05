# House CRUD Test

## Overview

This test is for a simple Django CRUD views to add, edit and display Houses.

UI mockup is in [crud-test.html](crud-test.html).

Just implement as much functionality as you can in a time-box of 2 hours focusing fist on quality rather than quantity.

There're a lot of requirements so you're not expected to complete all of them, implement what you can and do it well,
And don't leave half implemented code and functionality, remove anything that's not completely finished in the final result.

At least the fist function (Add House) has to be implemented perfectly from every perspective (function, logic, code quality, tests, UX).

## Functionality to implement (in order of priority)

### 1. Add House view

![](https://www.evernote.com/l/AHR6kVOimNhEAptuqzsASeKXsCVHHXON5VwB/image.png)

It should be with languages as inline formset where languages can be added/removed in the list.

![](https://www.evernote.com/l/AHSY8s1byANBk7YjdpsjcLT9dkai28MYDcwB/image.png)

Fields:

* Community
    - Required
* Room Count
    - Required
    - Widget: horizontal radio buttons
* Phone number
    - Length: 11
    - Only numbers allowed
* Tags
    - Required: at least one tag should be added
    - Widget: Inline formset
* Price
    - Only numbers allowed, from 0 to 99999
* Date
    - Required
    - Widget: Datepicker
* Professional
    - Required
    - Widget: horizontal radio buttons

### 2. House List view

![](https://www.evernote.com/l/AHRlRb8RWsxI4ZfsCMdDawIptRNdWTCOtD0B/image.png)

### 3. Edit House view

Same as add

### 4. House Detail view

![](https://www.evernote.com/l/AHSPFjRgvBROzamFG2_cvifetmFCZ-6CTgoB/image.png)

### 5. Delete House

![](https://www.evernote.com/l/AHTpOW13eelOX44ZWOaG8psPjLFeGKvKUvYB/image.png)

### 6. Pagination

![](https://www.evernote.com/l/AHQPkBVV1X5DaaiUWL0TaQTHeU6DyIzbuqsB/image.png)

### 7. Batch Delete

![](https://www.evernote.com/l/AHSsX1ZWe5hC2piuYM7Yk5rQJGBkwTujGNcB/image.png)

## Project setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run django server:

```
./manage.py runserver
```

3. Open http://localhost:8000/ in a browser

## Good Luck!
