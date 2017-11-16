import numpy as np
import pandas as pd

# height, weight, body fat data
height = np.array([
        67.75,  72.25,  66.25,  72.25,  71.25,  74.75,  69.75,  72.5 ,
        74.  ,  73.5 ,  74.5 ,  76.  ,  69.5 ,  71.25,  69.5 ,  66.  ,
        71.  ,  71.  ,  67.75,  73.5 ,  68.  ,  69.75,  68.25,  70.  ,
        67.75,  71.5 ,  67.5 ,  67.5 ,  64.75,  69.  ,  73.75,  71.25,
        71.25,  71.  ,  73.5 ,  65.  ,  70.  ,  68.25,  72.25,  67.  ,
        68.75,  69.5 ,  70.  ,  71.5 ,  68.  ,  73.25,  67.5 ,  71.25,
        68.5 ,  66.75,  72.25,  69.  ,  67.75,  73.5 ,  67.5 ,  72.  ,
        68.  ,  69.5 ,  70.75,  65.75,  73.25,  68.5 ,  70.25,  67.  ,
        70.  ,  67.5 ,  70.75,  71.5 ,  69.25,  71.5 ,  71.5 ,  68.75,
        73.75,  64.  ,  65.75,  67.5 ,  69.5 ,  68.5 ,  70.25,  69.25,
        67.75,  67.25,  72.75,  70.  ,  69.25,  67.5 ,  67.25,  65.75,
        72.5 ,  73.  ,  70.  ,  69.5 ,  70.5 ,  71.75,  74.5 ,  77.75,
        73.25,  66.5 ,  68.25,  72.  ,  73.5 ,  72.  ,  71.25,  73.75,
        69.25,  68.5 ,  73.5 ,  74.25,  75.5 ,  69.25,  68.5 ,  70.  ,
        70.  ,  70.25,  71.75,  69.25,  72.75,  72.  ,  74.  ,  72.25,
        74.5 ,  71.5 ,  68.75,  66.75,  66.5 ,  67.  ,  68.75,  67.75,
        73.25,  69.75,  71.5 ,  70.5 ,  73.25,  66.75,  69.5 ,  69.75,
        70.75,  74.  ,  71.25,  75.  ,  71.  ,  69.5 ,  67.75,  72.25,
        77.5 ,  70.75,  72.75,  69.75,  72.5 ,  70.25,  69.  ,  74.5 ,
        72.25,  67.25,  73.5 ,  75.25,  69.  ,  72.25,  68.75,  71.5 ,
        72.25,  73.  ,  68.75,  70.5 ,  72.  ,  73.75,  68.  ,  72.25,
        69.5 ,  69.5 ,  67.75,  65.5 ,  71.  ,  71.5 ,  71.75,  69.25,
        67.  ,  71.5 ,  69.25,  74.5 ,  74.25,  68.  ,  67.25,  69.75,
        74.25,  71.5 ,  74.25,  72.  ,  72.5 ,  68.25,  69.25,  76.  ,
        70.5 ,  74.75,  72.75,  68.25,  69.  ,  71.5 ,  72.75,  67.5 ,
        70.25,  69.25,  71.5 ,  74.  ,  69.75,  73.  ,  65.5 ,  72.5 ,
        70.25,  70.75,  68.  ,  74.5 ,  71.75,  70.75,  73.  ,  64.  ,
        69.75,  70.  ,  71.75,  69.25,  70.5 ,  72.25,  67.5 ,  67.25,
        68.75,  66.75,  68.25,  74.25,  69.5 ,  68.5 ,  65.75,  71.75,
        71.5 ,  67.25,  67.5 ,  67.5 ,  72.25,  69.5 ,  69.5 ,  65.75,
        65.75,  68.25,  72.  ,  72.75,  68.5 ,  69.25,  70.5 ,  67.  ,
        69.75,  66.  ,  70.5 ,  70.  ])

