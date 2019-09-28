#qtbl           qtable                                      
#dtb            row-dict-list
#cnl            col-name-list                          
#mat            mat                                         
#row            row-dict
#rvl            row-value-list
#rowarg         row | rvl
#col            col-dict-list
#ckey           col-key
#colname        colname<same as ckey>
#ckl            col-key-list
#cvl            col-value-list
#colarg         col | cvl
#columns        col-name-list<same as colname>            
#index          row-index-list
#ri             row-index
#ci             col-index
#loc            (ri,ci)
#nloc           (ri,ckey)
#ele            element<{ckey:value}>
#v              value
#eles-list      
#rslct<>        return(<rows>)-select-rows-via-cond_func(<>)
#cslct<>        return(<cols>)-select-cols-via-cond_func(<>)
#eslct<>        return(<eles>)-select-eles-list-via-cond_func(<>)
#lslct<>        return(<locs>)-select-locs-list-via-cond_func(<>)
#nlslct<>       return(<nlocs>)-select-nlocs-list-via-cond_func(<>)



from qtable.qtable import *
import elist.elist as elel
import edict.edict as eded
import tlist.tlist as tltl
import dlist.dlist as dldl
import efuntool.efuntool as eftl

def qtbl2dtb(qtbl):
    '''
        from qtable.qtable import *
        from xdict.jprint import pobj,pdir,parr
        qtbl
        qtbl = Qtable(mat= np.arange(25).reshape((5,5)),index=['a','c','d','a','e'],columns=['one', 'two', 'three','one','four'])
        parr(qtbl2dtb(qtbl))
        >>> qtbl
           one  two  three  one  four
        a    0    1      2    3     4
        c    5    6      7    8     9
        d   10   11     12   13    14
        a   15   16     17   18    19
        e   20   21     22   23    24
        >>>
        >>> parr(qtbl2dtb(qtbl))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
    '''
    ks = qtbl.columns
    mat = qtbl.to_mat()
    depth = len(qtbl.index)
    dtb = elel.mapv(mat,lambda row:eded.kvlist2d(ks,row))
    return(dtb)

def get_cnl(dtb):
    '''
        get_cnl(dtb)
        ['one', 'two', 'three', 'four']
    '''
    row = dtb[0]
    kl,vl = eded.d2kvlist(row)
    return(kl)

def row2rvl(row):
    '''
        row2rvl(dtb[0])
        [3, 1, 2, 4]
    '''
    return(list(row.values()))

def rvl2row(rvl,cnl):
    '''
        cnl = ['one', 'two', 'three', 'four']
        rvl2row([3, 1, 2, 4],cnl)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
    '''
    return(eded.kvlist2d(cnl,rvl))

def dtb2mat(dtb):
    '''
        dtb2mat(dtb)
        >>> parr(dtb2mat(dtb))
        [3, 1, 2, 4]
        [8, 6, 7, 9]
        [13, 11, 12, 14]
        [18, 16, 17, 19]
        [23, 21, 22, 24]
        >>>
    '''
    m = elel.mapv(dtb,row2rvl)
    return(m)

