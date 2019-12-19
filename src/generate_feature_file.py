#!/usr/bin/python
import sys
import os
import csv
import random

# Any number can be used in place of '0'.
random.seed(0)

featureDict = {}
def encode_feature( row ):
    for i in range( 1, len( row ) ):
        key = str(i) + ':' + row[i]
        value = len( featureDict ) + 1
        featureDict.setdefault( key, value )

def line_to_feature( line ):
    # convert the csv line to liblinear feature
    #['recurrence-events', '40-49', 'ge40', '30-34', '3-5', 'no', '3', 'left', 'left_low', 'no']
    fea = {}
    for i in range( 1, len( row ) ):
        key = str(i) + ':' + row[i]
        fea[ featureDict[ key ] ] = '1'

    # class
    if line[0] == 'recurrence-events':
        label = '1'
    elif line[0] == 'no-recurrence-events':
        label = '0'

    return label + '\t' + ' '.join( [ str(a[0]) + ":" + a[1] for a in sorted( fea.items() ) ] ) 











if __name__ == '__main__':
    if len( sys.argv ) != 4:
        print( "Usage: <data_file> <train_feature_file> <test_feature_file>" )
        sys.exit( -1 )

    train_features = []
    train_features_string = []

    test_features = []
    test_features_string = []

    with open( sys.argv[1], 'r' ) as infile:
        csv_reader = csv.reader(infile, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            encode_feature( row )
            fea = line_to_feature( row )

            if random.randint(0, 9) == 0:
                # put to test set
                test_features.append(fea)
                test_features_string.append(','.join(row))
            else:
                # put to train set
                train_features.append( fea )
                train_features_string.append(','.join(row))

    with open( sys.argv[2], 'w' ) as outfile:
        for i in range( 0, len( train_features ) ):
            outfile.write( train_features[i] + ' # ' + train_features_string[i] + '\n')

    with open( sys.argv[3], 'w' ) as outfile:
        for i in range( 0, len( test_features ) ):
            outfile.write( test_features[i] + ' # ' + test_features_string[i] + '\n')

    








