<?php

$arr=['xt','bob','kevin','michel'];
$s='';
foreach ($arr as $my_var)
{
    $s=' '.$my_var.$s;
}
//最后一个$my_var还残留着
echo "$s\n";

//break可选择跳出层数
$i = 0;
while (++$i) {
    switch ($i) {
    case 5:
        echo "At 5\n";
        break 1;  /* 只退出 switch. */
    case 10:
        echo "At 10; quitting\n";
        break 2;  /* 退出 switch 和 while 循环 */
    default:
        break;
    }
}
//continue也可以

$i = 0;
while ($i++ < 5) {
    echo "Outer\n";
    while (1) {
        echo "Middle\n";
        while (1) {
            echo "Inner\n";
            continue 3;
        }
        echo "This never gets output.\n";
    }
    echo "Neither does this.\n";
}
