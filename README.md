# EZPlug for Home Assistant
This custom integration allows you to detect and control your EZVIZ Smart Plugs.
The built-in EZVIZ integration for Home Assistant does not supprt smart plugs, so I decided to make my own integration.

Testato con: Presa T30

Notes:
- Turning the plugs on/off is quick
- Updating plug on/off state takes a while (minute or two) - I could make this faster, but since it's using a cloud API, you can't just spam it every X seconds
- Internet access required

⚠️You should not consider this integration stable. It's just something that I quickly put together, so don't expect it to be good, stable or fast

⚠️This integration uses the EZVIZ Cloud API, so it will not work offline!

## Setup
1. Clone this repo into your Home Assistant's `config/custom_components` directory (`git clone delfigamer11/haezplug`). If you don't have a `custom_components` directory, create it. Make sure you put the files in an `ezplug` directory. Don't put the files directly into the `custom_components` directory. (See directory structure below)
2. Add the following to your Home Assistant configuration file:
```
switch:
  - platform: ezplug
    email: "your_ezviz_account@email.com"
    password: "your_password"
    id: "ezplug"
```
3. Restart your Home Assistant instance.
Your EZVIZ Smart Plugs should show up in Home Assistant.

## Issues?
Make sure you put everything in the right directory.
```
your_home_assistant_config_dir
├── configuration.yaml
├── custom_components
│   └── ezplug
│       ├── __init__.py
│       ├── manifest.json
│       └── switch.py
├── ...
```
