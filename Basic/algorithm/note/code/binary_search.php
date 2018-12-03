<?php

/**
 * 二分查找
 */
function binarySearch($needle, $array)
{
    $low = 0;
    $high = count($array);

    while ($low <= $high) {
        $middle = floor(($low + $high) / 2);
        if ($array[$middle] == $needle) {
            return $middle;
        }

        if ($array[$middle] > $needle) {
            $high = $middle - 1;
        } else {
            $low = $middle + 1;
        }
    }
    return null;
}


$array = [1, 3, 5, 7, 9];
echo binarySearch(3, $array) . PHP_EOL;
echo binarySearch(-1, $array) . PHP_EOL;
