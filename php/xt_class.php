<?php
//基本
class SimpleClass
{
    const constant = 'constant value';
    function showConstant() {
        echo  self::constant . "\n";
    }
    // property declaration
    public $var = 'a default value';

    // method declaration
    public function displayVar() {
        echo $this->var."\n";
    }
}
$a=new SimPleClass();
$a->displayVar();
$a->showConstant();

echo SimpleClass::class;
?>

