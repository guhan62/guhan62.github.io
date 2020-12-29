---
title: "[Guide] NextCloud on Ubuntu 18.04"
date: 2020-07-03T17:57:44-04:00
draft: false
categories: ['guide', 'nextcloud']
---

# 0. NextCloud, what's that?

*If you are not interested to read the intro -*
[Skip to the Guide](#1-the-guide-to-setting-up)

[NextCloud](https://nextcloud.com/), is a fork of [OwnCloud](https://owncloud.org/)   - being a suite of client-server software for creating and using file hosting services. Similar to 
Google Drive or DropBox where one can store Documents, photos and can share it with family and friends.  Nextcloud is free and open-source which allows the client to be in control of their data and files, and getting rid of third-party sites that offer the similar services. [Nextcloud Wiki](https://en.wikipedia.org/wiki/Nextcloud).
Nextcloud is a very vibrant community, and the application being modular the administrator can install tons of plugins from the [Nextcloud App Store](https://apps.nextcloud.com/) that can help the nextcloud clients harness the power of self-hosted cloud services rather than third party services.

## Why do I need it?
The question is really a tough one, when services are provided for free why bother pay for one. For me it boils down to one simple reason privacy and control. But you can argue,
* Server maintenance is tough and can be insecure if not set-up right initially.
* Application security can be compromised.

>**“Privacy isn’t about something to hide. Privacy is about something to protect. And that’s who you are. That’s what you believe in. That’s who you want to become. Privacy is the right to the self. Privacy is what gives you the ability to share with the world who you are on your own terms.”**
>
> -Edward Snowden

You may not hide anything today, but you are exposing your habits, behavior to every single trackers on these services. Google does claim that they do collect information from services that you are using and do not use it for [any marketing/promotional services](https://policies.google.com/privacy) and only to improve their services for you which is good, but that is a lot of data collected on you which can provide you relevant [ad experiences](https://policies.google.com/privacy#whycollect).

This puts you on a path, where your behavior begins to be controlled by external factors and decisions. We are completely hooked to digital services that is easy to understand from the usage of services, history to build a profile and be easily able to predict your behavior.

## Choose your Hero [VPC]!
There are multiple good Cloud services, 
* [Vultr](https://www.vultr.com/?ref=8035292) 
* [upCloud](https://upcloud.com/) 
* [DigitalOcean](https://www.digitalocean.com/), [AWS](https://aws.amazon.com), [Linode](https://www.linode.com/) 
* etc ...  

These vendors are good and used by many tech enthusiasts and companies.   
I personally use [Vultr](https://www.vultr.com/?ref=8035292), because it sounds cool!  **:warning:Affiliate Link:warning:** :point_right:[Vultr](https://www.vultr.com/?ref=8035292)  

*After you give this post a read and planning to sign up for Vultr, do click on the link.*  
**Virtual Cloud, can fuel your side-projects and hackathon projects for any web-application or services**. Once your idea is evolved - Host and share it. Feedback and ideas from other devs, make you a better developer. I have an Ubuntu server with the basic 5$ plan which is reasonable as of now.

## Prerequisites:
This guide requires two essential steps, in a VPC. Guide being targeted for Ubuntu 18.04 users, it recommends setting up your VPC with basic admin utilities like SSH, Root/Users and Firewall.  

* **VPC Secure Setup** - Initial Secure configuration is vital for any VPC. [Refer Vultr Doc](https://www.vultr.com/docs/initial-secure-server-configuration-of-ubuntu-18-04)  

*  **LAMP Stack** - Nextcloud is a php application so the easiest stack to mount our application on would be the LAMP stack. [Refer DigitalOcean Guide on LAMP][1]

*  **(Optional) DNS Record** - Any instance of hosted web-application that is publicly accessible with data flowing from client/server requires secured transport. For this we need to enable SSL encryption on our Server for the Nextcloud application. Nextloud offers [self-signed SSL certificates](https://docs.nextcloud.com/server/12/admin_manual/installation/source_installation.html#enabling-ssl-label) they are not good being on a public domain as they are comparatively weak. So it is better to go for commercial vendors (from Domain vendors) or using [Let's Encrypt](https://letsencrypt.org/), which offers a free trusted SSL certificate for your server.

---  

# 1. The Guide to setting up!
**Ensure basic [VPC setup](https://www.vultr.com/docs/initial-secure-server-configuration-of-ubuntu-18-04) is completed**
Host being a Ubuntu 18.04 (Linux platform).

### PHP Deps
php is a very popular scripting language suited for web-development. Many popular applications like Wordpress, Drupal, Facebook use Php as their back-end. Nextcloud is a php application. Installing `php 7.2`  latest and necessary php packages for Nextcloud is vital for functioning. 

* Installing php and additional pachages  
```shell
sudo apt-get install libapache2-mod-php7.2
sudo apt-get install php7.2-gd php7.2-json php7.2-mysql php7.2-curl php7.2-mbstring
sudo apt-get install php7.2-intl php-imagick php7.2-xml php7.2-zip
```
* The base packages for nextcloud core are provided by `libapache2-mod-php7.2`, having the following packages,
```shell
bcmath bz2 calendar Core ctype date dba dom ereg exif fileinfo filter ftp gettext
hash iconv libxml mhash openssl pcre Phar posix Reflection session shmop SimpleXML
soap sockets SPL standard sysvmsg sysvsem sysvshm tokenizer wddx xmlreader xmlwriter zlib .
```
[Refer NextCloud PHP Prerequisites](https://docs.nextcloud.com/server/15/admin_manual/installation/source_installation.html#prerequisites-label)

## Database for NextCloud
Let's set up a Nextcloud user and a database Nextcloud exclusively for our Nextcloud Application.

```Bash
sudo mysql -u root -p

CREATE DATABASE nextcloud;

CREATE USER 'nextcloud'@'localhost' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextcloud'@'localhost';

FLUSH PRIVILEGES;
\q
```

## Installing Nextcloud on server
Web Servers, serve content from a root folder. Similar to when you start a localhost with a web-framework or file-sharing network in your company or college. You can browse all content within the directories that have permissions. In our case the top-level directory is `/var/www` which serves as the document root for Apache HTTP server.

For good examples on Virtual Hosts refer to this [doc][2].  
Virtual hosts are clones of the hosts with different virtual addresses but point to the address requested by a client. Now let's set up our site directory and set permissions.

```Bash
# Link can be outdated you can go to link below for the active link
# https://nextcloud.com/install/#instructions-server 

wget https://download.nextcloud.com/server/releases/nextcloud-19.0.0.zip -O ~/Downloads
unzip ~/Downloads/nextcloud-19.0.0.zip

cd /var/www
sudo mkdir nextcloud
sudo mv ~/Downloads/nextcloud-19.0.0/* /var/www/nextcloud/
sudo chown -R $USER:$USER /var/www/nextcloud
sudo chmod -R 755 /var/www
```
The ownership is set to user-level, for the application to access it's content at a user level and not write or exec malicious code without privileges.
If you have trouble with setting directory permissions :sweat_smile:, consider a [chmod calculator][3].  

Let's configure our Firewall first, so that Heimdall can really guard the gateway

```Terminfo
vultr@vpc:~$ sudo ufw app list
Available applications:
	Apache
	Apache Full
	Apache Secure
	OpenSSH
```	
The above applications indicate they require firewall permissions. Now `Apache Full` is the recommended profile as it enables both HTTPS/HTTP traffic over ports `80` and `443`.  
Let's allow the 'Apache Full' configuration.  
`sudo ufw allow 'Apache Full'`  
You can check the status of your firewall with,  
`sudo ufw status`  

It will include Apache Full as an active profile on your Firewall.


## Apache WebServer The Gatekeeper!
{{< img src="./Apache_Heimdall_proc.jpeg" 
	title="Apache Heimdall" caption="Image Credits WallpaperCave & WikiMedia Commons" 
	>}}

Now we have setup the structure of our nextcloud application, and now let's fortify it. 
Virtual Hosts are multiple entry points to the same location. Imagine Heimdall as Apache and each entry-point into Asgard is a virtual host.  

```Bash
# Default Config /etc/apache2/sites-available/example.com.conf
sudo nano /etc/apache2/sites-available/nextcloud.conf
```

* Now writing the Apache configuration for our nextcloud instance, here the guide recommends getting a domain name for cheap on namecheap.com, name.com or godaddy.com rather than self-signed SSL certificates, thought self-signed are easy they are good in a LAN or a local setting not suitable over a Cloud setting, as Apache ships with a default SSL certificate If you are willing to go ahead with a domain name it would be easier for **Let's Encrypt** to issue certificates that are reliable and free.

### Default SSL
* This path is the default SSL, write-up a configuration for NextCloud on Apache Sites.
	```bash
	sudo nano /etc/apache2/sites-available/nextcloud.conf  
* Copy paste the following configuration  
	```xml
	Alias /nextcloud "/var/www/nextcloud/"
	<Directory /var/www/nextcloud/>
	Options +FollowSymlinks
	AllowOverride All
	<IfModule mod_dav.c>
		Dav off
	</IfModule>
	SetEnv HOME /var/www/nextcloud
	SetEnv HTTP_HOME /var/www/nextcloud
	</Directory>
* Enable the site configuration for Nextcloud and rewrite the Apache binaries, and also enable the SSL module for Apache and enable the default-ssl config to allow https traffic via default SSL certificate
 	```Bash
	sudo a2ensite nextcloud
	sudo a2enmod rewrite headers env dir mime
	sudo a2enmod ssl
	sudo a2ensite default-ssl
	sudo systemctl restart apache2
### Let's Encrypt provided SSL certificates
* Assuming `my_domain` is assigned with an A record with correct key/value pairs of the public IP from your Vultr Dashboard is setup with your domain vendor.
* If setting up with a procured domain `my_domain`, then open up the configuration file
	```Bash
	sudo nano /etc/apache2/sites-available/nextcloud.conf```
* Paste the following configuration
	```xml
	<VirtualHost *:80>
	DocumentRoot /var/www/nextcloud
	ServerName my_domain
	Redirect permanent / https://my_domain/
	<Directory /var/www/nextcloud>
		Options +FollowSymlinks
		AllowOverride All
		<IfModule mod_dav.c>
			Dav off
	</IfModule>
	</Directory>
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
	</VirtualHost>
* Restart Apache after enabling the site-configration and rewriting Apache Binaries,
	```Bash
	sudo a2ensite nextcloud
	sudo a2enmod rewrite headers env dir mime
	sudo systemctl restart apache2	
Let's break few of the jargon,
* `Options +FollowSymLinks` - Imagine you have a Media Network and you have a neat setup of your media folders in your home folder would you consider to move it around to `/var/www/nextcloud` - No Way - Just create a softlink of the directory and point in your application now the WebServer can follow the path to serve Media. [Refer Doc][4]
* `Dav? mod_Dav?` - [WebDAV][7] Protocol serves file authoring service over HTTP, NextCloud has an option to use this protocol. But in a simple, few-user setup we need not worry about this. If interested refer [Refer Manual][8].

## Securing our NextCloud instance
* Certbot is a software by Let’s Encrypt which automates major of the work for creating a SSL certificate for your website. Let’s Encrypt Certificates are valid only for 90 days. But, the certbot runs a cron job to renew the certificate if bound for expiration.  
* Installing Certbot with apt and additional dependencies.
	```Bash
	# Installing the certbot package with inclusing the Repo PPA
	sudo apt-get install software-properties-common
	sudo add-apt-repository universe
	sudo add-apt-repository ppa:certbot/certbot
	sudo apt-get update  
	# Installing Python3 package for certbot
	sudo apt-get install certbot python3-certbot-apache	
* Running the certbot command on `my_domain` with apache option, generates configuration for Apache for a default SSL config.
	```Bash
	sudo certbot --apache -d my_domain -d www.my_domain
* The setup process if run for the first time asks for additional details, complete it and then the total setup is done!
[Refer certbot docs](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache)

* Now add the `my_domain` to trusted domain in the nextcloud configuration found under `/var/www/nextcloud/config.php`
	```php
	'trusted_domains' =>
		array (
		0 => 'localhost',
		1 => 'my_domain',
		2 => 'public_ip'  # Replace with your public IP if required
	),
* Open `https://my_domain` on your browser where you will be greeted with installation screen and do the final configuration setup for the Database or also can be done manually over the config.php. 

## Sight of Life from Cloud!
Enter the domain in your browser and voila. The work is done. Now you can configure everything via the Nextcloud web interface. Nextcloud is really useful for universities, file-sharing in companies secured and totally in control.

**Welcome to Nextcloud!**

E-mail configuration is pending will update this blog once I test the services.

[1]: <https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04> "DigitalOcean : LAMP Stack setup on Ubuntu 18.04"
[2]: <https://httpd.apache.org/docs/2.4/vhosts/examples.html> "Apache DOCS : vHost examples"
[3]: <https://chmod-calculator.com/> "Chmod Calculator"
[4]: <https://httpd.apache.org/docs/2.4/mod/core.html#allowoverride> "Apache DOCS : Config - AllowOverride"
[5]: <https://httpd.apache.org/docs/2.4/mod/core.html#options> "Apache DOCS : Options"
[6]: <https://httpd.apache.org/docs/2.4/mod/mod_dav.html> "Apache Docs : Mod Dav"
[7]: <https://en.wikipedia.org/wiki/WebDAV> "WebDAV Protocol Wiki"
[8]: <https://docs.nextcloud.com/server/18/user_manual/files/access_webdav.html> "Nextcloud WebDav Manual"
[9]: <https://www.cs.nmsu.edu/~istrnad/cs480/lecture_notes/dns_record_types.jpg> "Domain Records"
[10]: <https://certbot.eff.org/lets-encrypt/ubuntubionic-apache> "Let's Encrypt Apache configuration"

### References:
1. [Nextcloud Manual](https://docs.nextcloud.com/server/16/admin_manual/installation/source_installation.html#example-installation-on-ubuntu-18-04-lts-server)
2. [Certbot Docs](https://certbot.eff.org/docs/)
3. [Apache httpd web server Docs](https://httpd.apache.org/docs/2.4/mod)