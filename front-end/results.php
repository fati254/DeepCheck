<!DOCTYPE html>
<html>
<head>
    <title>Résultats</title>

    <!-- Lien vers la feuille de style CSS pour le design de la page -->
    <link rel="stylesheet" href="css/style.css">
</head>

<body>

<!-- Titre principal de la page des résultats -->
<h1>Résultats d'analyse</h1>

<?php
// Vérifier si la variable "result" existe dans l'URL (méthode GET)
if (isset($_GET['result'])) {

    // Afficher le résultat envoyé dans l'URL
    echo "<p>Résultat: " . $_GET['result'] . "</p>";

} else {

    // Message affiché si aucun résultat n'a été envoyé
    echo "<p>Aucun résultat disponible</p>";
}
?>

<!-- Lien pour retourner au tableau de bord (dashboard) -->
<a href="dashboard.php">Retour</a>

</body>
</html>