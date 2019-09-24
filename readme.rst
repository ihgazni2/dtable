.. contents:: Table of Contents
   :depth: 5


*dtable*
========
- A list of dict ,
- each dict has the same keys.
- Simple table for small dataset


Installation
------------

    ::

        $ pip3 install dtable

License
-------

- MIT

Usage
=====

import
------

    ::
        
        import dtable.dtable as dtdt
        from dtable.dtable import *

0. qtbl2dtb
-----------

    ::
    
        
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
            

.. image:: ./images/qtbl2dtb.svg

1. get_cnl
----------

    ::
    
        
                get_cnl(dtb)
                ['one', 'two', 'three', 'four']
            

.. image:: ./images/get_cnl.svg

2. row2rvl
----------

    ::
    
        
                row2rvl(dtb[0])
                [3, 1, 2, 4]
            

.. image:: ./images/row2rvl.svg

3. rvl2row
----------

    ::
    
        
                cnl = ['one', 'two', 'three', 'four']
                rvl2row([3, 1, 2, 4],cnl)
                {'one': 3, 'two': 1, 'three': 2, 'four': 4}
            

.. image:: ./images/rvl2row.svg

4. dtb2mat
----------

    ::
    
        
                dtb2mat(dtb)
                >>> parr(dtb2mat(dtb))
                [3, 1, 2, 4]
                [8, 6, 7, 9]
                [13, 11, 12, 14]
                [18, 16, 17, 19]
                [23, 21, 22, 24]
                >>>
            

.. image:: ./images/dtb2mat.svg

5. mat2dtb
----------

    ::
    
        
                >>> parr(mat2dtb(m,cnl))
                {'one': 3, 'two': 1, 'three': 2, 'four': 4}
                {'one': 8, 'two': 6, 'three': 7, 'four': 9}
                {'one': 13, 'two': 11, 'three': 12, 'four': 14}
                {'one': 18, 'two': 16, 'three': 17, 'four': 19}
                {'one': 23, 'two': 21, 'three': 22, 'four': 24}
                >>>
            

.. image:: ./images/mat2dtb.svg

6. dtb2qtbl
-----------

    ::
    
        
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
            

.. image:: ./images/dtb2qtbl.svg

7. init_dtb
-----------

    ::
    
        
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
                
            

.. image:: ./images/init_dtb.svg

8. cvl2col
----------

    ::
    
        
                ckey = 'three'
                cvl = ['aa', 'bb', 'cc', 'dd', 'ee']
                >>> parr(cvl2col(ckey,cvl))
                {'three': 'aa'}
                {'three': 'bb'}
                {'three': 'cc'}
                {'three': 'dd'}
                {'three': 'ee'}
                >>>
            

.. image:: ./images/cvl2col.svg

9. get_ckey
-----------

    ::
    
        
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
            

.. image:: ./images/get_ckey.svg

10. get_ckl
-----------

    ::
    
        
                >>> parr(col)
                {'three': 'aa'}
                {'three': 'bb'}
                {'three': 'cc'}
                {'three': 'dd'}
                {'three': 'ee'}
                >>> get_ckl(col)
                ['three', 'three', 'three', 'three', 'three']
                >>>
            

.. image:: ./images/get_ckl.svg

11. col2cvl
-----------

    ::
    
        
                >>> parr(col)
                {'three': 'aa'}
                {'three': 'bb'}
                {'three': 'cc'}
                {'three': 'dd'}
                {'three': 'ee'}
                >>> get_cvl(col)
                ['aa', 'bb', 'cc', 'dd', 'ee']
                >>>
            

.. image:: ./images/col2cvl.svg

12. get_colnums
---------------

    ::
    
        
                >>> parr(dtb)
                {'three': 'aa', 'x': 'xx1', 'y': 'yy1'}
                {'three': 'bb', 'x': 'xx2', 'y': 'yy2'}
                {'three': 'cc', 'x': 'xx3', 'y': 'yy3'}
                {'three': 'dd', 'x': 'xx4', 'y': 'yy4'}
                {'three': 'ee', 'x': 'xx5', 'y': 'yy5'}
                >>>
                get_colnums(dtb)
                3
            

.. image:: ./images/get_colnums.svg

13. colarg2cvl
--------------

    ::
    
        
            

.. image:: ./images/colarg2cvl.svg

14. colarg2col
--------------

    ::
    
        
            

.. image:: ./images/colarg2col.svg

15. add_col
-----------

    ::
    
        
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
            

.. image:: ./images/add_col.svg

16. add_cols
------------

    ::
    
        
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
            

.. image:: ./images/add_cols.svg

17. rm_col
----------

    ::
    
        
                >>> parr(rm_col(dtb,'seven'))
                {'one': 3, 'two': 1, 'three': 2, 'four': 4, 'five': 100, 'six': 6}
                {'one': 8, 'two': 6, 'three': 7, 'four': 9, 'five': 200, 'six': 6}
                {'one': 13, 'two': 11, 'three': 12, 'four': 14, 'five': 300, 'six': 6}
                {'one': 18, 'two': 16, 'three': 17, 'four': 19, 'five': 400, 'six': 6}
                {'one': 23, 'two': 21, 'three': 22, 'four': 24, 'five': 500, 'six': 6}
                >>>
            

