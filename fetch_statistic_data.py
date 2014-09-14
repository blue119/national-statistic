#!/usr/bin/env python3
#  -*- coding: UTF-8 -*-

import http.cookiejar
import urllib.request
import urllib.parse
import pickle
import time
import sys
import csv
from collections import OrderedDict
from pprint import pprint
from bs4 import BeautifulSoup

class P2P101(object):

    """Docstring for P2P101. """

    def __init__(self, cj = None):
        """@todo: to be defined1. """

        def cookie_load(cjf):
            with open(cjf, 'rb') as f:
                cj = pickle.load(f)
            return cj

#  Request Headers
#  Host: ebas1.ebas.gov.tw
#  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0
#  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#  Accept-Language: en-US,en;q=0.5
#  Accept-Encoding: gzip, deflate
#  Referer: http://ebas1.ebas.gov.tw/pxweb/Dialog/..%5CDialog%5Cvarval.asp?ma=PR0102A1M&ti=%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%D3%AB~%A9%CA%BD%E8%A4%C0%C3%FE%AB%FC%BC%C6-%A4%EB&path=../PXfile/PriceStatistics/&lang=9&strList=L
#  Cookie: __utma=172213751.831462429.1409029679.1409985415.1410004061.7; __utmz=172213751.1409228409.2.2.utmcsr=dgbas.gov.tw|utmccn=(referral)|utmcmd=referral|utmcct=/point.asp; ASPSESSIONIDQQSBQABB=OHGNJLHDFPJKACGKNCEGMDME; ASPSESSIONIDSQTDSBBB=IJDFGECAFOAEDOKFIGECGFIL; ASPSESSIONIDASSCTDDD=OGDDDNMAHOKNJBEAOMIPLLII; ASPSESSIONIDQQSARDBA=DOCMFAHDNLDABGHNINKLHDMI; ASPSESSIONIDSQSASBAB=GHBAPBMAAOHEBJKDKKBLMBKM; __utmc=172213751; ASPSESSIONIDSSTDRAAB=PEDKIGBBDNNNELBLCDLJHENN; ASPSESSIONIDQSTASAAB=CDGPMKGBHLKLPGABPIAHDEDE; __utmb=172213751.21.10.1410004061
#  Connection: keep-alive
#  Cache-Control: max-age=0

        def _get_opener(cj):
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            return opener

        self.url = 'http://p2p101.com/'
        self.cj = cookie_load(cj) if cj else http.cookiejar.CookieJar()
        self.opener = _get_opener(self.cj)

    def cookie_save(self):
        t = time.strftime('%Y%m%dT%H%M')
        import IPython; IPython.embed()
        _f = '%s_cookiejar.pickle' % t
        with open(_f, 'wb') as f:
            pickle.dump(self.cj, f, pickle.HIGHEST_PROTOCOL)
        print('File save on %s' % _f)

    def open(self, url = "", soupize = True):
        url = self.url + url
        print('Fetch ' + url)
        page = self.opener.open(url).readlines()

        if not soupize: return page

        page = ''.join([p.decode() for p in page])
        return BeautifulSoup(page)

    def has_login(self):
        # fetch front-page
        sp = self.open()

        if sp.find('strong', {'class':'vwmy'}):
            return True
        else:
            return False

#  trList=L
#  var1=%B4%C1%B6%A1 #期間
#  var2=%B0%D3%AB%7E%A9%CA%BD%E8%A7O%A4%C0%C3%FE #商品性質別分類
#  var3=%BA%D8%C3%FE #種類
#  Valdavarden1=3
#  Valdavarden2=17
#  Valdavarden3=2
#  values1=1
#  values1=2
#  values1=3
#  values2=1
#  values2=2
#  values2=3
#  values2=4
#  values2=5
#  values2=6
#  values2=7
#  values2=8
#  values2=9
#  values2=10
#  values2=11
#  values2=12
#  values2=13
#  values2=14
#  values2=15
#  values2=16
#  values2=17
#  values3=1
#  values3=2

