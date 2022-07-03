# Code Writing by Mohamed Amine Guedria
# Guedria.amine@gmail.com
# This code save the frequency and Effective Voltage(Vrms)  datensreading from a microphone and  a .wav-file in Excel table


import xlsxwriter


class Datei(object):

    def excel2(list1, list2, pos1):  # Excel table Effective Voltage

        x = 1
        y = 1

        workbook = xlsxwriter.Workbook("Voltage.xlsx")  # create an Excel table
        worksheet2 = workbook.add_worksheet("Vrms")  # create worksheet in Excel
        worksheet2.write(0, 24, "WV_Vrms")  # Write title in coordinate(x,y)
        worksheet2.write(0, pos1, "MICRO_Vrms")  # Write title in coordinate(x,y)
        chart2 = workbook.add_chart({'type': 'line'})  # create a graphic type line
        # -------------------- write the dates in Excel ---------------------------#
        for i in list1:
            worksheet2.write(x, 24, i)
            x += 1

        for i in list2:
            if (i == 0000):
                pos1 += 1
                y = 1
                worksheet2.write(0, pos1, "MICRO_Vrms")
                worksheet2.write(y, pos1, "Pause")

            else:
                worksheet2.write(y, pos1, i)
                y += 1
        # -------------------- graphic setups ---------------------------#
        chart2.add_series({'values': '=Vrms!$B$1:$B$1000', 'name': 'WAV File Vrms '})
        chart2.add_series({'values': '=Vrms!$A$1:$A$1000', 'name': 'Micro Frequency '})
        chart2.add_series({'values': '=Vrms!$C$1:$C$1000', 'name': 'Micro Frequency '})

        chart2.add_series({'values': '=Vrms!$X$1:$X$1000', 'name': 'MICRO Vrms'})
        chart2.set_x_axis({
            'date_axis': True,
            'min': 1,
            'max': len(list1) * 2,
        })
        chart2.set_y_axis({'name': 'Vrms.xlsx'})
        chart2.set_legend({'position': 'top'})
        worksheet2.insert_chart('O1', chart2)
        # -------------------- write Maximum in Excel ---------------------------#

        worksheet2.write(17, 5, "=MAX(A1:A10000)")
        worksheet2.write(18, 5, "=MAX(B1:B10000)")
        worksheet2.write(19, 5, "DEFF")
        worksheet2.write(19, 6, "=D3-D2")

        workbook.close()

    def excel1(liste, wavliste, frqlist):  # Excel table Effective Voltage

        cot = 1
        coott = 0

        workbook = xlsxwriter.Workbook('Frequenz.xlsx')  # create an Excel table
        worksheet = workbook.add_worksheet("FREQ")  # create worksheet in Excel
        chart = workbook.add_chart({'type': 'line'})  # create a graphic type line

        # -------------------- write the dates in Excel ---------------------------#
        worksheet.write(0, coott, "frequency")
        for i in liste:
            if (i == 0000):
                coott += 1
                cot = 1
                worksheet.write(0, coott, "frequency")
                worksheet.write(cot, coott, "Pause")

            else:
                worksheet.write(cot, coott, i)
                cot += 1

        x = 1
        y = 24
        worksheet.write(0, 24, "frequency wav")

        for i in wavliste:
            if (i == 0000):
                y += 1
                x = 1
                worksheet.write(0, y, ".wav Frequency")
                worksheet.write(x, y, i)
            else:
                worksheet.write(x, y, i)
                x += 1
        cot2 = 1
        for i in frqlist:
            aa = int(i)
            worksheet.write(cot2, 37, aa)
            cot2 += 1
        # ----------- get the Median ------------------#
        worksheet.write(0, 23, "Median MICRO")
        worksheet.write(2, 23, "=Median(B2:B100)", )
        worksheet.write(3, 23, "=Median(C2:C100)", )
        worksheet.write(4, 23, "=Median(D2:D100)", )
        worksheet.write(5, 23, "=Median(E2:E100)", )
        worksheet.write(6, 23, "=Median(F2:F100)", )
        worksheet.write(7, 23, "=Median(G2:G100)", )
        worksheet.write(8, 23, "=Median(H2:H100)", )
        worksheet.write(9, 23, "=Median(I2:I100)", )
        worksheet.write(10, 23, "=Median(J2:J100)", )
        worksheet.write(11, 23, "=Median(K2:K100)", )
        worksheet.write(12, 23, "=Median(L2:L100)", )
        worksheet.write(1, 23, "=Median(A2:A100)", )

        worksheet.write(0, 22, "Median WAV")
        worksheet.write(2, 22, "=Median(Z2:Z100)", )
        worksheet.write(3, 22, "=Median(AA2:AA100)", )
        worksheet.write(4, 22, "=Median(AB2:AB100)", )
        worksheet.write(5, 22, "=Median(AC2:AC100)", )
        worksheet.write(6, 22, "=Median(AD2:AD100)", )
        worksheet.write(7, 22, "=Median(AE2:AE100)", )
        worksheet.write(8, 22, "=Median(AF2:AF100)", )
        worksheet.write(9, 22, "=Median(AG2:AG100)", )
        worksheet.write(10, 22, "=Median(AH2:AH100)", )
        worksheet.write(11, 22, "=Median(AI2:AI100)", )
        worksheet.write(12, 22, "=Median(AJ2:AJ100)", )
        worksheet.write(1, 22, "=Median(Y2:Y100)", )
        # -------------------- graphic setups ---------------------------#
        chart.add_series({'name': 'Aufgenommenen Frequenzen ',
                          'categories': "='FREQ'!AL2:AL13",
                          'values': "='FREQ'!X2:X13"})
        chart.add_series({'name': '.wav Frequenzen',
                          'categories': "='FREQ'!AL2:AL13",
                          'values': "='FREQ'!W2:W13"})

        chart.set_title({'name': 'Frequenzenvergleich'})
        chart.set_y_axis({'name': 'Frequency in HZ',
                          'major_gridlines': {'visible': True}
                          })
        chart.set_x_axis({'name': 'Frequency in HZ',
                          'major_gridlines': {'visible': True}
                          })

        worksheet.insert_chart('O1', chart)

        workbook.close()

    def excel3(frqliste, voltageliste, s, n):
        # name of excel depend on the test type
        if (n == 1):
            name = 'Micro_Messung.xlsx'
        elif (n == 2):
            name = 'Stethoskop_Messung.xlsx'
        elif (n == 3):
            name = 'Box_Messung.xlsx'

        option = {
            20: 1,
            50: 2,
            100: 3,
            200: 4,
            300: 5,
            400: 6,
            500: 7,
            1000: 8,
            1500: 9,
            2000: 10,
            2500: 11,
            3000: 12
        }

        cot = 0
        cot2 = 0
        coott = 0

        workbook = xlsxwriter.Workbook(name)  # create an Excel table
        worksheet = workbook.add_worksheet("test")  # create a work sheet

        chart = workbook.add_chart({'type': 'line'})  # create graphic type line

        worksheet.write(0, coott, "frequency(1)")
        worksheet.write(1, coott, "Voltage(1)")
        # -------------------- write the dates in Excel ---------------------------#

        for i in frqliste:
            ii = int(i)
            worksheet.write(cot, coott + 1, ii)

            worksheet.write(cot2, 24, ii)
            cot2 += 1
            coott += 1

        x = 1
        ss = int(s)
        y = option[ss]
        # ----------- write the dates in the suitable position ------------------#
        for i in voltageliste:
            if (i == 20):
                voltageliste.remove(20)
                x = 1
                y = 1
                worksheet.write(x, y, i)


            elif (i == 50):
                voltageliste.remove(50)
                x = 1
                y = 2
                worksheet.write(x, y, i)

            elif (i == 100):
                voltageliste.remove(100)
                x = 1
                y = 3
                worksheet.write(x, y, i)


            elif (i == 200):
                voltageliste.remove(200)
                x = 1
                y = 4
                worksheet.write(x, y, i)


            elif (i == 300):
                voltageliste.remove(300)
                x = 1
                y = 5
                worksheet.write(x, y, i)


            elif (i == 400):
                voltageliste.remove(400)
                x = 1
                y = 6
                worksheet.write(x, y, i)


            elif (i == 500):
                voltageliste.remove(500)
                x = 1
                y = 7
                worksheet.write(x, y, i)


            elif (i == 1000):
                voltageliste.remove(1000)
                x = 1
                y = 8
                worksheet.write(x, y, i)


            elif (i == 1500):
                voltageliste.remove(1500)
                x = 1
                y = 9
                worksheet.write(x, y, i)


            elif (i == 2000):
                voltageliste.remove(2000)
                x = 1
                y = 10
                worksheet.write(x, y, i)


            elif (i == 2500):
                voltageliste.remove(2500)
                x = 1
                y = 11
                worksheet.write(x, y, i)


            elif (i == 3000):
                voltageliste.remove(3000)
                x = 1
                y = 12
                worksheet.write(x, y, i)



            else:
                worksheet.write(x, y, i)
                x += 1
            # ----------- get the Median ------------------#
            worksheet.write(0, 23, "=Median(B2:B100)", )
            worksheet.write(1, 23, "=Median(C2:C100)", )
            worksheet.write(2, 23, "=Median(D2:D100)", )
            worksheet.write(3, 23, "=Median(E2:E100)", )
            worksheet.write(4, 23, "=Median(F2:F100)", )
            worksheet.write(5, 23, "=Median(G2:G100)", )
            worksheet.write(6, 23, "=Median(H2:H100)", )
            worksheet.write(7, 23, "=Median(I2:I100)", )
            worksheet.write(8, 23, "=Median(J2:J100)", )
            worksheet.write(9, 23, "=Median(K2:K100)", )
            worksheet.write(10, 23, "=Median(L2:L100)", )
            worksheet.write(11, 23, "=Median(M2:M100)", )
        # -------------------- graphic setups ---------------------------#
        chart.add_series({
            'name': 'FFT',
            'categories': "='test'!B1:M1",
            'values': "='test'!X1:X12",
            'marker': {
                'type': 'square', 'size': 5,
                'border': {'color': 'black'},
                'fill': {'color': 'red'}, },

        })

        chart.set_x_axis({'name': 'Frequenz[Hz]',
                          'major_gridlines': {'visible': True}
                          })
        chart.set_y_axis({'name': 'Amplitude[V]',
                          'major_gridlines': {'visible': True}
                          })

        worksheet.insert_chart('O6', chart)

        workbook.close()
