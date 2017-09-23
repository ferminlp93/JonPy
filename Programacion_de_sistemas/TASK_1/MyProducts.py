
import numpy

# --------------------------------------------------------------------------------
# This methods assumes both parameters are 'ndarray', i.e. Numpy arrays, or lists
#
# 
def vector_vector_product( a, b ):
    # 
    if type(a) is numpy.ndarray:
        if a.shape != b.shape : raise Exception( "a.shape  doesn't match b.shape" )
    if len(a) != len(b) : raise Exception( "len(a) = %d is not equal to len(b) = %d" % (len(a), len(b)) )
    #
    result = 0.
    for i in range(len(a)): result += a[i] * b[i]
    return result
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# This methods assumes both parameters are 'ndarray', i.e. Numpy arrays, or lists 
#
def matrix_vector_product( m, v ):
    # 
    if type(m) is numpy.ndarray:
        if len(m.shape) != 2 : raise Exception( "Invalid shape of the matrix" )
        if len(v.shape) != 1 : raise Exception( "Invalid shape of the vector" )
        if m.shape[1] != len(v) : raise Exception( "The number of columns in matrix = %d is not equal to len(v) = %d" % (m.shape[1], len(v)) )
    if len(v) != len(m[0]):
        raise Exception( "The number of columns in matrix = %d is not equal to len(v) = %d" % (len(m[0]), len(v)) )
    #
    # The result should be a vector of length equal to the number of rows of the matrix
    if type(m) is numpy.ndarray:
        result = numpy.zeros( m.shape[0] )
        for i in range(len(result)):
            for j in range(len(v)):
                result[i] += m[i,j] * v[j]
    else:
        result = [0] * len(m[0])
        for i in range(len(result)):
            for j in range(len(v)):
                result[i] += m[i][j] * v[j]

    return result
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# This methods assumes both parameters are 'ndarray', i.e. Numpy arrays, or lists of lists
# 
# Trivial matrix product, not efficiently implemented
#
def matrix_matrix_product_1( a, b ):
    # 
    if type(a) is numpy.ndarray:
        if len(a.shape) != 2 : raise Exception( "Invalid shape of the first matrix" )
        if len(b.shape) != 2 : raise Exception( "Invalid shape of the second matrix" )
        if a.shape[1] != b.shape[0] :
            raise Exception( "The number of columns in the first matrix = %d is not equal to the number of rows of the second matrix = %d" % (a.shape[1], b.shape[0]) )
    else:
        if len(a[0]) != len(b):
            raise Exception( "The number of columns in the first matrix = %d is not equal to the number of rows of the second matrix = %d" % (len(a[0]), len(b) ) )
    #
    # The result should be a matrix with the number of rows of the first one and the number of columns of the second one
    if type(a) is numpy.ndarray:
        result = numpy.zeros( (a.shape[0], b.shape[1]) )
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                for k in range(a.shape[1]):
                    result[i,j] += a[i,k] * b[k,j]
    else:
        result = numpy.zeros( [ len(a), len(b[0]) ] )
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                for k in range(len(b)):
                    result[i,j] += a[i][k] * b[k][j]
    return result
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# This methods assumes both parameters are 'ndarray', i.e. Numpy arrays.
#
# Implementation taking advantage of the dot product provided by Numpy
#
def matrix_matrix_product_2( a, b ):
    # 
    if len(a.shape) != 2 : raise Exception( "Invalid shape of the first matrix" )
    if len(b.shape) != 2 : raise Exception( "Invalid shape of the second matrix" )
    if a.shape[1] != b.shape[0] : raise Exception( "The number of columns in the first matrix = %d is not equal to the number of rows of the second matrix = %d" % (a.shape[1], b.shape[0]) )
    #
    # The result should be a matrix with the number of rows of the first one and the number of columns of the second one
    result = numpy.zeros( (a.shape[0], b.shape[1]) )
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = numpy.dot( a[i,:], b[:,j] )
    return result
# --------------------------------------------------------------------------------