#  context1=
#  begin1=
#  context2=
#  begin2=
#  context3=
#  begin3=

#  matrix=PR0102A1M
#  root=..%2FPXfile%2FPriceStatistics%2F
#  classdir=..%2FPXfile%2FPriceStatistics%2F
#  noofvar=3
#  elim=NNN
#  numberstub=1
#  lang=9

#  varparm=ma%3DPR0102A1M%26ti%3D%25AE%25F8%25B6O%25AA%25CC%25AA%25AB%25BB%25F9%25B0%25D3%25AB%257E%25A9%25CA%25BD%25E8%25A4%25C0%25C3%25FE%25AB%25FC%25BC%25C6%25A4%25EB%26path%3D%252E%252E%252FPXfile%252FPriceStatistics%252F%26xu%3D%26yp%3D%26lang%3D9

#  消費者物價商品性質分類指數月
#  ti=%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%D3%AB%7E%A9%CA%BD%E8%A4%C0%C3%FE%AB%FC%BC%C6%A4%EB
#  infofile=
#  mapname=
#  multilang=
#  mainlang=
#  timevalvar=
#  hasAggregno=0
#  sel=%C4%7E%C4%F2
#  stubceller=3
#  headceller=34
#  pxkonv=asp1




    def login(self, user, passwd):
        params = urllib.parse.urlencode({
            'trList' : 'L', \
            'var1' : '%B4%C1%B6%A1', \
            'var2' : '%B0%D3%AB%7E%A9%CA%BD%E8%A7O%A4%C0%C3%FE', \
            'var3' : '%BA%D8%C3%FE', \
            'Valdavarden1' : '3', \
            'Valdavarden2' : '17', \
            'Valdavarden3' : '2', \
            'values1' : '1', \
            'values1' : '2', \
            'values1' : '3', \
            'values2' : '1', \
            'values2' : '2', \
            'values2' : '3', \
            'values2' : '4', \
            'values2' : '5', \
            'values2' : '6', \
            'values2' : '7', \
            'values2' : '8', \
            'values2' : '9', \
            'values2' : '10', \
            'values2' : '11', \
            'values2' : '12', \
            'values2' : '13', \
            'values2' : '14', \
            'values2' : '15', \
            'values2' : '16', \
            'values2' : '17', \
            'values3' : '1', \
            'values3' : '2', \
            'context1' : '', \
            'begin1' : '', \
            'context2' : '', \
            'begin2' : '', \
            'context3' : '', \
            'begin3' : '', \
            'matrix' : 'PR0102A1M', \
            'root' : '..%2FPXfile%2FPriceStatistics%2F', \
            'classdir' : '..%2FPXfile%2FPriceStatistics%2F', \
            'noofvar' : '3', \
            'elim' : 'NNN', \
            'numberstub' : '1', \
            'lang' : '9', \
            'ti' : '%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%D3%AB%7E%A9%CA%BD%E8%A4%C0%C3%FE%AB%FC%BC%C6%A4%EB', \
            'infofile' : '', \
            'mapname' : '', \
            'multilang' : '', \
            'mainlang' : '', \
            'timevalvar' : '', \
            'hasAggregno' : '0', \
            'sel' : '%C4%7E%C4%F2', \
            'stubceller' : '3', \
            'headceller' : '34', \
            'pxkonv' : 'asp1'})

        #  url = "member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"

        params = params.encode('utf-8')
        self.opener.open(self.url + url, params)

        #check login
        return self.has_login()

def grab_db_tree(html):
    html = html.replace('</span><ul>', '</span></li><ul>')
    page = BeautifulSoup(html)
    tree = page.find('ul', {'id':'buildtree'})

    p = tree.find('span', {'class':"rootFront"})
    print('* ' + p.string)
    p = p.findNext('span', {'class':"folder"})
    print('* ' + p.string)
    ul = p.find_next('ul')
    import IPython; IPython.embed()

    while ul:
        if len(ul.find_all('li')):
            for li in ul.find_all('li'):
                if li.span['class'][0] == 'folder': print('\t' + '* ' + li.string)
                if li.span['class'][0] == 'file': print('\t'*2 + '* ' + li.a['href'])
        else:
            t = 1
            print('* ' + ul.string)
        ul = ul.find_next_sibling()

