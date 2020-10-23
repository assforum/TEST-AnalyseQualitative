<table>
  <tr>
    <th>Participant</th><th>texte</th><th>wordcloud</th><th>data</th>
  </tr>
  <tr>
    <td>

<?php 

$message = shell_exec("python C:/wamp64/www/TEST-AnalyseQualitative/trial.py");
//$command = escapeshellcmd('python C:\Users\Mohamed\AppData\Local\Programs\Python\Python38-32\python.exe C:/wamp64/www/TEST-AnalyseQualitative/trial.py');
//exec("python C:/wamp64/www/TEST-AnalyseQualitative/trial.py",$outputs,$status_code);
/*var_dump($status_code);
    $output = shell_exec($command);
    echo $output;
  */
  $directory = "C:/wamp64/www/TEST/participants/wordClouds/";
 $filecount = 0;
foreach (glob("participants/wordClouds/*.txt") as $filename) {
  $fileLines=file($filename);
$filecount = count($fileLines);
    echo "<h8> le nombre de participant est : ".$filecount."</h8>";
}
for ($x = 0; $x <= $filecount-1; $x++) {
    
    $filen="C:/wamp64/www/TEST-AnalyseQualitative/participants/tags/tags".$x.".txt";
  $tag = file($filen, FILE_IGNORE_NEW_LINES);
echo " <img src='C:/wamp64/www/TEST/participants/wordClouds/participant'".$x;
   }


   ?>
     </td>
     <td>
       <?php $str = file_get_contents("./exemple.txt");

preg_match_all('{(\d+\.\d+)}', $str, $m);
var_dump($m);
 ?>

     </td>
     <td>
       

     </td>
  </tr>

</table>

<?php 
/*
$lignes = file("exemple.txt"); 
            // affichage des renseignements
                echo "<table border=1>";
            // traitement de chaque ligne 
                for ($i=0; $i<count($lignes); $i++) 
                {
           
            // nouvelle ligne
        echo "<tr><th>Participant</th><th>texte</th><th>wordcloud</th><th>data</th></tr>";             
            // éclatement en éléments distincts
                $personne=explode(";",$lignes[$i]); 
            // pour chaque colonne
                for($j = 0; $j < count($personne); $j++)
                {               
            // nouvelle colonne
                    $filename="exemple.txt";
                    $str = file_get_contents("./exemple.txt");

preg_match_all('{(\d+\.\d+)}', $str, $m);
$a=var_dump($m);
                 
  

                echo "<tr><td>".($i+1)."</td><td>" . $filename. "</td><td><img src='participants/wordClouds/participant".$x.".png' width='100' height='50' /></td><td>". $personne[$j] ."</td>";
                }
            // fin de ligne
                echo "</tr>";
                }
                echo "</table>";
*/
   ?>