.. image:: ./images/rm_col.svg

18. rm_cols
-----------

    ::
    
        
                >>> parr(rm_cols(dtb,'three','five'))
                {'one': 3, 'two': 1, 'four': 4, 'six': 6}
                {'one': 8, 'two': 6, 'four': 9, 'six': 6}
                {'one': 13, 'two': 11, 'four': 14, 'six': 6}
                {'one': 18, 'two': 16, 'four': 19, 'six': 6}
                {'one': 23, 'two': 21, 'four': 24, 'six': 6}
                >>>
            

.. image:: ./images/rm_cols.svg

19. get_cvl
-----------

    ::
    
        
                >>> get_cvl(dtb,'one')
                [3, 8, 13, 18, 23]
                >>>
            

.. image:: ./images/get_cvl.svg

20. get_col
-----------

    ::
    
        
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
                
            

.. image:: ./images/get_col.svg

21. get_cols
------------

    ::
    
        
                #得到的是一张新子表
                >>> parr(get_cols(dtb,'one','two'))
                {'one': 3, 'two': 1}
                {'one': 8, 'two': 6}
                {'one': 13, 'two': 11}
                {'one': 18, 'two': 16}
                {'one': 23, 'two': 21}
                >>>
            

.. image:: ./images/get_cols.svg

22. get_cvls
------------

    ::
    
        
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
            

.. image:: ./images/get_cvls.svg

23. rename_col
--------------

    ::
    
        
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
            

.. image:: ./images/rename_col.svg

24. rename_cols
---------------

    ::
    
        
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
            

.. image:: ./images/rename_cols.svg

25. swapcol
-----------

    ::
    
        
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
            

.. image:: ./images/swapcol.svg

26. repl_col
------------

    ::
    
        
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
            

.. image:: ./images/repl_col.svg

27. repl_cols
-------------

    ::
    
        
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
            

.. image:: ./images/repl_cols.svg

28. get_rownums
---------------

    ::
    
        
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
            

.. image:: ./images/get_rownums.svg

29. get_row
-----------

    ::
    
        
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
            

.. image:: ./images/get_row.svg

30. get_rvl
-----------

    ::
    
        
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
            

.. image:: ./images/get_rvl.svg

31. get_rows
------------

    ::
    
        
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
            

.. image:: ./images/get_rows.svg

32. get_rvls
------------

    ::
    
        
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
            

.. image:: ./images/get_rvls.svg

33. rowarg2rvl
--------------

    ::
    
        
            

.. image:: ./images/rowarg2rvl.svg

34. rowarg2row
--------------

    ::
    
        
            

.. image:: ./images/rowarg2row.svg

35. append_row
--------------

    ::
    
        
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
            

.. image:: ./images/append_row.svg

36. append_rows
---------------

    ::
    
        
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
            

.. image:: ./images/append_rows.svg

37. prepend_row
---------------

    ::
    
        
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
            

.. image:: ./images/prepend_row.svg

38. prepend_rows
----------------

    ::
    
        
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
            

.. image:: ./images/prepend_rows.svg

39. rmrow
---------

    ::
    
        
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
            

.. image:: ./images/rmrow.svg

40. rmrows
----------

    ::
    
        
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
            

.. image:: ./images/rmrows.svg

41. insert_row
--------------

    ::
    
        
                >>> parr(dtb)
                {'one': 8, 'two': 6, 'three': 7, 'four': 9}
                {'one': 23, 'two': 21, 'three': 22, 'four': 24}
                >>>
                >>> parr(insert_row(dtb,1,[77,88,99,100]))
                {'one': 8, 'two': 6, 'three': 7, 'four': 9}
                {'one': 77, 'two': 88, 'three': 99, 'four': 100}
                {'one': 23, 'two': 21, 'three': 22, 'four': 24}
                >>>
            

.. image:: ./images/insert_row.svg

42. insert_rows
---------------

    ::
    
        
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
            

.. image:: ./images/insert_rows.svg

43. repl_row
------------

    ::
    
        
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
            

.. image:: ./images/repl_row.svg

44. repl_rows
-------------

    ::
    
        
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
            

.. image:: ./images/repl_rows.svg

45. swaprow
-----------

    ::
    
        
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
            

.. image:: ./images/swaprow.svg

46. crop
--------

    ::
    
        
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
            

.. image:: ./images/crop.svg

47. flipud
----------

    ::
    
        
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
            

.. image:: ./images/flipud.svg

48. subtb
---------

    ::
    
        
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
            

.. image:: ./images/subtb.svg

49. transpose
-------------

    ::
    
        
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
            

.. image:: ./images/transpose.svg

50. rslctr
----------

    ::
    
        
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
        
            

.. image:: ./images/rslctr.svg

51. rslctri
-----------

    ::
    
        
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
                
            

.. image:: ./images/rslctri.svg

52. slctr
---------

    ::
    
        
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
            

.. image:: ./images/slctr.svg

53. slctri
----------

    ::
    
        
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
            

.. image:: ./images/slctri.svg



Words
=====
    
    ::

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
