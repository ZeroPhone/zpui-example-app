# Example ZPUI app

This is an example app for ZPUI. You can easily use this as a base for your app!

Features:

- A demo for Menu and PrettyPrinter UI elements
- A demo on how to easily work with external files
- A way to quickly add tests to your app
- An easy rename script to make this app your own
- Logging examples (it's like print statements but way better!)
- An extensive readme you are reading right now :3
- Dual licensing (Apache 2.0, OR GPL 3.0 or later) to allow for license compatibility

## How-to

Modify this snippet to your liking, replacing the app name and AUTHOR in the URL: (**dev-only**)

```bash
git clone https://gitlab.com/AUTHOR/zpui-NEWAPPNAME
cd zpui-NEWAPPNAME
sudo python install.py # don't need to use sudo for emulator!
```

* To **rename** this app template (required to start development), run `python3 rename.py zpui_NEWAPPNAME` to rename the app to whatever you want. (**dev-only**)
* To **change** the app, edit `src/zpui_NEWAPPNAME/app.py`; add other Python files etc. as needed.
* To **install** the app, run `sudo python install.py`. Omit `sudo` if you're installing the app into an emulator, for local development or otherwise.
  ** **NOTE**: You won't need this command after making changes to `app.py` or other files in `src/zpui_NEWAPPNAME/`, becase those changes will apply automatically. You will only need to re-run this command if you change `pyproject.toml`. (**dev-only**)
* To **edit the app metadata**, edit `pyproject.toml` and adjust details as needed (should only be needed once). (**dev-only**)
* To **load** the app, run `sudo systemctl restart zpui.service` or use `Restart ZPUI` main menu entry. If you're using the emulator, just rerun `python main.py`.
* To **update** the app, just run `git pull` inside of this folder.
* To **debug** the app, run `sudo journalctl -fu zpui.service`, or see the output of `python main.py` if you're running the emulator.

When publishing your app, remove the **rename**, maybe **change**, **NOTE**, and **edit the app metadata** sections above, to avoid user confusion. (**dev-only**)

Disclaimer: currently, ZPUI apps will run as `root`, unless you're running an emulator. Specifically, apps will be loaded as modules into the ZPUI systemd service, which is ran as root. Historically, this allows to make system management apps without permission roadblocks, but it might not be ideal for apps that don't require privileges, and it isn't great for debugging. As such, this model will change later on for security reasons, and you'll be notified when it does.

### [Report issues here!](https://gitlab.com/AUTHOR/zpui-NEWAPPNAME)

## Development/debugging

* If your app's output doesn't show up in `journalctl` when running your app system-wide, make sure you're using `logger.` statements instead of `print()`. You can change log levels by editing the default log level in `setup_logger` call at the top of the app, or change it during runtime from inside ZPUI (Settings=>Logging settings) (**dev-only**)
* App publishing instructions are not yet ready, but refer [here](https://zpui.readthedocs.io/en/latest/app_publish.html) to check if they have been (**dev-only**)
* Try and use [ZPUI docs](https://zpui.readthedocs.io/en/latest) if anything's unclear - though please forgive me, because quite a few parts of those are yet to be updated
* If you're facing problems, feel free to [reach out!](https://zpui.readthedocs.io/en/latest/contact.html)

## License

This work is dual-licensed under BSD and GPL 3.0 (or any later version).
You can choose between one of them if you use this work.

`SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-or-later`
