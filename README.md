<div align=center>

## 𝐇𝐞𝐫𝐨𝐤𝐮 𝐃𝐞𝐩𝐥𝐨𝐲 𝐮𝐬𝐢𝐧𝐠 𝐆𝐨𝐨𝐠𝐥𝐞 𝐂𝐨𝐥𝐚𝐛

### <img src="https://graph.org/file/504ba776ef0724a4ae85b.png" width="25" alt="Google Colab Logo"> 𝐆𝐨𝐨𝐠𝐥𝐞 𝐂𝐨𝐥𝐚𝐛 : [𝐃𝐞𝐩𝐥𝐨𝐲 𝐋𝐢𝐧𝐤](https://colab.research.google.com/drive/18_-tQqddc9VgQW7959O9U-N0mYrDIJBa)

</div>

# Deploy on Heroku

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/Tamilupdates/ZML-X)

**Important Note**
1. Upload all of your private files here: `config.env`, `token.pickle`, `rcl.conf`, `accounts.zip`, `shorteners.txt` etc...

**Mandatory Veriables in Config**

- `UPSTREAM_REPO`: Your github repository link, if your repo is private add `https://<deploy_token>:<empty_password>@gitlab.com/<your_username>/<repository_name>
` format. `Str`.
  - **NOTE**: Don't forget to remove '<' and '>' . Follow [**THIS TUTORIAL**](https://graph.org/GitLab-Upstream-Tutorial-06-02) to generate upstream repo. 
              - Any change in docker or requirements you need to deploy/build again with updated repo to take effect. 
              - **DON'T delete .gitignore file**. For more information read [THIS](https://github.com/Tamilupdates/ZML-X#upstream-repo-recommended).
- `UPSTREAM_BRANCH`: Upstream branch for update. Default is `upstream`. `Str`

- `BOT_TOKEN`: The Telegram Bot Token that you got from [BotFather](https://telegram.me/BotFather). `Str`
- `OWNER_ID`: The Telegram User ID (not username) of the Owner of the bot. `Int`
- `TELEGRAM_API`: This is to authenticate your Telegram account for downloading Telegram files. You can get this from <https://my.telegram.org>. `Int`
- `TELEGRAM_HASH`: This is to authenticate your Telegram account for downloading Telegram files. You can get this from <https://my.telegram.org>. `Str`

- `BASE_URL`: Add a valid `BASE URL` to use torrent selection. Copy it from your heroku app. Right click on `OPEN APP` and copy link address. Format of URL should be `https://APPNAME-IDENTIFIER.herokuapp.com/`, where `APPNAME` is the name of your heroku app and IDENTIFIER is an unic number. Example: `https://ZeeApp1-mjw69x6ex696.herokuapp.com/`. `Str`
- `TORRENT_TIMEOUT`: Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds. `Int`

------

## Deploy using CLI

- Deployment instructions uploaded [HERE](https://gist.github.com/Dawn-India/9be1ca66b392dee82bcbc8d7f7ebefe8)
- Carefully copy-paste every CMD one by one. If you miss maybe your BOT will not run.


---------------------------------------------------------------------------------------------


# Deploy to RAILWAY

**Important Note**
1. Upload all of your private files here: `config.env`, `token.pickle`, `rcl.conf`, `accounts.zip`, `shorteners.txt` etc...

**Mandatory Veriables in Config**

- `UPSTREAM_REPO`: Your GitLab  repository link, if your repo is private add `https://<deploy_token>:<empty_password>@gitlab.com/<your_username>/<repository_name>
` format. `Str`.
  - **NOTE**: Don't forget to remove '<' and '>' . Follow [**THIS TUTORIAL**](https://graph.org/GitLab-Upstream-Tutorial-06-02) to generate upstream repo. 
              - Any change in docker or requirements you need to deploy/build again with updated repo to take effect. 
              - **DON'T delete .gitignore file**. For more information read [THIS](https://github.com/Tamilupdates/ZML-X#upstream-repo-recommended).
- `UPSTREAM_BRANCH`: Upstream branch for update. Default is `upstream`. `Str`

- `BOT_TOKEN`: The Telegram Bot Token that you got from [BotFather](https://telegram.me/BotFather). `Str`
- `OWNER_ID`: The Telegram User ID (not username) of the Owner of the bot. `Int`
- `TELEGRAM_API`: This is to authenticate your Telegram account for downloading Telegram files. You can get this from <https://my.telegram.org>. `Int`
- `TELEGRAM_HASH`: This is to authenticate your Telegram account for downloading Telegram files. You can get this from <https://my.telegram.org>. `Str`

- `BASE_URL`: Valid `BASE URL` where the bot is deployed to use torrent web files selection. Read deployment instructions to generate.
`BASE_URL` should be in this format `https://<railway_app_name>.up.railway.app/` `Str`
- `TORRENT_TIMEOUT`: Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds. `Int`

------

## Deploy using CLI

- Deployment instructions uploaded [HERE](https://gitlab.com/-/snippets/2551167)
- Carefully copy-paste every CMD one by one. If you miss maybe your BOT will not run.