def mat2dtb(m,cnl):
    '''
        >>> parr(mat2dtb(m,cnl))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    return(elel.mapv(m,rvl2row,[cnl]))

def dtb2qtbl(dtb):
    '''
        dtb2qtbl(dtb)
        qtbl
        >>> dtb2qtbl(dtb)
           one  two  three  four
        0    3    1      2     4
        1    8    6      7     9
        2   13   11     12    14
        3   18   16     17    19
        4   23   21     22    24
        >>>
    '''
    columns = get_cnl(dtb)
    index = elel.init_range(0,len(dtb),1)
    m = dtb2mat(dtb)
    qtbl = Qtable(mat=np.array(m),index=index,columns=columns)
    return(qtbl)

def init_dtb(*args):
    '''
        >>> init_dtb()
        []
        >>>
        >>> parr(init_dtb(m,cnl))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(init_dtb(qtbl))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        
    '''
    if(len(args) == 0):
        return([])
    elif(len(args) == 1):
        if(isinstance(args[0],Qtable)):
            return(qtbl2dtb(qtbl))
        else:
            return(args[0])
    else:
        return(mat2dtb(args[0],args[1]))

def cvl2col(ckey,cvl):
    '''
        ckey = 'three'
        cvl = ['aa', 'bb', 'cc', 'dd', 'ee']
        >>> parr(cvl2col(ckey,cvl))
        {'three': 'aa'}
        {'three': 'bb'}
        {'three': 'cc'}
        {'three': 'dd'}
        {'three': 'ee'}
        >>>
    '''
    ckl = elel.init(len(cvl),ckey)
    tl = tltl.kvlists2tl(ckl,cvl)
    col = tltl.tlist2dlist(tl)
    return(col)

def get_ckey(col):
    '''
        >>> parr(col)
        {'three': 'aa'}
        {'three': 'bb'}
        {'three': 'cc'}
        {'three': 'dd'}
        {'three': 'ee'}
        >>>
        >>> get_ckey(col)
        'three'
        >>>
    '''
    return(list(col[0].keys())[0])

def get_ckl(col):
    '''
        >>> parr(col)
        {'three': 'aa'}
        {'three': 'bb'}
        {'three': 'cc'}
        {'three': 'dd'}
        {'three': 'ee'}
        >>> get_ckl(col)
        ['three', 'three', 'three', 'three', 'three']
        >>>
    '''
    ckl,cvl = dldl.dlist2kvlist(col)
    return(ckl)

def col2cvl(col):
    '''
        >>> parr(col)
        {'three': 'aa'}
        {'three': 'bb'}
        {'three': 'cc'}
        {'three': 'dd'}
        {'three': 'ee'}
        >>> get_cvl(col)
        ['aa', 'bb', 'cc', 'dd', 'ee']
        >>>
    '''
    ckl,cvl = dldl.dlist2kvlist(col)
    return(cvl)

#
def get_colnums(dtb):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        get_colnums(dtb)
        3
    '''
    cnl = get_cnl(dtb)
    return(len(cnl))


def colarg2cvl(colarg):
    '''
    '''
    if(dldl.is_dlist(colarg)):
        cvl = col2cvl(colarg)
    else:
        cvl = colarg
    return(cvl)

def colarg2col(colarg,ckey):
    '''
    '''
    if(dldl.is_dlist(colarg)):
        col = colarg
    else:
        col = cvl2col(ckey,colarg)
    return(col)

def add_col(dtb,colname,colarg):
    '''
        >>> colname
        'five'
        >>> col
        [100, 200, 300, 400, 500]
        >>> parr(add_col(dtb,colname,col))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4, 'five': 100}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9, 'five': 200}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14, 'five': 300}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19, 'five': 400}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24, 'five': 500}
        >>>
    '''
    def map_func(i,v,o1,o2):
        v[o1] = o2[i]
        return(v)
    cvl = colarg2cvl(colarg)
    dtb = elel.mapiv(dtb,map_func,[colname,cvl])
    return(dtb)

def add_cols(dtb,*args):
    '''
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4, 'five': 100}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9, 'five': 200}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14, 'five': 300}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19, 'five': 400}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24, 'five': 500}
        >>>
        >>> parr(add_cols(dtb,"six",[6,6,6,6,6],"seven",[7,7,7,7,7]))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4, 'five': 100, 'six': 6, 'seven': 7}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9, 'five': 200, 'six': 6, 'seven': 7}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14, 'five': 300, 'six': 6, 'seven': 7}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19, 'five': 400, 'six': 6, 'seven': 7}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24, 'five': 500, 'six': 6, 'seven': 7}
        >>>
    '''
    args = elel.divide(args,2)
    dtb = eftl.params_pipeline(add_col,dtb,*args)
    return(dtb)

def rm_col(dtb,colname):
    '''
        >>> parr(rm_col(dtb,'seven'))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4, 'five': 100, 'six': 6}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9, 'five': 200, 'six': 6}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14, 'five': 300, 'six': 6}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19, 'five': 400, 'six': 6}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24, 'five': 500, 'six': 6}
        >>>
    '''
    def map_func(v,o):
        del v[o]
        return(v)
    dtb = elel.mapv(dtb,map_func,[colname])
    return(dtb)

