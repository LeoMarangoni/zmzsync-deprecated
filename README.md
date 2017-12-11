# zmzsync

Zmz sync was made to facillitate account migration between zimbra servers inspired in imapsync.

For now it only migrates full accounts without to many options, but it will be improved over time

------

Get Started:
-----

> - Clone this repository
> - pip install requeriments.txt
> - execute zmzsync.py


### **Help Menu:**
```help
  -h, --help            show this help message and exit

  --host1 HOST1         Source zimbra server

  --host2 HOST2         Destination zimbra server
  
  --user1 USER1         User to login on host1

  --user2 USER2         User to login on host2

  --password1 PASSWORD1
                        Password for user1

  --password2 PASSWORD2
                        Password for user2

  --authuser1 AUTHUSER1
                        User to auth with on host1

  --authuser2 AUTHUSER2
                        User to auth with on host2
```

### **Docker:**
This project was created to be used like a plugin for [Hermes-API](https://github.com/LeoMarangoni/hermes). Hermes plugins are integrated using docker images, so this project has a Dockerfile to be builded.
#### Pull it form docker hub: [marangoni/zmzsync](https://hub.docker.com/r/marangoni/zmzsync/)

```bash
docker pull marangoni/zmzsync
```
