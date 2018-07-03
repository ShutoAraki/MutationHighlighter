# MutationHighlighter
This is an extension package for UCSF Chimera that visualizes missense mutations with unknown significance that could be causes of rare genetic diseases.

This package allows users to see where the potentially problematic residues are in certain protein as well as its possible effect on their neighbor residues by highlighting hydrogen bonds.

The following is a protein called Lactate dehydrogenase A (LDHA) with its mutations obtained from ClinVar database.


![alt text]( "LDHA")


@author: Shuto Araki

@created: December, 2017

# Requirements
UCSF Chimera Production version 1.11.2 or above
Download the software [here](http://www.cgl.ucsf.edu/chimera/download.html).

# Install Procedure
1. Download this repository.
2. Open the UCSF Chimera.
3. Go to Preferences >> Tools
4. Add the path to wherever you saved the repository to Locations section.
5. On the same settings page, also check IDLE and add it on your toolbar.
6. Open the IDLE from home screen and type ```python import MutationHighlighter.gui ```
7. There will be a new icon on your toolbar and that's my package!