def fetch_home():
    """
    總體統計資料庫: http://ebas1.ebas.gov.tw/pxweb/Dialog/statfile9L.asp
        臺灣地區物價統計: http://ebas1.ebas.gov.tw/pxweb/Dialog/price.asp
        國民所得及經濟成長統計資料庫: http://ebas1.ebas.gov.tw/pxweb/Dialog/NI.asp

        薪資及生產力統計查詢系統: http://win.dgbas.gov.tw/dgbas04/bc5/earning/ht456.asp
        縣市重要統計指標查詢系統: http://ebas1.ebas.gov.tw/pxweb/Dialog/statfile9.asp

    1. fetch home page
    2. grab the db tree that include name, ma, and ti value
    3. foreach leafnode
        3.1 fetch var that include column name and range
    """
    home_page = 'http://ebas1.ebas.gov.tw/pxweb/Dialog/price.asp'
    # home_page = 'http://ebas1.ebas.gov.tw/pxweb/Dialog/NI.asp'
    cj = http.cookiejar.CookieJar()

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = []
    opener.addheaders.append(('User-agent', 'Mozilla/5.0'))

    # home_page = 'http://ebas1.ebas.gov.tw/pxweb/Dialog/..%5CDialog%5Cvarval.asp?path=../PXfile/PriceStatistics/&lang=9&strList=L&'
    # home_page += urllib.parse.urlencode({ 'ma': 'PR0405A1M', 'ti': '出口物價用途別分類指數(新台幣計價)-月'.encode('big5')})
    # print(home_page)

    page = opener.open(home_page).readlines()
    page = ''.join([p.decode('big5') for p in page])
    grab_db_tree(page)

    # with open('/tmp/aaa.html', 'wb') as f:
        # f.writelines(page)




















def my_urlencode(k, v, params):
    # application/x-www-form-urlencoded format
    tmp = urllib.parse.urlencode({k:v})

    if len(params):
        params = "%s&%s" % (params, tmp)
    else:
        params = tmp
    return params

def fetch_query_table(MA, TI, PATH):
    """
    :arg1: ma
    :arg2: ti
    :arg3: path
    :return: column value as dictionary {'<var>':[value, ], }
    """

    column_values = OrderedDict()
    opener = urllib.request.build_opener()
    opener.addheaders = []
    opener.addheaders.append(('User-agent', 'Mozilla/5.0'))

    query_table_url = "http://ebas1.ebas.gov.tw/pxweb/Dialog/..%5CDialog%5Cvarval.asp?lang=9&strList=L&path=" + PATH + "&"
    query_table_url+= urllib.parse.urlencode({ 'ma': MA, 'ti': TI.encode('big5')})
    #  print(query_table_url)
    #  print(query_table_url)

    page = opener.open(query_table_url).readlines()
    page = ''.join([p.decode('big5') for p in page])
    page = BeautifulSoup(page)

    values = [ v.b.string for v in page.find_all('td', {'class', 'tdtop'}) if v.b ]

    groups = page.find_all('td', {'class', 'tdmiddle'})
    groups = [ [op.string.strip() for op in g.find_all('option')] for g in groups ]

    for i in range(len(values)):
        column_values[values[i]] = groups[i]

    opener.close()

    return column_values