def rm_cols(dtb,*args):
    '''
        >>> parr(rm_cols(dtb,'three','five'))
        {'one': 3, 'two': 1, 'four': 4, 'six': 6}
        {'one': 8, 'two': 6, 'four': 9, 'six': 6}
        {'one': 13, 'two': 11, 'four': 14, 'six': 6}
        {'one': 18, 'two': 16, 'four': 19, 'six': 6}
        {'one': 23, 'two': 21, 'four': 24, 'six': 6}
        >>>
    '''
    args = elel.mapv(args,lambda ele:[ele])
    dtb = eftl.params_pipeline(rm_col,dtb,*args)
    return(dtb)

#
def get_cvl(dtb,colname):
    '''
        >>> get_cvl(dtb,'one')
        [3, 8, 13, 18, 23]
        >>>
    '''
    
    return(elel.mapv(dtb,lambda row:row[colname]))

def get_col(dtb,colname):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> parr(get_col(dtb,'x'))
        {'three': 'xx1'}
        {'three': 'xx2'}
        {'three': 'xx3'}
        {'three': 'xx4'}
        {'three': 'xx5'}
        >>>
        
    '''
    cvl = get_cvl(dtb,colname)
    ckl = elel.init(len(cvl),colname)
    return(cvl2col(ckey,cvl))

def get_cols(dtb,*args):
    '''
        #得到的是一张新子表
        >>> parr(get_cols(dtb,'one','two'))
        {'one': 3, 'two': 1}
        {'one': 8, 'two': 6}
        {'one': 13, 'two': 11}
        {'one': 18, 'two': 16}
        {'one': 23, 'two': 21}
        >>>
    '''
    qtbl = dtb2qtbl(dtb)
    qtbl =  qtbl.cols(*args)
    dtb = qtbl2dtb(qtbl)
    return(dtb)

def get_cvls(dtb,*args):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> parr(get_cvls(dtb,'x','y'))
        ['xx1', 'yy1']
        ['xx2', 'yy2']
        ['xx3', 'yy3']
        ['xx4', 'yy4']
        ['xx5', 'yy5']
        >>>
    '''
    cols = get_cols(dtb,*args)
    ndtb = dtb2mat(cols)
    return(ndtb)

def rename_col(dtb,cn,ncn):
    '''
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'four': 4}
        {'one': 8, 'two': 6, 'four': 9}
        {'one': 13, 'two': 11, 'four': 14}
        {'one': 18, 'two': 16, 'four': 19}
        {'one': 23, 'two': 21, 'four': 24}
        >>>
        >>> parr(rename_col(dtb,'four',400))
        {'one': 3, 'two': 1, 400: 4}
        {'one': 8, 'two': 6, 400: 9}
        {'one': 13, 'two': 11, 400: 14}
        {'one': 18, 'two': 16, 400: 19}
        {'one': 23, 'two': 21, 400: 24}
        >>>
    '''
    col = get_cvl(dtb,cn)
    dtb = rm_col(dtb,cn)
    dtb = add_col(dtb,ncn,col)
    return(dtb)

def rename_cols(dtb,cns,ncns):
    '''
        parr(dtb)
        {'one': 3, 'two': 1, 400: 4}
        {'one': 8, 'two': 6, 400: 9}
        {'one': 13, 'two': 11, 400: 14}
        {'one': 18, 'two': 16, 400: 19}
        {'one': 23, 'two': 21, 400: 24}
        >>>
        cns = ['one','two']
        ncns = [1000,2000]
        >>> parr(rename_cols(dtb,cns,ncns))
        {400: 4, 1000: 3, 2000: 1}
        {400: 9, 1000: 8, 2000: 6}
        {400: 14, 1000: 13, 2000: 11}
        {400: 19, 1000: 18, 2000: 16}
        {400: 24, 1000: 23, 2000: 21}
        >>>
    '''
    args = elel.interleave(cns,ncns)
    args = elel.divide(args,2)
    dtb = eftl.params_pipeline(rename_col,dtb,*args)
    return(dtb)

