<?php

$fp = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/screen_cads_only.csv','r') or die("can't open file");

$arr = []; // create cells assoc array


$i = 0;
while($csv_line = fgetcsv($fp,10000, ',')) {
   
 
    if($i == 0){
        $i++;
        continue;
    }

    
    // Mepivacaine,10,2,2.5,0,0.625,5,0.15625,1,0.0390625,0,0.00976562,0,0.0024414,1,0.00061034,0

    //$dilutions = [10 => 0, 2.5 => 0, 0.625 => 3, .156 => 3, .039 => 3, .0098 => 4, .0024 => 4, .0006 => 4];



   if(!isset($arr[$csv_line[506]])){
    $arr[$csv_line[506]] = [explode("::", $csv_line[0])[1]];    
   }
   else{
    $arr[$csv_line[506]][explode("::", $csv_line[0])[1]] = 0;  
   }

    $cnt = 0;
    foreach($csv_line as $key => $val){
        if(is_numeric($val) && $val < -1) $cnt++;
    }

    $arr[$csv_line[506]][explode("::", $csv_line[0])[1]] = $cnt;

   
}
//print_r($cells);
fclose($fp) or die("can't close file");

foreach($arr as &$arr2){
    krsort($arr2);
}

$arr0 =[];

//print_r(array_slice($arr, 0, 5));
//die();

foreach($arr as $arr2 => $val){

    if(!isset($arr0[$arr2])){
        $arr0[$arr2] = [];
    }

    if(is_array($val)==false) continue;



    foreach($val as $key => $val2){

        $dilution = $key;

        //if(in_array($dilutions, round(explode("::", $csv_line[0])[1]), 0));
        if($dilution > 9) $dilution = "10";
        elseif($dilution > 2.4) $dilution = "2.5";
        elseif($dilution > 0.62) $dilution = "0.625";
        elseif($dilution > 0.155) $dilution = "0.156";
        elseif($dilution > 0.038) $dilution = "0.039";
        elseif($dilution > 0.009) $dilution = "0.0097";
        elseif($dilution > 0.0023) $dilution = "0.0024";
        elseif($dilution > 0.0005) $dilution = "0.0006";
        else continue;

        $arr0[$arr2][$dilution] = $val2;
    }

}

$file = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/screen_cads_only_filtered-v2.csv','w+');  

fputcsv($file, ['drug', "10", "2.5", "0.625", "0.156", "0.039", "0.0097", "0.0024", "0.0006"] );

foreach ($arr0 as $key => $val)
  {
    $temp = [$key];

    foreach ($val as $key2 => $val2){
        //$temp[] = $key2;
        $temp[] = $val2;
    }

  fputcsv($file, $temp);
  }

fclose($file); 


//print_r(array_slice($sums0, 0, 5, true));


?>