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
