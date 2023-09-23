---
title: "The DigitalOcean Compass"
date: 2022-03-29T10:50:52-05:00
draft: true
categories: ["infra"]
---
### What's this compass about?
When you get a new VPS instance from DigitalOcean to set up an application and have control over your LinuxBox - there is a small gap to setup the instance the right way as, the default user is `root`.  
`Root` can be evil when teams members use their keys to log into the box. So some basic administration work is required when you launch an Ubuntu Box with DigitalOcean. This compass can help you be prepared for a better sailing experience.

* New User & setting up keys.
* Permissions for the new user.

```shell
sudo apt update
sudo apt upgrade

useradd new_user
usermod -a -G sudo new_user
usermod -a -G docker new_user

chown -R new_user:new_user /home/new_user/
chown root:root /home/new_user
chmod 700 /home/new_user/.ssh
chmod 644 /home/new_user/.ssh/authorized_keys


ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 22
ufw enable
```