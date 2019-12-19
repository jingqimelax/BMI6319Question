#!/usr/bin/python
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print( "Usage: <testfile> <predictfile>" )
        sys.exit(1)

    test = []
    with open( sys.argv[1] ) as infile:
        for line in infile:
            test.append( line.split()[0] )

    predict = []
    with open( sys.argv[2] ) as infile:
        for line in infile:
            predict.append( line.strip() )

    ret = {}
    for i in range( 0, len( test ) ):
        key= test[i] + "\t" + predict[i]
        ret.setdefault( key, 0 )
        ret[ key ] += 1

    correct = ret['0\t0']
    p = ret['0\t0'] + ret['1\t0']
    r = ret['0\t0'] + ret['0\t1']

    p = float(correct) / p
    r = float(correct) / r
    f = 2 * p * r / ( p + r )

    print( "no-recurrance-events: %.3f\t%.3f\t%.3f" % ( p, r, f ) )

    correct = ret['1\t1']
    p = ret['0\t1'] + ret['1\t1']
    r = ret['1\t0'] + ret['1\t0']

    p = float(correct) / p
    r = float(correct) / r
    f = 2 * p * r / ( p + r )
    print( "recurrance-events: %.3f\t%.3f\t%.3f" % ( p, r, f ) )



