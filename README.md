Quick script to test different approaches to the problem of detecting
the last item in a list, prompted by this
[SO post](https://stackoverflow.com/questions/39808908/detect-if-item-is-the-last-in-a-list).

Results on my machine (seconds):

*10k iterations*
```txt
check_last_num():            3.9227688719984144
check_last_num_ind():        5.9376225670021086
check_last_num_ind_acc():    6.796169109999028
skip_last_num():             4.144758571997954
```

*1M iterations*
```txt
check_last_num():            453.88007892300084
check_last_num_ind():        715.3580137629979
check_last_num_ind_acc():    870.466355964003
skip_last_num():             536.3545343529986
```

I figure python must be optimizing the for each loop.

TODO: test with C

<!--  <a name="10k"></a> [10k](#10k) -->