def swapcol(dtb,cn0,cn1):
    '''
        >>> parr(dtb)
        {400: 4, 1000: 3, 2000: 1}
        {400: 9, 1000: 8, 2000: 6}
        {400: 14, 1000: 13, 2000: 11}
        {400: 19, 1000: 18, 2000: 16}
        {400: 24, 1000: 23, 2000: 21}
        >>>
        >>> parr(swapcol(dtb,400,2000))
        >>> parr(swapcol(dtb,400,2000))
        {400: 1, 1000: 3, 2000: 4}
        {400: 6, 1000: 8, 2000: 9}
        {400: 11, 1000: 13, 2000: 14}
        {400: 16, 1000: 18, 2000: 19}
        {400: 21, 1000: 23, 2000: 24}
        >>>
    '''
    def map_func(row,o1,o2):
        tmp = row[o1]
        row[o1] = row[o2]
        row[o2] = tmp
        return(row)
    return(elel.mapv(dtb,map_func,[cn0,cn1]))

def repl_col(dtb,cn,col,ncn=None):
    '''
        >>> parr(dtb)
        {400: 1, 1000: 3, 2000: 4}
        {400: 6, 1000: 8, 2000: 9}
        {400: 11, 1000: 13, 2000: 14}
        {400: 16, 1000: 18, 2000: 19}
        {400: 21, 1000: 23, 2000: 24}
        >>>
        >>> parr(repl_col(dtb,400,['a','b','c','d','e']))
        {1000: 3, 2000: 4, 400: 'a'}
        {1000: 8, 2000: 9, 400: 'b'}
        {1000: 13, 2000: 14, 400: 'c'}
        {1000: 18, 2000: 19, 400: 'd'}
        {1000: 23, 2000: 24, 400: 'e'}
        >>>
        >>> parr(repl_col(dtb, 400,['aa','bb','cc','dd','ee'],"three"))
        {1000: 3, 2000: 4, 'three': 'aa'}
        {1000: 8, 2000: 9, 'three': 'bb'}
        {1000: 13, 2000: 14, 'three': 'cc'}
        {1000: 18, 2000: 19, 'three': 'dd'}
        {1000: 23, 2000: 24, 'three': 'ee'}
        >>>
    '''
    if(ncn == None):
        ncn = cn
    else:
        pass
    cnl = get_cnl(dtb)
    #pandas not support non-string colname,need a trick
    tmpcn = elel.join(cnl,"@")
    #dont use new dtb, keep inplace
    dummy = rename_col(dtb,cn,tmpcn)
    #################################
    qtbl = dtb2qtbl(dtb)
    qtbl = qtbl.repl_col(tmpcn,ncn,col)
    ndtb = qtbl2dtb(qtbl)
    ###this is a trick , to keep inplace
    dtb.clear()
    dtb.extend(ndtb)
    ###
    return(ndtb)

def repl_cols(dtb,*args):
    '''
        >>> parr(dtb)
        {1000: '3', 2000: '4', 'three': 'aa'}
        {1000: '8', 2000: '9', 'three': 'bb'}
        {1000: '13', 2000: '14', 'three': 'cc'}
        {1000: '18', 2000: '19', 'three': 'dd'}
        {1000: '23', 2000: '24', 'three': 'ee'}
        >>>
        cns = [1000, 2000]
        cols = [['x1','x2','x3','x4','x5'],['y1','y2','y3','y4','y5']]
        parr(repl_cols(dtb,cns,cols))
        >>> parr(repl_cols(dtb,cns,cols))
        {'three': 'aa', 1000: 'x1', 2000: 'y1'}
        {'three': 'bb', 1000: 'x2', 2000: 'y2'}
        {'three': 'cc', 1000: 'x3', 2000: 'y3'}
        {'three': 'dd', 1000: 'x4', 2000: 'y4'}
        {'three': 'ee', 1000: 'x5', 2000: 'y5'}
        >>>
        cns = [1000, 2000]
        cols = [['xx1','xx2','xx3','xx4','xx5'],['yy1','yy2','yy3','yy4','yy5']]
        ncns = ['x','y']
        >>> parr(repl_cols(dtb,cns,cols,ncns))
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
    '''
    cnl = get_cnl(dtb)
    prefix = elel.join(cnl,"@")
    cns = args[0]
    cols = args[1]
    ncns = (args[2] if(len(args)>2) else cns)
    tmpcns = elel.mapv(cns,lambda cn:prefix+'@'+str(cn))
    dummy = rename_cols(dtb,cns,tmpcns)
    qtbl = dtb2qtbl(dtb)
    qtbargs = elel.interleave(ncns,cols)
    qtbl = qtbl.repl_cols(tmpcns,*qtbargs)
    ndtb = qtbl2dtb(qtbl)
    ###this is a trick , to keep inplace
    dtb.clear()
    dtb.extend(ndtb)
    ###
    return(ndtb)

