import csv
import copy
import os

from smartva.loggers import status_logger
from smartva.symptom_conversions import child_conversionVars
from smartva.utils import status_notifier

# variables generated by this step of the procedure
generatedHeaders = ['s2991', 's2992', 's2993', 's2994', 's2995', 's5991', 's6991', 's8991', 's8992', 's11991', 's13991',
                    's16991', 's30991', 's113991', 's114991', 's116991', 's135991', 's139991', 's141991', 'real_age',
                    'real_gender']

durationSymptoms = ['s2', 's9', 's14', 's28', 's29', 's31', 's111', 's117', 's119', 's122', 's126', 's128', 's142',
                    's146']

durCutoffs = {'s2': 2, 's9': 1000, 's14': 1000, 's28': 270, 's29': 8, 's31': 300, 's111': 5, 's117': 3, 's119': 2,
              's122': 7, 's126': 3, 's128': 3, 's142': 5, 's146': 3.5}

injuries = ['s155', 's156', 's157', 's158', 's159', 's160', 's161', 's162', 's163', 's165']

binaryVars = ['s7', 's17', 's18', 's19', 's110', 's112', 's115', 's118', 's120', 's121', 's123', 's124', 's125', 's127',
              's129', 's130', 's131', 's132', 's133', 's134', 's136', 's137', 's138', 's143', 's144', 's145', 's147',
              's148', 's149', 's150', 's151', 's152', 's153', 's154', 's155', 's156', 's157', 's158', 's159', 's160',
              's161', 's162', 's163', 's164', 's165', 's188', 's189', 's190']


