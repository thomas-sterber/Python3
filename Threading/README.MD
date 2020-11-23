# Python3 threading 101

## basics
  import threading
  
  function th1 als thread th anlegen
    th = threading.Thread(target=th1)
  
  thread th starten
    th.start())
  
  
    th.is_alive()
    threading.active_count()
  
  Auf Beendigung eines Threads warten bevor es weiter geht
    th.join()
    
## examples scripts
