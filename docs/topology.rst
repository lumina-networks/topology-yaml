Topology-Yaml Commands
**********************

The Topology-Yaml tool provides the capability to create, read, and delete provided topology files.

Commands
--------

Create
~~~~~~

**Topology-Yaml Create** takes the path to a file as a filename argument and two mutually exclusive options, --data and --json, describing the format of the source topology file.

.. literalinclude:: create.txt


Read
~~~~

**Topology-Yaml Read** takes the filename argument which is the path to the file to read. The --format argument describes the output format and can be either yaml, yml or json.


.. literalinclude:: read.txt


Delete
~~~~~~

**Topology-Yaml Delete** takes the filename argument which is the path to the file that will be deleted.


.. literalinclude:: delete.txt