def fetch_statistic_table(MA, PATH, time_range, cv):
    """
    :return: statistic table as raw html file
    """

    def _build_var_paramas(params, time_range, cv):
        """
        my_urlencode('var1', '期間'.encode('big5'), params)
        my_urlencode('var2', '基本分類暨項目群'.encode('big5'), params)
        my_urlencode('var3', '種類'.encode('big5'), params)
        my_urlencode('Valdavarden1', '1', params)
        my_urlencode('Valdavarden2', '1', params)
        my_urlencode('Valdavarden3', '1', params)
        my_urlencode('values1', '1', params)
        my_urlencode('values2', '1', params)
        my_urlencode('values3', '1', params)
        """
        c = 0
        for k in cv.keys():
            c+=1
            params = my_urlencode('var%d' % c, k.encode('big5'), params)

            key_len = len(cv[k])
            if k == '期間': key_len = time_range[1] - time_range[0] + 1

            params = my_urlencode('Valdavarden%d' % c, str(key_len), params)

            v_s = 1
            if k == '期間': v_s = time_range[0]

            for v in range(v_s, key_len+v_s):
                params = my_urlencode('values%d' % c, str(v), params)

        return params


    pxweb_url = 'http://ebas1.ebas.gov.tw/pxweb/Dialog/Saveshow.asp'
    opener = urllib.request.build_opener()
    opener.addheaders = []
    opener.addheaders.append(('User-agent', 'Mozilla/5.0'))

    params = ''
    params = my_urlencode('noofvar', str(len(cv)), params)
    params = _build_var_paramas(params, time_range, cv)

    params = my_urlencode('matrix', MA, params)
    params = my_urlencode('root', PATH, params)
    params = my_urlencode('classdir', PATH, params)
    params = my_urlencode('lang', '9', params)
    params = my_urlencode('pxkonv', 'asp1', params)

    # params = my_urlencode('ti', '消費者物價商品性質分類指數月'.encode('big5'), params)
    # params = my_urlencode('strList', 'L', params)
    # params = my_urlencode('context1', '',  params)
    # params = my_urlencode('context2', '',  params)
    # params = my_urlencode('context3', '',  params)
    # params = my_urlencode('begin1', '', params)
    # params = my_urlencode('begin2', '', params)
    # params = my_urlencode('begin3', '', params)
    # params = my_urlencode('elim', 'NNN', params)
    # params = my_urlencode('numberstub', '1', params)
    # params = my_urlencode('varparm', ccc+ddd+eee, params)
    # params = my_urlencode('infofile', '', params)
    # params = my_urlencode('mapname', '', params)
    # params = my_urlencode('multilang', '', params)
    # params = my_urlencode('mainlang', '', params)
    # params = my_urlencode('timevalvar', '', params)
    # params = my_urlencode('hasAggregno', '0', params)
    # params = my_urlencode('sel', '繼續'.encode('big5'), params)
    # params = my_urlencode('stubceller', '3', params)
    # params = my_urlencode('headceller', '34', params)

    #  print('Query: ', pxweb_url)
    #  print('Params: ', params)
    params = params.encode() # str to bytes

    #FIXME: duplicate code snippet
    page = opener.open(pxweb_url, params).readlines()

    with open('/tmp/aaa.html', 'wb') as f:
        f.writelines(page)

    return ''.join([p.decode('big5') for p in page])

def parser_statistic_table(html):
    """
    arg1: a object with readline method and html contents that got from national statistic site
    return: a list contents [[header], [content], ...]
    """
    #  print('Processing ')
    #  import IPython; IPython.embed()
    #  html = ''.join(html.readlines())

    # remove some useless tag that may inpact to parse with bs4
    #  import IPython; IPython.embed()
    html = '<table class="pxtable"' + html.split('<table class="pxtable"')[1]
    html = html.split('</blockquote>')[0]
    html = html.replace('\t', '').replace('\r', '').replace('\n', '')
    html_soup = BeautifulSoup(html)

    #  print('\tGrab header')

    #  <th class="headfirst" colspan="1" rowspan="2">&nbsp;</th>
    #  <th class="headfirst" colspan="2">期中人口(人)</th>
    #  <th class="headfirst" colspan="2"> 平均匯率(元/美元)</th>

    #  import IPython; IPython.embed()
    header_title = [ s.string.strip() for s in html_soup.findAll('th', {'class':'headfirst'})][1:]
    header_unit_num_per_unit = int(html_soup.findAll('th', {'class':'headfirst'})[-1]['colspan'])
    header_unit = [ s.string.strip() for s in html_soup.findAll('th', {'class':'headlast', 'colspan':'1'})]

    header = []
    if header_unit_num_per_unit == 1:
        header = header_title
    else:
        for title in header_title:
            c = 0
            for i in range(header_unit_num_per_unit):
                header.append("%s_%s" % (title, header_unit[c]))
                c+=1

    header.insert(0, '期間') #FIXME: fixed value?

    # contents
    #  print('\tGrab contents')
    contents = []
    a = html_soup.find('td', {"class":"stub1"})
    while a.get('class') != ["footnote"]:
        row = []
        if a.get('class') == ["stub1"]:
            row.append(a.string.strip())
            a = a.findNext('td')
            while a.get('class') != ["stub1"]:
                if a.get('class') == ["footnote"]: break
                row.append(a.string.strip())
                a = a.findNext('td')
        contents.append(row)

    contents.insert(0, header)
    return contents

