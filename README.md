# Migri Queue 

You can send email or sms or whatsapp notification daily to your devices with this code to see your application status on Finnish immigration office website. This project is intended for fun and not for commercial use! Please keep your private token or any sensitive info secret! 

# on you local linux macine with cron schedule

## Install dependent packages

```
pip install selenimum
pip install webdriver-manager
```

## SMTP server error then activate Display unlock captcha

* https://accounts.google.com/DisplayUnlockCaptcha

## Running python script with CRON linux with scheduling

```
crontab -e
crontab -l
```

Ref: https://crontab.guru

## See system log 

```
tail -f /var/log/syslog
```

# Migri Queue on gitlab ci/cd pipeline 

## Schedule your pipeline on Gitlab.

The gitlab piepline yml file is included there. Create a private repo and push the codes with necessray cahgens and schedule a ci cd pipelie, which will send you notification according to your choosen time!
