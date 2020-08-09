import configparser

config = configparser.RawConfigParser()
config.read('conf.ini')

def GetConfig():
  for i in config:
    for t in i:
      t = str(t)
  return config