def statistic_table_to_csv(stat_table, csv_fn):
    with open(csv_fn, 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        [csv_writer.writerow(row) for row in stat_table]

def parse_argv_range(column_values, RANGE):
    """
    find the index form column_values['期間']
    """
    s_t = column_values['期間'].index(RANGE[0]) + 1
    e_t = column_values['期間'].index(RANGE[1]) + 1

    return [s_t, e_t]

def build_stat_tree():
    """
    return {'MA': (TI, PATH)}
    """
    fn = 'tree_list/national_statistic_tree.txt'
    with open(fn, 'r') as f:
        f.readline()
        stat_tree = [ (i.split('\t')) for i in f.readlines() if not 'folder' in  i ]

    stat_ret = {}
    for stat in stat_tree:
        MA, TI, PATH = stat
        PATH = PATH.replace('\n', '')
        stat_ret[MA] = (TI, PATH)

    return stat_ret

def main(MA, TI, PATH, RANGE, opt = None):
    """@todo: Docstring for main.

    :arg1: ma
    :arg2: ti
    :arg3: path
    :arg4: range
    :returns: @todo

    """
    #  print(MA, TI, PATH, RANGE)
    column_values = fetch_query_table(MA, TI, PATH)
    if opt == '--show-query-range':
        print('\n'.join(column_values['期間']))
        return

    if opt == '--show-query-tables':
        print(column_values)
        return

    time_range = parse_argv_range(column_values, RANGE)

    statistic_table_html = fetch_statistic_table(MA, PATH, time_range, column_values)
    #  print(column_values)

    stat_table = parser_statistic_table(statistic_table_html)
    #  print(stat_table)
    statistic_table_to_csv(stat_table, "tree_list/csv_bucket/%s_%s_%s_%s.csv" % (MA, TI, RANGE[0], RANGE[1]))

def usage():
    print("%s <ma> <rang>" % sys.argv[0])
    print("")
    print("\t%s NA0101A1A 1979" % sys.argv[0])
    print("\t%s NA0101A1A 1980-1990" % sys.argv[0])
    print("")
    print("\t%s --show-tree" % sys.argv[0])
    print("\t%s --show-query-tables <ma>" % sys.argv[0])
    print("\t%s --show-query-range <ma>" % sys.argv[0])
    sys.exit(-1)

if __name__ == '__main__':
    argv = sys.argv

    if len(argv) < 2: usage()

    stat_tree = build_stat_tree()
    if argv[1] == '--show-tree':
        show_tree = []
        for k in stat_tree:
            show_tree.append((k, stat_tree[k][0]))

        show_tree = sorted(show_tree)
        for i in show_tree:
            print('\t'.join(i))
        sys.exit(0)

    if len(argv) < 3: usage()

    MA = argv[1]

    opt = None
    if argv[1] == '--show-query-range':
        opt = '--show-query-range'
        MA = argv[2]

    if argv[1] == '--show-query-tables':
        opt = '--show-query-tables'
        MA = argv[2]

    TI = stat_tree[MA][0]
    PATH = stat_tree[MA][1]
    RANGE = argv[2].split('-') if '-' in argv[2] else [argv[2], argv[2]]
    main(MA, TI, PATH, RANGE, opt)