weight = np.array([
        154.25,  173.25,  154.  ,  184.75,  184.25,  210.25,  181.  ,
        176.  ,  191.  ,  198.25,  186.25,  216.  ,  180.5 ,  205.25,
        187.75,  162.75,  195.75,  209.25,  183.75,  211.75,  179.  ,
        200.5 ,  140.25,  148.75,  151.25,  159.25,  131.5 ,  148.  ,
        133.25,  160.75,  182.  ,  160.25,  168.  ,  218.5 ,  247.25,
        191.75,  202.25,  196.75,  363.15,  203.  ,  262.75,  205.  ,
        217.  ,  212.  ,  125.25,  164.25,  133.5 ,  148.5 ,  135.75,
        127.5 ,  158.25,  139.25,  137.25,  152.75,  136.25,  198.  ,
        181.5 ,  201.25,  202.5 ,  179.75,  216.  ,  178.75,  193.25,
        178.  ,  205.5 ,  183.5 ,  151.5 ,  154.75,  155.25,  156.75,
        167.5 ,  146.75,  160.75,  125.  ,  143.  ,  148.25,  162.5 ,
        177.75,  161.25,  171.25,  163.75,  150.25,  190.25,  170.75,
        168.  ,  167.  ,  157.75,  160.  ,  176.75,  176.  ,  177.  ,
        179.75,  165.25,  192.5 ,  184.25,  224.5 ,  188.75,  162.5 ,
        156.5 ,  197.  ,  198.5 ,  173.75,  172.75,  196.75,  177.  ,
        165.5 ,  200.25,  203.25,  194.  ,  168.5 ,  170.75,  183.25,
        178.25,  163.  ,  175.25,  158.  ,  177.25,  179.  ,  191.  ,
        187.5 ,  206.5 ,  185.25,  160.25,  151.5 ,  161.  ,  167.  ,
        177.5 ,  152.25,  192.25,  165.25,  171.75,  171.25,  197.  ,
        157.  ,  168.25,  186.  ,  166.75,  187.75,  168.25,  212.75,
        176.75,  173.25,  167.  ,  159.75,  188.15,  156.  ,  208.5 ,
        206.5 ,  143.75,  223.  ,  152.25,  241.75,  146.  ,  156.75,
        200.25,  171.5 ,  205.75,  182.5 ,  136.5 ,  177.25,  151.25,
        196.  ,  184.25,  140.  ,  218.75,  217.  ,  166.25,  224.75,
        228.25,  172.75,  152.25,  125.75,  177.25,  176.25,  226.75,
        145.25,  151.  ,  241.25,  187.25,  234.75,  219.25,  118.5 ,
        145.75,  159.25,  170.5 ,  167.5 ,  232.75,  210.5 ,  202.25,
        185.  ,  153.  ,  244.25,  193.5 ,  224.75,  162.75,  180.  ,
        156.25,  168.  ,  167.25,  170.75,  178.25,  150.  ,  200.5 ,
        184.  ,  223.  ,  208.75,  166.  ,  195.  ,  160.5 ,  159.75,
        140.5 ,  216.25,  168.25,  194.75,  172.75,  219.  ,  149.25,
        154.5 ,  199.25,  154.5 ,  153.25,  230.  ,  161.75,  142.25,
        179.75,  126.5 ,  169.5 ,  198.5 ,  174.5 ,  167.75,  147.75,
        182.25,  175.5 ,  161.75,  157.75,  168.75,  191.5 ,  219.15,
        155.25,  189.75,  127.5 ,  224.5 ,  234.25,  227.75,  199.5 ,
        155.5 ,  215.5 ,  134.25,  201.  ,  186.75,  190.75,  207.5 ])

percentBodyFat = np.array([
        12.6,   6.9,  24.6,  10.9,  27.8,  20.6,  19. ,  12.8,   5.1,
        12. ,   7.5,   8.5,  20.5,  20.8,  21.7,  20.5,  28.1,  22.4,
        16.1,  16.5,  19. ,  15.3,  15.7,  17.6,  14.2,   4.6,   8.5,
        22.4,   4.7,   9.4,  12.3,   6.5,  13.4,  20.9,  31.1,  38.2,
        23.6,  27.5,  33.8,  31.3,  33.1,  31.7,  30.4,  30.8,   8.4,
        14.1,  11.2,   6.4,  13.4,   5. ,  10.7,   7.4,   8.7,   7.1,
         4.9,  22.2,  20.1,  27.1,  30.4,  24. ,  25.4,  28.8,  29.6,
        25.1,  31. ,  28.9,  21.1,  14. ,   7.1,  13.2,  23.7,   9.4,
         9.1,  13.7,  12. ,  18.3,   9.2,  21.7,  21.1,  18.6,  30.2,
        26. ,  18.2,  26.2,  26.1,  25.8,  15. ,  22.6,   8.8,  14.3,
        20.2,  18.1,   9.2,  24.2,   9.6,  17.3,  10.1,  11.1,  17.7,
        21.7,  20.8,  20.1,  19.8,  21.9,  24.7,  17.8,  19.1,  18.2,
        17.2,  21. ,  19.5,  27.1,  21.6,  20.9,  25.9,  16.7,  19.8,
        14.1,  25.1,  17.9,  27. ,  24.6,  14.8,  16. ,  14. ,  17.4,
        26.4,  17.4,  20.4,  15. ,  18. ,  22.2,  23.1,  25.3,  23.8,
        26.3,  21.4,  28.4,  21.8,  20.1,  24.3,  18.1,  22.7,   9.9,
        10.8,  14.4,  19. ,  28.6,   6.1,  24.5,   9.9,  19.1,  10.6,
        16.5,  20.5,  17.2,  30.1,  10.5,  12.8,  22. ,   9.9,  14.8,
        13.3,  15.2,  26.5,  19. ,  21.4,  20. ,  34.7,  16.5,   4.1,
         1.9,  20.2,  16.8,  24.6,  10.4,  13.4,  28.8,  22. ,  16.8,
        25.8,   0. ,  11.9,  12.4,  17.4,   9.2,  23. ,  20.1,  20.2,
        23.8,  11.8,  36.5,  16. ,  24. ,  22.3,  24.8,  21.5,  17.6,
         7.3,  22.6,  12.5,  21.7,  27.7,   6.8,  33.4,  16.6,  31.7,
        31.5,  10.1,  11.3,   7.8,  26.4,  19.3,  18.5,  19.3,  45.1,
        13.8,   8.2,  23.9,  15.1,  12.7,  25.3,  11.9,   6.1,  11.3,
        12.8,  14.9,  24.5,  15. ,  16.9,  11.1,  16.1,  15.5,  25.9,
        25.5,  18.4,  24. ,  26.4,  12.7,  28.8,  17. ,  33.6,  29.3,
        31.4,  28.1,  15.3,  29.1,  11.5,  32.3,  28.3,  25.3,  30.7])

# creating a dataframe 
bodyData = pd.DataFrame()
bodyData['height'] = height
bodyData['weight'] = weight
bodyData['percentBodyFat'] = percentBodyFat


