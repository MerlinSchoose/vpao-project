2) 3.  On observe des points aberrants autour de la boîte qui n'ont rien à voir
       avec le sol.

   4.  L'algorithme prends un nombre de voisins autour du point étudié, puis
       calcule la moyenne des distances entre ces voisins et élimine ceux qui
       sont plus loin que la moyenne des distances du pointCloud.

   5.  Cf cours: Le calcul est effectué en se basant sur un ACP.

   6.  En théorie la majorité des normals du sol ont la même direction et
       représentent la majorité des normals totales du pointCloud. On peut donc
       considérer que la normale du sol est la normale la plus présente.

   7.  Pour aligner le sol sur le plan horizontal, on peut créer un matrice de
       rotation permettant de transformer la normale estimée du sol en un vecteur
       (0, 1, 0) et d'appliquer cette matrice à toutes les normales.

3) 12. Cf cours
       registration::RegistrationResult with fitness=1.000000e+00,
       inlier_rmse=2.316329e-03, and correspondence_set size of 3048

   13. Cf cours (Ça dégoute)

   14. registration::RegistrationResult with fitness=1.000000e+00,
       inlier_rmse=1.701586e-03, and correspondence_set size of 3048

   15. On pourrait appliquer la pipeline sur chaque nuage de points en faisant
       une acquisition équivalente, puis comparer les RMSE et considérer toutes
       pièces dont la RMSE est supérieure à un certain threshold comme
       défectueuse. Cette solution est relativement adaptée, mais elle n'est pas
       parfaite, car elle introduit un threshold arbitraire.
