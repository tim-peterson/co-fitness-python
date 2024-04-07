<?php


$genes = ['LPIN1'];

$cells = []; // create cells assoc array

foreach($genes as $gene){

  $fp = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/'.$gene.' CRISPR (DepMap Public 22Q4+Score Chronos).csv','r') or die("can't open file");

  $i = 0;
  while($csv_line = fgetcsv($fp,1024, ',')) {
    
      if($i == 0){
        $i++;
        continue;
      } 

      if(isset($csv_line[3]) ){
          $cells[$csv_line[3]][] = $csv_line[1];
      }
      else{
          $cells[$csv_line[3]] = [$csv_line[1]];
      }
    
  }

}

//print_r(array_slice($avgs, 0, 5, true));

$file = fopen('/Volumes/GoogleDrive/.shortcut-targets-by-id/1kwxxl9k8ktmM4Mf0b1jQ2wUiKz5Vjtte/DepMap/'.implode('-', $genes).'-cancer-types-depmap0.csv','w+');  


fputcsv($file, ['cancer type', 'avg', 'indiv vals...'] );

foreach ($cells as $key => $val){
    if(count($val) == 0) $avg = 0;
    else $avg = array_sum($val)/count($val);

    fputcsv($file, [$key] + [$avg] + $val );
}

fclose($file); 



?>