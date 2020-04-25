#!/usr/bin/env python3

import argparse
from sys import stderr

from lms import Server

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("host", help="hostname of the Logitech Media Server")
  parser.add_argument("port", help="port of the Logitech Media Server", type=int)
  #parser.add_argument("player_id", help="Id of the player/squeezebox")
  known_args, unkown_args  = parser.parse_known_args()
  lms_args = [i for i in unkown_args if not i.startswith("--")]
  lms_kwargs = dict([i[2:].split('=') for i in unkown_args if i.startswith("--")])
  server = Server(known_args.host, known_args.port)
  if 'player' in lms_kwargs:
    server.update()
    try:
      player = server.player(lms_kwargs['player'])
    except (KeyError) as e:
      print(server, file=stderr)
      raise Exception("Player {} not found".format(known_args.player_id)) from e
    del lms_kwargs['player']
    if (lms_args or lms_kwargs):
      player.query(*lms_args, **lms_kwargs)
    else:
      print(player)
  else:
    if (lms_args or lms_kwargs):
      print(server.query(*lms_args, **lms_kwargs))
    else:
      server.update()
      print(server)

if __name__ == "__main__":
  main()
