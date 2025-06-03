# xmb-es-de

A custom theme for **EmulationStation Desktop Edition (ES-DE)** designed to emulate the classic **XcrossMediaBar (XMB)** style interface.

> ⚠️ **Important:** This theme requires extra setup to function correctly due to limitations in the ES-DE theme engine.  
> ES-DE does **not** natively support a system carousel in the gamelist view.  
> This feature is *faked* by generating XML files that define the system order, which the theme references.

---

## 📋 Setup Instructions (All OS)

1. **Enable Debug Mode in ES-DE**  
   Open ES-DE and go to:  
   `Main Menu > Other Settings > Enable "Debug mode"`

   This is required so the theme can detect the system order from `es_log.txt`.

---

## 🤖 Android Setup

1. Copy the folder:

   ```
   xmb-es-de/setup/Android/theme-changed
   ```

   to your ES-DE scripts directory:

   ```
   ~ES-DE/scripts/
   ```
   
   the result should be:

   ```
   ~ES-DE/scripts/theme-changed/generate_xml.sh
   ```

This script will automatically run when switching to the **xmb-es-de** theme and generate the required XML files based on the loaded system order in `es_log.txt`.

---

## 💻 Windows / Linux / macOS Setup (Python required)

1. Copy the folder:

   ```
   xmb-es-de/setup/Other OS/theme-changed
   ```

   to your ES-DE scripts directory:

   ```
   ~ES-DE/scripts/
   ```

   the result should be:

   ```
   ~ES-DE/scripts/theme-changed/generateXML.bat
   ```

This script will automatically run when switching to the **xmb-es-de** theme and generate the required XML files based on the loaded system order in `es_log.txt`.

---

## 🚀 First-Time Launch

1. Launch ES-DE and switch to the **xmb-es-de** theme.
2. Perform a **metadata rescan** to update the system carousel.

---

## 🔁 Updating System Order (After Adding/Removing Systems)

1. **Exit ES-DE completely.**  
   This ensures the new system order is saved to `es_log.txt`.

2. **Relaunch ES-DE.**

3. Switch from **xmb-es-de** to any other theme, then switch back to **xmb-es-de**.

4. Perform a **metadata rescan** to reflect the updated system order.
`Main Menu > Utilities > Rescan Rom Directory`

---

## 🛠️ Alternative Setup Options

If you'd prefer to configure the XML manually, you can use:

### ✅ Python GUI Tool

- Run `XMB XML Generator.pyw`  
- Use the GUI to configure and export the XML files

### ✅ Excel Macro Tool

- Run 'XMB xml Generator.xlsm'
- Use the macro-enabled Excel file to generate the required XML files

After using either tool, **copy the generated `theme-customizations` folder** to the root of the `xmb-es-de` theme folder.

---

## 🎉 You're Ready!

Enjoy the XMB-style experience in ES-DE!

---
