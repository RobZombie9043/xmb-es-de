# xmb-es-de

A custom theme for **EmulationStation Desktop Edition (ES-DE)** inspired by the classic **XrossMediaBar (XMB)** style interface.

> ⚠️ **Important:** This theme requires extra setup to function correctly due to limitations in the ES-DE theme engine.  
> ES-DE does **not** natively support a system carousel in the gamelist view.  
> This feature is *faked* by generating XML files that define the system order, which the theme references.

---

## Preview
| PS 20th Anniversary | Wave - Blue | Famicom |
|----|----|----|
|![Screenshot_20250603-132709](https://github.com/user-attachments/assets/05d9dbf7-ff24-49c0-aa40-7dc89ee7ae4f)|![Screenshot_20250603-132855](https://github.com/user-attachments/assets/7a6a488d-baa7-4afc-a5a6-3059525d6a46)|![Screenshot_20250603-132915](https://github.com/user-attachments/assets/ee01703b-305e-4ae0-aea8-716687d541a1)|

| Dynamic | NC Silhouette | Cyber Psycho |
|----|----|----|
|![Screenshot_20250603-132956](https://github.com/user-attachments/assets/30cbc794-aa44-405e-9b3b-bf2340c96012)|![Screenshot_20250603-132930](https://github.com/user-attachments/assets/7f7f4915-79a9-4c12-a3f7-7b3bfaeb0f00)|![Screenshot_20250603-132939](https://github.com/user-attachments/assets/a2fa5389-ae4a-4815-9541-fc9e3f8578af)|

---

## 📋 Setup Instructions (All OS)

1. **Download theme**  
   Download theme from the GitHub page  
   Extract to ```~ES-DE/themes/xmb-es-de-main``` (inside this folder should be the theme.xml file)
   
2. **Enable Custom Event Scripts in ES-DE**  
   Open ES-DE and go to:  
   `Main Menu > Other Settings > "Enable Custom Event Scripts"`

   This is required to run the script to generate the xml files needed.
   
3. **Enable Debug Mode in ES-DE**  
   Open ES-DE and go to:  
   `Main Menu > Other Settings > Enable "Debug mode"`

   This is required so the theme can detect the system order from `es_log.txt`.

---

## 🤖 Android / Linux / macOS Additional Setup

> ⚠️ This has only been tested on Android so far but should hopefully be cross-compatible. I'll remove this comment once it has been confirmed to work on Linux / macOS. 

4. Copy the ```theme-changed``` folder:

   ```
   xmb-es-de/setup/Android-Linux-macOS/theme-changed
   ```

   to your ES-DE scripts directory:

   ```
   ~ES-DE/scripts/
   ```
   
   the result should be:

   ```
   ~ES-DE/scripts/theme-changed/generate_xml.sh
   ```

This script will automatically run when switching to the **XMB** theme and generate the required XML files based on the loaded system order in `es_log.txt`.

---

## 💻 Windows Additional Setup (Python required)

4. Copy the ```theme-changed``` folder:

   ```
   xmb-es-de/setup/Windows/theme-changed
   ```

   to your ES-DE scripts directory:

   ```
   ~ES-DE/scripts/
   ```

   the result should be:

   ```
   ~ES-DE/scripts/theme-changed/generateXML.bat
   ```

This script will automatically run when switching to the **XMB** theme and generate the required XML files based on the loaded system order in `es_log.txt`.

---

## 🚀 First-Time Launch

1. Launch ES-DE and switch to the **XMB** theme.

---

## 🔁 Updating System Order (After Adding/Removing Systems)

1. **Exit ES-DE completely.** 

2. **Relaunch ES-DE.**   
   This ensures the new system order is saved to `es_log.txt`.

4. Switch from **XMB** to any other theme, then switch back to **XMB**.

---

## 🛠️ Alternative Setup Options

If you'd prefer to configure the XML manually rather than run scripts, you can use:

### ✅ Python GUI Tool

- Run `XMB XML Generator.pyw`  
- Use the GUI to configure and export the XML files

### ✅ Excel Macro Tool

- Run `XMB xml Generator.xlsm`
- Use the macro-enabled Excel file to generate the required XML files

After using either tool, **copy the generated** `theme-customizations` **folder** to the root of the `xmb-es-de-main` theme folder.

---

## 🎉 You're Ready!

Enjoy the XMB-style experience in ES-DE!

---

## Credits

- Original XMB interface design by Sony Interactive Entertainment.
- System controller icons largely sourced from the RetroArch monochrome controller set 
- Cyperpunk wallpaper - https://wallpapersden.com/cyberpunk-2077-yellow-background-wallpaper/
- PS 20th Anniversary wallpaper by zonetrooper - https://www.deviantart.com/zonetrooper/art/PlayStation-20th-Anniversary-527200450
- Sewitch 2 Bokeh wallpaper by baxysquare - https://www.reddit.com/r/NintendoSwitch2/comments/1l1ozv7/switch_2_bokeh_wallpaper/
---
