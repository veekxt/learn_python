<?php

$foo='xt';
$bar=$foo;
$bar='root';
echo "foo is $foo, bar is $bar\n";

//引用
$foo='xt';
$bar=&$foo;
$bar='root';
echo "foo is $foo, bar is $bar\n";

//函数引用传递
function xt_swap(&$a,&$b)
{
    $tmp=$a;
    $a=$b;
    $b=$tmp;
}
$a=2;
$b=4;
xt_swap($a,$b);
echo "$a ,$b";
