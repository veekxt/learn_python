<?php

function xt_sum($a,$b)
{
    return $a+$b;
}

echo xt_sum(4,5),"\n";

//可变参数
function sum(...$numbers) {
    $acc = 0;
    foreach ($numbers as $n) {
        $acc += $n;
    }
    return $acc;
}

echo sum(1, 2, 3, 4)."\n";
