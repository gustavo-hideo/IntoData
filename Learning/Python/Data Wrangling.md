# Data Wrangling | Python




## Manipulating Dates

### Getting DATE features

**add_datepart**

* Year; 
* Month;
* Week;
* Day;
* Dayofweek;
* Dayofyear;
* Is_month_end;
* Is_month_start;
* is_quarter_end;
* Is_quarter_start;
* Is_year_end;
* Is_year_start;
* Elapsed

```python
from fastai.tabular import add_datepart

add_datepart(data, 'DateColumn')
```