####

def get_rownums(dtb):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> get_rownums(dtb)
        5
        >>>
    '''
    return(len(dtb))

def get_row(dtb,which):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> get_row(dtb,3)
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        >>>
    '''
    return(dtb[which])

def get_rvl(dtb,which):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> get_rvl(dtb,2)
        ['cc', 'xx3', 'yy3']
        >>>
    '''
    row = get_row(dtb,which)
    return(row2rvl(row))

def get_rows(dtb,*args):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> parr(get_rows(dtb,[0,2,4]))
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
    '''
    whiches = eftl.compatibize_apply_or_call_args(*args)
    return(elel.select_seqs(dtb,whiches))

def get_rvls(dtb,*args):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> parr(get_rvls(dtb,[0,2,4]))
        ['aa', 'xx1', 'yy1']
        ['cc', 'xx3', 'yy3']
        ['ee', 'xx5', 'yy5']
        >>>
    '''
    rows = get_rows(dtb,*args)
    rvls = elel.mapv(rows,row2rvl)
    return(rvls)

def rowarg2rvl(rowarg):
    '''
    '''
    if(isinstance(rowarg,dict)):
        rvl = row2rvl(rowarg)
    else:
        rvl = row
    return(rvl)

def rowarg2row(rowarg,cnl):
    '''
    '''
    if(isinstance(rowarg,dict)):
        row = rowarg
    else:
        row = rvl2row(rowarg,cnl)
    return(row)

def append_row(dtb,rowarg):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        >>>
        >>> parr(append_row(dtb,['ff', 'xx6','yy6']))
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        >>>
        >>> parr(append_row(dtb,{'three': 'gg', 'x': 'xx7', 'y': 'yy7'}))
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        >>>
    '''
    cnl = get_cnl(dtb)
    row = rowarg2row(rowarg,cnl)
    dtb.append(row)
    return(dtb)

