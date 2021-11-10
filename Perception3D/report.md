1) 1.  Mire: Symmetric Circles.

   3.  objecPoints correspond aux points dans le plan de la mire, et imgPoints
       correspond aux points correspondant dans l'image.

   5.  Cf cours

   6.  ?

   7.  La figure obtenue représente la position des mires dans l'espace pour
       chaque acquisition.

   8.  La figure obtenue représente la Root Mean Square Error, soit pour
       chaque mire étudiée, la distance en pixels entre les point projetés et
       les points reprojetés après la reconstruction 3D.

   9.  Pour améliorer la calibration, on peut étudier les RMS pour identifier
       les outliers et vérifier si leurs acquisitions n'ont pas été mal faites.
       Les facteurs importants sont spécifiés dans le cours.

   10. RMS: 0.394053715049852
       camera matrix:
        [[678.04925032   0.         315.69044912]
        [  0.         675.59676374 194.13795736]
        [  0.           0.           1.        ]]
       distortion coefficients:  [ 0.18138071 -0.49320258 -0.0111219  -0.00055014  0.2524249 ]

2) 11. Une correction map correspond à une méthode qui permet à partir de
        la position d'un pixel dans l'image déformé, d'obtenir la position
        correspondante dans l'image corrigé.

    14. On observe dans notre image une distortion radiale, visible grâce aux
        coussinets sur les bords de l'image, ainsi que de la distortion
        tangentielle, visible car les coins ne correspondent à l'image
        d'origine.

    15. ?

3)  16. Cf cours

    17. RMS: 0.18219724135784668
        Left camera matrix:
         [[1.05636412e+03 0.00000000e+00 9.62640001e+02]
         [0.00000000e+00 1.05667851e+03 6.12172612e+02]
         [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
        Left distortion coefficients:  [-0.26237681  0.13443624  0.00044232  0.00031454 -0.04058712]

        Right camera matrix:
         [[1.05323710e+03 0.00000000e+00 9.54063331e+02]
         [0.00000000e+00 1.05345351e+03 6.08116049e+02]
         [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
        Right distortion coefficients:  [-0.26106338  0.13154953  0.00043334  0.00062923 -0.03734463]

        Rotation matrix:
         [[ 9.99930963e-01  1.17330077e-02 -6.37171968e-04]
         [-1.17167200e-02  9.99703091e-01  2.13646598e-02]
         [ 8.87654505e-04 -2.13557193e-02  9.99771547e-01]]

        Translation:  [-0.27060746  0.00258373  0.00029731]

    18. Certaines images posent problème, en particulier 1, 2, 27, 28 car elles
        correspondent aux images où la mire est la plus proche de l'objectif

    19. À rectifier des images stéréos.

    20. On observe un effet de bulle (un trou noir au milieu de l'image).

    21. Après avoir corrigé l'effet de bulles, on affiche les lignes epipolaires
        et on observe qu'elles sont correctement alignées, on en conclut que
        la calibration est correctement effectuée.
