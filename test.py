#!/usr/bin/env python
import xlrd

def parser():
    parserdata = xlrd.open_workbook('test.xls', encoding_override='cp1252')
    worksheet = parserdata.sheet_by_index(0)
    dat = []
    for rownum in range(worksheet.nrows):
        row = worksheet.row_values(rownum)
        j = 0
        dat.append([])
        for element in row:
            # ID (0)
            if (j == 0):
                dat[rownum].append(element)
            # Name (1)
            if (j == 4):
                dat[rownum].append(element)
            # Price (2)
            if (j == 5):
                dat[rownum].append(element)
            # Old Price (3)
            if (j == 6):
                dat[rownum].append(element)
            # Quantity (4)
            if (j == 7):
                dat[rownum].append(element)
            # Image link (5)
            if (j == 19):
                dat[rownum].append(element)
            j += 1
    return dat


def table(dat):
    tableHtml = "<table border=1 cellpadding=15 ><tr>"

    j = 0
    for tab in dat:
        if j == 0:
            tableHtml = tableHtml + "<th>" + "Изображение" + "</th>" + "<th>" + tab[1] + "</th>" + "<th>" + tab[0] + "</th>" + "<th>" + tab[4] + "</th>" + "<th>" + tab[2] + "</th>" + "<th>" + tab[3] + "</th>"
            j += 1
            tableHtml = tableHtml + "</tr><tr>"
            continue

        tableHtml = tableHtml + "<td>" + "<img src='" + tab[5] + "' style='width: 40; height: 60'>" + "</td>" + "<td>" + tab[1] + "</td>" + "<td>" + str(tab[0]) + "</td>" + "<td>" + str(tab[4]) + "</td>" + "<td>" + str(tab[2]) + "</td>" + "<td>" + str(tab[3]) + "</td>"
        j += 1
        tableHtml = tableHtml + "</tr><tr>"

    tableHtml = tableHtml + "</tr></table>"

    return tableHtml

dat = parser()
table(dat)


