import json

with open("rally.json") as rally_json:
  data = json.load(rally_json)
  print "duration, nova.boot_server,vm.wait_for_ping,vm.wait_for_ssh,vm.run_command,nova.delete_server"
  for guest in data[0]["result"] :
    guest_csv="%s" % guest["duration"]
    for atomic in guest["atomic_actions"] :
      guest_csv="%s,%s" % (guest_csv,guest["duration"])
    print guest_csv
