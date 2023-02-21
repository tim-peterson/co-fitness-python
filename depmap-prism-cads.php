<?php

$fp = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/secondary-screen-cell-line-info.csv','r') or die("can't open file");

$cells = []; // create cells assoc array
$cells0 = [];

while($csv_line = fgetcsv($fp,1024, ',')) {
   
    $cells0[$csv_line[1]] = $csv_line[3];

    if(isset($csv_line[3]) ){
        $cells[$csv_line[3]][] = $csv_line[1];
    }
    else{
        $cells[$csv_line[3]] = [$csv_line[1]];
    }
   
}
//print_r($cells[0]);
fclose($fp) or die("can't close file");


$fp = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/secondary_screen_replicate_collapsed_logfold_change_t.csv','r') or die("can't open file");

$sums = []; // create cells assoc array

$j = 0;
$cell_indices = [];
$sums = [];

$drug = "BRD-K49328571-001-15-0"; //dasatinib

while($csv_line = fgetcsv($fp,1024, ',')) {
   
    if($j == 0){
        for($i = 0; $i < count($csv_line); $i++){

            foreach($cells as $key => $val){
                if(in_array($csv_line[$i], $val)){
                    
                    if(isset($cell_indices[$key])){
                        $cell_indices[$key][] = $i;
                        
                    }
                    else $cell_indices[$key] = [$i];
                }
            }
        }
        $j++;

    }
    else {

        if(strpos($csv_line[0], "BRD-K49328571-001-15-0")===false) continue;

        $sums[$csv_line[0]] = [];

        for($i = 0; $i < count($csv_line); $i++){

            foreach($cell_indices as $key => $val){
    
                if(in_array($i, $val)){
                            
                    if(isset($sums[$csv_line[0]][$key])){
                        $sums[$csv_line[0]][$key][] = $csv_line[$i];
                        
                    }
                    else $sums[$csv_line[0]][$key] = [$csv_line[$i]];
                }
        
            }

        }


    }
   
}

fclose($fp) or die("can't close file");

$avgs = [];
// do actual summing
foreach($sums as $key => $val){

    $avgs[$key] = [];
    foreach($val as $k => $v){

        $filtered = array_filter($v, 'is_numeric');
        if(count($filtered) == 0) continue;

        $avgs[$key][$k] = array_sum($filtered)/count($filtered);
    }
    

}


$header = ['dose'];
foreach($avgs as $k => $v){

    $header = $header + array_keys($v);
    //array_push($header, array_keys($v));
    $tissues = ['colorectal'] + array_keys($v);
    break;
}


$arr = [];
foreach($avgs as $k => $v){

    $dose = explode("::", $k)[1];

    $temp = [$dose];

    foreach($tissues as $key => $val){

        if(!isset($v[$val])) $temp[] = "";
        else $temp[] = $v[$val];

    }

    $arr[] = $temp;

}


/*foreach($avgs as $k => &$v){
    asort($v);
}
print_r(array_slice($avgs, 0, 5, true));
*/

$file = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/dasatinib-primary-tissue-specificity.csv','w+');  

fputcsv($file, $header );

foreach ($arr as $row)
  {


  fputcsv($file, $row);
  }

fclose($file); 



?>