import csv
import requests
from lxml import html
import re


def write_to_csv(filename, arrays):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(arrays)


def clean_date(item):
    try:
        return re.sub(r'\xa0', u'', item)
    except TypeError:
        pass


class Day(object):
    """parse data from day page"""

    def __init__(self):
        super(Day, self).__init__()
        self.url = 'http://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'
        self.filename = 'day.csv'
        self.site = requests.get(self.url)
        self.body = html.fromstring(self.site.content)

    def parse_data(self):
        trs = self.body.xpath('//table[@summary]//tr')[1:]
        all_data = []
        for tr in trs:
            date = self.clean_empty(tr.xpath('.//td[1]/text()'))
            date = self.clean_date(date)
            mon = self.clean_empty(tr.xpath('./td[2]/text()'))
            tue = self.clean_empty(tr.xpath('./td[3]/text()'))
            wed = self.clean_empty(tr.xpath('./td[4]/text()'))
            thu = self.clean_empty(tr.xpath('./td[5]/text()'))
            fri = self.clean_empty(tr.xpath('./td[6]/text()'))

            data = [date, mon, tue, wed, thu, fri]
            all_data.append(data)

        all_data = [array for array in all_data if array[0]]
        write_to_csv(self.filename, all_data)

    def clean_empty(self, elem):
        if len(elem) > 0:
            return elem[0]

    def clean_date(self, item):
        try:
            return re.sub(r'\xa0', u'', item)
        except TypeError:
            pass

    def main(self):
        self.parse_data()


class Week(object):
    '''parse data from week page'''

    def __init__(self):
        super(Week, self).__init__()
        self.url = 'http://www.eia.gov/dnav/ng/hist/rngwhhdW.htm'
        self.filename = 'week.csv'
        self.site = requests.get(self.url)
        self.body = html.fromstring(self.site.content)

    def clean_empty(self, elem):
        if len(elem) > 0:
            return elem[0]

    def parse_data(self):
        trs = self.body.xpath('//table[@width="675"][@border="0"][@cellspacing="1"]//tr')[2:]
        all_data = []
        for tr in trs:
            week_of = self.clean_empty(tr.xpath('.//td[1]/text()'))
            week1_end = self.clean_empty(tr.xpath('./td[2]/text()'))
            week1_value = self.clean_empty(tr.xpath('./td[3]/text()'))
            week2_end = self.clean_empty(tr.xpath('./td[4]/text()'))
            week2_value = self.clean_empty(tr.xpath('./td[5]/text()'))
            week3_end = self.clean_empty(tr.xpath('./td[6]/text()'))
            week3_value = self.clean_empty(tr.xpath('./td[7]/text()'))
            week4_end = self.clean_empty(tr.xpath('./td[8]/text()'))
            week4_value = self.clean_empty(tr.xpath('./td[9]/text()'))
            week5_end = self.clean_empty(tr.xpath('./td[10]/text()'))
            week5_value = self.clean_empty(tr.xpath('./td[11]/text()'))

            data = [week_of, week1_end, week1_value, week2_end, week2_value, week3_end, week3_value,
                    week4_end, week4_value, week5_end, week5_value]
            data = [clean_date(item) for item in data]

            all_data.append(data)

        all_data = [data for data in all_data if data[0]]

        write_to_csv(self.filename, all_data)

    def main(self):
        self.parse_data()


class Month(object):
    """parse data from day page"""

    def __init__(self):
        super(Month, self).__init__()
        self.url = 'http://www.eia.gov/dnav/ng/hist/rngwhhdM.htm'
        self.filename = 'month.csv'
        self.site = requests.get(self.url)
        self.body = html.fromstring(self.site.content)

    def parse_data(self):
        trs = self.body.xpath('//table[@cellpadding="2"]/tr')[1:]
        all_data = []
        for tr in trs:
            date = self.clean_empty(tr.xpath('.//td[1]/text()'))
            jan = self.clean_empty(tr.xpath('./td[2]/text()'))
            feb = self.clean_empty(tr.xpath('./td[3]/text()'))
            mar = self.clean_empty(tr.xpath('./td[4]/text()'))
            apr = self.clean_empty(tr.xpath('./td[5]/text()'))
            may = self.clean_empty(tr.xpath('./td[6]/text()'))
            jun = self.clean_empty(tr.xpath('./td[7]/text()'))
            jul = self.clean_empty(tr.xpath('./td[8]/text()'))
            aug = self.clean_empty(tr.xpath('./td[9]/text()'))
            sep = self.clean_empty(tr.xpath('./td[10]/text()'))
            oct = self.clean_empty(tr.xpath('./td[11]/text()'))
            nov = self.clean_empty(tr.xpath('./td[12]/text()'))
            dec = self.clean_empty(tr.xpath('./td[13]/text()'))

            data = [date, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
            data = [clean_date(item) for item in data]

            all_data.append(data)

        all_data = [array for array in all_data if array[0]]
        write_to_csv(self.filename, all_data)

    def clean_empty(self, elem):
        if len(elem) > 0:
            return elem[0]

    def main(self):
        self.parse_data()


if __name__ == '__main__':
    day = Day()
    day.main()
    week = Week()
    week.main()
    month = Month()
    month.main()