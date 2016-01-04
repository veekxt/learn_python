<?php
namespace h\i\j;
function add2($a,$b){
    echo "call add2 !","\n";
    return $a+$b;
}
//调用两次
add2(4,5);
\h\i\j\add2(1,2);
// 注意当前的namespace，下面是个错误示范
// h\i\j\add2(2,3);