def append_rows(dtb,*rowargs):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        >>>
        >>> parr(append_rows(dtb,[1,2,3],[11,22,33]))
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        {'three': 1, 'x': 2, 'y': 3}
        {'three': 11, 'x': 22, 'y': 33}
        >>>
    '''
    cnl = get_cnl(dtb)
    rows = elel.mapv(rowargs,rowarg2row,[cnl])
    dtb.extend(rows)
    return(dtb)

def prepend_row(dtb,rowarg):
    '''
        >>> parr(dtb)
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        {'three': 1, 'x': 2, 'y': 3}
        {'three': 11, 'x': 22, 'y': 33}
        >>>
        >>> parr(prepend_row(dtb,[0,0,0]))
        {'three': 0, 'x': 0, 'y': 0}
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        {'three': 1, 'x': 2, 'y': 3}
        {'three': 11, 'x': 22, 'y': 33}
        >>>
    '''
    cnl = get_cnl(dtb)
    row = rowarg2row(rowarg,cnl)
    ndtb = elel.prepend(dtb,row)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(ndtb)

def prepend_rows(dtb,*rowargs):
    '''
        >>> parr(dtb)
        {'three': 0, 'x': 0, 'y': 0}
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        {'three': 1, 'x': 2, 'y': 3}
        {'three': 11, 'x': 22, 'y': 33}
        >>>
        >>>
        >>> parr(prepend_rows(dtb,[100,200,300],[0,0,0]))
        {'three': 100, 'x': 200, 'y': 300}
        {'three': 0, 'x': 0, 'y': 0}
        {'three': 0, 'x': 0, 'y': 0}
        {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
        {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
        {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
        {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
        {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
        {'three': 'ff', 'x': 'xx6', 'y': 'yy6'}
        {'three': 'gg', 'x': 'xx7', 'y': 'yy7'}
        {'three': 1, 'x': 2, 'y': 3}
        {'three': 11, 'x': 22, 'y': 33}
        >>>
    '''
    cnl = get_cnl(dtb)
    rows = elel.mapv(rowargs,rowarg2row,[cnl])
    ndtb = elel.prextend(dtb,rows)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(dtb)

def rmrow(dtb,which):
    '''
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(rmrow(dtb,2))
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    ndtb = elel.select_seqs_not(dtb,[which])
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(ndtb)

def rmrows(dtb,*whiches):
    '''
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(rmrows(dtb,[0,2]))
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    whiches = eftl.compatibize_apply_or_call_args(*whiches)
    ndtb = elel.select_seqs_not(dtb,whiches)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(dtb)

def insert_row(dtb,index,rowarg):
    '''
        >>> parr(dtb)
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(insert_row(dtb,1,[77,88,99,100]))
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 77, 'two': 88, 'three': 99, 'four': 100}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    cnl = get_cnl(dtb)
    row = rowarg2row(rowarg,cnl)
    ndtb = elel.insert(dtb,index,row)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(ndtb)

def insert_rows(dtb,index,*rowargs):
    '''
        >>> parr(dtb)
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 77, 'two': 88, 'three': 99, 'four': 100}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(insert_rows(dtb,1,['a','b','c','d'],['aa','bb','cc','dd']))
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 'a', 'two': 'b', 'three': 'c', 'four': 'd'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': 77, 'two': 88, 'three': 99, 'four': 100}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    cnl = get_cnl(dtb)
    rows = elel.mapv(rowargs,rowarg2row,[cnl])
    ndtb =  elel.insert_section(dtb,rows,index)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(dtb)

def repl_row(dtb,index,rowarg):
    '''
        >>> parr(dtb)
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 'a', 'two': 'b', 'three': 'c', 'four': 'd'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': 77, 'two': 88, 'three': 99, 'four': 100}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(repl_row(dtb,3,["uuu","vvv","www","xxx"]))
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 'a', 'two': 'b', 'three': 'c', 'four': 'd'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    cnl = get_cnl(dtb)
    row = rowarg2row(rowarg,cnl)
    dtb[index] = row
    return(dtb)

def repl_rows(dtb,indexes,*rowargs):
    '''
        >>>
        >>> parr(dtb)
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 'a', 'two': 'b', 'three': 'c', 'four': 'd'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(repl_rows(dtb,[0,4],["@","@@","@@@","@@@@"],["&","&&","&&&","&&&&"]))
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    cnl = get_cnl(dtb)
    rows = elel.mapv(rowargs,rowarg2row,[cnl])
    elel.set_seqs(dtb,indexes,rows)
    return(dtb)

def swaprow(dtb,i0,i1):
    '''
        >>>
        >>> parr(dtb)
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(swaprow(dtb,0,3))
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
    '''
    row = dtb[i0]
    dtb[i0] = dtb[i1]
    dtb[i1] = row
    return(dtb)

def crop(dtb,top,left,bottom,right):
    '''
        crop will not change the original dtb
        >>> parr(dtb)
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(crop(dtb,1,'two',3,'three'))
        {'two': '&&', 'three': '&&&'}
        {'two': 'bb', 'three': 'cc'}
        {'two': '@@', 'three': '@@@'}
        >>>
    '''
    qtbl = dtb2qtbl(dtb)
    qtbl = qtbl.crop(top,left,bottom,right)
    ndtb = qtbl2dtb(qtbl)
    return(ndtb)

def flipud(dtb):
    '''
        >>> parr(dtb)
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> parr(flipud(dtb))
        {'one': '23', 'two': '21', 'three': '22', 'four': '24'}
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        >>>
    '''
    qtbl = dtb2qtbl(dtb)
    qtbl = qtbl.flipud()
    ndtb = qtbl2dtb(qtbl)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(dtb)

def subtb(dtb,rowseqs,colnames):
    '''
        >>> parr(dtb)
        {'one': '23', 'two': '21', 'three': '22', 'four': '24'}
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        >>>
        >>> parr(subtb(dtb,[0,2,4],['three','four']))
        {'three': '22', 'four': '24'}
        {'three': 'cc', 'four': 'dd'}
        {'three': 'www', 'four': 'xxx'}
        >>>
    '''
    rows = get_rows(dtb,*rowseqs)
    cols = get_cols(rows,*colnames)
    return(cols)

def transpose(dtb):
    '''
        transpose will lost key-info
        >>> parr(dtb)
        {'one': '23', 'two': '21', 'three': '22', 'four': '24'}
        {'one': '@', 'two': '@@', 'three': '@@@', 'four': '@@@@'}
        {'one': 'aa', 'two': 'bb', 'three': 'cc', 'four': 'dd'}
        {'one': '&', 'two': '&&', 'three': '&&&', 'four': '&&&&'}
        {'one': 'uuu', 'two': 'vvv', 'three': 'www', 'four': 'xxx'}
        >>> parr(transpose(dtb))
        {0: '23', 1: '@', 2: 'aa', 3: '&', 4: 'uuu'}
        {0: '21', 1: '@@', 2: 'bb', 3: '&&', 4: 'vvv'}
        {0: '22', 1: '@@@', 2: 'cc', 3: '&&&', 4: 'www'}
        {0: '24', 1: '@@@@', 2: 'dd', 3: '&&&&', 4: 'xxx'}
        >>>
        >>>
    '''
    qtbl = dtb2qtbl(dtb)
    qtbl = qtbl.transpose()
    ndtb = qtbl2dtb(qtbl)
    ####
    dtb.clear()
    dtb.extend(ndtb)
    ####
    return(dtb)


##################################################



##################################################
#r    row
#i    row-index
################



def rslctr(dtb,cond_func,*oargs):
    '''
        #cond_func(row,*oargs)
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> ndtb = rslctr(dtb,lambda row:row['two']%2==0)
        >>> parr(ndtb)
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        >>>

    '''
    conds = elel.mapv(dtb,cond_func,oargs)
    nseqs = elel.indexes_all(conds,True)
    ndtb = elel.select_seqs(dtb,nseqs)
    return(ndtb)

def rslctri(dtb,cond_func,*oargs):
    '''
        #ri  row-index
        #cond_func(ri,row,*oargs)
        >>> ndtb = rslctri(dtb,lambda i,row:(row['two']%2==1)and(i>2))
        >>>
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> ndtb = rslctri(dtb,lambda i,row:(row['two']%2==1)and(i>2))
        >>>
        >>> parr(ndtb)
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        
    '''
    conds = elel.mapiv(dtb,cond_func,oargs)
    nseqs = elel.indexes_all(conds,True)
    ndtb = elel.select_seqs(dtb,nseqs)
    return(ndtb)


def slctr(dtb,colnames,cond_func,*oargs):
    '''
        #colnames   returned colnames
        #slctr(dtb,colnames,cond_func,*oargs)
        #cond_func(row,*oargs)
        
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>>
        >>> ndtb = slctr(dtb,['one','two'],lambda row:row['two']%2==0)
        >>>
        >>> parr(ndtb)
        {'one': 8, 'two': 6}
        {'one': 18, 'two': 16}
        >>>
    '''
    dtb = rslctr(dtb,cond_func,*oargs)
    dtb = get_cols(dtb,colnames)
    return(dtb)

def slctri(dtb,colnames,cond_func,*oargs):
    '''
        #colnames   returned colnames
        #slctr(dtb,colnames,cond_func,*oargs)
        #cond_func(row,*oargs)
        parr(dtb)
        ndtb = slctri(dtb,['one','two'],lambda i,row:(row['two']%2==1)and(i>2))
        parr(ndtb)
        >>> parr(dtb)
        {'one': 3, 'two': 1, 'three': 2, 'four': 4}
        {'one': 8, 'two': 6, 'three': 7, 'four': 9}
        {'one': 13, 'two': 11, 'three': 12, 'four': 14}
        {'one': 18, 'two': 16, 'three': 17, 'four': 19}
        {'one': 23, 'two': 21, 'three': 22, 'four': 24}
        >>> ndtb = slctri(dtb,['one','two'],lambda i,row:(row['two']%2==1)and(i>2))
        >>> parr(ndtb)
        {'one': 23, 'two': 21}
        >>>
    '''
    dtb = rslctri(dtb,cond_func,*oargs)
    dtb = get_cols(dtb,colnames)
    return(dtb)


##########################################################



