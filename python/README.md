In any device for which you want to use the device-agnostic Python API, you must add the path of the ```abstract_classes``` folder and the implementation you want in ```PYTHONPATH```. For example for the NAO case:

```
export PYTHONPATH=$PYTHONPATH:/home/nao/rapp-robots-api/python/abstract_classes
export PYTHONPATH=$PYTHONPATH:/home/nao/rapp-robots-api/python/implementations/nao_v4_naoqi2.1.4
```

Then any python-based application can be executed using the rapp-robot-api implementation for NAO.
