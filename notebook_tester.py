import os
import papermill as pm


pm.execute_notebook(
   './Intro.ipynb',
   'desihigh/pmout/Intro.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './DESI.ipynb',
   'desihigh//pmout/DESI.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './DesigningDESI.ipynb',
   'desihigh/pmout/DesigningDESI.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './SnowWhiteDwarf.ipynb',
   'desihigh/pmout/SnowWhiteDwarf.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './Clusters.ipynb',
   'desihigh/pmout/Clusters.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './FromMayaToDESI.ipynb',
   'desihigh/pmout/FromMayaToDESI.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './SupernovaeBrain.ipynb.ipynb',
   'desihigh/pmout/SupernovaeBrain.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

os.chdir('./Espanol/')

pm.execute_notebook(
   './Intro_es.ipynb',
   '../desihigh//pmout/Intro_es.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './DESI_es.ipynb',
   '../desihigh/pmout/DESI_es.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './DesigningDESI_es.ipynb',
   '../desihigh/pmout/DesigningDESI_es.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './SnowWhiteDwarf_es.ipynb',
   '../desihigh/pmout/SnowWhiteDwarf_es.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(
   './Clusters_es.ipynb',
   '../desihigh/pmout/Clusters_es.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)

pm.execute_notebook(                                                                                                                                                                                                                      
   './FromMayaToDESI_es.ipynb',                                                                                                                                                                                                     
   '../desihigh/pmout/FromMayaToDESI_es.ipynb',                                                                                                                                                                                             
   parameters=dict(alpha=0.6, ratio=0.1)                                                                                                                                                                                                   
) 

pm.execute_notebook(                                                                                                                                                                                                                      
   './SupernovaeBrain_es.ipynb',                                                                                                                                                                                                     
   '../desihigh/pmout/SupernovaeBrain_es.ipynb',                                                                                                                                                                                              
   parameters=dict(alpha=0.6, ratio=0.1)
)            
