<?php
$myarr = array('foo'=>'bar','bar'=>'foo');
$myarr2 = ['foo'=>'bar2','bar'=>'foo2','2'=>'1','last'];
var_dump($myarr2);

var_dump($myarr2[3]);
//增加
$myarr[] = 'who';
$myarr['add'] = 'mya';
//删除
unset($myarr['add']);
var_dump($myarr);

$array = array(
    "foo" => "bar",
    42    => 24,
    "multi" => array(
         "dimensional" => array(
             "array" => "foo"
         )
    )
);
var_dump($array["multi"]["dimensional"]["array"]);

function getArray() {
    return array(1, 2, 3);
}

// on PHP 5.4
$secondElement = getArray()[1];
