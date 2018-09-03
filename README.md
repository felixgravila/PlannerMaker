# PDF PLANNER MAKER

Makes a monthly planner PDF based on template month, week and day pages as follows:
* First page is the monthly overview
* Each day has an instance of the day page
* Week page between Sunday and Monday

## Getting Started

Sourcing the PDF templates is an exercise left to the reader. I have personally used the free to download template by [pandaplanner](https://pandaplanner.com/).

## Setting up

### Dependencies
* PyPDF2
* pandas

Move the three created template files inside the folder under the following names:
* month.pdf
* week.pdf
* day.pdf

## Running

Default using python3

`./makeplanner.py [year:[2018-2100]] [month:[1-12]] [filename:string?]`

or

`python makeplanner.py [year:[2018-2100]] [month:[1-12]] [filename:string?]`

### Example

```
$ ./makeplanner.py 2018 9
Wrote Planner-September-2018.pdf
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