class ChildSymptomPrep(object):
    def __init__(self, input_file, output_dir, shortform):
        self.inputFilePath = input_file
        self.output_dir = output_dir
        self.want_abort = 0
        self.shortform = shortform

    def run(self):
        status_notifier.update({'progress': (8,)})

        reader = csv.reader(open(self.inputFilePath, 'rb'))
        adultwriter = csv.writer(open(self.output_dir + os.sep + 'child-symptom.csv', 'wb', buffering=0))

        status_logger.info('Child :: Processing symptom data')

        matrix = list()
        headers = list()

        first = 1
        # read in new .csv for processing
        # we add the generated headers later this time
        for row in reader:
            if first == 1:
                for col in row:
                    headers.append(col)
                first = 0
            else:
                matrix.append(row)

        # Add svars for text
        keys = child_conversionVars.keys()
        keys.extend(['s99991', 's999910', 's999911', 's999912', 's999913', 's999914', 's999915', 's999916', 's999917',
                     's999918', 's999919', 's99992', 's999920', 's999921', 's999922', 's999923', 's999924', 's999925',
                     's999926', 's999927', 's999928', 's999929', 's99993', 's999930', 's999931', 's999932', 's999933',
                     's999934', 's999935', 's999936', 's999937', 's999938', 's999939', 's99994', 's999940', 's999941',
                     's999942', 's999943', 's999944', 's999945', 's999946', 's999947', 's999948', 's999949', 's99995',
                     's99996', 's99997', 's99998', 's99999'])
        headers_copy = copy.deepcopy(headers)
        for col in headers_copy:
            if col not in keys:
                index = headers.index(col)
                for row in matrix:
                    del row[index]
                headers.remove(col)

        # now convert variable names
        for i, header in enumerate(headers):
            try:
                headers[i] = child_conversionVars[header]
            except KeyError:
                pass

        # add new variables and create space for them in the matrix
        for gen in generatedHeaders:
            headers.append(gen)
            for row in matrix:
                row.append("0")

        # new stuffs
        for row in matrix:
            s2 = row[headers.index('s2')]
            if s2 == '' or s2 == str(999):
                row[headers.index('s2')] = 0
                s2 = 0

            s3 = row[headers.index('s3')]
            if s3 == '' or s3 == str(99):
                row[headers.index('s3')] = 0
                s3 = 0
            s4 = row[headers.index('s4')]
            if s4 == '' or s4 == str(99):
                row[headers.index('s4')] = 0
                s4 = 0

            # months
            s3 = float(s3) / 12
            # days
            s4 = float(s4) / 365
            # combine
            s2 = float(s2) + s3 + s4
            row[headers.index('s2')] = float(s2)

            index = headers.index('s2')
            s2991index = headers.index('s2991')
            s2992index = headers.index('s2992')
            s2993index = headers.index('s2993')
            s2994index = headers.index('s2994')
            s2995index = headers.index('s2995')

            #            if row[headers.index('sid')] == '9':
            #                print "s2 num %s" % float(row[index])

            if float(row[index]) <= .4166667:
                row[s2991index] = 1
            elif float(row[index]) > .4166667 and float(row[index]) <= 1:
                row[s2992index] = 1
            elif float(row[index]) > 1 and float(row[index]) <= 3:
                row[s2993index] = 1
            elif float(row[index]) > 3 and float(row[index]) <= 7:
                row[s2994index] = 1
            elif float(row[index]) > 7:
                row[s2995index] = 1

            # change sex from female = 2, male = 1 to female = 1, male = 0
            # if unkonwn sex will default to 0 so it does not factor into analysis
            index = headers.index('sex')
            val = int(row[index])
            if val == 2:
                row[index] = 1
            elif val == 1:
                row[index] = 0
            elif val == 9:
                row[index] = 0

            # make new variables to store the real age and gender, but do it after we've modified the sex
            # vars from 2, 1 to 1, 0
            ageindex = headers.index('real_age')
            genderindex = headers.index('real_gender')
            row[ageindex] = row[headers.index('s2')]
            row[genderindex] = row[headers.index('sex')]

            for sym in durationSymptoms:
                index = headers.index(sym)
                # replace the duration with 1000 if it is over 1000 and not missing
                if row[index] == '':
                    row[index] = 0
                elif float(row[index]) > 1000:
                    row[index] = 1000
                # use cutoffs to determine if they will be replaced with a 1 (were above or equal to the cutoff)
                if float(row[index]) >= durCutoffs[sym]:
                    row[index] = 1
                else:
                    row[index] = 0

            # The "varlist" variables in the loop below are all indicators for different questions about injuries (road traffic, fall, fires)
            # We only want to give a VA a "1"/yes response for that question if the injury occured within 10 days of death (i.e. s166<=10)
            # Otherwise, we could have people who responded that they were in a car accident 20 years prior to death be assigned to road traffic deaths

            if not self.shortform:
                for injury in injuries:
                    index = headers.index(injury)
                    injury_cut_index = headers.index('s166')
                    # 30 is the injury cutoff
                    if float(row[injury_cut_index]) > 10:
                        row[index] = 0

            # dichotomize!
            index = headers.index('s5991')
            val = row[headers.index('s5')]
            if val == '':
                val = '0'
            if val == '2':
                row[index] = '1'

            index = headers.index('s6991')
            val = row[headers.index('s6')]
            if val == '':
                val = '0'
            if val == '2' or val == '3':
                row[index] = '1'

            index1 = headers.index('s8991')
            index2 = headers.index('s8992')
            val = row[headers.index('s8')]
            if val == '':
                val = '0'
            if val == '1':
                row[index1] = '1'
            elif val == '2':
                row[index2] = '1'

            index = headers.index('s11991')
            val = row[headers.index('s11')]
            if val == '':
                val = '0'
            if val == '4' or val == '5':
                row[index] = '1'

            index = headers.index('s13991')
            val = row[headers.index('s13')]
            if val == '':
                val = '0'
            if val == '1' or val == '2':
                row[index] = '1'

            index = headers.index('s16991')
            val = row[headers.index('s16')]
            if val == '':
                val = '0'
            if val == '2':
                row[index] = '1'

            index = headers.index('s30991')
            val = row[headers.index('s30')]
            if val == '':
                val = '0'
            if val == '3' or val == '4':
                row[index] = '1'

            index = headers.index('s113991')
            val = row[headers.index('s113')]
            if val == '':
                val = '0'
            if val == '3':
                row[index] = '1'

            index = headers.index('s114991')
            val = row[headers.index('s114')]
            if val == '':
                val = '0'
            if val == '3' or val == '2':
                row[index] = '1'

            index = headers.index('s116991')
            val = row[headers.index('s116')]
            if val == '':
                val = '0'
            if val > '2':
                row[index] = '1'

            index = headers.index('s135991')
            val = row[headers.index('s135')]
            if val == '':
                val = '0'
            if val == '3':
                row[index] = '1'

            # s139 can be multiple
            index = headers.index('s139991')
            val = row[headers.index('s139')]
            if val == '':
                val = ['0']
            else:
                val = val.split(' ')
            if '1' in val:
                row[index] = '1'

            # s141 can me multiple, but we only care if 1 (and only 1) is selected
            index = headers.index('s141991')
            val = row[headers.index('s141')]
            if val == '':
                val = ['0']
            else:
                val = val.split(' ')
            if '1' in val and len(val) == 1:
                row[index] = '1'

            # ensure all binary variables actually ARE 0 or 1:
            for var in binaryVars:
                val = row[headers.index(var)]
                if val == '' or val != '1':
                    row[headers.index(var)] = '0'

        # rename s2 -> age
        s2index = headers.index('s2')
        headers[s2index] = 'age'

        droplist = ['s3', 's4', 's166', 's5', 's6', 's8', 's11', 's13', 's16', 's30', 's113', 's114', 's116', 's135',
                    's139', 's141']
        for d in droplist:
            index = headers.index(d)
            headers.remove(d)
            for row in matrix:
                del row[index]

        adultwriter.writerow(headers)
        for row in matrix:
            adultwriter.writerow(row)

        return 1

    def abort(self):
        self.want_abort = 1
